# import time
import queue
import threading
import numpy as np
import pyaudio
import win32com.client
from scipy import signal

FRAME_SIZE = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 22050
# 16000 22050 44100 48000
split_nums = [-4096, -512, -64, -8, 8, 64, 512, 4096, 2147483647]

auraSdk = win32com.client.Dispatch("aura.sdk.1")
print('SwitchMode...')
auraSdk.SwitchMode()
print('Enumerate...')
devices = auraSdk.Enumerate(0)

mem = [devices[1], devices[3], devices[0], devices[2]]
water = devices[4]
board = devices[5]
top = devices[6]


def mem4(l: list(), slp: int = 0.1) -> None:
    # assert(len(l) == 4)
    # for i in l:
    #     assert(type(i) == int)
    #     assert(0 <= i <= 8)
    for i in range(4):
        for j in range(l[i]):
            mem[i].Lights(j).color = 0xff00ff
        for j in range(l[i], 8):
            mem[i].Lights(j).color = 0x00ff00
        mem[i].Apply()
    # time.sleep(slp)


p = pyaudio.PyAudio()
q = queue.Queue()
ad_rdy_ev = threading.Event()
window = signal.hamming(FRAME_SIZE)


def audio_callback(in_data, frame_count, time_info, status):
    q.put(in_data)
    ad_rdy_ev.set()
    return (None, pyaudio.paContinue)

# Settings-Privay-Microphone: Allow desktop apps to access your microphone

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=False,
                frames_per_buffer=FRAME_SIZE,
                stream_callback=audio_callback)


print("start_stream...")
stream.start_stream()

print("running...")

while stream.is_active():
    ad_rdy_ev.wait()
    if not q.empty():
        data = q.get()
        while not q.empty():
            q.get()
        rt_data = np.frombuffer(data, np.dtype('<i2'))
        rt_data = rt_data * window

        d1 = list()
        ll = FRAME_SIZE >> 2
        rr = (FRAME_SIZE >> 2) | (FRAME_SIZE >> 3)
        for _ in range(4):
            x = np.average(rt_data[ll: rr])

            for i in range(9):
                if x < split_nums[i]:
                    d1.append(i)
                    break

            ll = rr
            rr += FRAME_SIZE >> 8
        mem4(d1)

    ad_rdy_ev.clear()

stream.stop_stream()
stream.close()
p.terminate()

print("End...")
input()
