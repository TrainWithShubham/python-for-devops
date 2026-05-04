import boto3
import json

def get_connection(service):
    return boto3.client(service)

def list_buckets(client):
    response = client.list_buckets()
    names = []
    for bucket in response['Buckets']:
        print(bucket['Name']) # This shows it in the terminal
        names.append(bucket['Name'])
    return names 

def create_bucket(client, bucket_name):
    client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'us-east-2'},
    )
    msg = f"Bucket created successfully: {bucket_name}"
    print(msg) # This shows it in the terminal
    return msg

def show_regions(client):
    response = client.describe_regions()
    region_list = []
    for region in response['Regions']:
        print(region['RegionName']) # This shows it in the terminal
        region_list.append(region['RegionName'])
    return region_list

# --- The lines you mentioned are right here! ---

s3_client = get_connection('s3')
ec2_client = get_connection('ec2') 

user_provided_bucket_name = input("Enter the name of the bucket: ")

# We use your lines, but we put "status =", "buckets =", and "regions =" 
# in front so we can grab the data they produce.
status  = create_bucket(s3_client, user_provided_bucket_name)
buckets = list_buckets(s3_client)
regions = show_regions(ec2_client)

# --- Now we save everything we grabbed ---

final_output = {
    "creation_result": status,
    "all_buckets": buckets,
    "available_regions": regions
}

with open('output.json', 'w') as json_file:
    json.dump(final_output, json_file, indent=4)

print("\nAll done! Check your terminal for the output and output.json for the file.")