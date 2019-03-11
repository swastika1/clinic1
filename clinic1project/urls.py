from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import clinic1app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic1app.urls')),
    path('summernote/', include('django_summernote.urls')),
    #path('admin/', admin.site.urls),
    # jadhbvfjadsbdjdfjsdbvf


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
