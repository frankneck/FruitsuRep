from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from fruitsu import settings
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('login/', include('main_app.urls'))
]

handler404 = pageNotFound
