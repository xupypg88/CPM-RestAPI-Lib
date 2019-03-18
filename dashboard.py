import cpmworker



def main ():
    wr = cpmworker

    #todo Get the list of the S3 records
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