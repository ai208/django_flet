from rest_framework import viewsets
from .serializers import WeightSerializer, RoutineRecordSerializer,RoutineSerializer
from health.models import Weight, RoutineRecord,Routine
from django.contrib.auth import get_user_model

# Create your views here.
# 2 Serializer の後に作った
class WeightViewSet(viewsets.ModelViewSet):
    # all はやめたほうがいい。後で、変更する router用で必要
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Weight.objects.filter(user=self.request.user)
        else:# createと同様にする
            User = get_user_model()
            return Weight.objects.filter(user=User.objects.get(id=1))
    # 作成の時、自動で認識する ユーザーを送らなくていい。
    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:# 確認用
            User = get_user_model()
            serializer.save(user = User.objects.get(id=1)) # objects が必要 get 単数 fileter 複数 の違い いつもは大体　fileter


# Routineも必要
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Routine.objects.filter(user=self.request.user)
        else:# createと同様にする
            User = get_user_model()
            return Routine.objects.filter(user=User.objects.get(id=1))
    # 作成の時、自動で認識する
    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:# 確認用
            User = get_user_model()
            serializer.save(user = User.objects.get(id=1)) # objects が必要 get 単数 fileter 複数 の違い いつもは大体　fileter

class RoutineRecordViewSet(viewsets.ModelViewSet):
    # allはやめたほうがいい。 router用で必要
    queryset = RoutineRecord.objects.all()
    # スペルミス
    serializer_class = RoutineRecordSerializer
    #ログインしているユーザーだけ
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return RoutineRecord.objects.filter(user=self.request.user)
        else:# createと同様にする
            User = get_user_model()
            return RoutineRecord.objects.filter(user=User.objects.get(id=1))
    # 作成の時、自動で認識する
    def perform_create(self,serializer):
        if self.request.user.is_authenticated: #いつもはサーバー側で受け取ってユーザーをセット
            serializer.save(user=self.request.user)
        else:# 確認用
            User = get_user_model()
            serializer.save(user = User.objects.get(id=1)) # objects が必要 get 単数 fileter 複数 の違い いつもは大体　fileter
