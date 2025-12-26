from django.urls import path
from Artist import views
app_name="Artist" 

urlpatterns = [
     path('HomePage/',views.HomePage,name="HomePage"),
     path('MyProfile/',views.MyProfile,name="MyProfile"),
     path('EditProfile/',views.EditProfile,name="EditProfile"),

     path('EditProfile/',views.EditProfile,name="EditProfile"),
     path('ChangePassword/',views.ChangePassword,name="ChangePassword"),

     path('Artwork/',views.Artwork,name="Artwork"),
     path('AjaxSubtype/',views.AjaxSubtype,name="AjaxSubtype"),
     path('deleteartwork/<int:did>',views.DeleteArtwork,name="DeleteArtwork"),
     path('galleryartwork/<int:gid>',views.GalleryArtwork,name="GalleryArtwork"),

     path('ViewCustomerRequest/',views.ViewCustomerRequest, name="ViewCustomerRequest"),
     path('Accept/<int:aid>',views.Accept,name="Accept"),
     path('Reject/<int:rid>',views.Reject,name="Reject"),
     path('WorkUpdate/<int:id>/<int:status>',views.WorkUpdate,name="WorkUpdate"),
     

     path('ViewBooking/',views.ViewBooking,name="ViewBooking"),

     path('tracking/<int:id>/<int:status>',views.tracking,name="tracking"),

     path('Amount/<int:aid>',views.Amount, name="Amount"),

     path('Feedback/',views.Feedback, name="Feedback"),
    

     path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),


]