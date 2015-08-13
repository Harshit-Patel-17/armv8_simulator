_start:
mov w2,#5
mov w3,#3
udiv w1, w2, w3
mov x4, #0xaa
str x1, [x4]
