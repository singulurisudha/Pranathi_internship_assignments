from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import PyPDF2
import re
from rest_framework import serializers
from recruit.models import Job
from .serializers import CandidateSerializer

class ResumeAPIView(APIView):
    def extract_text_from_resume(self,resume_file):
        if resume_file.name.endswith('.pdf'):
            pdf_text = ""
            try:
                pdf_reader = PyPDF2.PdfReader(resume_file)
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_text += page.extract_text()
                return pdf_text
            except Exception as e:
                # Handle exceptions, such as incorrect file format or unreadable file
                print("Error while extracting text:", str(e))
        else:
            # Handle unsupported file formats
            print("Unsupported file format")
    def extract_resume_info(self, resume_text):
        lines = resume_text.split('\n')
        resume_info = {}
        current_section = None

        for line in lines:
            line = line.strip()
            if line.startswith(('S k i l l s', 'E d u c a t i o n')):
                current_section = line
                resume_info[current_section] = []
            elif current_section and line:
                resume_info[current_section].append(line)

        # Removing empty sections and formatting the output
        resume_info = {key: value for key, value in resume_info.items() if value}
        return resume_info
    def remove_space_from_letters(self, resume_info):
        cleaned_resume_info = {}
        for key, value in resume_info.items():
            new_key = key.replace(' ', '')  # Remove spaces from the keys
            if isinstance(value, str):
                cleaned_value = value.replace(' ', '')  # Remove spaces from the values
                cleaned_resume_info[new_key] = cleaned_value
            elif isinstance(value, list):
                cleaned_values = [v.replace(' ', '') for v in value]  # Remove spaces from the values in the list
                cleaned_resume_info[new_key] = cleaned_values
            else:
                cleaned_resume_info[new_key] = value  # No spaces removed for other types
        print(cleaned_resume_info)    
        return cleaned_resume_info
    
    def find_matching_skills(self,job_skills, applicant_data):
        matching_skills = []

        for key, value in applicant_data.items():
            if isinstance(value, list):
                for item in value:
                    for skill in job_skills:
                        if skill.strip().lower() in item.lower():
                            matching_skills.append(item)
                            break  # Exit inner loop once a match is found for the skill

        return matching_skills
    def find_education_details(self, applicant_data):
        education_keywords = ['B.Tech', 'Intermediate', 'SSC']  # Keywords to identify education details
        education_details = []

        for key, value in applicant_data.items():
            if isinstance(value, list):
                for item in value:
                    if any(keyword.lower() in item.lower() for keyword in education_keywords):
                        education_details.append(item)

        return education_details
    
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
            
        if serializer.is_valid():
            resume = serializer.validated_data['resume']
            resume_text = self.extract_text_from_resume(resume)

            if resume_text:
                # Extracting skills and education information
                resume_info = self.extract_resume_info(resume_text)
                
                if resume_info is not None:
                    resume_info = self.remove_space_from_letters(resume_info)

                    validated_skills = resume_info.get('S k i l l s', [])  # Update the key to 'S k i l l s' after cleaning
                    validated_education = resume_info.get('E d u c a t i o n', [])  # Update the key to 'E d u c a t i o n' after cleaning

                    # Extracting education details
                    #education = [item for item in validated_education if any(q in item for q in ['B.Tech', 'Intermediate', 'SSC'])]

                    # Extracting skills details
                    job_instance = Job.objects.get(job_id=1)

                    # Extract required skills from the job instance
                    job_skills_required = job_instance.skills.split(",")  # Example job skills required
                    skills = self.find_matching_skills(job_skills_required, resume_info)
                    education = self.find_education_details(resume_info)

                    # Keyword to match in skills
                    keyword = 'Python'  # You can adjust this keyword as needed

                    # Filter unique skills containing the keyword
                    matching_skills = list(set([skill.lower() for skill in skills if isinstance(skill, str) and keyword.lower() in skill.lower()]))

                    # Filter education containing 'B.Tech', 'Intermediate', or 'SSC'
                    education_keywords = ['B.Tech', 'Intermediate', 'SSC']
                    matching_education = [edu for edu in education if any(keyword.lower() in edu.lower() for keyword in education_keywords)]

                    # Display filtered skills and education
                    print("Skills containing '{}' keyword:".format(keyword))
                    print(matching_skills)

                    print("\nEducation details:")
                    print(matching_education)

                    print("Filtered Education:", education)
                    print("Filtered Skills:", skills)

                    return Response({
                        "validated_skills": validated_skills,
                        "validated_education": validated_education,
                        # Other response data as needed
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Failed to extract information from the resume"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            return Response({"message": "Failed to extract text from the resume"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)