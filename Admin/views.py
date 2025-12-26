from django.shortcuts import render
from Admin.models import *
from Guest.models import *
from User.models import *
from Artist.models import *

# Create your views here.
def HomePage(request):
    adminData = tbl_admin.objects.get(id=request.session['aid'])
    return render(request,'Admin/HomePage.html',{"adminData":adminData})

def District(request):
    districtDatas = tbl_district.objects.all()
    if request.method=="POST":
        districtname=request.POST.get("txt_districtname")
        checkdistrict=tbl_district.objects.filter(district_name=districtname).count()
        if checkdistrict > 0:
            return render(request,"Admin/District.html",{'msg':"District already existed"})
        else:
            tbl_district.objects.create(district_name=districtname)
            return render(request,'Admin/District.html',{'msg':'Inserted successfully'})
    else:
        return render(request,'Admin/District.html',{'districtDatas':districtDatas})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/District.html',{'msg':'Deleted successfully'})

def EditDistrict(request,eid):
    districtOne=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        checkdistrict=tbl_district.objects.filter(district_name=request.POST.get("txt_districtname")).count()
        if checkdistrict > 0:
            return render(request,"Admin/District.html",{'msg':"District already existed"})
        else:
            districtOne.district_name=request.POST.get("txt_districtname")
            districtOne.save()
            return render(request,'Admin/District.html',{'msg':'Edited successfully'})
    else:
        return render(request,"Admin/District.html",{"districtOne":districtOne})

def Category(request):
    categoryDatas = tbl_category.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get("txt_categoryname")
        tbl_category.objects.create(category_name=categoryname)
        return render(request,'Admin/Category.html',{'msg':'Inserted successfully'})
    else:
        return render(request,'Admin/Category.html',{'categoryDatas':categoryDatas})

def DeleteCategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Admin/Category.html',{'msg':'Deleted successfully'})

def EditCategory(request,eid):
    categoryOne=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        categoryOne.category_name=request.POST.get("txt_categoryname")
        categoryOne.save()
        return render(request,'Admin/Category.html',{'msg':'Edited successfully'})
    else:
        return render(request,"Admin/Category.html",{"categoryOne":categoryOne})


def Place(request):
    districtDatas = tbl_district.objects.all()
    placeDatas = tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        placename=request.POST.get('txt_placename')
        tbl_place.objects.create(place_name=placename,district=district)
        return render(request,'Admin/Place.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/Place.html',{'districtDatas':districtDatas, 'placeDatas':placeDatas})

def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return render(request,'Admin/Place.html',{'msg':'Deleted successfully'})


def EditPlace(request,eid):
    districtDatas = tbl_district.objects.all()
    placeOne=tbl_place.objects.get(id=eid)
    if request.method=="POST":
            district=tbl_district.objects.get(id=request.POST.get('sel_district'))
            placeOne.place_name=request.POST.get("txt_placename")
            placeOne.district = district
            placeOne.save()
            return render(request,'Admin/Place.html',{'msg':'Edited successfully'})
    else:
        return render(request,"Admin/Place.html",{"placeOne":placeOne,'districtDatas':districtDatas})

def Subcategory(request):
    categoryDatas = tbl_category.objects.all()
    subcategoryDatas = tbl_subcategory.objects.all()
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryname=request.POST.get('txt_subcategory')
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=category)
        return render(request,'Admin/Subcategory.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/Subcategory.html',{'categoryDatas':categoryDatas,'subcategoryDatas':subcategoryDatas})

def DeleteSubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return render(request,'Admin/subcategory.html',{'msg':'Deleted successfully'})

def EditSubcategory(request,eid):
    categoryDatas = tbl_category.objects.all()
    subcategoryOne=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        category=tbl_category.objects.get(id=request.POST.get('sel_category'))
        subcategoryOne.subcategory_name=request.POST.get("txt_subcategory")
        subcategoryOne.category = category
        subcategoryOne.save()
        return render(request,'Admin/Subcategory.html',{'msg':'Edited successfully'})
    else:
        return render(request,"Admin/Subcategory.html",{"subcategoryOne":subcategoryOne,'categoryDatas':categoryDatas})

def AdminRegistration(request):
    adminDatas = tbl_admin.objects.all()
    if request.method=="POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        checkadminregistration=tbl_admin.objects.filter(admin_email=email).count()
        if checkadminregistration > 0:
            return render(request,"Admin/AdminRegistration.html",{'msg':"Admin already existed"})
        else:
            tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
            return render(request,'Admin/AdminRegistration.html',{'msg':'Inserted successfully'})
    else:
        return render(request,'Admin/AdminRegistration.html',{'adminDatas':adminDatas})

def DeleteAdmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return render(request,'Admin/AdminRegistration.html',{'msg':'Deleted successfully'})

def UserList(request):
    userDatas = tbl_user.objects.all()
    return render(request,'Admin/UserList.html',{"userDatas":userDatas})

def ViewComplaint(request):
    complaintData = tbl_complaint.objects.filter(complaint_status=0)
    complaintOne = tbl_complaint.objects.filter(complaint_status=1)
    return render(request,'Admin/ViewComplaint.html',{"complaintData":complaintData,"complaintOne":complaintOne})

def Reply(request,eid):
    complaintOne=tbl_complaint.objects.get(id=eid)
    if request.method == "POST":
        complaintOne.complaint_reply=request.POST.get("txt_reply")
        complaintOne.complaint_status=1
        complaintOne.save()
        return render(request,'Admin/Reply.html',{'msg':'Replied Successfully..'})
    else:
        return render(request,'Admin/Reply.html',{"complaintOne":complaintOne})

def ArtType(request):
    arttypeData = tbl_arttype.objects.all()
    if request.method=="POST":
        arttypename=request.POST.get("txt_arttypename")
        checkarttype=tbl_admin.objects.filter(arttype_name=arttypename).count()
        if checkarttype > 0:
            return render(request,"Admin/ArtType.html",{'msg':"ArtType already existed"})
        else:
            tbl_arttype.objects.create(arttype_name=arttypename)
            return render(request,'Admin/ArtType.html')
    else:
        return render(request,'Admin/ArtType.html',{'arttypeData':arttypeData})

def ArtSubType(request):
    arttypeData = tbl_arttype.objects.all()
    artsubtypeData = tbl_artsubtype.objects.all()
    if request.method=="POST":
        arttype=tbl_arttype.objects.get(id=request.POST.get('sel_arttype'))
        artsubtypename=request.POST.get('txt_subtype')
        tbl_artsubtype.objects.create(artsubtype_name=artsubtypename,arttype=arttype)
        return render(request,'Admin/ArtSubType.html',{'msg':'Inserted Successfully'})
    else:
        return render(request,'Admin/ArtSubType.html',{'arttypeData':arttypeData,'artsubtypeData':artsubtypeData})    

def DeleteArtType(request,did):
    tbl_arttype.objects.get(id=did).delete()
    return render(request,'Admin/ArtType.html',{'msg':'Deleted successfully'})

def DeleteArtSubType(request,did):
    tbl_artsubtype.objects.get(id=did).delete()
    return render(request,'Admin/ArtSubType.html',{'msg':'Deleted Successfully'})

def ArtistVerification(request):
    pending = tbl_artist.objects.filter(artist_status=0)
    accepted =tbl_artist.objects.filter(artist_status=1)
    rejected =tbl_artist.objects.filter(artist_status=2)
    return render(request,'Admin/ArtistVerification.html',{"pending":pending,"accepted":accepted,"rejected":rejected})

def ArtistAccept(request,aid):
    artistverificationData = tbl_artist.objects.get(id=aid)
    artistverificationData.artist_status=1
    artistverificationData.save()
    return render(request,"Admin/ArtistVerification.html",{'msg':"Requested Accepted...."})

def ArtistReject(request,rid):
    artistverificationData = tbl_artist.objects.get(id=rid)
    artistverificationData.artist_status=2
    artistverificationData.save()
    return render(request,"Admin/ArtistVerification.html",{'msg':"Requested Rejected...."})

def ViewFeedback(request):
    artist=tbl_artist.objects.all()
    artistfeedback=tbl_feedback.objects.filter(artist_id__in=artist)
    user=tbl_user.objects.all()
    userfeedback=tbl_feedback.objects.filter(user_id__in=user)
    return render(request,'Admin/ViewFeedback.html',{'artistfeedback':artistfeedback,'userfeedback':userfeedback})





        
