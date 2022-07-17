# Software Engineering I Project

This project contains two separate parts. The first is an app to search USA
Climbing Open Championship winners. The second is an API to send an email.


## USA Climbing Champion Finder
This is a desktop app that uses a teammate's Wikipedia scraper API to display USA Climbing athletes
that won gold medal in a particular year or to find out how many gold medals
a past champion has won. This part can be found in the championFinder directory.
Must be logged into OSU VPN to use it as is.


## DevSendEZ
This is an API developed for a teammate to use for their meeting scheduler
app.  It allows users to send an an HTML or plain text email by using a POST 
request to the server. Must be logged into OSU VPN to use it as is. This part 
of the project can be found in the sendEmail directory. Below are the details
on how to use the API.


### API Server (POST Request)
Send a POST request with the below JSON format to server (previously http://flip1.engr.oregonstate.edu:9584/)

### JSON POST Request Example:
```
{  
  "recipient": "devsendez@gmail.com",  
  "senderName": "me",  
  "senderEmail": "test@email.com",  
  "subject": "Test Subject",  
  "text": "words and things and words",  
  "html": "<!DOCTYPE html><html><body><h1>Test Header</h1></body></html>"  
}
```

*HTML is optional.*

### JSON Response Example:
```
{"Status":"sent"}  
{"Status":"error"}  
{'Status':'invalid request format error'}
```
