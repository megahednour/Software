#!/usr/bin/python

from boto3.session import Session

session = Session(aws_access_key_id='AKIAJNE22F7SSLQUXJNA',aws_secret_access_key='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')

s3 = session.resource('s3')
s3.create_bucket(Bucket='mysessionBucket1983')

