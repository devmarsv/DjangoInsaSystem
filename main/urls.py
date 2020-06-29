from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='main_index'),
    path('', views.index, name='main_loginView'),
    path('login/', views.login, name='main_login'),
    path('logout/', views.logout, name='main_logout'),
    path('index/download/', views.download, name='main_download'),
    path('index/inputForm/', views.inputForm, name='main_inputForm'),
    path('index/SearchForm/', views.SearchForm, name='main_SearchForm'),
    path('index/SearchFormAjax/', views.SearchFormAjax, name='main_SearchFormAjax'),
    path('index/download/', views.download, name='main_download'),
    path('index/register/', views.register, name='main_register'),
    path('index/idchk/',views.idchk, name='main_idchk'),
    path('index/UpdateForm/',views.updateForm, name='main_UpdateForm'),
    path('index/Update/',views.update, name='main_Update'),

]
