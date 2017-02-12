# stateMachine

----
## Intersect of two DFSM
see [Wikipedia](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)

>This is a program that takes two deterministic finite state machines (DFSM) and makes a DFSM that accepts the intersect or union of languages of those two state machines.

----
## Usage
1. Download repository
2. Run from terminal 
**python state.py path/to/file**  

----

## State machines syntax


>Deterministic state machines should be stored in file ( such as test) with the following syntax. State machines should be listed one after the other like in the test file.

----
### Initial states
    start = I;  
    end = F1, F2, F3,...

>I is the name of the initial state. 
Fn are the names of final states of DFSM

---
### Actions/Transition functions
> Transitions are represented as 
  **S1 C : S2**  - when in S1 state and C is read , state machine goes to state S2. C is an input symbol 

    transitions:
    S1 C1 : S2
    S2 C2 : S3
    ....
    ;

## changelog
* 12-Feb-2017





