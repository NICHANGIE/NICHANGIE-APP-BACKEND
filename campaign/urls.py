from django.urls import path
from .views import CampaignList, CampaignDetails


urlpatterns = [
path('<int:pk>/', CampaignDetails.as_view()),
path('', CampaignList.as_view()),
]
