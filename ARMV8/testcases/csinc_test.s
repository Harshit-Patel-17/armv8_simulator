_start:
mov w1,#0
adds w2, w1,#0
cset w3, eq
mov w1,#3
mov w2,#4
csneg w3, w1, w2, ne
