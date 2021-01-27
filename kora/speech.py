"""
Simplify Python Client of Google Cloud Speech-to-Text
Need to install (and restart first) with `import kora.install.speech`
Then
```
from kora.speech import Recognizer
sp = Recognizer(sa_file, lang='th', output_dir=None)
op = sp.open(uri)
op.to_df()
```
"""

import pandas as pd
import os.path
from pathlib import Path
from fastcore.foundation import patch

from google.cloud.speech_v1p1beta1 import SpeechClient
from google.cloud.speech_v1p1beta1.types import \
    RecognitionAudio, RecognitionConfig, TranscriptOutputConfig
from google.api_core.operation import Operation


class Recognizer:
    """ Make SpeechClient easier to use """

    def __init__(self, sa_file, lang='th', output_dir=None):
        """ Need a service account file for authentication
            e.g. drive/MyDrive/service-account.json
        """
        self.client = SpeechClient.from_service_account_file(sa_file)
        self.lang = lang
        self.output_dir = output_dir
        self.ops = []

    def open(self, uri):
        audio = RecognitionAudio(uri=uri)
        cfg = RecognitionConfig(language_code=self.lang, enable_word_time_offsets=True)
        req = {"audio": audio, "config": cfg}
        if self.output_dir:
            output_name = Path(uri).stem + '.json'
            output_uri = os.path.join(self.output_dir, output_name)
            req['output_config'] = TranscriptOutputConfig(gcs_uri=output_uri)
        op = self.client.long_running_recognize(request=req)
        self.ops.append(op)
        return op


@patch
def __repr__(self: Operation):
    """ Show operation progress """
    self.done()  # refresh
    pc = self.metadata.progress_percent
    name = self.operation.name
    return f"<{name} ({pc}%)>"

@patch
def to_df(self: Operation):
    """ Return dataframe of its result """
    left = []
    right = []
    data = []
    for i, result in enumerate(self.result().results):
        for w in result.alternatives[0].words:
            left.append(w.start_time.total_seconds())
            right.append(w.end_time.total_seconds())
            data.append([w.word, i+1])
    index = pd.IntervalIndex.from_arrays(left, right, closed='left', name='time')
    return pd.DataFrame(data, index, ['word', 'order'])
