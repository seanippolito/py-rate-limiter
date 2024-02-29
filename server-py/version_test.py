import sys
import requests 
from requests.auth import HTTPBasicAuth 
from flask import Flask
print(f"Hello, I'm Python Version {sys.version}")

# Making a GET request 
# r = requests.get('https://api.github.com/users/seanippolito') 
# print(r)
# print(r.content)
# print("---------------------------------------------------------")
# print(r.url)
# print("---------------------------------------------------------")
# print(r.status_code)
# print("---------------------------------------------------------")
# print(r.headers)
# print("---------------------------------------------------------")
# print(r.encoding)
# print("---------------------------------------------------------")
# print(r.elapsed)
# print("---------------------------------------------------------")
# print(r.cookies)
# print("---------------------------------------------------------")
# print(r.history)
# print("---------------------------------------------------------")
# print(r.is_permanent_redirect)
# print("---------------------------------------------------------")
# print(r.is_redirect)
# print("---------------------------------------------------------")
# print(r.iter_content())
# print("---------------------------------------------------------")
# print(r.json())
# print("---------------------------------------------------------")
# print(r.text)
# print("---------------------------------------------------------")
# print(r.request)
# print("---------------------------------------------------------")
# print(r.reason)
# print("---------------------------------------------------------")
# print(r.raise_for_status())
# print("---------------------------------------------------------")
# print(r.ok)
# print("---------------------------------------------------------")
# print(r.links)
# print("---------------------------------------------------------")

# # Making a get request 
# response = requests.get('https://api.github.com/seanippolito', 
#             auth = HTTPBasicAuth('seanippolito', 'pass')) 
# # print request object 
# print(response) 
# print(response.content)

# # create a session object 
# s = requests.Session() 
  
# # make a get request 
# s.get('https://api.github.com/cookies/set/sessioncookie/123456789') 
  
# # again make a get request 
# r = s.get('https://api.github.com/cookies') 
  
# # check if cookie is still set 
# print(r.text) 

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)