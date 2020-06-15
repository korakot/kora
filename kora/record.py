import os
from IPython.display import display, Javascript, Audio
from google.colab import output
from base64 import b64decode


RECORD_AUDIO = """
const sleep  = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
    const reader = new FileReader()
    reader.onloadend = e => resolve(e.srcElement.result)
    reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    recorder = new MediaRecorder(stream)
    chunks = []
    recorder.ondataavailable = e => chunks.push(e.data)
    recorder.start()
    await sleep(time)
    recorder.onstop = async ()=>{
        blob = new Blob(chunks)
        text = await b2text(blob)
        resolve(text)
    }
    recorder.stop()
})
"""

def audio(sec=3):
    """ Record audio for a given duration """
    display(Javascript(RECORD_AUDIO))
    s = output.eval_js('record(%d)' % (sec*1000))
    b = b64decode(s.split(',')[1])
    return Audio(b)


# Add to class Audio
def _audio_save(self, filename=None):
    """ Audio's method to save as a file 
        Default format is probably webm
    """
    with open('/tmp/audio.webm', 'wb') as f:
        f.write(self.data)
    os.system("ffmpeg -y -i /tmp/audio.webm "+filename)
    return filename
Audio.save = _audio_save