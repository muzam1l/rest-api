from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BranchesSerializer
from rest_framework.decorators import action
from .models import Bank, Branch

class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('ifsc')
    serializer_class = BranchesSerializer
    def get_queryset(self):
        city = self.request.query_params.get('city')
        bank_name = self.request.query_params.get('bank_name')
        qs = Branch.objects.all()
        if city is not None:
            qs = qs.filter(city=city)
        if bank_name is not None:
            bank_id = None
            try:
                bank_id = Bank.objects.get(name=bank_name)
            except Bank.DoesNotExist as err:
                pass
            qs = qs.filter(bank=bank_id)
        return qs
