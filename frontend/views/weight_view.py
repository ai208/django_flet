import flet as ft
from datetime import date
# from controllers.weight_controller import WeightController # routineでは要らなかった save weight を呼ぶから必要
# 消しても動いた。

class WeightView:
    def __init__(self,page,controller):
        self.page = page
        self.controller = controller
        self.container = ft.Column() #refresh 用　Routineと同じ

        # 入力フォーム
        self.weight_input=ft.TextField(label = "今日の体重(kg)")
        self.save_button = ft.ElevatedButton("保存",on_click=self.save_weight)
        self.result_text = ft.Text("")

    def save_weight(self,e):
        today = str(date.today())
        value = self.weight_input.value.strip()
        if not value:
            return
        try: #数字であることの確認
            weight = float(value)
        except ValueError:
            self.result_text.value = "数字を入力してください"
            self.page.update()
            return
        # controller に保存
        self.controller.save_weight(today,weight)
        self.result_text.value=f"今日の体重は{weight}kgで保存されました。"
        self.weight_input.value ="" #入力欄をクリアする
        self.refresh()
    #更新する
    def refresh(self):
        self.container.controls = self.build().controls
        self.page.update()
    # UIの作成
    def build(self):
        self.container.controls = ft.Column(
            controls =[
                ft.Row(
                    controls=[
                        self.weight_input,
                        self.save_button
                    ]
                ),
                self.result_text
            ]
        )
        return self.container
