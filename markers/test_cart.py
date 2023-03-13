import pytest


@pytest.mark.regression
def testaddtocart():
    print("add to cart success")

@pytest.mark.sanity
def testdelcart():
    print("delete to cart success")