from django.contrib import admin
from messaging_app.models import Message

class MessageAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'sender', 'receiver', 'subject')

admin.site.register(Message, MessageAdmin)