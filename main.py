# coding=utf-8
# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import boto3
# import pandas as pd
import os
import subprocess
import zipfile
import sys

sts_client = boto3.client('sts')
assumed_role_object = sts_client.assume_role(
    RoleArn="arn:aws:iam::798104083011:role/nest_role",
    RoleSessionName="AssumeRoleSession1"
)

# s3_client = boto3.resource('s3')
s3_client = boto3.client("s3")
bucket_name = 'test-lambda-s3-08152022'
s3_folder = 'libs'
local_dir = '/tmp/libs'
########################################++
s3 = boto3.resource('s3')
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.filter(Prefix=s3_folder):
    print(obj.key)
    target = os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
    if not os.path.exists(os.path.dirname(target)):
        os.makedirs(os.path.dirname(target))
    if obj.key[-1] == '/':
        continue
    if "zip" in obj.key:
        print("Downloading: " + obj.key)
        print("Target is: " + target)
        bucket.download_file(obj.key, target)

########################################

print(os.path.isdir('/tmp/libs/my_test/'))

#######################################
sys.path.append('/tmp/libs')
print("Current working directory is: " + os.getcwd())

# task = os.getcwd()
# os.chdir(local_dir + "/my_test/")
# print("Current working directory is: " + os.getcwd())

# files = [f for f in os.listdir('.') if os.path.isfile(f)]
# for f in files:
#     if not f.endswith(".zip"):
#         continue
#     zip_ref = zipfile.ZipFile(f)
#     zip_ref.extractall(path=local_dir)
#     zip_ref.close()
#     os.remove(f)

with zipfile.ZipFile('/tmp/libs/my_test/site-packages.zip', 'r') as zip_ref:
    zip_ref.extractall('/tmp/libs')

print("---", os.path.isdir('/tmp/libs/site-packages/pandas'))

sys.path.append('/tmp/libs/site-packages')
print("=============================")
os.chdir(local_dir)
print("Files in local_dir:")
next_files = [f for f in os.listdir('.')]
print("Check files in: " + local_dir)
for f in next_files:
    print(f)

import numpy

print(numpy.__version__)


# import pandas as pd
# print(pd.__version)
# import my_test.my_test as m
# import my_test.Another_test as at
# print(pd.__version__)

# print("Amen")
# m.my_test().test_s3()
# at.Solution().print_0()


# print("Current working directory is: " + os.getcwd())
# print("Before directory change")
# os.chdir("/tmp/libs/my_test/my_test")
# print("After directory change")

# print(os.environ)
# print("************************88")

def print_hi(event, context):
    # print(pd.__version__)
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(event))  # Press Ctrl+F8 to toggle the breakpoint.


#
# def download_code_from_s3(bucketName, file_path):
#     s3_resource = boto3.resource('s3')
#     bucket = s3_resource.Bucket(bucketName)
#     bucket.download_file(file_path, os.path.join('/tmp/', file_path))
#
#
# def lambda_handler(event, context):
#     url_data = (r'https://raw.githubusercontent.com/oderofrancis/rona/main/Countries-Continents.csv')
#     download_code_from_s3('truehelper', 'panda_layer.zip')
#     # subprocess.run(['unzip', '/tmp/panda_layer.zip', '-d', '/tmp/'])
#     print("File downloaded")
#     from panda_layer import pandas as pd
#     df = pd.read_csv(url_data)
#     print(df.head())
#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
