# -*- coding: utf-8 -*-

import pytest
from my_package.lbd.hello import handler

def test():
    response = handler(event={"name": "alice"}, context=None)
    assert response["message"] == "hello alice"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
