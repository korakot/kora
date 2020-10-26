"""
Install manimlib and jupyter-manim, and config them in Colab
"""

import os

os.system("apt install libcairo2-dev libgif-dev")
os.system("apt install texlive-latex-recommended texlive-fonts-extra texlive-science")
os.system("pip install jupyter-manim")

from manimlib.imports import *
import jupyter_manim


# Reduce quality to half of LOW
LOW_QUALITY_CAMERA_CONFIG.update({'pixel_height': 240, 'pixel_width': 426})
defaults = get_ipython().magics_manager.registry['ManimMagics'].defaults
defaults.update({'height': 240, 'width': 426, 'remote': True})
# Without -l, it will use production Q. So, make it LOW by default
PRODUCTION_QUALITY_CAMERA_CONFIG.update(LOW_QUALITY_CAMERA_CONFIG)
