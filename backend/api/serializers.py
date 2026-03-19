from rest_framework import serializers
from health.models import Weight, RoutineRecord,Routine

# 1 最初に、作った。 Vaildation をしないといけない。　
class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
        extra_kwargs = {
            "user": {"read_only": True}  # ← これがないと必須扱いになる　練習用
        }

class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'
        extra_kwargs = {
            "user": {"read_only": True}  # ← これがないと必須扱いになる
        }

class RoutineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineRecord
        fields = '__all__'
        extra_kwargs = {
            "user": {"read_only": True}  # ← これがないと必須扱いになる
        }
