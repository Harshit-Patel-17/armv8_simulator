_start:
mov x0, #0xaa
mov x1, #-372
str x1, [x0]
subs x0, x0, #4
ldrsb x2, [x0, #4]
mov w3, w2
