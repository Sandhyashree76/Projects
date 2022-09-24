'''Q1. Write a Python code to check the status code issued by a server in response
to a client's request made to the server. Print all of the methods and attributes
available to objects on successful request[hint: use dir() method to find the
methods and attributes].'''
import requests

r=requests.get("https://github.com")
print(r.status_code)
print(dir(r))


'''Q2. Write a Python code to send a request to a web page, and print the response
text and content. Also get the raw socket response from the server.'''

r=requests.get("https://lnbspace.github.io/")
print(r.content)
print(r.text)
print(r.raw)

'''Q3. Write a Python code to send a request to a web page, and print the
information of headers. Also parse these values and print key-value pairs holding
various information'''

s=requests.get("https://lnbspace.github.io/")
print(s.headers)
print(s.headers['Server'])
print(s.headers['Last-Modified'])
print(s.headers['expires'])
print(s.headers['Cache-Control'])
print(s.headers['Content-Encoding'])
print(s.headers['Accept-Ranges'])
print(s.headers['Date'])

'''Q4. Write a Python code to send a request to a web page and stop waiting for a
response after a given number of seconds. In the event of times out of request,
raise the Timeout exception.'''

from requests.exceptions import Timeout

try:
    r=requests.get('http://marketingmist.blogspot.com/p/homepage.html',timeout=3)
    print(r)
except Timeout:
    print("try again")

else:
    print("successfull")
