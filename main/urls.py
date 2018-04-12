from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('pooltracker/', include('pooltracker.urls')),
]
