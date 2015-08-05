_start:
mov w1,#0
cmn w2,#0
cset w7, eq
mov w2,#4
mov w4,#5
cinv w3, w2, ne 
