import re
import sys


#Checking if the user has enetered the correct number of parameters

if len(sys.argv) != 3:
	exit("Program executed as: python " + sys.argv[0] + " -option(i/u) path/to/file");

#Opening file and reading it
try: 
	with open(sys.argv[2] , "r") as f:
		dat = f.read();
except IOError:
	exit("Open error");

# Checking option

if sys.argv[1][1] == 'i' :
	print "Intersection state machine: "
elif sys.argv[1][1] == 'u' :
	print "Union state machine: "
else:
	exit("Wrong option, must be -i or -u")


#Getting information for the first and second state machine

rAll = re.compile(r'start\s*=\s*(?P<start>[A-Za-z0-9_]+)\s*;\s*' +
				r'end\s*=\s*(?P<endlist>[A-Za-z0-9_ ,]+)\s*;\s*' +
				r'transitions:\s*(?P<actions>[A-Za-z0-9: \n]+);\s*'
)

first = rAll.match(dat)
second = rAll.match(dat[first.end():])


#Getting informating of initial states of both state machines
startState1 =  first.group('start')
startState2 =  second.group('start')

# Start state of the new state machine
state = startState1+startState2

#Getting all end states of both state machines

endStates1 = first.group('endlist')
endStates2 = second.group('endlist')

endState1 = re.findall(r'[A-Za-z0-9_]+' , endStates1)
endState2 = re.findall(r'[A-Za-z0-9_]+' , endStates2)

#Getting all actions for both states


actions =  first.group('actions')
actions2 = second.group('actions')

# Createing maps for actions, and sets for states 

automat1 = {}
states1  = set()

automat2 = {}
states2 = set()

alphabet = set()

# Getting all the states and actions into defined maps

rState = re.compile(r'([A-Z0-9_]+)\s*([0-9A-Za-z_])\s*:\s*([A-Za-z_0-9]+)\s*\n')

for m in rState.finditer(actions):
	automat1[m.group(1) , m.group(2)] = m.group(3)
	states1.add(m.group(1))
	alphabet.add(m.group(2))

for x in rState.finditer(actions2):
	automat2[x.group(1) , x.group(2)] = x.group(3)
	states2.add(x.group(1))
	alphabet.add(x.group(2))



# Creating state machine map and end state lists


automat3 = {}
intersection = set()
union = set()

# Making the Cartesian product of 2 state machines

for s1 in states1:
	for s2 in states2:
		for i in alphabet:
			automat3[s1+s2, i] = automat1[s1,i] + automat2[s2,i]
			if(s1 in endState1 and s2 in endState2):
				intersection.add(s1+s2)
			if(s1 in endState1 or s2 in endState2):
				union.add(s1+s2)


# Run the state machine

while True:
    try:
    	print "Next character: (ctrl+D to exit)"
        c= raw_input()
        if(c not in alphabet):
            raise ValueError
        state = automat3[state,c];
        print "Current state: " + state
    except EOFError:
        break
    except ValueError:
        print "Not in the alphabet. Try again."
        continue




if sys.argv[1][1] == 'i' :

	if state in intersection:
		print "State machine accepts the word"
	else:
		print "State machine does not accept the word"

elif sys.argv[1][1] == 'u' :
	if state in union:
		print "State machine accepts the word"
	else:
		print "State machine does not accept the word"










