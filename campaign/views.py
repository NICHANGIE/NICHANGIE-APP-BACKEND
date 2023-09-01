from rest_framework import generics, permissions
from .models import FundraisingCampaign
from .serializers import CampaignSerializer


class CampaignList(generics.ListCreateAPIView):
    queryset = FundraisingCampaign.objects.all()
    serializer_class = CampaignSerializer
    
    
class CampaignDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FundraisingCampaign.objects.all()
    serializer_class = CampaignSerializer
