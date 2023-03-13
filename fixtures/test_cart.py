import pytest

@pytest.fixture
def setup():
    print("open browser")
    print("login")
    print("browse the products")

    yield
    print("log off")
    print("close the browser")

def testaddtocart(setup):
    print("add to cart success")

def testdelcart(setup):
    print("delete to cart success")