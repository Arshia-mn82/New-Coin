from .models import *
from rest_framework.serializers import ModelSerializer

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        
class SavingPlanSerializer(ModelSerializer):
    class Meta:
        model = saving_plan
        fields = "__all__"