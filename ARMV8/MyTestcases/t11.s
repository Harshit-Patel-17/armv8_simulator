_start:
mov x0, #0xaa
mov w1, #6
mov w2, #3
udiv x1, x1, x2
stp x1, x2, [x0]
ldp x3, x4, [x0]
