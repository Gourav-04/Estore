from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('tracker/',views.tracker,name="TrackStatus"),
    path('search/',views.search,name="Search"),
    path('productView/',views.productView,name="productView"),
    path('checkout/',views.checkout,name="checkout"),
]