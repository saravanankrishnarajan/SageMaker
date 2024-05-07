# lambda startup function

import boto3
import math
import json
import os
import re

# importing transform_data function
from tranform_data import transform_data

# read environment variable
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

client = boto3.client(client='sagemaker-runtime')

def lambda_handler(event, context):

    try:
        


    except:
        