# -*- coding: utf-8 -*-

import pytest
from my_package.boto_ses import boto_ses

def test():
    s3_client = boto_ses.client("s3")
    s3_client.list_buckets()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
