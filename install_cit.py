#NOTE: This is not done or tested and does NOT work on Windows.
#ALSO SYSTEM_WIDE DOES NTO WORK... I want to try ot get it to work without using execfile

#TODO: Include the she-bang for python so it makes it easier to use

#A simple install script to install city-issue-tracker
from __future__ import print_function #Back to the Future
import argparse #Helps with the basic creation of script
from subprocess import call, Popen #Gives ability to use the commandline from inside 
import subprocess
import os

#Consts
local = "local"
system = "system"

path = '' #Normal the path is nothing except in the case of a local install(which is default)

parser = argparse.ArgumentParser(description="Setup, Install and create run scripts for City-Issue-Tracker")

#Add an argument that will do a global install
parser.add_argument('--system_wide', action='store_const', const=system, default=local, help="Enable system wide install")

args = parser.parse_args()

print(args)

#If sing the local install
if args.system_wide == local:

	#TODO Rename to pyenv_folder
	pyenv_folder = 'virtualenv-1.9'
	#Get the virtualenv
	# http://www.virtualenv.org/en/latest/virtualenv.html#installation
	call(['curl', '-0', 'https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz', '-o', pyenv_folder+'.tar.gz'], stdout=subprocess.PIPE)

	# untar it
	call(['tar','xvfz', pyenv_folder+'.tar.gz'])

	# delete tar file
	call(['rm',pyenv_folder+'.tar.gz'])

	#Go into folder( I think this has to happen for the pip fallback stuff)
	os.chdir(pyenv_folder)

	# Activate the virtualenv
	call(['python','virtualenv.py','CIT'])

	#Back out of the folder
	os.chdir('..')

	#Setup the python path to use
	path = './virtualenv-1.9/CIT/bin/'

print(path+'pip')

#TODO: Install the depens
call([path + 'pip','install','-r', 'install/requirements.txt'])


#Create the run file
f = open('run.py','w')
#NOTE: I don't want it done this way but for now it works
#print("#!"+path+"python\nfrom subprocess import Popen\nPopen(['"+path+"python"+"','app/app.py'])",file=f)#Time travel used
print("#!"+path+"python\nfrom app import app\napp.run(debug=True)",file=f)#Time travel used


f.close()

#Make newly created file runnable
call(['chmod','a+x','run.py'])

#TODO: http://docs.python.org/2/distutils/setupscript.html <- Setup something like that(maybe?)
