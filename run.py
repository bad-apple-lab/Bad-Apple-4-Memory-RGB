import time
import win32com.client

auraSdk = win32com.client.Dispatch("aura.sdk.1")
print('SwitchMode...')
auraSdk.SwitchMode()
print('Enumerate...')
devices = auraSdk.Enumerate(0)

mem = [devices[1], devices[3], devices[0], devices[2]]

b = open('2.bin', 'rb').read()

print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)

lc = time.perf_counter()

while b:
    for i in range(4):
        c = int(b[i])
        for j in range(8):
            mem[i].Lights(j).color = 0x00ff00 if c & 1 else 0x0000ff
            c >>= 1
        mem[i].Apply()
    b = b[4:]
    print('.', end='', flush=True)

    rc = time.perf_counter()
    if rc - lc < 1/31:
        rc = time.perf_counter()
    lc = rc


print('End...')
