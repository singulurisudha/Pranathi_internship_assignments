import requests

def main():
    response = requests.get("https://api.exchangeratesapi.io/latest")
    print("Status Code : ",response.status_code)
    print("Content Type : ",response.headers['Content-Type'])
    if response.status_code != 200:
        print("Status Code: ", response.status_code)
        raise Exception("There was an error!")
    data = response.json()
    print("JSON data: ", data)
main()