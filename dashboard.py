from cpmworker import *
import os

def main ():
    cpm_client = CPMworker(os.environ.get('CPMAPIHOST'), os.environ.get('CPMAPIKEY'))

    #todo Get the list of the S3 records
    records = []
    for record in cpm_client.describe_S3_backups(cpm_client.s3status_success):
        records.append({ 'rec_id': record['id'],
                         'policy_id' : record['policy'],
                         'restore_points' : [restore_point for restore_point in cpm_client.describe_S3_backup(record['id'])]
                         })

    print(str(records))

    #todo Group it by the policy and instance
    #todo Create th S3 restore points' ID list

    #todo generate link to S3 repository and retrieve the restore points' xml files
    #todo link the restore points xml files to the storage xml files
    #todo Format the structure with the backup chains in JSON
    """
    Backup
       |- Restore Point
       |      |- Instance
       |      |       |- Volume 1          
       |      |       |- Volume 2
       |      |       |- .....
       |      |
       |      |- Instance
       |              |- .....
       |- Restore Point
              |- ....
    """
main()