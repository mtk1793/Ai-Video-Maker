import subprocess,json,pathlib,wave
import numpy as np
P=pathlib.Path(__file__).resolve().parent
import os
os.chdir(P)
# source start, duration, subject crop x, kind. Cuts preserve the setup and payoff.
shots=[(297.0,.55,700,'tease'),(30.0,4.35,640,'question'),(37.25,2.1,285,'reply'),(285.0,1.0,650,'robot'),(297.0,.85,700,'robot'),(300.2,1.0,620,'robot'),(60.22,2.35,410,'reaction')]
T=sum(s[1] for s in shots)
def run(c):subprocess.run(c,check=True)
for i,(start,dur,x,kind) in enumerate(shots):
 # Focused portrait reframing and a small progressive push, rather than a small landscape inset.
 vf=f"crop=400:534:{x}:0,scale=1440:1922,zoompan=z='1.001+0.00025*on':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1080x1920:fps=30,eq=contrast=1.06:saturation=1.10,setsar=1"
 run(['ffmpeg','-v','error','-y','-ss',str(start),'-i','source.mp4','-t',str(dur),'-vf',vf,'-c:v','libx264','-preset','veryfast','-crf','20','-c:a','pcm_s16le','-ar','48000','-ac','2',f'v2_{i}.mkv'])
open('v2_concat.txt','w').write(''.join(f"file 'v2_{i}.mkv'\n" for i in range(len(shots))))
# ASS per-word active highlighting. Phrase stays still; only the spoken word changes color.
header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,76,&H00FFFFFF,&H0000E5FF,&H00101010,&H90000000,-1,0,0,0,100,100,-1,0,1,5,2,5,70,140,0,1
Style: Hook,DejaVu Sans,70,&H00FFFFFF,&H0000E5FF,&H00101010,&H90000000,-1,0,0,0,100,100,-1,0,1,4,1,8,60,120,200,1
Style: Credit,DejaVu Sans,21,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,1,0,2,40,100,170,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
e=[]
def add(a,b,style,text):
 e.append(f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{text}')
add(0,.55,'Hook','HE WAS RIGHT\\n{\\c&H00E5FF&}TO PANIC.')
add(.55,4.9,'Hook','IT IS JUST\\n{\\c&H00E5FF&}A ROBOT HAND...')
add(7,10.35,'Hook','HIS NIGHTMARES:')
add(10.35,T,'Hook','{\\c&H00E5FF&}FAIR ENOUGH.')
add(0,T,'Credit','Tears of Steel / (CC) Blender Foundation\\nmango.blender.org / CC BY 3.0 / edited excerpt')
words=[w for s in json.load(open('transcript_v2.json')) for w in s['words']]
for lo,hi,offset in [(0,4.3,.55),(7.25,9.35,4.9-7.25)]:
 ws=[w for w in words if lo<=w['start']<hi]
 for k in range(0,len(ws),3):
  group=ws[k:k+3]
  for n,w in enumerate(group):
   a=max(lo,w['start'])+offset;b=min(hi,max(w['end'],w['start']+.10))+offset
   if n==len(group)-1:b=min(hi,group[-1]['end']+.08)+offset
   txt=' '.join(('{\\c&H00E5FF&}' if j==n else '{\\c&HFFFFFF&}')+v['word'].strip().upper() for j,v in enumerate(group))
   add(a,b,'Cap','{\\pos(510,1400)\\fscx95\\fscy95\\t(0,75,\\fscx100\\fscy100)}'+txt)
add(7,8,'Cap','{\\pos(510,1400)}SMALL UPGRADE.')
add(8,8.85,'Cap','{\\pos(510,1400)}BIG PROBLEM.')
add(8.85,9.85,'Cap','{\\pos(510,1400)}NOPE.')
add(9.85,T,'Cap','{\\pos(510,1400)}THIS IS PRETTY FREAKY.')
open('captions_v2.ass','w').write(header+'\n'.join(e)+'\n')
# Original synthesized percussion, riser, bass hit and whooshes; no third-party music pack.
sr=48000;n=int((T+.5)*sr);t=np.arange(n)/sr;audio=np.zeros(n);rng=np.random.default_rng(42)
def mix(a,start):
 idx=int(start*sr);end=min(n,idx+len(a));audio[idx:end]+=a[:end-idx]
def hit(start,amp=.22):
 q=np.arange(int(.38*sr))/sr;mix(amp*np.sin(2*np.pi*(75*q-45*q*q))*np.exp(-12*q),start)
def whoosh(start,d=.25):
 q=np.arange(int(d*sr))/sr;noise=rng.standard_normal(len(q));noise=np.convolve(noise,np.ones(9)/9,mode='same');mix(.12*noise*np.sin(np.pi*q/d)**2,start)
for s in [0,7,8,8.85,9.85]:hit(s);whoosh(max(0,s-.16))
for s in np.arange(7,9.9,.425):hit(float(s),.10)
# A short ascending tonal riser leads into the robot reveal.
q=np.arange(int(.6*sr))/sr;mix(.05*np.sin(2*np.pi*(220*q+1000*q*q))*np.linspace(0,1,len(q)),6.4)
audio=np.clip(audio,-.95,.95);stereo=np.stack([audio,audio],axis=1)
with wave.open('sound_design.wav','wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((stereo*32767).astype('<i2').tobytes())
# Tame original montage audio, retain clear dialogue, then normalize the complete mix.
af="[0:a]volume='if(between(t,7,9.85),0.25,1)':eval=frame,highpass=f=75[a];[a][1:a]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=9[out]"
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','v2_concat.txt','-i','sound_design.wav','-filter_complex',af,'-map','0:v','-map','[out]','-vf','ass=captions_v2.ass','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart','AI_Is_Harmless_V2.mp4'])
print('Duration',T)
