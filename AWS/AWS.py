import boto3
sts_client = boto3.client('sts')
assumedRoleObject = sts_client.assume_role(
    RoleArn="arn::aws:iam::865489921604:role/sit-MIFID-MM-DevTester-role",
    RoleSessionName="AssumeRoleSession1")
credentials = assumedRoleObject['Credentials']
s3_resource = boto3.resource(
    's3',
    aws_access_key_id = credentials['AKIAJCAIXM3K2YQINONA'],
    aws_secret_access_key = credentials['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'],
    aws_session_token = credentials['SessionToken'],)

for bucket in s3_resource.buckets.all():
    print(bucket.name)