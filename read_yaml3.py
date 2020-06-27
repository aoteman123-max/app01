import os

import pytest
import yaml


def sum_data():
    with open("./data" + os.sep + "data4.yaml", "r", encoding="utf-8")as f:
        data = yaml.safe_load(f)
        list_data = []
        for i in data.values():
            list_data.append((i.get("a"), i.get("b"), i.get("c")))
    return list_data


class Test:
    @pytest.mark.parametrize("a,b,c", sum_data())  # 多个参数在一对双引号内容
    def test_012_1(self, a, c, b):  # 注意parametrize参数名字和个数必须和测试方法参数一致
        """计算 a+b == c"""
        print("\n{}+{}={}".format(a, b, c))
        # 断言
        assert a + b == c
