# -*- coding: utf-8 -*-

def handler(event, context):
    name = event.get("name", "Mr X")
    message = f"hello {name}"
    return {"message": message}
