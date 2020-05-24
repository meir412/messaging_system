import json

from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from messaging_app.models import Message

def home(request):
    """ Static home page view, links to documentation and code repo """
    return render(request, 'index.html')


def getMessages(request, user_id):
    """ This view retreives all messages for a specific user according to the user_id of the receiver of the message """
    
    data = {"response": None, "error": None}
    try:
        receiver = User.objects.get(id=user_id)

    except ObjectDoesNotExist:
        data['error'] = f"User with id {user_id} doesn't exist in the database"
        return JsonResponse(data, status=404)

    query = Message.objects.filter(receiver=receiver)
    if len(query) == 0:
        data['error'] = f"User '{receiver.username}' hasn't received any messages yet"
        return JsonResponse(data, status=404)
    
    data['response'] = _returnData(query)
    return JsonResponse(data)
        

def getUnreadMessages(request, user_id):
    """ This view retreives all unread messages for a specific user according to the user_id of the receiver of the message """
    
    data = {"response": None, "error": None}
    try:
        receiver = User.objects.get(id=user_id)

    except ObjectDoesNotExist:
        data['error'] = f"User with id {user_id} doesn't exist in the database"
        return JsonResponse(data, status=404)

    query = Message.objects.filter(receiver=receiver, unread=True)
    if len(query) == 0:
        data['error'] = f"User '{receiver.username}' doesn't have any unread messages"
        return JsonResponse(data, status=404)

    data['response'] = _returnData(query)
    return JsonResponse(data)


def readMessage(request, message_id):
    """ This view returns a specific message according to the message id """

    data = {"response": None, "error": None}
    try:
        message = Message.objects.get(id=message_id)
    
    except ObjectDoesNotExist:
        data['error'] = f"Message with id {message_id} doesn't exist in the database"
        return JsonResponse(data, status=404)

    if message.unread == True:
        message.unread = False
        message.save()

    data['response'] = {
            "message_id": message.id,
            "sender": message.sender.username,
            "receiver": message.receiver.username,
            "subject": message.subject,
            "message": message.message
        }
    
    return JsonResponse(data)


def deleteMessage(request, message_id):
    """ This view deletes a specific message according to the message id """

    data = {"response": None, "error": None}
    try:
        message = Message.objects.get(id=message_id)
    
    except ObjectDoesNotExist:
        data['error'] = f"Message with id {message_id} doesn't exist in the database"
        return JsonResponse(data, status=404)

    message.delete()

    data['response'] = "Message deleted succesfully"
    return JsonResponse(data)

def _returnData(query):

    data = []
    for message in query:        
        data.append({
            "message_id": message.id,
            "sender": message.sender.username,
            "receiver": message.receiver.username,
            "subject": message.subject,
            "message": message.message
        })
    
    return data
