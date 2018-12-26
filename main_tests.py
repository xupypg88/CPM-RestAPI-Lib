from cpmworker import *
import os
import urllib3
import unittest

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST=os.environ.get('CPMAPIHOST')
API_KEY=os.environ.get('CPMAPIKEY')

# todo write tests based on unittest module


class APIFunctionsUsersCase(unittest.TestCase):

    def test_getaccountslist(self):
        predefined = [{u'scan_regions': [2], u'name': u'main_backup3', u'capture_vpcs': True, u'scan_tagged_resources': False, u'authentication': u'R', u'is_dr_account': False, u'user': 1, u'id': 2}, {u'name': u'dr', u'allow_deleting_snapshots': True, u'authentication': u'R', u'is_dr_account': True, u'user': 1, u'id': 3}, {u'scan_regions': [2], u'name': u'esche', u'capture_vpcs': True, u'scan_tagged_resources': False, u'authentication': u'R', u'is_dr_account': False, u'user': 1, u'id': 4}, {u'scan_regions': [2], u'name': u'grizzly2_tied', u'capture_vpcs': True, u'assume_from_account': 2, u'scan_tagged_resources': False, u'authentication': u'A', u'role_name': u'Mikhail.Topskiy', u'is_dr_account': False, u'account_number': u'124556737267', u'external_id': None, u'id': 5, u'user': 2}, {u'scan_regions': [2], u'aws_access_key': u'AKIAJWLC2F2AIAH5POJQ', u'name': u'key', u'capture_vpcs': True, u'scan_tagged_resources': False, u'authentication': u'C', u'is_dr_account': False, u'user': 1, u'id': 6}]
        wk = CPMworker(HOST, API_KEY)
        print(wk.describe_accounts())
        return

    def test_getuserslist(self):
        #self.assertEqual(1,2,"what!?")
        return

    def test_createuser(self):
        """
        creates managed and Independent test user
        :return:
        """
        return

    def test_removeuser(self):
        """

        :return:
        """
        return

    def test_createaccount(self):
        """
        creates both DR and standard account
        :return:
        """
        return

    def test_removeaccount(self):
        return

    def test_assumerole(self):
        return

if __name__ == '__main__':
    unittest.main()