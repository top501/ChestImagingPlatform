import common
import input_output
import utils
import classification
import phenotypes
import particles
import visualization
import qualitycontrol
import segmentation
import registration

import os
if os.sys.platform == "win32":
  print ("Warning: nipype not available in Windows")
else:
  import nipype