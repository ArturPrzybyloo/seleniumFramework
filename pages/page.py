from tests.admin.base_admin import BasePageAdmin


class Page(BasePageAdmin):

    def test_cos(self):
        self.driver.get("https://selenium-python.readthedocs.io/page-objects.html")
        assert "adssada" in self.driver.title
        pass
