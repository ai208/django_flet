from rest_framework import viewsets
from .serializers import WeightSerializer, RoutineRecordSerializer,RoutineSerializer
from health.models import Weight, RouteineRecord,Routine

# Create your views here.
# 2 Serializer の後に作った
class WeightViewSet(viewsets.ModelViewSet):
    # all はやめたほうがいい。後で、変更する
    # queryset = Weight.objects.all() 
    serializer_class = WeightSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        return Weight.objects.filter(user=self.request.user)
    # 作成の時、自動で認識する
    def perform_create(self,serialiser):
        serialiser.save(user=self.request.user)
        
    
# Routineも必要
class RoutineViewSet(viewsets.ModelViewSet):
    # queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        return Routine.objects.filter(user=self.request.user)
    # 作成の時、自動で認識する
    def perform_create(self,serialiser):
        serialiser.save(user=self.request.user)

class RoutineRecordViewSet(viewsets.ModelViewSet):
    # allはやめたほうがいい。
    # queryset = RouteineRecord.objects.all()
    serializer_class = RoutineRecordSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        return RouteineRecord.objects.filter(user=self.request.user)
    # 作成の時、自動で認識する
    def perform_create(self,serialiser):
        serialiser.save(user=self.request.user)
