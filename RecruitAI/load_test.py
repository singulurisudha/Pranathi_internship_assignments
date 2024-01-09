import os
from django.core.wsgi import get_wsgi_application
from locust import HttpUser, task, between  # Import the task decorator and 'between' function

# Set up Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RecruitAI.settings")
application = get_wsgi_application()

# Now, import your Django models
from recruit.models import Job, Candidate

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Adjust wait time as needed

    @task
    def test_validate_resume(self):
        # Fetch a candidate from the database (you might need to filter or get a specific one)
        candidate_obj = Candidate.objects.first()

        # Replace with your Django application's base URL
        base_url = "http://localhost:8000"

        # Replace with the endpoint path from your Django application
        endpoint = "/validate-resume/"

        # Use the candidate's resume path from the database
        files = {'resume': ('resume.pdf', open(candidate_obj.resume.path, 'rb'), 'application/pdf')}

        # Make a POST request to the endpoint
        response = self.client.post(base_url + endpoint, files=files)

        # Print the response content or handle it as needed
        print(response.content)
