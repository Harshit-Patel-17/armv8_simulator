_start:
mov w7,#4
mov w2,#6
mov x3,#53
ands w0, w2, #6
umull x2,w2,w7
adc w0, w7, w2
ror w7,w2,w3
LDRB W7, [X2, X3]
mov x2,#52
LDRSB W7, [X2, X3]
asr w3,w2,#5
lsl w4,w3,#10
ccmn w0, #7, #11, EQ
cinv w0, w7, EQ
ccmn w0, w7, #11, CC
lsr w4,w3,#10
cls w0, w7
clz w0, w7
CMN w7, #5, LSL #2
sdiv w3,w2,w7
umull x3,w2,w7
udiv x1,x2,x3
cset w0, EQ
LDRH  W4, [X1], #30
bic w0, w7, w2, lsl #2
bics w0, w7, w2, lsl #2
cCCg w0, w7, CC
sdiv w3,w2,w7
LDP w7, W2, [X3], #16
csinc w0, w7, w2, EQ
STP w7, W2, [X3, #128]!
asr w3,w2,#5
lsl w4,w3,#10
ands w0, w7, #6
