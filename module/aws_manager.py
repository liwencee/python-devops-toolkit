import boto3

ec2 = boto3.client("ec2")

def list_instances():
    instances = ec2.describe_instances()
    for r in instances["Reservations"]:
        for i in r["Instances"]:
            print(f"ID: {i['InstanceId']}, State: {i['State']['Name']}, Tags: {i.get('Tags')}")

def manage_instance(action, tag_key=None, tag_value=None):
    filters = []
    if tag_key and tag_value:
        filters = [{"Name": f"tag:{tag_key}", "Values": [tag_value]}]

    response = ec2.describe_instances(Filters=filters)
    for r in response["Reservations"]:
        for i in r["Instances"]:
            iid = i["InstanceId"]
            if action == "start":
                ec2.start_instances(InstanceIds=[iid])
                print(f"Started: {iid}")
            elif action == "stop":
                ec2.stop_instances(InstanceIds=[iid])
                print(f"Stopped: {iid}")
# This script provides a command-line interface for managing AWS resources, Docker containers, and generating inventory files.
# It allows users to list EC2 instances, manage their state, deploy Docker containers, and generate inventory files based on specified hosts.
# It uses the argparse module to handle command-line arguments and subcommands.     