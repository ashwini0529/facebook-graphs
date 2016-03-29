#A python script that posts on your timeline using access token.
import requests

face_token = 'Your access token'
post = 'Hello'
post.replace(' ', '+')
requests.post("https://graph.facebook.com/me/feed/?message=" + post + "&access_token=" + face_token)
