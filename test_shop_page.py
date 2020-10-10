import pytest

from .pages.shop_page import serviceability_link_shops


class TestsGeneral():
    def test_the_performance_of_the_reference_stores_code(self):
        """проверка исправности формы авторизации для гостей"""
        file_database_settings = "pages/database_access.txt"
        serviceability_link_shops(file_database_settings)