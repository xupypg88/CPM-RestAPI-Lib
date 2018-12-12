from cpmworker import *
import os

host=os.environ.get('CPMAPIHOST')
api_key=os.environ.get('CPMAPIKEY')

# todo write tests based on unittest module

if __name__ == '__main__':

    wk = CPMworker(host, api_key)

    print(wk.get_accounts())