from django.urls import path
from . import views

urlpatterns = [
    path('getmessages', views.getMessages, name='get-messages'),
    path('getunreadmessages', views.getUnreadMessages, name='get-unread-messages'),
    path('readmessage/<int:message_id>', views.readMessage, name='read-message'),
    path('deletemessage/<int:message_id>', views.deleteMessage, name='delete-message'),
]
