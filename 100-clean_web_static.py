#!/usr/bin/python3
""" Function that deploys """

from fabric.api import *

env.hosts = ['54.85.153.236', '54.160.89.208']
env.user = "ubuntu"

did_run = False


def do_clean(number=0):
    """The functions that cleans the archives."""

    global did_run
    # First deletes archives in local (once)!
    if not did_run:
        try:
            archives = local('ls -ltr versions', capture=True).split('\n')[1::]
            archives = [archive.split()[-1] for archive in archives]
            count = len(archives)
            number = int(number)

            # Deletes all - number archives in local
            if number > 1 and count > number:
                for i in range(count - number):
                    local('rm versions/{}'.format(archives[i]))
            elif count > 1 and count > number:
                for i in range(count - 1):
                    local('rm versions/{}'.format(archives[i]))
            did_run = True
        except Exception as e:
            print(e)

    # Delete the folders in /data/web_static/releases in remote
    remote = '/data/web_static/releases'
    try:
        archives = run('ls -ltr {}'.format(remote)).split('\n')[1::]
        archives = [archive.split()[-1] for archive in archives
                    if not archive.count('test')]
        count = len(archives)
        number = int(number)

        # Deletes all - number archives in remote
        if number > 1 and count > number:
            for i in range(count - number):
                sudo('rm -rf {}/{}'.format(remote, archives[i]))
        elif count > 1 and count > number:
            for i in range(count - 1):
                sudo('rm -rf {}/{}'.format(remote, archives[i]))
    except Exception:
        pass
