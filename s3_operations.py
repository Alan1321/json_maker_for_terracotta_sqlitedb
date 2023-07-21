import json
import boto3

def read_bucket(bucket_name, prefix):
    """
    Reading all files data from a s3 bucket specific folder (prefix) and return the data back
    """
    data = []
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name,Prefix=prefix)
    while True:
        for obj in response.get('Contents', []):
            data.append(obj)

        # check if there are more pages to retrieve
        if response['IsTruncated']:
            response = s3.list_objects_v2(Bucket=bucket_name,ContinuationToken=response['NextContinuationToken'])
        else:
            break
    return data

