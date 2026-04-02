import flet as ft
from controllers.weight_controller import WeightController
from views.weight_view import WeightView  # WeightView のパスに合わせて
# viewの確認用
# 体重記録　アプリ
def main(page: ft.Page):
    page.title = "体重管理アプリ"
    page.vertical_alignment = ft.MainAxisAlignment.START #これの意味は？

    # ユーザーIDはテスト用に 1 固定
    user_id = 1
    controller = WeightController(user_id)

    # WeightView 作成
    weight_view = WeightView(page, controller)
    page.add(weight_view.build())

if __name__ == "__main__":
    ft.app(target=main)
