from django.urls import path
from .views import calendarevent, HomePageView

urlpatterns = [
    path('calendarevent', calendarevent),
    path('', HomePageView.as_view(), name='home'),
]
