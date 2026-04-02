import flet as ft
from controllers.routine_controller import RoutineController
from views.routine_view import RoutineView
# ここで展開する　dashboard でする。
# 
def main(page):
    routine_controller = RoutineController(user_id=1)
    routine_view = RoutineView(page,routine_controller)
    page.add(routine_view.build())

ft.app(target=main)