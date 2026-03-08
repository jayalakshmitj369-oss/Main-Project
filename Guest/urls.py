from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('',views.index, name="index"),

    path('UserRegistration/',views.UserRegistration, name="UserRegistration"),
    path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),

    path('Login/',views.Login, name="Login"),

    path('ArtistRegistration/',views.ArtistRegistration, name="ArtistRegistration"),

    path('Forgotpassword/',views.Forgotpassword, name="Forgotpassword"),

    path('Newpassword/',views.Newpassword, name="Newpassword"),

    path('Otp/',views.Otp, name="Otp"),
]