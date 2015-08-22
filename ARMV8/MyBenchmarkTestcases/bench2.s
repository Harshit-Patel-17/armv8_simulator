_start:
mov x1,#-10
mov x2,#5
fmov d1,#7.5
fmov d2,x1
fmov x3,d1
movn x4,#5, lsl #32
movk x7,#10
fmin s31,s1,s2
fadd v30.2d,v31.2d,v2.2d
subs w4,w1,w2
csneg w1,w2,w3,ne
ccmn w1, w3, #15, eq
bics x1,x2,x3
umull x1,w2,w29
ldrsb  x3, [x2, #15]!
asr w25,w29,w30
lsl w25,w29,w30
fmax s30,s31,s1
fadd d29,d30,d3
csinc w0,w4,w2,eq
cinv w7,w1,ne
lsl w4,w3,#10
udiv x1,x2,x3
sdiv x1,x2,x3
LDP w7, W2, [X3], #16
csinc w0, w7, w2, EQ
STP w7, W2, [X3, #128]!
clz w0, w7
cmn w3, #5, LSL #12
adc w0, w7, w2
fmax s1,s2,s3
bics w0, w1, w2, lsr #5
