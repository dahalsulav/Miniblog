from django.urls import path
from blogs.views import blogdetails, bloglist
urlpatterns = [ 
    path('',bloglist),
    path('<id>/',blogdetails),
]
