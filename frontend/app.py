import flet as ft
from views.dashboard_view import DashboardView
# dashboard 完成した。
def main(page: ft.Page):
    page.title = "ホーム画面"
    user_id = 1
    dashboard_view= DashboardView(page,user_id)
    page.add(dashboard_view.build())

if __name__ == "__main__":
    ft.app(target=main)
