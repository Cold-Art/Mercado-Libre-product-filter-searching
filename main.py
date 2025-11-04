import Locations


class TestMercado:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.actions = Locations.MercadoPage()

    def test_navigate(self):
        self.actions.navigate()

    def test_mercado_filter(self):
        self.actions.filters()

    def test_zipcode(self):
        self.actions.zipcode()

    def test_order_posts(self):
        self.actions.order_posts()

    def test_research(self):
        self.actions.research()

    @classmethod
    def teardown(cls):
        cls.driver.quit()