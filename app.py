# -*- coding: utf-8 -*-

import boto3
from my_package.lbd import hello
from chalice import Chalice

app = Chalice(app_name="my_app")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.handler(event, context)
