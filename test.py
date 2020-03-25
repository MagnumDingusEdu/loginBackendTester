import requests

url = "http://localhost:8080/api/register"

params = {"user":"test2", "pass":"kunwarmadarchod", "name":"magnum"}
author = {"token":"16a14f6aa33373b4022de6d9dee3d2503d28681b"}

r = requests.post(url, data=params)


# data = r.json()
print(r.text)