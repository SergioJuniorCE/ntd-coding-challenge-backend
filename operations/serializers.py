from rest_framework import serializers

from operations.models import Operation


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
