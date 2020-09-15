from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('', views.ContactView.as_view(), name='home'),
]
