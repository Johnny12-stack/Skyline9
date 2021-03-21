from django.urls import path
from .views import BagView
from . import views

urlpatterns = [
    path('', BagView.as_view(), name="BagView"),

]