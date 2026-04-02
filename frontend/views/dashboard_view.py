import flet as ft
from datetime import date #　日にちは必要
from controllers.weight_controller import WeightController
from controllers.routine_controller import RoutineController
from views.routine_view import RoutineView
from views.weight_view import WeightView

class DashboardView:
    def __init__(self,page,user_id):
        self.page = page
        self.user_id = user_id
        # コントローラーはviewの引数だから必要 クラスを呼ぶ
        self.weight_controller = WeightController(user_id)
        self.routine_controller = RoutineController(user_id)
        # viewを作る
        self.weight_view= WeightView(page,self.weight_controller)
        self.routine_view = RoutineView(page,self.routine_controller)

        #部品 の箱
        self.container= ft.Column()
    # 更新　routineとweightと繋ぐ？
    def refresh(self):
        # 両方とも更新する
        self.routine_view.refresh()
        self.weight_view.refresh()
        self.page.update()

    #UIの作成
    def build(self):
        self.container.controls = ft.Column(
            controls = [
                self.weight_view.build(),
                ft.Divider(),
                self.routine_view.build()
            ]
        )
        return self.container