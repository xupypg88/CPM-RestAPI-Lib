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
        regions = botocl.describe_regions()['Regions']
        print(regions)
        print('Ok!\nChecking resources.\nThis may take a few seconds')
        return

if __name__ == '__main__':
    unittest.main()