import os
import urllib3
import unittest
import boto3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ACCESS=os.environ.get('BOTOACCESS')
SECRET=os.environ.get('BOTOSECRET')



class APIFunctionsUsersCase(unittest.TestCase):

    def test_preparingInfrastructure(self):
        print('Cheking if Amazon is available')
        botocl = boto3.client('ec2', aws_access_key_id=ACCESS, aws_secret_access_key=SECRET)
        response = (botocl.describe_instances()['Reservations'])

        for reservation in response:
            for instance in reservation['Instances']:
                for tag in instance['Tags']:
                    if tag['Key']=='ServerType' and tag['Value']=='CPM':
                        #{u'Monitoring': {u'State': 'disabled'}, u'PublicDnsName': 'ec2-54-90-178-204.compute-1.amazonaws.com', u'StateReason': {u'Message': 'Client.UserInitiatedShutdown: User initiated shutdown', u'Code': 'Client.UserInitiatedShutdown'}, u'State': {u'Code': 80, u'Name': 'stopped'}, u'EbsOptimized': False, u'LaunchTime': datetime.datetime(2018, 12, 14, 10, 33, 1, tzinfo=tzutc()), u'PublicIpAddress': '54.90.178.204', u'PrivateIpAddress': '192.168.0.73', u'ProductCodes': [{u'ProductCodeId': '17p1fh23ueq6b2b9xg6d8jwok', u'ProductCodeType': 'marketplace'}], u'VpcId': 'vpc-01cd0749678d2df62', u'CpuOptions': {u'CoreCount': 1, u'ThreadsPerCore': 1}, u'StateTransitionReason': 'User initiated (2018-12-14 15:19:00 GMT)', u'InstanceId': 'i-07986c16ad99bd9d4', u'EnaSupport': True, u'ImageId': 'ami-065727b4a9dd9c49e', u'PrivateDnsName': 'ip-192-168-0-73.ec2.internal', u'KeyName': 'CPM_instance', u'SecurityGroups': [{u'GroupName': 'N2WS_CPM_2.4.0_13-12-2018', u'GroupId': 'sg-02c2b5966b2a85dda'}], u'ClientToken': '154473399227343884', u'SubnetId': 'subnet-0cdb0a8ceb3c3b206', u'InstanceType': 't2.micro', u'NetworkInterfaces': [{u'Status': 'in-use', u'MacAddress': '06:5d:81:ea:da:da', u'SourceDestCheck': True, u'VpcId': 'vpc-01cd0749678d2df62', u'Description': 'Primary network interface', u'NetworkInterfaceId': 'eni-0d1e098935908cc45', u'PrivateIpAddresses': [{u'PrivateDnsName': 'ip-192-168-0-73.ec2.internal', u'PrivateIpAddress': '192.168.0.73', u'Primary': True, u'Association': {u'PublicIp': '54.90.178.204', u'PublicDnsName': 'ec2-54-90-178-204.compute-1.amazonaws.com', u'IpOwnerId': '346423605891'}}], u'PrivateDnsName': 'ip-192-168-0-73.ec2.internal', u'Attachment': {u'Status': 'attached', u'DeviceIndex': 0, u'DeleteOnTermination': True, u'AttachmentId': 'eni-attach-006ce48a2b9c259a8', u'AttachTime': datetime.datetime(2018, 12, 13, 20, 46, 34, tzinfo=tzutc())}, u'Groups': [{u'GroupName': 'N2WS_CPM_2.4.0_13-12-2018', u'GroupId': 'sg-02c2b5966b2a85dda'}], u'Ipv6Addresses': [], u'OwnerId': '346423605891', u'PrivateIpAddress': '192.168.0.73', u'SubnetId': 'subnet-0cdb0a8ceb3c3b206', u'Association': {u'PublicIp': '54.90.178.204', u'PublicDnsName': 'ec2-54-90-178-204.compute-1.amazonaws.com', u'IpOwnerId': '346423605891'}}], u'SourceDestCheck': True, u'Placement': {u'Tenancy': 'default', u'GroupName': '', u'AvailabilityZone': 'us-east-1e'}, u'Hypervisor': 'xen', u'BlockDeviceMappings': [{u'DeviceName': '/dev/sda1', u'Ebs': {u'Status': 'attached', u'DeleteOnTermination': True, u'VolumeId': 'vol-06931e1fee8e75604', u'AttachTime': datetime.datetime(2018, 12, 13, 20, 46, 35, tzinfo=tzutc())}}, {u'DeviceName': '/dev/sdf', u'Ebs': {u'Status': 'attached', u'DeleteOnTermination': False, u'VolumeId': 'vol-0f1ca7c1b47fc762f', u'AttachTime': datetime.datetime(2018, 12, 13, 21, 26, 30, tzinfo=tzutc())}}], u'Architecture': 'x86_64', u'RootDeviceType': 'ebs', u'IamInstanceProfile': {u'Id': 'AIPAIFIRXWZOY4U5H3F34', u'Arn': 'arn:aws:iam::346423605891:instance-profile/CPM_full_backup'}, u'RootDeviceName': '/dev/sda1', u'VirtualizationType': 'hvm', u'Tags': [{u'Value': 'CPM', u'Key': 'ServerType'}, {u'Value': 'Infrastructure', u'Key': 'Type'}, {u'Value': 'Jenkins_Lab_CPM_2.4.0_13-12-2018', u'Key': 'Name'}], u'HibernationOptions': {u'Configured': False}, u'AmiLaunchIndex': 0}
                        print(instance)
                        if instance['State']['Name'] == 'stopped':
                            botocl.start_instances(InstanceIds=[instance['InstanceId']])
                        if instance['State']['Name'] == 'running':
                            botocl.stop_instances(InstanceIds=[instance['InstanceId']])



if __name__ == '__main__':
    unittest.main()