import requests

payload = {
    "requestor" : "RM",
    "version"   : "1.0"
}

response = requests.post("https://api.nodemailer.com/user", json=payload)

if response.status_code == 200:
    account = response.json()
    print(account)
else:
    raise Exception(f"Failed to create fake email account. \n {response.text}")