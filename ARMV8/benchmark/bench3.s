_start:
mov x4,#52
mov w6,#5
mov x7,#46
LDRH  W6, [x7, #128]!
udiv x1,x2,x3
ands w0, w1, #9
clz w0, w1
bic w0, w1, w2, lsl #4
umull x3,w2,w1
LDRB W7, [X2, X3]
adc w0, w1, w2
ands w0, w1, w2, lsl #2
ccmn w0, w1, #11, NE
cls w0, w1
umull x3,w2,w1
ror w1,w2,w5
cinv w0, w1, CS
CMN w1, #5, LSL #2
cneg w0, w1, NE
lsl w6,w5,#10
sdiv w5,w2,w1
lsr w6,w5,#10
LDP W6, W7, [X7, #16]!
asr w5,w2,#5
lsl w6,w5,#10
sdiv w5,w2,w1
STP X1, X2, [X7], #64
mov w7,#8
ccmn w0, #7, #11, CS
asr w5,w2,#5
cset w0, CS
csinc w0, w1, w2, CS
LDRSB W7, [X2, X3]
bics w0, w1, w2, lsr #5
