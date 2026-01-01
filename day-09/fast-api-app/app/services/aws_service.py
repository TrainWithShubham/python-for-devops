import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def get_aws_resources():
    try:
        ec2 = boto3.client("ec2")
        s3 = boto3.client("s3")
        ec2_instances = []
        for r in ec2.describe_instances().get("Reservations", []):
            for i in r.get("Instances", []):
                ec2_instances.append({
                    "instance_id": i.get("InstanceId"),
                    "state": i.get("State", {}).get("Name")
                })
        s3_buckets = [b["Name"] for b in s3.list_buckets().get("Buckets", [])]
        return {"ec2_instances": ec2_instances, "s3_buckets": s3_buckets}
    except NoCredentialsError:
        return {"error": "AWS credentials not configured"}
    except ClientError as e:
        return {"error": str(e)}
