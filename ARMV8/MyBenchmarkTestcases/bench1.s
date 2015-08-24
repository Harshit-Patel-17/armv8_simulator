_start:
mov w1,#0xffffffff
mov w30,#0xfffffff
umull x30,w1,w30
mov w2,#0xfff
cls w3,w2
sdiv w30,w1,w2
ands x1,x1,#0xf0
csneg w4,w1,w30,ne
fmov s1,#-5.25
fmov s2,#10.0
fmov v31.d[1], x2
fadd d3,d1,d2
fsub v3.4s,v1.4s,v2.4s
fmax d4,d3,d31
movk x15, #0xfff0, lsl #48
bics w0, w1, w2, lsl #3
fsub d3,d3,d2
movz x15, #32
ror w25,w3,w3
ccmn w25, w3, #6, eq
cls x4,x3
mov x10,#0xffffffffffffff33
udiv x11,x10,x2
cset w10, eq
csneg x1,x2,x3,ne
ldrh  W3, [x30, #15]!
stp w2, w3, [x4, #16]!
ldp w1, w2, [x4], #16
cinv x30,x25,eq
fmin s31,s1,s31
