from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path("register", views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('editor', views.editor_view, name='editor')
]
