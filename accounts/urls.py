from django.urls import path
from .views import SignUp
from .views import user_profile

urlpatterns = [

    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', user_profile, name='user_profile'),


]