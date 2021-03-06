# ARMv8 Simulator #

## Getting started ##

1) Clone the project to your local repository.

2) Run `setup.sh` file using following command on linux terminal. It will setup `pyelftools` and `matplotlib` in your machine.
```
#!Linux Shell Command

$sudo sh setup.sh
```
3) Go to folder <project_path>/ARMV8 from linux terminal.

4) Run following command to get help in using the application to simulate various ARM programs.
```
#!Linux Shell Command

$python main.py --help
```

## New features ##

1) Support for 5-stage pipelining (IF->ID->EX->MA->WB).

2) Support for data-forwarding mode. (See section data-forwarding for more details)

3) Support for new instructions CSET, CSINC, CSNEG, ADC, ANDS, BIC, BICS, CCMN, CINV, CLS, CLZ, CMN, CNEG, LDRB, LDRH, LDRSB, LDP, STP, ASR, LSL, LSR, ROR, SDIV,UMULL, UDIV, MOVK, MOVN, MOVZ, FMOV, FADD, FSUB, FMAX, FMIN.

4) New debugger commands `cycles`, `stalls`, `pipe`, `energy`, `activity` and `nc`.

## Data forwarding ##

Run simulation with `--forward` command-line argument at the end to enable data-forwarding in 5-stage instruction pipeline. It is assumed that data can be forwarded from `EX/MA and MA/WB interstage registers` for use by subsequent instructions.

For example, the first command below will simulate ARM programs without data-forwarding while the other one will enable data-forwarding in  simulation.

```
#!Linux Shell Command

$python main.py MyTestcases/t1.out
$python main.py MyTestcases/t1.out --forward
```