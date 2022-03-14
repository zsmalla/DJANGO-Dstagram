from django.urls import path

from .views import *

# 2차 URL 파일
app_name = 'photo'

urlpatterns = {
    path('', photo_list, name='photo_list'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
}