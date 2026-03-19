from rest_framework import serializers
from health.models import Weight, RouteineRecord,Routine  

# 1 最初に、作った。
class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'

class RoutineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteineRecord
        fields = '__all__'
