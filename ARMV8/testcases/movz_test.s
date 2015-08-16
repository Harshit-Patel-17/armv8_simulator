_start:
mov w1, 0xffffffff
mov w2, 0x1
umull x1, w1, w2 
movz x1, 0x1111, lsl 48
