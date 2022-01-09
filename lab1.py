import requests
#print(requests.__version__)

# used and modified code from  https://docs.python-requests.org/en/latest/
r = requests.get('https://raw.githubusercontent.com/jjpatric/ECE404-lab1/main/lab1.py')
print(r.text)
