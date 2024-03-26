import boto3

def list_unattached_volumes():
    # Initialize the Boto3 EC2 client
    ec2_client = boto3.client('ec2')
    
    # Get a list of all EBS volumes
    response = ec2_client.describe_volumes()
    
    # Filter unattached volumes
    unattached_volumes = []
    for volume in response['Volumes']:
        if len(volume['Attachments']) == 0:
            unattached_volumes.append(volume)
    
    return unattached_volumes

def main():
    unattached_volumes = list_unattached_volumes()
    
    if unattached_volumes:
        print("Unattached EBS volumes:")
        for volume in unattached_volumes:
            print(f"Volume ID: {volume['VolumeId']}, Size: {volume['Size']} GiB")
    else:
        print("No unattached EBS volumes found.")

if __name__ == "__main__":
    main()
