from django.contrib import admin
from messaging_app.models import Message

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)