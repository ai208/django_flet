import requests

API_URL = "http://localhost:8000/api/weights/"  # Django API URL

# 今回は、get　create と　update(save) user はrequest に入っているからいらない。
# routine も修正しないといけない？

#所得 get
def get_weight(date):
    return requests.get(API_URL,params={"date":date}).json()
# 戻り値がリスト

#新規作成 post data は　date weight user はバックエンドでする
def create_weight(data):
    return requests.post(API_URL,json=data)

# 更新 put
def update_weight(id, data):
    return requests.put(f"{API_URL}{id}/",json=data)
