from django.urls import path
from User import views
app_name="User"

urlpatterns=[
    path('HomePage/',views.HomePage, name="HomePage"),
    
    path('MyProfile/',views.MyProfile, name="MyProfile"),
    path('EditProfile/',views.EditProfile, name="EditProfile"),

    path('ChangePassword/',views.ChangePassword, name="ChangePassword"),

    path('Complaint/',views.Complaint, name="Complaint"),
    path('DeleteComplaint/<int:did>',views.DeleteComplaint,name="DeleteComplaint"),

    path('ViewArtwork/',views.ViewArtwork, name="ViewArtwork"),

    path('ViewArtist/<int:id>',views.ViewArtist, name="ViewArtist"),
    
    path('CustomRequest/<int:id>',views.CustomRequest, name="CustomRequest"),

    path('MyCustomRequest/',views.MyCustomRequest, name="MyCustomRequest"),
    path('Accept/<int:aid>',views.Accept,name="Accept"),
    path('Reject/<int:rid>',views.Reject,name="Reject"),

    path('Comment/<int:id>',views.Comment, name="Comment"),

    path('Like/<int:id>', views.Like, name="Like"),
    path('Dislike/<int:id>', views.Dislike, name="Dislike"),

    path('BookNow/<int:id>', views.BookNow, name="BookNow"),  

    path('MyBooking/',views.MyBooking, name="MyBooking"), 

    path('Payment/<int:id>', views.Payment,name="Payment"),

    path('Feedback/',views.Feedback, name="Feedback"),

    path('ViewGallery/<int:id>',views.ViewGallery,name="ViewGallery"),

       
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),



    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('Logout/',views.Logout, name="Logout"),


]