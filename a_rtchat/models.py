from django.db import models
from django.contrib.auth.models import User
import shortuuid

from PIL import Image

# Create your models here.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import os

# Create your models here.

# Clé maître pour chiffrer et déchiffrer (doit être de 16, 24 ou 32 octets)
MASTER_KEY = os.getenv('MASTER_KEY', '0123456789abcdef0123456789abcdef').encode('utf-8')

def encrypt_message(key, message):
    """Chiffrer un message avec AES"""
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    return base64.b64encode(iv + encrypted).decode('utf-8')


def decrypt_message(key, encrypted_message):
    """Déchiffrer un message avec AES"""
    encrypted_message = base64.b64decode(encrypted_message)
    iv = encrypted_message[:16]
    encrypted = encrypted_message[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(cipher.decrypt(encrypted), AES.block_size).decode('utf-8')


class ChatGroup(models.Model):
    group_name=models.CharField(max_length=128,unique=True)
    groupchat_name=models.CharField(max_length=128,null=True,blank=True)
    admin=models.ForeignKey(User,related_name='groupchats',blank=True,null=True,on_delete=models.SET_NULL)
    #users_online=models.ManyToManyField(User,related_name='online_in_groups',blank=True,default=shortuuid.uuid)
    users_online = models.ManyToManyField(User, related_name='online_in_groups', blank=True)
    members=models.ManyToManyField(User,related_name='chat_groups',blank=True)
    is_private=models.BooleanField(default=False)
    
    def __str__(self):
        return self.group_name
    
    def save(self, *args, **kwargs):
        if not self.group_name:
            self.group_name = shortuuid.uuid()
        super().save(*args, **kwargs)
    
class GroupMessage(models.Model):
    group=models.ForeignKey(ChatGroup,related_name='chat_messages',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.CharField(max_length=300)
    encrypted_body = models.TextField(blank=True, null=True)  # Champ pour stocker le message chiffré
    file = models.FileField(upload_to='files/', blank=True, null=True)
    created=models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # On chiffre le message uniquement s'il y a un contenu dans 'body'
        if self.body:
            self.encrypted_body = encrypt_message(MASTER_KEY, self.body)
        else:
            self.encrypted_body = None
        super().save(*args, **kwargs)

    @property
    def decrypted_body(self):
        # Si vous souhaitez disposer d'un accès au texte déchiffré dans votre code,
        # vous pouvez utiliser cette propriété.
        if self.encrypted_body:
            return decrypt_message(MASTER_KEY, self.encrypted_body)
        return ""
    
    @property
    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)
        else:
            return None
    """
    def __str__(self):
        # Pour l'affichage dans l'administration et ailleurs, on affiche uniquement le message chiffré.
        if self.body:
            return f'{self.author.username}: {self.encrypted_body}'
        elif self.file:
            return f'{self.author.username}: {self.file}' """
    def __str__(self):
        if self.body:
            return f'{self.author.username}: {self.encrypted_body}'
        elif self.file:
            return f'{self.author.username}: {self.filename}'
        else:
            return f'{self.author.username}: (message vide)'

    
    class Meta:
        ordering=['-created']

    @property    
    def is_image(self):
        try:
            image = Image.open(self.file) 
            image.verify()
            return True 
        except:
            return False