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
        wk = CPMworker(HOST, API_KEY)
        print(os.environ.get('BOTOACCESS'))
        print(os.environ.get('CPMAPIKEY'))
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