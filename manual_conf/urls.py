from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('manual/', include('manual.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
