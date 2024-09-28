import requests

from sendEmail import sendMail

api_key='1154338ec65d47b0bdce9fb7fd90250c'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2024-08-28&sortBy=publishedAt&apiKey=1154338ec65d47b0bdce9fb7fd90250c'
#make a request
request =requests.get(url)
#Get dictionary with data (Json makes the data into a dict data type)
content = request.json()

#access article titles and descriptions
body=""
for article in content['articles']:
    if article['title'] is not None:
        body+=article['title'] + '\n'+ article['description'] + '\n\n'
body=body.encode('utf-8')
sendMail(message=body)