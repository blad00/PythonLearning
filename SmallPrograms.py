#x = int(raw_input("Please enter an integer: "))
x=1
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)