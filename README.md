# Bad-Apple-4-Memory-RGB

use ASUS Aura SDK

![](out.gif)

```sh
pip install pywin32
ffmpeg -v quiet -i "1080p.mp4" -vf scale=8:8 -c:v rawvideo -pix_fmt gray -f rawvideo - > 1.bin
gcc convert.c -o c.out && ./c.out
python run.py # python3
```

##### sound waveform (realtime)

Settings -> Privay -> Microphone:
1. Change -> On;
2. Allow desktop apps to access your microphone.

Right click speakers icon -> Sound -> Recording -> Stereo Mix:
1. Right click -> Enable;
2. Right click -> Properties -> Listen -> Listen to this device.

Settings -> System -> Sound:
1. Input -> Choose your input device -> Stereo Mix (Realtek(R) Audio)

***Stereo Mix** can be replaced with one that has the same function.

```sh
pip install pywin32 pyaudio
python wave.py # python3
```
