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
from playapp.views import ChecklistCreate, ChecklistUpdateView, PlayDetailView, PlaylistView, \
    PlayCreateView, PlayPreviousListView

urlpatterns = [
    # path('', views.index, name="index"),
    path('', PlaylistView.as_view(), name="index"),
    path('play/', PlayCreateView.as_view(), name="create-play"),
    path('previous/', PlayPreviousListView.as_view(), name="play-previous"),
    path('play/<int:play_id>/', PlayDetailView.as_view(), name="view-play"),
    path('play/<int:play_id>/item/', ChecklistCreate.as_view(), name="create-item"),
    path('play/<int:play_id>/item/<int:check_id>/', ChecklistUpdateView.as_view(), name="check-item"),
    
    
    path('play/<int:play_id>/delete/', views.index, name="play-delete"),
    path('play/<int:play_id>/item/<int:check_id>/delete/', views.index, name="delete-item"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
