import boto3
import json
from moto import mock_aws

@mock_aws
def main():
 
    ec2 = boto3.client("ec2", region_name="us-east-1")
    s3 = boto3.client("s3", region_name="us-east-1")

    
   
    s3.create_bucket(Bucket="my-test-bucket")

    ec2.run_instances(
        ImageId="ami-12345678",  # Dummy AMI
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

  
    ec2_response = ec2.describe_instances()
    ec2_instances = []

    for reservation in ec2_response["Reservations"]:
        for instance in reservation["Instances"]:
            ec2_instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })


    s3_response = s3.list_buckets()
    s3_buckets = [bucket["Name"] for bucket in s3_response["Buckets"]]

    
    final_output = {
        "EC2_Instances": ec2_instances,
        "S3_Buckets": s3_buckets
    }

    print("\nAWS Resource Summary (Mocked):\n")
    print(json.dumps(final_output, indent=4))


    with open("aws_output.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("\nOutput saved to aws_report.json successfully!")

if __name__ == "__main__":
    main()