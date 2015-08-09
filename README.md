# ARMv8 Simulator #

## Getting started ##

1) Clone the project to your local repository.

2) Run `make.sh` file using following command on linux terminal.
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

## New features ##

1) Added support for 5-stage pipelining (IF->ID->EX->MA->WB).

2) Added support for data-forwarding mode. (See section data-forwarding for more details)

3) Added support for new instructions CSET, CSINC, CSNEG, ADC, ANDS, BIC, BICS, CCMN, CINV, CLS, CLZ, CMN, CNEG, LDRB, LDRH, LDRSB, LDP, STP, ASR, LSL, LSR, ROR, SDIV,UMULL, UDIV.

4) Added new debugger commands `cycles` and `stalls`.

## Data forwarding ##

Run simulation with `--forward` command-line argument at the end to enable data-forwarding in 5-stage instruction pipeline. It is assumed that data can be forwarded from EX/MA and MA/WB interstage registers for use by subsequent instructions.

For example, the first command below will simulate ARM programs without data-forwarding while the other one will enable data-forwarding in  simulation.

```
#!Linux Shell Command

$python main.py MyTestcases/t1.out
$python main.py MyTestcases/t1.out --forward
```