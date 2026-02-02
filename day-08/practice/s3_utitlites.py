import boto3
import boto3.session

class AWSUtils:
    def __init__(self):
        self.s3 = self.get_connection("s3")
        self.ec2 = self.get_connection("ec2")

    def get_connection(self,service):
        boto3.session(access="ADSLDNASKLJND")
        return boto3.client(service) # creating a client for S3 so that it can call APIs

    def show_buckets(self):
        response = self.s3.list_buckets()

        for bucket in response["Buckets"]:
            print(bucket["Name"])

    def create_bucket(self, bucket_name):
        try:
            response = self.s3.create_bucket(
                Bucket=bucket_name, 
                CreateBucketConfiguration={
                'LocationConstraint': 'us-west-2',
            },)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print("Bucket created successfully")
            else:
                print("Error occured while creating the bucket")

        except:
            print("Error occured")
        
    def show_regions(self):
        response = self.ec2.describe_regions()

    def upload_to_bucket(self, file_path,bucket_name,key_name):
        self.s3.upload_file(file_path,bucket_name,key_name)
        print("File uploaded successfully")

print("Start")
if __name__ == "__main__": # ye file ka jo execution hoga vo if confition ke andar hoga
    print("Enter")
    aws = AWSUtils()
    print("hello from AWS Class wali file")
    aws.show_buckets()

print("Exit")