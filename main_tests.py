from cpmworker import *

if __name__ == '__main__':

    host = "ec2-18-235-133-229.compute-1.amazonaws.com"
    api_key = "b9490fab3f625213809e87fab64a818b4b60041ea5c59c4405117fc4ede350214ede059b736c2010754906421bd95c8c742178f696ac395d769f5304cffa30ee"

    wk = CPMworker(host, api_key)


    print(wk.get_accounts())