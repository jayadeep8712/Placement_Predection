from django.urls import path
from .import views

urlpatterns = [
    path("home",views.home,name='homepage'),
    path("about",views.about,name='aboutpage'),
    path("courses",views.courses,name='coursespage'),
    path("team",views.team,name='teampage'),
    path("testimonial",views.testimonial,name='testimonialpage'),
    path("error_",views.error_,name='error_page'),
    path("contact",views.contact,name='contactpage'),
    path("login",views.login,name='loginpage'),
    path("signup",views.signup,name="signuppage"),
    path("placement",views.placement,name="placementpage"),
    path("prediction",views.prediction,name="predictpage")
]