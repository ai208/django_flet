# from services.routine_api import *
import services.weight_api as weight_api
# 相対パスと絶対パス　テストの時に異常があった テストが動くようにすると、通常で動かない
# controller
# get と save の二つ
# save では場合分けがある。

class WeightController:
    def __init__(self,user_id):
        self.user_id = user_id

    def get_weight(self,date):
        return weight_api.get_weight(date)

    def save_weight(self,date,weight):
        data = self.get_weight(date)
        if len(data)==0: #データなし　新規作成
            weight_api.create_weight({"date":date,"weight":weight})
        else: #更新
            weight_api.update_weight(data[0]["id"],{"date":date,"weight":weight})

