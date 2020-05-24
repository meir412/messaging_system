from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getmessages/<int:user_id>', views.getMessages, name='get-messages'),
    path('getunreadmessages/<int:user_id>', views.getUnreadMessages, name='get-unread-messages'),
    path('readmessage/<int:message_id>', views.readMessage, name='read-message'),
    path('deletemessage/<int:message_id>', views.deleteMessage, name='delete-message'),
]
