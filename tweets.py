import os
import tweepy
import requests
import file

API = tweepy.API(file.auth)

#Fazendo um tweet simples
def tweet():
    API.update_status(status = texto)
    
#Fazendo um tweet com imagem
def tweetImg():
    filename = "imagemTweet.jpg"
    request = requests.get(url, stream=True)
    
    if(request.status_code == 200):
        with open(filename, "wb") as image:
            for chunk in request:
                image.write(chunk)
        API.update_status_with_media(status = texto, filename = filename)
        os.remove(filename)
    else:
        print("Não foi possível carregar a imagem")

#Respondendo um tweet com texto
def tweetReply():
    API.update_status(status = texto, in_reply_to_status_id = replyId)

#Respondendo um tweet com imagem
def tweetReplyImg():
    filename = "imagemTweet.jpg"
    request = requests.get(url, stream=True)
    
    if(request.status_code == 200):
        with open(filename, "wb") as image:
            for chunk in request:
                image.write(chunk)
        API.update_status_with_media(status = texto, filename = filename, in_reply_to_status_id = replyId, auto_populate_reply_metadata = True)
        os.remove(filename)
    else:
        print("Não foi possível carregar a imagem")

texto = "AAooAA"
url = "https://i.pinimg.com/564x/a7/c2/bb/a7c2bbdd94b75b942d19818663d67465.jpg"
replyId = ""

tweet()