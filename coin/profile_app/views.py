from .models import *
from django.http.response import JsonResponse
from .serializer import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def welcome(requset):
    return JsonResponse("Welcoem to Coin" , safe=False)
class Login(TokenObtainPairView):
    pass


class Refresh(TokenRefreshView):
    pass


class ProfileView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class TransactionView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)
    
class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)
    

    
class SavingPlanView(ListCreateAPIView):
    queryset = saving_plan.objects.all()
    serializer_class = SavingPlanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)
    
class SavingPlanDetailView(RetrieveUpdateDestroyAPIView):
    queryset = saving_plan.objects.all()
    serializer_class = SavingPlanSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(profile=self.request.user.profile)
    
    
def increasing_saving(request , saving_id):
    if request.method == "POST":
        amount = request.POST.get("amount")
        query = saving_plan.objects.get(id = saving_id)
        query.current_amount += amount
        if query.current_amount >= query.target_amount:
            query.status = True
            return JsonResponse("Saving Completed" , safe=False)
        query.save()
        return JsonResponse("Saving Updated" , safe=False)
    
    

    
        