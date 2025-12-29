import boto3
import boto3.session

class AWSUtils:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.buckets = []

    def show_buckets(self):

        for bucket in self.s3_client.list_buckets()["Buckets"]:
            self.buckets.append(bucket["Name"])


if __name__ == "__main__":
    aws_utils = AWSUtils()
    aws_utils.show_buckets()
    print(aws_utils.buckets)