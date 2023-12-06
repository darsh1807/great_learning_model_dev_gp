import requests

input_data = [5.1,3.5,1.4,0.2]
r = requests.post("http://127.0.0.1:5000",json = input_data)

print(r.text)
print(r.status_code)