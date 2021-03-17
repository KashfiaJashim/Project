"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Profile import views as profileView
from Artwork import views as Artworkview
from Blog import views as Blog_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', profileView.showHome, name='homepage'),
    path('signup/', profileView.registration, name='signup'),
    path('createProfile/', profileView.createprofile, name='createProfile'),
    path('showProfile/', profileView.showProfile, name='showProfile'),
    path('ShowArtwork/', Artworkview.showArtwork, name='ShowArtwork'),
    path('InsertArtwork/', Artworkview.insertArtwork, name='InsertArtwork'),
    path('ShowBlogs/', Blog_views.showBlog,name='ShowBlogs'),
    path('ShowBlogs/<int:b_id>', Blog_views.showDetails, name='detail_view'),
    path('InsertBlogs/', Blog_views.insertBlog,name='InsertBlogs'),
    path('accounts/',include('django.contrib.auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
