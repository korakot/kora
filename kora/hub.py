"""
Shortcuts for tensorflow_hub
Instead of `import tensorflow_hub as hub`, call `from kora import hub`.
You will get hub.embed for Universal Sentence Encoder.
There will be more shortcuts for hub in the future.
"""
from tensorflow_hub import * 


_embed = None  # for lazy loading
use_url = "https://tfhub.dev/google/universal-sentence-encoder/4"

def load_use():
    """ lazy load and cache it """
    global _embed
    if _embed is None:
        _embed = load(use_url)
    return _embed


def embed(input):
    """ embed 1 sentence, or a list of sentence """
    if type(input) == str:
        return load_use()([input])[0]   # just 1
    else:
        return load_use()(input)
