import boto3
import json



def get_connection(service):
    return boto3.client(service)


def list_buckets(client):

  response = client.list_buckets()
  for bucket in response['Buckets']:
         print(bucket['Name'])     


def create_bucket(client, bucket_name):
   
  response = client.create_bucket(
     Bucket= bucket_name,
     CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
 )

  print(f"Bucket created successfully: {bucket_name}")

def show_regions(client):
        response = client.describe_regions()
        for region in response['Regions']:
            print(region['RegionName'])

            
s3_client = get_connection('s3')
ec2_client = get_connection('ec2') 


user_provided_bucket_name = input("Enter the name of the bucket you want to create: ")

create_bucket(s3_client, user_provided_bucket_name)
list_buckets(s3_client)
show_regions(ec2_client)







