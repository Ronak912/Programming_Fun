line = 5
for val in xrange(1, int(line)+1):
    temp = val
    print str(temp).rjust(len('{}'.format(line))), '{0:o}'.format(temp).rjust(len('{0:o}'.format(line))), '{0:x}'.format(temp).rjust(len('{0:x}'.format(line))), '{0:b}'.format(temp).rjust(len('{0:b}'.format(line)))