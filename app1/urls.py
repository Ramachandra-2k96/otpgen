from django.urls import path
from app1.views import home,generateOTP
urlpatterns = [
	path('',home),
 	path('generateotp',generateOTP),
]