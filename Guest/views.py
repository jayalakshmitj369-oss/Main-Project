from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
import random
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"Guest/index.html")

def UserRegistration(request):
    districtDatas = tbl_district.objects.all()
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        # gender = request.POST.get("btn_gender")
        # dob = request.POST.get("txt_dob")
        district = request.POST.get("txt_district")

        place = tbl_place.objects.get(id=request.POST.get("sel_place"))

        photo = request.FILES.get("file_photo")
        password = request.POST.get("txt_password")
        repassword = request.POST.get("txt_repassword")
        checkuserregistration=tbl_user.objects.filter(user_email=email).count()
        checkartistregistration=tbl_artist.objects.filter(artist_email=email).count()
        if checkuserregistration > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email already existed"})
        elif checkartistregistration > 0:
            return render(request,"Guest/ArtistRegistration.html",{'msg':"Email already existed"})
        else:
            if password == repassword:
                tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,place=place,user_photo=photo,user_password=password)
                return render(request,'Guest/UserRegistration.html',{'msg':"Registration successful"})
            else:
                return render(request,'Guest/UserRegistration.html',{'msg':"Password mismatch"})
    else:
         return render(request,'Guest/UserRegistration.html',{'districtDatas':districtDatas})



def AjaxPlace(request):
    districtId = request.GET.get("did")
    place = tbl_place.objects.filter(district=districtId)
    return render(request,"Guest/AjaxPlace.html",{'place':place})


def Login(request):
    if request.method == "POST":
        email = request.POST.get('txt_email')
        password = request.POST.get('txt_password')

        usercount = tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        artistcount = tbl_artist.objects.filter(artist_email=email,artist_password=password).count()

        if usercount > 0:
            userdata = tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid'] = userdata.id
            return redirect("User:HomePage")
        elif admincount > 0:
            adminData = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid'] = adminData.id
            return redirect("Admin:HomePage")
        elif artistcount > 0:
            artistData = tbl_artist.objects.get(artist_email=email,artist_password=password)
            if artistData.artist_status==0:
                return render(request,'Guest/Login.html',{'msg':"Registration Pending....."})
            elif artistData.artist_status==2:
                 return render(request,'Guest/Login.html',{'msg':"Registration Rejected....."})
            else:
                request.session['tid'] = artistData.id
                return redirect("Artist:HomePage")
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid Email or Password"})
    else:
            return render(request,'Guest/Login.html')




def ArtistRegistration(request):
    districtDatas=tbl_district.objects.all()
    
    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        district = tbl_district.objects.get(id=request.POST.get("sel_district"))
        place = tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo = request.FILES.get("file_photo")
        proof = request.FILES.get("file_proof")
        password = request.POST.get("txt_password")
        checkartistregistration=tbl_artist.objects.filter(artist_email=email).count()
        checkuserregistration=tbl_user.objects.filter(user_email=email).count()
        if checkartistregistration > 0:
            return render(request,"Guest/ArtistRegistration.html",{'msg':"Email already existed"})
        elif checkuserregistration > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email already existed"})
        else:
            tbl_artist.objects.create(artist_name=name,artist_email=email,artist_contact=contact,artist_address=address,place=place,artist_photo=photo,artist_proof=proof,artist_password=password)
            return render(request,'Guest/ArtistRegistration.html',{'msg':'Registration Successful'})
    else:
        return render(request,'Guest/ArtistRegistration.html',{'districtDatas':districtDatas})
    
def Forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("txt_email")

        usercount = tbl_user.objects.filter(user_email=email).count()
        artistcount = tbl_artist.objects.filter(artist_email=email).count()

        if usercount == 0 and artistcount == 0:
            return render(request, "Guest/Forgotpassword.html", {
                "msg": "Email not registered"
            })

        if usercount > 0:
            user = tbl_user.objects.get(user_email=email)
            request.session["fid"] = user.id

        elif artistcount > 0:
            artist = tbl_artist.objects.get(artist_email=email)
            request.session["wid"] = artist.id

        otp = random.randint(111111, 999999)
        request.session["otp"] = otp

        send_mail(
            'Forgot password OTP',
            f"Hello,\n\nYour OTP is {otp}.\n\nIf you didn't request this, ignore this email.\n\nThanks,\nD MARKET Team",
            settings.EMAIL_HOST_USER,
            [email],
        )

        return redirect("Guest:Otp")

    return render(request, "Guest/Forgotpassword.html")


def Otp(request):
    if request.method == "POST":
        inp_otp = int(request.POST.get("txt_otp"))

        if inp_otp == request.session.get("otp"):
            return redirect("Guest:Newpassword")
        else:
            return render(request, "Guest/Otp.html", {
                "msg": "OTP does not match"
            })

    return render(request, "Guest/Otp.html")

def Newpassword(request):
    if request.method == "POST":
        new_pass = request.POST.get("txt_new_pass")
        con_pass = request.POST.get("txt_con_pass")

        if new_pass != con_pass:
            return render(request, "Guest/Newpassword.html", {
                'msg': 'Password does not match'
            })

        if "fid" in request.session:
            user = tbl_user.objects.get(id=request.session["fid"])
            user.user_password = new_pass
            user.save()

            request.session.flush()
            return render(request, "Guest/Newpassword.html", {
                'msg': 'User password updated successfully'
            })

        elif "wid" in request.session:
            artist = tbl_artist.objects.get(id=request.session["wid"])
            artist.artist_password = new_pass
            artist.save()

            request.session.flush()
            return render(request, "Guest/Newpassword.html", {
                "msg": "Password updated successfully"
            })

        else:
            return render(request, "Guest/Newpassword.html", {
                "msg": "Session expired"
            })

    return render(request, "Guest/Newpassword.html")


    
    

        