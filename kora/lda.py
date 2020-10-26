import os

os.system("pip install pythainlp")
os.system("pip install guidedlda")
os.system("pip install pyldavis")

import numpy as np
from pythainlp import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from guidedlda import GuidedLDA
import pyLDAvis 
from pyLDAvis._display import prepared_data_to_html
from fastcore.foundation import patch

# avoid warnings, INFO
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)  # in model.fit()

from logging import getLogger, ERROR
getLogger('guidedlda').setLevel(ERROR)
getLogger('numexpr.utils').setLevel(ERROR)


def fit(texts, n_topics=5, n_iter=500, seed=None, seed_confidence=0.15, **kwargs):
    vzer = CountVectorizer(tokenizer=word_tokenize)
    X = vzer.fit_transform(texts)
    vocab = vzer.get_feature_names()
    word2id = vzer.vocabulary_
    opts = get_opts(seed, word2id, seed_confidence)
    # create model
    model = GuidedLDA(n_topics=n_topics, n_iter=n_iter, **kwargs)
    model.fit(X, **opts)  # optional seed
    prepare(model, X, vocab)
    return model


def get_opts(seed, word2id, seed_confidence):
    opts = {}
    if seed:  # seed_topic_list e.g. [[w1,w2], [w3,w4]]
        seed_topics = {}   
        for t_id, st in enumerate(seed):
            for word in st:
                seed_topics[word2id[word]] = t_id
        opts['seed_topics'] = seed_topics
        opts['seed_confidence'] = seed_confidence
    return opts


def _norm(dists):
    return dists / dists.sum(axis=1)[:, None]

def prepare(model, X, vocab):
    doc_lengths = X.sum(axis=1).getA1().tolist()
    term_frequency = X.sum(axis=0).getA1().tolist()
    doc_topic_dists = _norm(model.transform(X)).tolist()
    topic_term_dists = _norm(model.components_).tolist()
    # to be displayed later
    model.viz_data = dict(vocab=vocab,
                          doc_lengths=doc_lengths,
                          term_frequency=term_frequency,
                          doc_topic_dists=doc_topic_dists,
                          topic_term_dists=topic_term_dists)


# auto-viz
@patch
def _repr_html_(self: GuidedLDA):
    data = pyLDAvis.prepare(**self.viz_data)
    return prepared_data_to_html(data)

pyLDAvis.enable_notebook()
