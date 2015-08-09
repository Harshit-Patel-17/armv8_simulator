_start:
mov x0, #0xaa
mov x1, #372
str x1, [x0]
subs x0, x0, #4
ldrh w2, [x0, #4]
