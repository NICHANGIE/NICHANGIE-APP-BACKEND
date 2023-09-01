from rest_framework import serializers
from .models import FundraisingCampaign


class CampaignSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = FundraisingCampaign