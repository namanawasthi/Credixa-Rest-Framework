from django.shortcuts import render
from rest_framework import viewsets
from .models import Banks,Branchs
from . import serializers
from rest_framework import filters
import django_filters

    

class BankAPIView(viewsets.ModelViewSet):
    queryset = Banks.objects.all()
    serializer_class = serializers.BankSerializer

class BranchAPIView(viewsets.ModelViewSet):
    serializer_class = serializers.BranchSerializer
    queryset = Branchs.objects.all()


class BankBranchView(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BankBranchSerializer
    
    def get_queryset(self):
        queryset = Branchs.objects.all()
        ifsc = self.request.query_params.get('ifsc',None)
        city = self.request.query_params.get('city',None)
        bank_name = self.request.query_params.get('bank_name',None)

        if ifsc is not None:
            try:
                queryset = queryset.filter(ifsc=ifsc)
            except:
                pass
        if bank_name is not None:
            try:
                bank = Banks.objects.get(name=bank_name)
                queryset = queryset.filter(bank=bank)
            except:
                pass
        if city is not None:
            try:
                queryset = queryset.filter(city=city)
            except:
                pass

        return queryset
