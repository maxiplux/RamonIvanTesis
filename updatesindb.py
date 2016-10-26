from fabric.api import *
print "Hello"
import os
def deploy():
	print os.system('git add .')
	print os.system('git commit -m "my first commit"')
	print os.system('git push heroku master')

	
if __name__ == '__main__':
   deploy()