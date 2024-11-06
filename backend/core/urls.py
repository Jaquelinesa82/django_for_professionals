from django.urls import path
from backend.core import views


app_name='core'

urlpatterns = [
    path('',views.home, name='home'),
]
