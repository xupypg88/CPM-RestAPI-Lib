# CPM-ReastAPI lib example
as it says =)
Here I am going to place some useful examples for API calls

todo: Module that checks the backup chains on S3 and show it like the chain with stats
Now I need to add a couple more wrappers for API calls to make it generate links on this files so we can see it as the one chain.

# Set up
You could either create settings file settings.json with two parameters api key and host ip (fqdn)  and place it into the project folder
Example content:

{
    "host" : "ec2-ex-am-pl-e.compute-1.amazonaws.com"
    "api_key" : "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
}

or add to environment variables with the same values instead:

CPMAPIHOST
CPMAPIKEY
