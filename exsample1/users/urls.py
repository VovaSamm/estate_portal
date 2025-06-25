from django.urls import path
from example_app.views import index

from exsample1.exsample1.urls import urlpatterns

urlpatterns=[
    path('',index)
]