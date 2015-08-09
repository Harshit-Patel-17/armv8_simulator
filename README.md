ARMv8 Simulator

Getting started

1) Clone the project to your local repository.

2) Run make.sh file using following command on linux terminal.
```
#!Linux Shell Command

$sudo ./make.sh
```
3) Go to folder <project_path>/ARMV8 from linux terminal.

4) Run following command to get help in using the application to simulate various ARM programs.
```
#!Linux Shell Command

$python main.py --help
```

New features

1) Added support for 5-stage pipelining.

2) Added support for data-forwarding mode. (See section data-forwarding for more details)

3) Added support for new instructions CSET, CSINC, CSNEG, ADC, ANDS, BIC, BICS, CCMN, CINV, CLS, CLZ, CMN, CNEG, LDRB, LDRH, LDRSB, LDP, STP, ASR, LSL, LSR, ROR, SDIV,UMULL, UDIV.