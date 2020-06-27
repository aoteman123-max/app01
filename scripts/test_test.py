import allure


class Testtest:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("我是测试步骤")
    def test_01(self):
        print("11111")
        allure.attach("我是步骤描述的内容","附件名字")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_03(self):
        assert True