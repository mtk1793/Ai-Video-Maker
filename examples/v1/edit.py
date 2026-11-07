import json,subprocess,pathlib
P=pathlib.Path(__file__).resolve().parent
import os
os.chdir(P)
segments=[(30,12.5),(270,1.6),(210,1.6),(190,1.6),(272,1.6),(60.2,2.6)]
head='''[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,DejaVu Sans,46,&H00FFFFFF,&H0000E5FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,2,35,35,330,1
Style: Title,DejaVu Sans,52,&H00FFFFFF,&H0000E5FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,2,0,8,40,40,160,1
Style: Small,DejaVu Sans,19,&H00DDDDDD,&H00FFFFFF,&H00101010,&H90000000,0,0,0,0,100,100,0,0,1,1,0,2,20,20,55,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
def ts(s):
 return f'{int(s//3600)}:{int(s//60)%60:02}:{int(s)%60:02}.{int(s*100)%100:02}'
e=[]
def add(a,b,style,text):e.append(f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{text}')
add(0,12.5,'Title','POV: YOU SAID\\n{\\c&H00E5FF&}AI IS HARMLESS')
add(12.5,18.9,'Title','THE AI\\n{\\c&H00E5FF&}5 MINUTES LATER')
add(18.9,21.5,'Title','OKAY.\\n{\\c&H00E5FF&}I GET IT NOW.')
add(0,21.5,'Small','TEARS OF STEEL / BLENDER FOUNDATION\\nCC BY 3.0 / REMIX / mango.blender.org')
for seg in json.load(open('transcript.json')):
 words=[w for w in seg['words'] if w['start']<12.48]
 for i in range(0,len(words),3):
  group=words[i:i+3]
  if not group:continue
  text=' '.join(w['word'].strip() for w in group).upper()
  add(group[0]['start'],min(12.5,max(group[-1]['end'],group[0]['start']+.22)),'Caption',text)
add(12.5,14.1,'Caption','JUST A SMALL UPDATE')
add(14.1,15.7,'Caption','NOTHING TO WORRY ABOUT')
add(15.7,17.3,'Caption','TOTALLY UNDER CONTROL')
add(17.3,18.9,'Caption','...RIGHT?')
add(18.9,21.5,'Caption','THIS IS PRETTY FREAKY.')
open('captions.ass','w').write(head+'\n'.join(e)+'\n')
for i,(start,dur) in enumerate(segments):
 # Soft background fills vertical canvas; original widescreen picture stays readable.
 vf="split=2[b][f];[b]scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,boxblur=35:3,eq=brightness=-0.30[bg];[f]scale=900:-2,crop=720:374,eq=contrast=1.07:saturation=1.15[fg];[bg][fg]overlay=0:400,setsar=1,fps=30"
 cmd=['ffmpeg','-v','error','-y','-ss',str(start),'-i','source.mp4','-t',str(dur),'-filter_complex',vf,'-c:v','libx264','-preset','fast','-crf','21','-c:a','aac','-ar','48000','-ac','2',f'part{i}.mp4']
 subprocess.run(cmd,check=True)
open('concat.txt','w').write(''.join(f"file 'part{i}.mp4'\n" for i in range(len(segments))))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i','concat.txt','-vf','ass=captions.ass,drawbox=x=0:y=0:w=iw*t/21.5:h=8:color=0xFFE500:t=fill','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:v','libx264','-preset','fast','-crf','20','-c:a','aac','-b:a','160k','-movflags','+faststart','AI_Is_Harmless_Short.mp4'],check=True)
