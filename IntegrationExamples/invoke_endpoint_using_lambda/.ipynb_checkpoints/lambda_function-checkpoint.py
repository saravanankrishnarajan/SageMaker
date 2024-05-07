# lambda startup function

import boto3
import math
import json
import os
import re

# importing transform_data function
from transform_data import transform_data
from os import system

#env_vars = system("cat ./.env")
env_vars = os.popen('cat ./.env').readlines()
#print(env_vars)
for var in env_vars:
    var=var.strip('\n')
    key, value = var.split('=')
    os.environ[key]=value


def lambda_handler(event, context):

    
    environ = os.environ.get('ENVIRON')

    #read environment variable
    if environ=='DEV':
        ENDPOINT_NAME = os.environ.get('ENDPOINT_NAME')
        profile_name = os.environ.get('PROFILE_NAME')
        boto_session = boto3.Session(profile_name=profile_name, region_name='us-east-1')
    
    else:
        ENDPOINT_NAME = os.environ.get('ENDPOINT_NAME')
    
    client = boto3.client(service_name='sagemaker-runtime',region_name='us-east-1')

    #print(ENDPOINT_NAME)
    try:
        # it can print in watch log
        print("Received event: " + json.dumps(event,indent=2))
        request = json.loads(json.dumps(event))
        transformed_data = [transform_data(instance['features']) for instance in request['instances']]
        # XGBoost accepts data in csv. It does not support JSON
        result = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, 
                                   Body=('\n'.join(transformed_data).encode('utf-8')),
                                   ContentType='text/csv')
        
        result = result['Body'].read().decode('utf-8')
        # splitting result using regular expression pattern
        pattern = r'[^0-9.]+'
        result = re.split(pattern,result)
        predictions = [math.expm1(float(r))for r in result if r!=""]
        return {
            'statuscode': 200,
            'ibase64Encoded': False,
            'body': json.dumps(predictions)
        }
              


    except Exception as err:
        return {
            'statuscode': 400,
            'ibase64Encoded': False,
            'body': 'Call Failed {0}'.format(err)
        }
        