import pytest

from .pages.checking_urls_shops import serviceability_link_shops_user_read


@pytest.mark.links_shops
class TestGeneral():
    def test_the_performance_of_the_reference_stores_code(self):
        """проверка целостности ссылок магазинов"""
        file_database_settings = "pages/database_access.txt"
        serviceability_link_shops_user_read(file_database_settings)

class TestShopPage():
    pass
