from rest_framework import serializers
from .models import Branch

class BranchesSerializer(serializers.HyperlinkedModelSerializer):
    # bank = serializers.RelatedField(source = 'name', read_only = True)
    bank = serializers.CharField(source='bank.name')
    class Meta:
        model = Branch
        fields = '__all__'
