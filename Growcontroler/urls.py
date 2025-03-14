from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('webinterface.urls')),
    path('admin/', admin.site.urls),
]
