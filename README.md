# stateMachine
Program for creating intersection of two state machines in Python

## Executing:
Run from terminal : python state.py path/to/file 


## Syntax for state machines
File should contain two state machines with the next syntax:
	
start = I ;   I - name of initial state
end = F1,F2,F3.... ; Fn - names of final states

transitions:
S1 C1 : S2
S2 C2 : S3
....
;

set of rules : ( S1 , C , S2)
when in state S1 when C is read, go to state S2
C - part of the input alphabet





