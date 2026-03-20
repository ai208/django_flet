import flet as ft
import requests
from datetime import date

API_ROUTINE_URL = "http://localhost:8000/api/routines/"
API_RECORD_URL = "http://localhost:8000/api/routinerecords/"
USER_ID = 1  # テスト用

def main(page: ft.Page):
    page.title = "Routine 入力"

    today_str = str(date.today())
    routine_checkboxes = []

    # Routine 一覧を取得してチェックボックス生成
    def load_routines():
        routine_checkboxes.clear()
        page.controls.clear()  # ページをクリア
        try:
            response = requests.get(API_ROUTINE_URL, params={"user": USER_ID})
            response.raise_for_status()
            routines_list = response.json()
        except Exception as e:
            page.add(ft.Text(f"ルーチン取得失敗: {e}"))
            return

        for routine in routines_list:
            # 今日の状態に合わせて初期値設定
            done_value = False
            try:
                response_get = requests.get(API_RECORD_URL, params={"user": USER_ID, "routine": routine["id"], "date": today_str})
                response_get.raise_for_status()
                data_list = response_get.json()
                if data_list:
                    done_value = data_list[0]["done"]
            except:
                pass

            cb = ft.Checkbox(
                label=routine["name"],
                value=done_value,
                on_change=lambda e, rid=routine["id"]: on_checkbox_change(rid, e)
            )
            routine_checkboxes.append(cb)

        # 新規追加用 TextField + Button
        routine_input = ft.TextField(label="新しい習慣を入力")
        add_button = ft.Button(
            "追加",
            on_click=lambda e, tf=routine_input: add_routine(tf)
        )

        # ページに追加
        page.add(ft.Column([routine_input, add_button]+routine_checkboxes) )

        page.update()

    # チェックボックス変更時（即 PUT/POST）
    def on_checkbox_change(routine_id, e):
        done = e.control.value
        try:
            response_get = requests.get(API_RECORD_URL, params={
                "user": USER_ID, "routine": routine_id, "date": today_str
            })
            response_get.raise_for_status()
        except Exception as ex:
            print(f"取得失敗: {ex}")
            return

        data_list = response_get.json()

        if len(data_list) > 0:
            record_id = data_list[0]["id"]
            data = {"done": done, "routine": routine_id, "user": USER_ID, "date": today_str}
            requests.put(f"{API_RECORD_URL}{record_id}/", json=data)
        else:
            data = {"done": done, "routine": routine_id, "user": USER_ID, "date": today_str}
            requests.post(API_RECORD_URL, json=data)

    # 新しい Routine を追加
    def add_routine(textfield: ft.TextField):
        name = textfield.value.strip()
        if not name:
            return  # 空文字は無視
        data = {"name": name, "user": USER_ID}
        try:
            response = requests.post(API_ROUTINE_URL, json=data)
            response.raise_for_status()
            textfield.value = ""  # 入力欄をクリア
            load_routines()       # チェックボックス一覧を更新
        except Exception as e:
            print(f"ルーチン追加失敗: {e}")

    # 初回ロード
    load_routines()

ft.app(target=main)
