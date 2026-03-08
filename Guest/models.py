from django.db import models
from Admin.models import *

# Create your models here.
class tbl_user(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_contact = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_photo = models.FileField(upload_to="Assets/UserDocs/")
    place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_email = models.CharField(max_length=50)
    artist_contact = models.CharField(max_length=50)
    artist_address = models.CharField(max_length=50)
    artist_photo = models.FileField(upload_to="Assets/ArtistDocs/")
    artist_proof = models.FileField(upload_to="Assets/ArtistDocs/")
    artist_password = models.CharField(max_length=50)
    artist_status = models.IntegerField(default=0)
    place = models.ForeignKey(tbl_place,on_delete=models.CASCADE)

