# from services.routine_api import *
import services.routine_api as routine_api
# controller

class RoutineController:
    # 初期化する
    def __init__(self,user_id):
        self.user_id = user_id
    # 一覧を取得
    def get_routines(self):
        return routine_api.get_routines(self.user_id) # 再帰になっていた

    #recordの保存
    def toggle_record(self,routine_id,done,date):
        #recordを取ってくる 日で指定する
        data_list=routine_api.get_record(self.user_id,routine_id,date)
        # routine_record modelのfield
        data = {
            "done":done,
            "routine":routine_id,
            "user":self.user_id,
            "date":date
        }
        # data_list があれば　アップデート　なければ新規作成
        if len(data_list)==0: #データがないときは
            routine_api.create_record(data)
        else:# データがあるとき
            routine_api.update_record(data_list[0]["id"],data)

    #追加する
    def add_routine(self,name):
        # routine modelのfield
        data={
            "name":name,
            "user":self.user_id
        }
        routine_api.create_routine(data)
    # 本日の状態を取ってくる
    def get_today_routine_status(self,date):
        routines = self.get_routines()
        result = [] #id, name, done を持つ　date はいらない
        for routine in routines:
            # 記録を取る 今日のもの
            record = routine_api.get_record(self.user_id,routine["id"],date)
            done = False
            # あれば　そのデータを使って done を更新する
            # 空データをはじく
            if len(record) > 0:
                done = record[0]["done"]
            result.append({
                "id":routine["id"],
                "name":routine["name"],
                "done":done
            })
        return result
    # 2件しか追加されないというバグが起きた。
    # 生成時に、確認する関数を作る
    def ensure_today_records(self,date):
        routines = self.get_routines() #引数が要らない
        for routine in routines:
            record = routine_api.get_record(self.user_id,routine["id"],date)
            if len(record)==0: # result を追加した
                # dataの中身は routine_record(model)の中身と同じ user routine date done
                # createはこれ def create_record(data): dataで渡さないといけない
                routine_api.create_record({
                    "done":False,
                    "routine":routine["id"],
                    "user":self.user_id,
                    "date":date
                })





