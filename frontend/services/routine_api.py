# api通信
import requests

API_ROUTINE_URL = "http://localhost:8000/api/routines/"
API_RECORD_URL = "http://localhost:8000/api/routinerecords/"

# 一覧を取ってくる マスターの方　userだけでいい
def get_routines(user_id):
    return requests.get(API_ROUTINE_URL,params={"user":user_id}).json()

# 記録を取ってくる ログ  userと　routine と日　が必要
def get_record(user_id,routine_id,date):
    return requests.get(API_RECORD_URL,params={"user":user_id,"routine":routine_id,"date":date}).json()
# recordを新しく作る userはいらない？ dataに入っているはず
# dataの中身は routine_record(model)の中身と同じ user routine date done
def create_record(data):
    return requests.post(API_RECORD_URL,json=data)

# record を更新する record_id と data にuseridがある？
# dataの中身は routine_record(model)の中身と同じ user routine date done
def update_record(record_id,data):
    return requests.put(f"{API_RECORD_URL}{record_id}/",json=data)

# routine を作成する
# dataの中身は routine(model)の中身と同じ user name
def create_routine(data):
    return requests.post(API_ROUTINE_URL,json=data)

