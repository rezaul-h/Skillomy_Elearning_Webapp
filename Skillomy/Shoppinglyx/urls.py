
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('teacher/', admin.site.urls,name='teacher'),
    path('', include('app.urls')),
    path('', include('django.contrib.auth.urls'))   
]
