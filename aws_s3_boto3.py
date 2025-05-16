#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro
"""
import boto3

s3 = boto3.client(service_name="s3")

# Listar todos os buckets:
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])

# Criar um bucket:
response = s3.create_bucket(Bucket="mysecondbuckets-eddy")
print(response)

# Deletar um bucket:
response = s3.delete_bucket(Bucket="mysecondbuckets-eddy")
print(response)
