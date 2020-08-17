"""
LIT : Language Interpretibility Toolkit
Help explain NLP models
"""

import os
import kora.install.yarn

# install dependencies
os.system("pip install lime sacrebleu transformers==2.11.0")

# download lit_nlp, and build front-end
os.chdir("/content")
os.system("npx degit PAIR-code/lit/lit_nlp#main lit_nlp")
os.chdir("/content/lit_nlp/client")
os.system("yarn && yarn build")
os.chdir("/content")
