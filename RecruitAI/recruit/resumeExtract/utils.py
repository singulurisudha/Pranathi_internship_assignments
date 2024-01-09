from pyresparser import ResumeParser

def extract_information_from_resume(resume_file):
    # Use pyresparser or other libraries to extract information
    data = ResumeParser(resume_file).get_extracted_data()
    
    # Extracting relevant information
    extracted_info = {
        'name': data.get('name', ''),
        'qualification': data.get('degree', ''),
        'skills': data.get('skills', [])
    }
    return extracted_info