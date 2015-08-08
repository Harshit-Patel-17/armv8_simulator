_start:
mov x0, 0xaa
mov w1,#3
str w1, [x0]
ldrb w2, [x0], #4
