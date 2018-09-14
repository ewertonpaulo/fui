from rest_framework import serializers
from .models import King

class KingSerialize(serializers.ModelSerializer):
    class Meta:
        model = King
        fields = (
            'id',
            'full_name',
            'rg',
            'cpf_cnpj',
            'phone',
            'email',
            'job',
            'andreess',
            'since'
        )