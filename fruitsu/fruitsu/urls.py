from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from users.views import *


from fruitsu import settings
from main_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('register/', user_views.register, name='register'),
    path('', include('users.urls')),
    path('UserProfile/', profile),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = pageNotFound
