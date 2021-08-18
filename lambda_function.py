import os
import json
import boto3

# make a change
# get env
env = os.environ.get("env")
# boto3 S3 initialization
s3_client = boto3.client("s3")



def lambda_handler(event, context):

   # Source
   source_bucket_name = event['Records'][0]['s3']['bucket']['name']
   source_file_key_name = event['Records'][0]['s3']['object']['key']

   # Destination
   destination_bucket_name = 'outbound-data-bucket'
   desitination_file_key_name = f'{env}/' + source_file_key_name

   # Copy Source Object
   copy_source_object = {'Bucket': source_bucket_name, 'Key': source_file_key_name}

   # S3 copy object operation
   s3_client.copy_object(CopySource=copy_source_object, Bucket=destination_bucket_name, Key=desitination_file_key_name)

   return {
       'statusCode': 200,
       'body': json.dumps('Process s3 data Job Done!')
   }