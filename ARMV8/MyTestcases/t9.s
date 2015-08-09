_start:
mov x0, #0xaa
mov w1, #2
mov w2, #3
stp w1, w2, [x0]
ldp w3, w4, [x0]
