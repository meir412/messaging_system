import json

# from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from messaging_app.models import Message


def getMessages(request, user_id):

    # query = Message.objects.filter(sender=request.user.id)
    sender = User.objects.get(id=user_id)
    query = Message.objects.filter(sender=sender)
    data = _returnData(query)

    return JsonResponse(data, safe=False)


def getUnreadMessages(request, user_id):

    sender = User.objects.get(id=user_id)
    query = Message.objects.filter(sender=sender, unread=True)
    data = _returnData(query)

    return JsonResponse(data, safe=False)


def readMessage(request, message_id):

    # After adding authentication, only allow sender or receiver to read message
    message = Message.objects.get(id=message_id)
    if message.unread == True:
        message.unread = False
        message.save()

    data = {
            "message_id": message.id,
            "sender": message.sender.username,
            "receiver": message.receiver.username,
            "subject": message.subject,
            "message": message.message
        }
    
    return JsonResponse(data)


def deleteMessage(request, message_id):

    # After adding authentication, only allow sender or receiver to read message
    message = Message.objects.get(id=message_id)
    message.delete()

    response = {"response":"Message deleted succesfully"}
    return JsonResponse(response)

def _returnData(query):

    data = []
    for message in query:
        if message.unread == True:
            message.unread = False
            message.save()
        
        data.append({
            "message_id": message.id,
            "sender": message.sender.username,
            "receiver": message.receiver.username,
            "subject": message.subject,
            "message": message.message
        })
    
    return data
