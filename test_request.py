import requests

url = "https://pages.fm/api/v1/pages/113685645036936/avatar"
access_token= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI3ODg4MzY3ZS01OTZmLTRjOGItYWM0Ni1mZWYzYTEyMDZmM2QiLCJsb2dpbl9zZXNzaW9uIjpudWxsLCJpYXQiOjE2OTM5NjUxOTEsImZiX25hbWUiOiJDaHJpc3RpYW4gQmVuaXRleiIsImZiX2lkIjoiODAxNjY1MzIwNzc0NjQwIiwiZXhwIjoxNzAxNzQxMTkxfQ.Sav-I947co5WlpLhdvFGHqzGHZTVi58T0DhyzQ8W_DI"
data = {
    "access_token": access_token
}

response = requests.get(url, data=data)

# In ra nội dung phản hồi
print(response.text)
