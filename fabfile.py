#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 1.0

import time
import os

from fabric.api import *

##
## available environments
##

def amazon():
    env.hosts = ['centos@18.231.48.193']
    env.app_root = '/srv/uberserver/'
    env.server_script = './server.py'
    env.git_origin = 'git@github.com:YuriHeupa/uberserver.git'
    env.key_filename = "lohann.pem"
    env.password = "Lpcf97109011"
    env.git_branch = 'master'
    env.virtual = '/var/www/.virtualenvs/uberserver/bin/activate'

def amazon():
    env.hosts = ['root@bitsteakcom']
    env.app_root = '/srv/uberserver/'
    env.server_script = './server.py'
    env.git_origin = 'git@github.com:YuriHeupa/uberserver.git'
    env.key_filename = "lohann.pem"
    env.password = "Lpcf97109011"
    env.git_branch = 'master'
    env.virtual = '/var/www/.virtualenvs/uberserver/bin/activate'

##
## available commands
##

def deploy():
    start = time.time()

    ## validate environment
    if not hasattr(env, 'app_root'):
        print('ERROR: unknown environment.')
        os.sys.exit(1)

    ## clone repository
    command = 'test -d %s.git || git clone %s %s -b %s'
    sudo(command % (env.app_root, env.git_origin, env.app_root, env.git_branch))

    ## update repository
    command = 'cd "%s" && git reset --hard && git pull && git checkout -B %s origin/%s && git pull'
    run(command % (env.app_root, env.git_branch, env.git_branch))

    ## update python packages
    command = 'source %s; cd %s; pip3 install -r requirements.txt' % (env.virtual, env.app_root)
    run(command)

    ## restart service
    command = 'source %s; cd %s; %s -v 103.0' % (env.virtual, env.app_root, env.server_script)
    run(command)

    final = time.time()
    puts('execution finished in %.2fs' % (final - start))
