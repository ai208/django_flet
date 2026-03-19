import flet as ft
import requests
from datetime import date

API_URL = "http://localhost:8000/api/weights/"  # Django API URL

def main(page: ft.Page):
    page.title = "体重入力"

    # 入力欄
    weight_input = ft.TextField(label="今日の体重 (kg)", keyboard_type=ft.KeyboardType.NUMBER)

    # 送信ボタンの処理
    def submit_click(e):
        weight_value = weight_input.value

        # 1️⃣ 数字チェック
        try:
            weight_float = float(weight_value)
        except ValueError:
            page.dialog = ft.AlertDialog(title=ft.Text("エラー"), content=ft.Text("数字を入力してください"))
            page.dialog.open = True
            page.update()
            return

        today_str = str(date.today())

        # 2️⃣ 今日のデータがあるか確認
        try:
            response_get = requests.get(API_URL, params={"user": 1, "date": today_str})  # user=1 はテスト用
            response_get.raise_for_status()
        except Exception as ex:
            page.dialog = ft.AlertDialog(title=ft.Text("エラー"), content=ft.Text(f"データ取得失敗: {ex}"))
            page.dialog.open = True
            page.update()
            return

        data_list = response_get.json()

        # 3️⃣ PUT or POST
        if len(data_list) > 0:
            # データが存在 → PUT
            weight_id = data_list[0]["id"]
            data = {"weight": weight_float, "date": today_str}
            response = requests.put(f"{API_URL}{weight_id}/", json=data)
        else:
            # データがない → POST
            data = {"weight": weight_float, "date": today_str}
            response = requests.post(API_URL, json=data)

        # 4️⃣ 成功時の処理
        if response.status_code in (200, 201):
            page.dialog = ft.AlertDialog(title=ft.Text("完了"), content=ft.Text("体重を保存しました"))
            page.dialog.open = True
            page.update()
            weight_input.value = ""
            page.update()
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("エラー"), content=ft.Text(f"保存に失敗しました: {response.status_code}"))
            page.dialog.open = True
            page.update()

    submit_button = ft.ElevatedButton("送信", on_click=submit_click)

    # ページに追加
    page.add(weight_input, submit_button)

ft.app(target=main)
