from fabric.api import *
print "Hello"
import os
def deploy():
	
    print os.system('svn commit -m "commit " ' )

	
if __name__ == '__main__':
   deploy()