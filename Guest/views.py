from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *

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
        gender = request.POST.get("btn_gender")
        dob = request.POST.get("txt_dob")
        district = request.POST.get("txt_district")

        place = tbl_place.objects.get(id=request.POST.get("sel_place"))

        photo = request.FILES.get("file_photo")
        password = request.POST.get("txt_password")
        repassword = request.POST.get("txt_repassword")
        checkuserregistration=tbl_user.objects.filter(user_email=email).count()
        if checkuserregistration > 0:
            return render(request,"Guest/UserRegistration.html",{'msg':"Email already existed"})
        else:
            if password == repassword:
                tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact,user_address=address,user_gender=gender,user_dob=dob,place=place,user_photo=photo,user_password=password)
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
        if checkartistregistration > 0:
            return render(request,"Guest/ArtistRegistration.html",{'msg':"Email already existed"})
        else:
            tbl_artist.objects.create(artist_name=name,artist_email=email,artist_contact=contact,artist_address=address,place=place,artist_photo=photo,artist_proof=proof,artist_password=password)
            return render(request,'Guest/ArtistRegistration.html',{'msg':'Registration Successful'})
    else:
        return render(request,'Guest/ArtistRegistration.html',{'districtDatas':districtDatas})
    


    
    

        