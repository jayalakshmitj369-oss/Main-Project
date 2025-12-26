from django.db import models
from Guest.models import *
from Artist.models import *

# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_customization(models.Model):
    customizaion_date=models.DateField(auto_now_add=True)
    customization_status=models.IntegerField(default=0)
    customization_details=models.CharField(max_length=50)
    customization_file=models.FileField(upload_to="Assets/CustomDocs/")
    customization_amount=models.CharField(max_length=50,null=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    artist=models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    artsubtype_id=models.ForeignKey(tbl_artsubtype,on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    booking_amount=models.CharField(max_length=50,null=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    artwork_id=models.ForeignKey(tbl_artwork,on_delete=models.CASCADE)

class tbl_like(models.Model):
    artwork_id=models.ForeignKey(tbl_artwork,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_comment(models.Model):
    comment_date=models.DateField(auto_now_add=True)
    comment_content=models.CharField(max_length=50)
    artwork_id=models.ForeignKey(tbl_artwork,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=50)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    artist_id=models.ForeignKey(tbl_artist,on_delete=models.CASCADE,null=True)


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    artist_to = models.ForeignKey(tbl_artist,on_delete=models.CASCADE,related_name="artist_to",null=True)
    artist_from = models.ForeignKey(tbl_artist,on_delete=models.CASCADE,related_name="artist_from",null=True)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    artist=models.ForeignKey(tbl_artist,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)