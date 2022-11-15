from django.conf.urls import url, re_path

from . import views

urlpatterns = [
    re_path(r'', views.employee, name='employee'),
    re_path(r'^edit-employee/$', views.edit_employee, name='edit_employee'),

]
