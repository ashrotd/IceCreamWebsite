
from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Ashrot IceCream Admin"
admin.site.site_title = "Ashrot IceCream Admin Portal"
admin.site.index_title = "Welcome to Ashrot IceCream"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
