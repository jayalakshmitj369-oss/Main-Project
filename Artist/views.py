from django.shortcuts import render,redirect
from Artist.models import *
from Guest.models import *
from Admin.models import *
from User.models import *
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime



# Create your views here.
def HomePage(request):
    artistData = tbl_artist.objects.get(id=request.session['tid'])
    return render(request,'Artist/HomePage.html',{'user':artistData})

def MyProfile(request):
    artistData = tbl_artist.objects.get(id=request.session['tid'])
    return render(request,'Artist/MyProfile.html',{'artist':artistData})

def EditProfile(request):
    artistData = tbl_artist.objects.get(id=request.session['tid'])
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        checkeditprofile=tbl_artist.objects.filter(artist_email=request.POST.get("txt_email")).count()
        if checkeditprofile > 0:
            return render(request,"Artist/EditProfile.html",{'msg':"Profile already existed"})
        else:
            artistData.artist_name = name
            artistData.artist_email = email
            artistData.artist_contact = contact
            artistData.artist_address = address
            artistData.save()
            return render(request,'Artist/EditProfile.html',{"msg":"Profile Updated.."})
    else:
        return render(request,'Artist/EditProfile.html',{'artist':artistData})
    
def ChangePassword(request):
    artistData = tbl_artist.objects.get(id=request.session['tid'])
    artistpass = artistData.artist_password
    if request.method == "POST":
        oldpassword = request.POST.get("txt_oldpassword")
        newpassword = request.POST.get("txt_newpassword")
        retypepassword = request.POST.get("txt_retypepassword")
        if artistpass == oldpassword:
            if newpassword == retypepassword:
                artistData.artist_password = newpassword
                artistData.save()
                return render(request,'Artist/ChangePassword.html',{"msg":"Password Successful.."})
            else:
                return render(request,'Artist/ChangePassword.html',{"msg":"Password Mismatch.."})
        else:
                return render(request,'Artist/ChangePassword.html',{"msg":"Password Incorrect.."})
    else:           
         return render(request,'Artist/ChangePassword.html',{'artist':artistData})
    
def Artwork(request):
    arttypeData = tbl_arttype.objects.all()
    artsubtypeData =tbl_artsubtype.objects.all()
    artworkData = tbl_artwork.objects.all()
    artistId = tbl_artist.objects.get(id=request.session['tid'])
    if request.method=="POST":
        title = request.POST.get("txt_title")
        photo = request.FILES.get("file_photo")
        details = request.POST.get("txt_details")
        price = request.POST.get("txt_price")
        artsubtype=tbl_artsubtype.objects.get(id=request.POST.get('sel_artsubtype'))
        tbl_artwork.objects.create(artwork_title=title,artwork_photo=photo,artwork_details=details,artwork_price=price,artsubtype_id=artsubtype,artist=artistId)
        return render(request,'Artist/Artwork.html',{'msg':'Inserted Successful'})
    else:
        return render(request,'Artist/Artwork.html',{"arttypeData":arttypeData,"artsubtypeData":artsubtypeData,"artworkData":artworkData})
    
def AjaxSubtype(request):
    arttypeId = request.GET.get("did")
    artsubtype = tbl_artsubtype.objects.filter(arttype=arttypeId)
    return render(request,"Artist/AjaxSubtype.html",{'artsubtype':artsubtype})

def DeleteArtwork(request,did):
    tbl_artwork.objects.get(id=did).delete()
    return render(request,'Artist/Artwork.html',{'msg':'Deleted successfully'})

def GalleryArtwork(request,gid):
    if request.method == "POST":
        file = request.FILES.get("file_name")
        artist=tbl_artwork.objects.get(id=gid)
        tbl_gallery.objects.create(gallery_file=file,artwork_id=artist)
        return render(request,'Artist/Gallery.html',{'msg':"Inseerted Successful"})
    else:
        return render(request,'Artist/Gallery.html')

def ViewCustomerRequest(request):
    customData = tbl_customization.objects.all()
    return render(request,'Artist/ViewCustomerRequest.html',{'customData':customData})

def Accept(request,aid):
    customData = tbl_customization.objects.get(id=aid)
    customData.customization_status=1
    customData.save()
    return render(request,'Artist/ViewCustomerRequest.html',{'msg':"Request Accepted"})

def WorkUpdate(request,id,status):
    work = tbl_customization.objects.get(id=id)
    work.customization_status=status
    work.save()
    return render(request,'Artist/ViewCustomerRequest.html',{'msg':"Work Updated"})

def Reject(request,rid):
    customData = tbl_customization.objects.get(id=rid)
    customData.customization_status=2
    customData.save()
    return render(request,'Artist/ViewCustomerRequest.html',{'msg':"Request Rejected"})


    
def ViewBooking(request):
    bookData = tbl_booking.objects.all()
    return render(request,'Artist/ViewBooking.html',{'bookData':bookData})

def tracking(request,id,status):
    book = tbl_booking.objects.get(id=id)
    book.booking_status=status
    book.save()
    return render(request,'Artist/ViewBooking.html',{'msg':"Tracking Updated"})

def Amount(request,aid):
    customData = tbl_customization.objects.get(id=aid)
    if request.method=="POST":
        amount=request.POST.get('txt_amount')
        customData.customization_status=1
        customData.customization_amount=amount
        customData.save()
        return render(request,'Artist/Amount.html',{'msg':"Amount Inserted"})
    else:
        return render(request,'Artist/Amount.html')
    
def Feedback(request):
    if request.method == "POST":
        feedback=request.POST.get('txt_feedback')
        artist=tbl_artist.objects.get(id=request.session['tid'])
        tbl_feedback.objects.create(feedback_content=feedback,artist_id=artist)
        return render(request,'Artist/Feedback.html',{'msg':"Feedback Submitted"})
    else:
        return render(request,'Artist/Feedback.html')




def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Artist/Chat.html",{"user":user})

def ajaxchat(request):
    from_artist = tbl_artist.objects.get(id=request.session["tid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),artist_from=from_artist,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Artist/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    artist = tbl_artist.objects.get(id=request.session["tid"])
    chat_data = tbl_chat.objects.filter((Q(artist_from=artist) | Q(artist_to=artist)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Artist/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(artist_from=request.session["tid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(artist_to=request.session["tid"]))).delete()
    return render(request,"Artist/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

def Logout(request):
    del request.session['tid']
    return redirect('Guest:Login')
