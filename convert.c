#include <stdio.h>

typedef unsigned char B;

const int FRAME_SIZE = 64;
const int FRAME_SIZE2 = 4;

int main() {
    FILE *f = fopen("1.bin", "rb");
    FILE *f2 = fopen("2.bin", "wb");
    B *buf = (B *)malloc(FRAME_SIZE);
    B *buf2 = (B *)malloc(FRAME_SIZE2);
    int count = 0;
    while (FRAME_SIZE == fread(buf, 1, FRAME_SIZE, f)) {
        memset(buf2, 0, FRAME_SIZE2);
        for (int i = 0; i < 8; i++) {
            for (int j = 2; j < 6; j++) {
                if (buf[i << 3 | j] & 128) {
                    buf2[j - 2] |= 1 << i;
                }
            }
        }
        fwrite(buf2, 1, FRAME_SIZE2, f2);
        printf("%d\n", count);
        count++;
    }
    fclose(f);
    fclose(f2);
    return 0;
}
