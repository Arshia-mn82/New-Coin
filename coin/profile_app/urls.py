from django.urls import path

from .views import *

urlpatterns = [
    path('welcome/' , welcome),
    path('profile/' , ProfileView.as_view()),
    path('token/' , Login.as_view()),
    path('token/refresh/' , Refresh.as_view()),
    path('savingplan/' , SavingPlanView.as_view()),
    path('savingplan/<int:pk>' , SavingPlanView.as_view()),

]