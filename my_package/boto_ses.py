# -*- coding: utf-8 -*-

import boto3

def assume_role(role_arn, session_name):
    sts_client = boto3.client("sts")
    response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=session_name)
    boto_ses = boto3.session.Session(
        aws_access_key_id=response["Credentials"]["AccessKeyId"],
        aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
        aws_session_token=response["Credentials"]["SessionToken"],
    )

    return boto_ses

role_arn = "arn:aws:iam::669508176277:role/sanhe-assume-role-for-iam-test"
session_name = "assume-role-session"
boto_ses = assume_role(role_arn, session_name)
