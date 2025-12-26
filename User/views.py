from django.shortcuts import render,redirect    
from Guest.models import *
from User.models import *
from Artist.models import *
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime, timedelta , time, datetime

# Create your views here.
def HomePage(request):
    userData = tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/HomePage.html',{'user':userData})

def MyProfile(request):
    userData = tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'user':userData})

def EditProfile(request):
    userData = tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        checkeditprofile=tbl_user.objects.filter(user_email=request.POST.get("txt_email")).count()
        if checkeditprofile > 0:
            return render(request,"User/EditProfile.html",{'msg':"Email already existed"})
        else:
            userData.user_name = name
            userData.user_email = email
            userData.user_contact = contact
            userData.user_address = address
            userData.save()
            return render(request,'User/EditProfile.html',{"msg":"Profile Updated.."})
    else:
        return render(request,'User/EditProfile.html',{'user':userData})

def ChangePassword(request):
    userData = tbl_user.objects.get(id=request.session['uid'])
    userpass = userData.user_password
    if request.method == "POST":
        oldpassword = request.POST.get("txt_oldpassword")
        newpassword = request.POST.get("txt_newpassword")
        retypepassword = request.POST.get("txt_retypepassword")
        if userpass == oldpassword:
            if newpassword == retypepassword:
                userData.user_password = newpassword
                userData.save()
                return render(request,'User/ChangePassword.html',{"msg":"Password Successful.."})
            else:
                return render(request,'User/ChangePassword.html',{"msg":"Password Mismatch.."})
        else:
                return render(request,'User/ChangePassword.html',{"msg":"Password Incorrect.."})
    else:           
         return render(request,'User/ChangePassword.html',{'user':userData})

def Complaint(request):
    complaintData = tbl_complaint.objects.filter(user_id=request.session['uid'])
    if request.method == "POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user_id=user)
        return render(request,'User/Complaint.html',{'msg':'Complaint Successful'})
    else:
        return render(request,'User/Complaint.html',{'complaintData':complaintData})

def DeleteComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'User/Complaint.html',{'msg':'Complaint Deleted Successfully..'})

def ViewArtwork(request):
    user = request.session.get("uid")  
    artworkData = tbl_artwork.objects.all()
    liked_artworks = tbl_like.objects.filter(user_id=user).values_list('artwork_id', flat=True)
    for art in artworkData:
        art.like_count = tbl_like.objects.filter(artwork_id=art.id).count()
        art.is_liked = art.id in liked_artworks
    return render(request, 'User/ViewArtwork.html', {"artworkData": artworkData})


def ViewArtist(request,id):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    artistData = tbl_artist.objects.get(id=id)
    tot=0
    ratecount=tbl_rating.objects.filter(artist=artistData).count()
    if ratecount>0:
        ratedata=tbl_rating.objects.filter(artist=artistData)
        for j in ratedata:
            tot=tot+j.rating_data
            avg=tot//ratecount
            # print(avg)
    else:
        avg=0

    return render(request,'User/ViewArtist.html',{'artistData':artistData,'parry':avg,'ar':ar})

def CustomRequest(request,id):
    arttypeData = tbl_arttype.objects.all()
    artsubtypeData =tbl_artsubtype.objects.all()
    if request.method=="POST":
        details = request.POST.get("txt_details")
        file = request.FILES.get("file_name")
        artsubtype=tbl_artsubtype.objects.get(id=request.POST.get('sel_artsubtype'))
        artistId=tbl_artist.objects.get(id=id)
        userId=tbl_user.objects.get(id=request.session['uid'])
        tbl_customization.objects.create(customization_details=details,customization_file=file,artsubtype_id=artsubtype,artist=artistId,user_id=userId)
        return render(request,'User/CustomRequest.html',{'msg':"Inserted Successful"})
    else:    
        return render(request,'User/CustomRequest.html',{'arttypeData': arttypeData,'artsubtypeData':artsubtypeData})
    
def MyCustomRequest(request):
    customData = tbl_customization.objects.all()
    return render(request,'User/MyCustomRequest.html',{'customData':customData})

def Accept(request,aid):
    customData = tbl_customization.objects.get(id=aid)
    customData.customization_status=3
    customData.save()
    return render(request,'User/MyCustomRequest.html',{'msg':"Request Accepted"})

def Reject(request,rid):
    customData = tbl_customization.objects.get(id=rid)
    customData.customization_status=4
    customData.save()
    return render(request,'User/MyCustomRequest.html',{'msg':"Request Rejected"})



def Comment(request,id):
    commentData = tbl_comment.objects.filter(artwork_id=id) 
    if request.method=="POST":
        comment = request.POST.get("txt_comment")
        userId=tbl_user.objects.get(id=request.session['uid'])
        artworkId=tbl_artwork.objects.get(id=id)
        tbl_comment.objects.create(comment_content=comment,user_id=userId,artwork_id=artworkId)
        return render(request,'User/Comment.html',{'msg':"Inserted Successful"})
    else:
        return render(request,'User/Comment.html',{'commentData':commentData})

def BookNow(request,id):
    userId=tbl_user.objects.get(id=request.session['uid'])
    artworkId=tbl_artwork.objects.get(id=id)
    tbl_booking.objects.create(user_id=userId,artwork_id=artworkId,booking_amount=artworkId.artwork_price)
    return render(request,'User/ViewArtwork.html',{'msg':"Booked.."})

def Like(request, id):
    user = tbl_user.objects.get(id=request.session["uid"])
    art = tbl_artwork.objects.get(id=id)
    tbl_like.objects.get_or_create(user_id=user, artwork_id=art)
    return redirect("User:ViewArtwork")

def Dislike(request, id):
    user = tbl_user.objects.get(id=request.session["uid"])
    tbl_like.objects.filter(user_id=user, artwork_id=id).delete()
    return redirect("User:ViewArtwork")

def MyBooking(request):
    bookData = tbl_booking.objects.filter(user_id=request.session['uid'])
    return render(request,'User/MyBooking.html',{'bookData':bookData})

def Payment(request,id):
    bookData = tbl_booking.objects.get(id=id)
    if request.method == "POST":
        bookData.booking_status=1
        bookData.save()
        return render(request,'User/Payment.html',{'msg':"Payment Successfull"})
    else:
        return render(request,'User/Payment.html',{'bookData':bookData})

def Feedback(request):
    if request.method == "POST":
        feedback=request.POST.get('txt_feedback')
        user=tbl_user.objects.get(id=request.session['uid'])
        tbl_feedback.objects.create(feedback_content=feedback,user_id=user)
        return render(request,'User/Feedback.html',{'msg':"Feedback Submitted"})
    else:
        return render(request,'User/Feedback.html')
    

def ViewGallery(request,id):
    viewgalleryData = tbl_gallery.objects.filter(artwork_id=id)
    return render(request,'User/ViewGallery.html',{"viewgalleryData":viewgalleryData})



def chatpage(request,id):
    artist  = tbl_artist.objects.get(id=id)
    return render(request,"User/Chat.html",{"artist":artist})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_artist = tbl_artist.objects.get(id=request.POST.get("tid"))
    print(to_artist)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,artist_to=to_artist,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(artist_from=tid) | Q(artist_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(artist_to=request.GET.get("tid")) | (Q(artist_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(artist=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(artist=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session['uid']),user_review=user_review,rating_data=rating_data,artist=tbl_artist.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(artist=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(artist=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(artist=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)

