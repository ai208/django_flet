import flet as ft
from datetime import date
# UIの作成
class RoutineView:
    def __init__(self,page,controller):
        self.page = page
        self.controller = controller
        self.container = ft.Column() # refreshについて
        # 入力フォーム
        self.routine_input=ft.TextField(
            label = "新しい習慣を追加"
        )
    # e on_change用
    def add_routine(self,e):
        name = self.routine_input.value.strip() # 空白を取る
        # なければ何もしない
        if not name:
            return
        self.controller.add_routine(name)
        self.routine_input.value = "" # 空白に戻す
        # self.page.controls.clear() #追加 必要な理由?
        # self.page.add(self.build()) # 追加 必要な理由?
        # self.page.update()
        self.refresh()

        #pageの更新
    def refresh(self):
        self.container.controls = self.build().controls
        self.page.update()
    #UIの作成
    def build(self):
        today = str(date.today())
        #追加 2026年3月25日 2つしか表示されない →　治らない
        self.controller.ensure_today_records(today)

        routines = self.controller.get_today_routine_status(today)
        checkboxes = []
        for routine in routines:
            cb = ft.Checkbox(
                label=routine["name"],
                value=routine["done"],
                on_change=lambda e,
                rid=routine["id"]: # 二個目の引数
                self.controller.toggle_record(
                    rid,
                    e.control.value, #true or false
                    today
                )
            )
            checkboxes.append(cb)
        self.container.controls= ft.Column(
            controls=[
                ft.Row(
                    controls = [
                        self.routine_input,
                        # Elevated Button イベントボタンでない理由は？
                        ft.ElevatedButton(
                            "追加",
                            on_click=self.add_routine
                        )
                    ]),
                    *checkboxes
            ])
        return self.container
