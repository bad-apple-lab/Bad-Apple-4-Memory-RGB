# Bad-Apple-4-Memory-RGB

use ASUS Aura SDK

![](out.gif)

```sh
ffmpeg -v quiet -i "1080p.mp4" -vf scale=8:8 -c:v rawvideo -pix_fmt gray -f rawvideo - > 1.bin
gcc convert.c -o c.out && ./c.out
python run.py # python3
```
