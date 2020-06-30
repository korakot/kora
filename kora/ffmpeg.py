"""
Make using ffmpeg easier. Define functions instead of calling !ffmpeg
"""

__all__ = ['cut', 'probe', 'Video', 'sample_video']

import os
from subprocess import getoutput

from IPython.display import HTML

from .json import render


def cut(input: str = 'video.mp4', start: float = 0.0, end: float = 60.0, output: str = None):
    def ts(mn: float):
        m, s = divmod(100*mn, 100)
        return '{:02.0f}:{:05.2f}'.format(m,s)

    if output is None:
        ext = input.split('.')[-1]
        output = 'output.'+ext
    params = f'-i {input} -ss {ts(start)} -to {ts(end)} -codec copy {output}'
    os.system(f'ffmpeg {params}')
    return output
# Example: cut('x.m4a', 2.10, 2.30)


def probe(filename: str):
    cmd = f'ffprobe -v quiet -show_format -show_streams -print_format json {filename}'
    return render(getoutput(cmd))


def Video(filename: str, width: int = 400):
    filename = os.path.abspath(filename)
    os.system(f'ln -snf {filename} /usr/local/share/jupyter/nbextensions/v.mp4')
    return HTML(f"<video width={width} src='/nbextensions/v.mp4' controls/>")


# a good test video in Colab
sample_video = '/usr/local/lib/python3.6/dist-packages/imageio/resources/images/realshort.mp4'