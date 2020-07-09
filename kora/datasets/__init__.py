import os
import sys
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')  # avoid printing "Using TensorFlow backend."

from keras.datasets import *

sys.stderr = stderr


