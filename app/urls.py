from django.urls import path

from app import views

app_name='app'

urlpatterns=[
    path('specific_template/',views.specific_template,name='specific_template'),
]