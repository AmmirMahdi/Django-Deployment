from django.urls import path
from first_app import views


app_name = 'first_app'
urlpatterns = [

    path(r'',views.index, name='index'),
    path(r'about/',views.about, name='about'),
    path(r'login/',views.form, name='form'),
    path(r'postform/',views.postform, name='post_form'),
    path(r'other/', views.other, name='other'),

    # register url
    path(r'register/', views.register, name='register'),


    path(r'user_login/', views.user_login, name='user_login')


]
