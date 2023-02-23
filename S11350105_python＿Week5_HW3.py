infile = open("States.txt", 'r')
states = [line.rstrip() for line in infile]
original_states = states[:13]
original_states.sort()
original_states = original_states[:5]
for state in original_states:
    print(state)
infile.close()
