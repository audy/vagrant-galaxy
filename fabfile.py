#!/usr/bin/env python

# Notes
# * use this instead: http://cfgparse.sourceforge.net/

GALAXY_HOME='/home/galaxy/galaxy-dist'

from fabric.api import *
from fabtools.vagrant import vagrant
import ConfigParser

universe_wsgi = './galaxy-dist/universe_wsgi.ini'

################
# Galaxy process

@task
def galaxy(cmd):
    if(cmd=='status'):
        status()
    elif(cmd=='start'):
        start_galaxy()        
    elif(cmd=='stop'):
        stop_galaxy()
    elif(cmd=='restart'):
        restart_galaxy()
    else:
        print "Invalid directive to Galaxy"
        
def start_galaxy():
    with cd(GALAXY_HOME):
        run('./run.sh --daemon')
def stop_galaxy():
    with cd(GALAXY_HOME):
        run('./run.sh --stop-daemon')
        
def restart_galaxy():
    with cd(GALAXY_HOME):
        run('./run.sh --stop-daemon')
        run('./run.sh --daemon')

def status():
    with cd(GALAXY_HOME):
        run('./run.sh --status')

# Tool Shed
@task
def toolshed(cmd):
    if(cmd=='status'):
        toolshed_status()
    elif(cmd=='start'):
        start_toolshed()        
    elif(cmd=='stop'):
        stop_toolshed()
    elif(cmd=='restart'):
        restart_toolshed()
    else:
        print "Invalid directive to Galaxy Toolshed"
        
def start_toolshed():
    with cd(GALAXY_HOME):
        sudo('./run_tool_shed.sh --daemon')

def stop_toolshed():
    with cd(GALAXY_HOME):
        sudo('./run_tool_shed.sh --stop-daemon')
        
def restart_toolshed():
    with cd(GALAXY_HOME):
        sudo('./run_tool_shed.sh --stop-daemon')
        sudo('./run_tool_shed.sh --daemon')

def toolshed_status():
    with cd(GALAXY_HOME):
        sudo('./run_tool_shed.sh --status')

#############################
# software package management
@task
def install(package):
    sudo('apt-get install %s' % (package))

##########################
# Galaxy config management
@task
def add_admin():
    pass

@task
def conf_set(k,v):
    Config = ConfigParser.ConfigParser()
    Config.read(universe_wsgi)
    Config.set('app:main',k,v)
    cfg = open(universe_wsgi,'w')
    Config.write(cfg)

@task 
def conf_get(k):
    Config = ConfigParser.ConfigParser()
    Config.read(universe_wsgi)
    print Config.get('app:main',k)
    
########################
# Vagrant on Galaxy test
@task
def install_vagrant():
    run('wget http://files.vagrantup.com/packages/0ac2a87388419b989c3c0d0318cc97df3b0ed27d/vagrant_1.3.4_x86_64.deb')
    sudo('sudo dpkg -i vagrant_1.3.4_x86_64.deb')

########################
# StarCluster on Galaxy test
#@task
#def install_starcluster():
#   pass

