from cpmworker import *

if __name__ == '__main__':


    wk = CPMworker(host, api_key)

    print(wk.get_accounts())