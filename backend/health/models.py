from django.db import models
from django.conf import settings
# Weight とルーティンとルーティンのログを作る

# 体重のクラス　フロントエンドから受け取る　id をuuidにした方がいいかもしれない。　後でする
class Weight(models.Model):
    # accountと紐づけ
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # 時系列データが必要
    date = models.DateField()
    # メインロジック
    weight = models.FloatField()
    # 一日一回
    class Meta:
        unique_together = ('user','date')
    def __str__(self):
        return f"{self.user.username}-{self.date}-{self.weight}kg"

# Routine
class Routine(models.Model):
    #account と紐づけ
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.user.username}-{self.name}"

# 記録　分析のロジック
class RoutineRecord(models.Model):
    #accountと紐づけ
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #routineと紐づけ
    routine= models.ForeignKey(Routine,on_delete=models.CASCADE)
    #時系列データが必要
    date = models.DateField()
    #true or false
    done = models.BooleanField(default=False)
    #一タスク一回
    class Meta:
        unique_together=('user','routine','date')
    def __str__(self):
        return f"{self.user.username}-{self.routine.name}-{self.date}-{'済み' if self.done else '未'}"


