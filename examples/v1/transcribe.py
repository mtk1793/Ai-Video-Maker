from pathlib import Path
import os
os.chdir(Path(__file__).resolve().parent)
from faster_whisper import WhisperModel
import json
m=WhisperModel('tiny.en',device='cpu',compute_type='int8',cpu_threads=4)
import wave, numpy as np
w=wave.open('audio.wav'); audio=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
s,_=m.transcribe(audio,word_timestamps=True)
a=[{'start':x.start,'end':x.end,'text':x.text,'words':[{'start':w.start,'end':w.end,'word':w.word} for w in x.words]} for x in s]
json.dump(a,open('transcript.json','w'),indent=2)
print(json.dumps(a))
