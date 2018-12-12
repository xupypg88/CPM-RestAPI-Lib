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
        predefined = [{'id': 2, 'user': 1, 'name': 'main_backup3', 'authentication': 'R', 'is_dr_account': False, 'scan_tagged_resources': False, 'scan_regions': [2], 'capture_vpcs': True}, {'id': 3, 'user': 1, 'name': 'dr', 'authentication': 'R', 'is_dr_account': True, 'allow_deleting_snapshots': True}, {'id': 4, 'user': 1, 'name': 'esche', 'authentication': 'R', 'is_dr_account': False, 'scan_tagged_resources': False, 'scan_regions': [2], 'capture_vpcs': True}, {'id': 5, 'user': 2, 'name': 'grizzly2_tied', 'authentication': 'A', 'is_dr_account': False, 'account_number': '124556737267', 'role_name': 'Mikhail.Topskiy', 'external_id': None, 'assume_from_account': 2, 'scan_tagged_resources': False, 'scan_regions': [2], 'capture_vpcs': True}]
        wk = CPMworker(HOST, API_KEY)
        self.assertEqual(wk.get_accounts(), predefined,"Passed!")
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