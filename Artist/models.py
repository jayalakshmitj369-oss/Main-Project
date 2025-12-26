from django.db import models
from Guest.models import *
from Admin.models import *
from Artist.models import *


# Create your models here.
class tbl_artwork(models.Model):
    artwork_title=models.CharField(max_length=50)
    artwork_details=models.CharField(max_length=50)
    artwork_photo=models.FileField(upload_to="Assets/ArtistDocs/")
    artwork_price=models.CharField(max_length=50)
    artsubtype_id=models.ForeignKey(tbl_artsubtype,on_delete=models.CASCADE)
    artist=models.ForeignKey(tbl_artist,on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    artwork_id=models.ForeignKey(tbl_artwork,on_delete=models.CASCADE)
    gallery_file=models.FileField(upload_to="Assets/ArtworkDocs/")

