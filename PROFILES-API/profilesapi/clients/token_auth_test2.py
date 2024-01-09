import requests

def client():
    data = {
        "username": "rest",
        "email":"rest@gmail.com",
        "password1": "rest",
        "password2":"rest"
        }

    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
                             data=data)

    # token_h = "Token e68b0d5950e3ee303c38222d23a30d57055a48ac"
    # headers = {"Authorization": token_h}

    # response = requests.get("http://127.0.0.1:8000/api/profiles/",
    #                         headers=headers)

    print("Status Code: ", response.status_code)
    
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()
