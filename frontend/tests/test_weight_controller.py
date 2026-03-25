import pytest
from frontend.controllers.weight_controller import WeightController

@pytest.fixture

def controller():
    # デバック用で1とする
    return WeightController(user_id=1)

def test_create_and_update_weight(controller):
    date = "2026-03-26"
    weight = 60.4
    # 保存
    controller.save_weight(date,weight)
    # 取り出す
    data = controller.get_weight(date)
    # 確認
    assert len(data) == 1
    assert data[0]["weight"] == weight
    # 更新
    new_weight = 65
    controller.save_weight(date,new_weight)
    data =controller.get_weight(date)
    assert len(data) == 1
    assert data[0]["weight"] == 65