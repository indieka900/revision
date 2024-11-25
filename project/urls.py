from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('firstApp.urls')),
    path('', include('thirdApp.urls')),
    # path('app2/', include('secondApp.urls')),
    path('stk/', include('stk.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
