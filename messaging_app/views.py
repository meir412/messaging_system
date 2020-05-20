from django.shortcuts import render
from django.http import JsonResponse


def getMessages(request, user_id):

    data = {
        'first': 1,
        'second': 2
    }
    return JsonResponse(data)


def getUnreadMessages(request):
    pass


def readMessage(request):
    pass


def deleteMessage(request):
    pass
