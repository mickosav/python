from my_module import find_index
import sys

# list of where python looks for modules on import:
print(sys.path)

# if module is not in the same directory we have 2 options:
# 1:
import sys
sys.path.append('path/to/module_directory')
import my_module
# ^ BAD

# 2:
# add it as a PYTHONPATH environment variable
# in ~/.bash_profile
# export PYTHONPATH="/path/to/your/module_directory"

