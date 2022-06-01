"""
This file handles all the URLs of my web application.
This file has the lists of all the endpoints that we will have for our website.
"""
from django.contrib import admin
from django.urls import path, include


url_patterns = [
    path('admin/', admin.site.urls),
    path('sayHello/', include('app.urls'))
]
