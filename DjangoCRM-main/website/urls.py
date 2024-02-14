from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.home, name='home'),
    #  path('login/', •views.login_user, • name='login'),
    path('logout/', views. logout_user, name= 'logout'),
    path('register/', views.register_user, name= 'register'),
    path('record/<str:pk>', views.customer_record, name= 'record'),
    path('delete/<str:pk>', views.delete_record, name= 'delete_record'),
    path('add_record/', views.add_record, name= 'add_record'),
    path('update_record/<str:pk>', views.update_record, name= 'update_record'),
    path('profiles/', views.Profile_List),
    path('profiles/<int:pk>', views.Profile_Detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)