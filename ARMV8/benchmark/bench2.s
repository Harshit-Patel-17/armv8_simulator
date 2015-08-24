_start:
mov w1,#5
mov w2,#8
mov x3,#46
mov w7,#4
adc w0, w1, w2
ands w0, w1, #6
ands w0, w1, w2, lsr #2
bic w0, w1, w2, lsl #2
bics w0, w1, w2, lsl #2
ccmn w0, #7, #11, EQ
ccmn w0, w1, #11, NE
cls w0, w1
clz w0, w1
cinv w0, w1, EQ
cneg w0, w1, NE
cset w0, EQ
csinc w0, w1, w2, EQ
CMN w1, #5, LSL #12
STP W1, W2, [X3, #128]!
asr w3,w2,#5
mov x2,#52
umull x3,w2,w1
lsl w4,w3,#10
sdiv w3,w2,w1
LDRB W7, [X2, X3]
LDRH  W6, [X3, #21]!
LDP W1, W2, [X3], #16
sdiv w3,w2,w1
asr w3,w2,#5
umull x3,w2,w1
lsl w4,w3,#10
ror w1,w2,w3
lsr w4,w3,#10
udiv x1,x2,x3
