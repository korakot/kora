from google.colab.output import *
from IPython.display import display, Javascript

def set_height(h):
    eval_js('google.colab.output.setIframeHeight("%s")' % h)

# Usage:
# set_style(fontSize='30px', color='red')
# print("Hello")
def set_style(**kw):
    import json
    display(Javascript('''
    for (rule of document.styleSheets[0].cssRules){
        if (rule.selectorText=='body') {
            Object.assign(rule.style, %s)
            break
        }
    }
    ''' % json.dumps(kw)))