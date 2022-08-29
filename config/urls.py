"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from playapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('previous/', views.index, name="task-previous"),
    path('play/', views.index, name="play-create"),
    path('play/<int:play_id>/', views.index, name="view-play"),
    path('play/<int:play_id>/delete/', views.index, name="play-delete"),
    path('play/<int:play_id>/item/', views.index, name="create-item"),
    path('play/<int:play_id>/item/<int:item_id>/', views.index, name="check-item"),
    path('play/<int:play_id>/item/<int:item_id>/delete/', views.index, name="delete-item"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
