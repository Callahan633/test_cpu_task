from rest_framework import serializers

from cpu_util.models import Record


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ('record_datetime', 'record_cpu_data',)

    def create(self, validated_data):
        return Record.objects.create(**validated_data)
