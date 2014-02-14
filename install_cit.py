#TODO: Include the she-bang for python so it makes it easier to use

#A simple install script to install city-issue-tracker
from __future__ import print_function #Back to the Future
import argparse #Helps with the basic creation of script
from subprocess import call, Popen #Gives ability to use the commandline from inside 
import subprocess
import os

#Consts
local = "local"
globe = "global"

#
path = '' #Normal the path is nothign except in the case of a local install

parser = argparse.ArgumentParser(description="Setup, Install and create run scripts for City-Issue-Tracker")

#Add an argument that will do a global install
parser.add_argument('--system_wide', action='store_const', const=globe, default=local, help="Enable global install")

args = parser.parse_args();

print(args)

#If sing the local install
if args.system_wide == "local":

	#TODO Rename to pyenv_folder
	tar_file = 'virtualenv-1.9'
	#Get the virtualenv
	# http://www.virtualenv.org/en/latest/virtualenv.html#installation
	call(['curl', '-0', 'https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz', '-o',tar_file+'.tar.gz'], stdout=subprocess.PIPE)

	# untar it
	call(['tar','xvfz', tar_file+'.tar.gz']);

	# delete tar file
	call(['rm',tar_file+'.tar.gz'])

	#Go into folder( I think this has to happen for the pip fallback stuff)
	os.chdir(tar_file)

	#Just to make sure we are in the correct dir
	print(os.getcwd())

	# Activate the virtualenv
	call(['python','virtualenv.py','CIT'])

	#Just out a folder
	os.chdir('..')

	#Setup the python path to use


path = './virtualenv-1.9/CIT/bin/';

print(path+'pip')

#TODO: Install the depens
call([path + 'pip','install','Flask'])


f = open('run.py','w')
#Create the run file
print("#!"+path+"python\nfrom app import app\napp.run()",file=f)#Time travel used
f.close()

#Make newly created file runnable
call(['chmod','a+x','run.py'])



#TODO: http://docs.python.org/2/distutils/setupscript.html <- Setup something like that
