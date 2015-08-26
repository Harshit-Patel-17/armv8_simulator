_start:
mov w1, 0xff09ffff
mov w2, 0x7f09ffff
fmov s1, w1
fmov s2, w2
fmin s3, s1, s2
fmax s4, s1, s2
