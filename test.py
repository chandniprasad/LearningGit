#Import the video
import subprocess
import os
location=os.path.abspath(os.path.join(os.getcwd()))
root=os.path.abspath(os.path.join(location, '..'))
path=os.path.abspath(os.path.join(location, 'video'))
print(path)
subprocess.run(['ls','video'])

#logic to trim the video

#ffmpeg -i abc.mp4 -ss 00:00:00 -t 00:01:00 -c:v copy -c:a copy output1.mp4