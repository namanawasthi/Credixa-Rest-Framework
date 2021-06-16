from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Bank',views.BankAPIView,basename='bank')
router.register(r'Branch',views.BranchAPIView,basename='branch')
router.register(r'BankBranch',views.BankBranchView,basename='BankBranch')

urlpatterns = [
    path('',include(router.urls)),
    ]
