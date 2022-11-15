from django.contrib import admin
from django.urls import path, re_path,include
from django.views.static import serve
from my_task import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/employee/',include(('api.employee.urls', 'web'), namespace='api_employee')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
