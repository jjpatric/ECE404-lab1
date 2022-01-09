import requests
#print(requests.__version__)

# used and modified code from  https://docs.python-requests.org/en/latest/
r = requests.get('http://www.google.com/')
print(r.text)
