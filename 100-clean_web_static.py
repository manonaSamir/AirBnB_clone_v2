#!/usr/bin/python3
""" Function that deploys """

from fabric.api import *

env.hosts = ['54.85.153.236', '54.160.89.208']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    with cd(path):
        sudo('ls -t | tail -n +{} | xargs rm -rf'.format(number))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        do_clean(sys.argv[1])
    else:
        print("Usage: python script_name.py number")


# from fabric.api import *


# env.hosts = ['54.85.153.236', '54.160.89.208']
# env.user = "ubuntu"


# def do_clean(number=0):
#     """ CLEANS """

#     number = int(number)

#     if number == 0:
#         number = 2
#     else:
#         number += 1

#     local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
#     path = '/data/web_static/releases'
#     run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
