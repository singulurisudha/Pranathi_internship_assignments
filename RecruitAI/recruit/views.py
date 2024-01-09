from rest_framework.views import APIView
from rest_framework.response import Response
from PyPDF2 import PdfReader
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .models import Job , Candidate
import re
import spacy
from .serializers import MatchJobSkillsSerializer
from spacy.matcher import Matcher
from docx import Document as DocxDocument


nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

class MatchJobSkillsView(APIView):

    def extract_name(self, resume_text):
        nlp_text = nlp(resume_text)
            
        # Extracting entities of type 'PERSON'
        persons = [ent.text for ent in nlp_text.ents if ent.label_ == 'PERSON']
            
        if persons:
            return persons[0]  # Assuming the first PERSON entity is the name
        else:
            # If no PERSON entity is found, try to find the first continuous sequence of proper nouns
            proper_nouns = []
            current_sequence = []

            for token in nlp_text:
                if token.pos_ == 'PROPN':
                    current_sequence.append(token.text)
                else:
                    if current_sequence:
                        proper_nouns.append(' '.join(current_sequence))
                        current_sequence = []

            if proper_nouns:
                return proper_nouns[0]  # Assuming the first sequence of proper nouns is the name
            else:
                return None  # No suitable name found
            


    def extract_text_from_resume(self, uploaded_file):
        try:
            if uploaded_file.name.endswith('.pdf'):
                return self.extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.endswith('.docx'):
                return self.extract_text_from_docx(uploaded_file)
            else:
                # Handle other file types here
                return None
        except Exception as e:
            print(f"Error extracting text from resume file: {str(e)}")
            return None
        

        
    def extract_text_from_pdf(self, uploaded_file):
        try:
            with uploaded_file as file:
                pdf_reader = PdfReader(file)
                text = ''
                for page_num in range(len(pdf_reader.pages)):
                    text += pdf_reader.pages[page_num].extract_text()
                return text
        except Exception as e:
            print(f"Error extracting text from PDF: {str(e)}")
            return None 

    def extract_text_from_docx(self, uploaded_file):
        try:
            doc = DocxDocument(uploaded_file)
            text = ''
            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'
            return text
        except Exception as e:
            print(f"Error extracting text from DOCX: {str(e)}")
            return None
    def extract_skills_from_text(self, text):
        # Fetch skills from Job model or provide default skills
        job_skills = Job.objects.first().skills.split(',') if Job.objects.exists() else []
        skills_pattern = r'\b(?:' + '|'.join(re.escape(skill.strip()) for skill in job_skills) + r')\b'
        matched_skills = re.findall(skills_pattern, text, flags=re.IGNORECASE)
        
        # Return unique skills by converting to set and then back to list
        unique_skills = list(set(matched_skills))
        
        # Filter empty strings if any
        return list(filter(None, unique_skills))
        
    
    def extract_qualifications_from_text(self,resume_text):
        qualifications_pattern = r'\b(?:B\.Tech|B\.E\.|B\.Sc\.|M\.Tech|Intermediate|SSC|Bachelor of Technology|High School Diploma|Diploma)\b'
        matched_qualifications = re.findall(qualifications_pattern, resume_text)
        return matched_qualifications
    
    def validate_resume_skills(self, resume_text, job_skills):
        # Implement logic to validate resume skills against job skills
        resume_skills = self.extract_skills_from_text(resume_text)
        validated_skills = [skill for skill in resume_skills if skill.lower().strip() in [s.lower().strip() for s in job_skills]]
        return validated_skills

    def validate_qualifications(self, resume_text, job_qualifications):
        # Implement logic to validate resume qualifications against job qualifications
        resume_qualifications = self.extract_qualifications_from_text(resume_text)
        validated_qualifications = [qualification for qualification in resume_qualifications if qualification.lower().strip() in [q.lower().strip() for q in job_qualifications]]
        return validated_qualifications
    
    def post(self, request):
        try:
            serializer = MatchJobSkillsSerializer(data=request.data)
            if serializer.is_valid():
                candidate_resume = serializer.validated_data.get('resume')

                candidate_resume_text = self.extract_text_from_resume(candidate_resume)
                candidate_name = self.extract_name(candidate_resume_text)

                job = Job.objects.first()  # Fetch the first job for simplicity
                job_qualifications = job.qualifications.split(',') if job.qualifications else []
                job_skills = job.skills.split(',') if job.skills else []

                resume_skills = self.extract_skills_from_text(candidate_resume_text)
                valid_skills = self.validate_resume_skills(candidate_resume_text, job_skills)
                valid_qualifications = self.validate_qualifications(candidate_resume_text, job_qualifications)

                response_data = {
                    'candidate_name': candidate_name,
                    'resume_skills_valid': resume_skills,
                    'qualifications_valid': valid_qualifications,
                    'required_skills': job_skills,
                    'required_qualifications': job_qualifications,
                    'validated_skills':valid_skills,
                    'validated_qualifications':valid_qualifications
                }
                if set(valid_skills) == set(job_skills):
                    response_data['message'] = 'Resume matches required skills and qualifications!'

                return Response(response_data)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"An error occurred: {e}")
            return Response({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)