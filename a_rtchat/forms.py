from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widgets={
            'body':forms.TextInput(attrs={'placeholder':'add message...','class':'p-4 text-black ','maxlength':'300','autofocus':True})
        }






        
        """
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name,self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name,self.channel_name
        )
    
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        body=text_data_json['body']

        message=GroupMessage.objects.create(
            body=body,
            author=self.user,
            group=self.chatroom
        )
        
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name , event
        )

        event ={
            'type':'message_handler',
            'message_id':message.id,
        }

    def message_handler(self,event):
        message_id=event['message_id']
        message=GroupMessage.objects.get(id=message_id)
        context={
            'message':message,
            'user':self.user,

        }
        html=render_to_string("a_rtchat/partials/chat_message_p.html",context=context)
        self.send(text_data=html)


        """