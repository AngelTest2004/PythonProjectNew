#import the model in other folder
import os
import sys
print(__file__)
#get the folder name
base_path=os.path.dirname(__file__)
print(base_path)
base_path=os.path.dirname(base_path)
print(base_path)
active_this_path=base_path+"\\venv\\Scripts"
print(active_this_path)
sys.path.append(active_this_path)

import activate_this
#the way to import package
#from venv.Scripts import activate_this
print(sys.path)