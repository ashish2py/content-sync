# content-syncOverview
Content/Files present on any local box should also be present on server and files present on server should be available on box if that box have permission to access that file.

Goals
Sync contents of local and server.

Challenges
Network fails while transferring files.
Sync only accessible file/resources from nodes/lesson material.
Support Azure and S3 

Specifications
RSYNC
To download/upload data between local and remote server.

Python Packages
Custom python package to calculate difference, syncable and accessible files on local/remote for an account.

Milestones
PUSH and PULL method with RSYNC
PUSH : Send local files/folder to remote server.
PULL :  Fetch files/folder from remote server to local server.


1 - Find an account of the box
    Find an account of the box, this will help to get the list of accessible content/resource from remote-server.
    
2 - Find location/address on the server [ media file path on remote server ]
    Ask server for the media path for an account, helps to create same folder structure on the local system while syncing the files from remote.
    
3 - Find all the resource/content accessible by the box/account
    Ask server for the accessible resources/content for an account and prepare a list of resources to be PUSHED on classcloud-box down.
    
4 - Rsync for all those files.
    After preparing accessible resource/content on remote system send it to local classcloud-box.

References

https://www.digitalocean.com/community/tutorials/how-to-use-rsync-to-sync-local-and-remote-directories-on-a-vps
https://pypi.python.org/pypi/rsync.py


