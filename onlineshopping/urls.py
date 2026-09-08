from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp import views
from myapp.views import (
    about,
    best,
    buy,
    home,
    kid,
    login_view,
    men,
    mobile,
    page,
    shopping,
    signup_view,
    toy,
    women,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # यहाँ name='home' होना ज़रूरी है
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('page/', page, name='page'),
    path('shopping/', shopping, name='shopping'),
    path('best/', best, name='best'),
    path('mobile/', mobile, name='mobile'),
    path('women/', women, name='women'),
    path('men/', men, name='men'),
    path('toy/', toy, name='toy'),
    path('kid/', kid, name='kid'),
    path('about/', about, name='about'),
    path('buy/', buy, name='buy'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_view, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)