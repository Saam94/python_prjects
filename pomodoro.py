# sets a timer for working -and rest periods
# run from the terminal

import sys
from pathlib import Path
import time
import winsound
path = Path.cwd()
print(str(path))

work = int(input('Set duration for working time (minutes): '))
break1 = int(input('Set duration for short break (minutes): '))
break2 = int(input('Set duration for long break (minutes): '))
input('Start timer')
starting = True
while starting == True:
    for i in range(4):
        print('Start working!')
        winsound.PlaySound("C:\Windows\Media\chimes.wav",winsound.SND_FILENAME)
        time.sleep(work*60)
        if i < 3:
            winsound.PlaySound("C:\Windows\Media\chimes.wav",winsound.SND_FILENAME)
            print('Time for short break!')
            time.sleep(break1*60)
        else:
            winsound.PlaySound("C:\Windows\Media\chimes.wav",winsound.SND_FILENAME)
            print('Time for long break')
    time.sleep(break2*60)
    winsound.PlaySound("C:\Windows\Media\chimes.wav",winsound.SND_FILENAME)
    print('Session finished!')
    start = input('Start new session? y/n:')
    if start == 'n':
        starting = False

