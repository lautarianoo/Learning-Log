from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('learning_logs.urls')),
    url(r'^users/', include(('users.urls', 'users'), namespace='users'))
]
