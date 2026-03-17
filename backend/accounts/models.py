from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    # メールログイン
    email = models.EmailField(unique=True,blank=False)
    #生年月日 bmiが子供と大人で違う　分析のために必要 最初は入力しない 後でマイページから
    birth_date = models.DateField(blank=True,null=True)

    #性別 女性の方が多いはずなので、femaleが先
    GENDER_CHOICES = [
        ("female","女性"),
        ("male","男性"),
        ("other","その他"),
    ]
    #任意入力
    gender = models.CharField(
        choices=GENDER_CHOICES,
        blank=True
    )
    # 目標体重 アプリの性質上必要 これがメインロジック
    target_weight=models.FloatField(blank=True,null=True)

    #ログインの時に使うフィールド
    USERNAME_FIELD = "email"
    # usernameさん　おはようございます　時間によって変化する とコメントを出したい
    REQUIRED_FIELDS = ["username"]
    def __str__(self):
        return self.username # 管理画面の表示

