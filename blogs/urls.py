from django.urls import path
from blogs.views import blogdetails, bloglist, deleteblog
urlpatterns = [ 
    path('',bloglist),
    path('<id>/',blogdetails),
    path('<id>/delete/',deleteblog),
]
