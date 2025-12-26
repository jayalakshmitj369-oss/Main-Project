from django.urls import path
from Admin import views
app_name="Admin"
urlpatterns = [
     path('HomePage/',views.HomePage, name="HomePage"),

     path('District/',views.District, name="District"),
     path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
     path('editdistrict/<int:eid>',views.EditDistrict,name="EditDistrict"),

     path('Category/',views.Category, name="Category"),
     path('deletecategory/<int:cid>',views.DeleteCategory,name="DeleteCategory"),
     path('editcategory/<int:eid>',views.EditCategory,name="EditCategory"),

     path('Place/',views.Place, name="Place"),
     path('deleteplace/<int:did>',views.DeletePlace,name="DeletePlace"),
     path('editplace/<int:eid>',views.EditPlace,name="EditPlace"),

     path('Subcategory/',views.Subcategory, name="Subcategory"),
     path('deletesubcategory/<int:did>',views.DeleteSubcategory,name="DeleteSubcategory"),
     path('editsubcategory/<int:eid>',views.EditSubcategory,name="EditSubcategory"),

     path('AdminRegistration/',views.AdminRegistration, name="AdminRegistration"),
     path('deleteadmin/<int:did>',views.DeleteAdmin,name="DeleteAdmin"),

     path('UserList/',views.UserList, name="UserList"),

     path('ViewComplaint/',views.ViewComplaint, name="ViewComplaint"),
     
     path('Reply/<int:eid>',views.Reply, name="Reply"),

     path('ArtType/',views.ArtType, name="ArtType"),
     path('deletearttype/<int:did>',views.DeleteArtType,name="DeleteArtType"),

     path('ArtSubType/',views.ArtSubType, name="ArtSubType"),
     path('deleteartsubtype/<int:did>',views.DeleteArtSubType,name="DeleteArtSubType"),

     path('ArtistVerification/',views.ArtistVerification, name="ArtistVerification"),
     path('ArtistAccept/<int:aid>',views.ArtistAccept,name="ArtistAccept"),
     path('ArtistReject/<int:rid>',views.ArtistReject,name="ArtistReject"),

     path('ViewFeedback/',views.ViewFeedback, name="ViewFeedback"),

    
]