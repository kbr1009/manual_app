from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_title = 'manualapp管理画面' 
admin.site.site_header = 'ManualApp管理画面' 
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('manual/', include('manual.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

