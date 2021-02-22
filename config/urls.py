from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.site.site_title = 'manualapp管理画面' 
admin.site.site_header = 'ManualApp管理画面' 
admin.site.index_title = 'メニュー'

urlpatterns = [
    path('', include('accounts.urls')),
    path('manual/', include('manual.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
