import requests

def main():
    response = requests.get("http://www.google.com")
    print("Status Code  :",response.status_code)
    response=requests.get("http://www.google.com/random-address/")
    print("Headers : ",response.headers)
    print("content-Type : ",response.headers["Content-Type"])
    print("Status Code  :",response.status_code)
    print("Content : ",response.text)
main()
