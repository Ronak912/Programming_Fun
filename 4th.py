"""
    /home/eric/
    /home/eric/Documents
    /home/eric/Documents/Expenses/dir1/dir2
    /home/eric/Documents/Expenses/2014-10.csv
    /home/eric/Documents/interview.md
    /home/eric/Documents/report.csv
    /home/eric/todo.md

"""

import os

for dirs in os.listdir('/Users/Ronak/Public'):
    print "Dirs: ", dirs


outputlst = []
def list_dir(inuputdir, outputlst):
    if not inuputdir:
        return None
    currdir = inuputdir
    for fileordir in os.listdir(currdir):
        #print fileordir
        fullpath = "{0}/{1}".format(currdir, fileordir)
        if not os.path.isdir(fullpath):
            #print "If"
            outputlst.append(fullpath)
            print "Files: ", fullpath
        else:
            print "Dirs: ", fullpath
            list_dir(fullpath, outputlst)

    return outputlst


def childDir(inputdir, lst):
    for fileordir in os.listdir(inputdir):
        fullpath = "{0}/{1}".format(inputdir, fileordir)
        if not os.path.isdir(fullpath):
            lst.append(fullpath)
        else:
            childDir(fullpath, lst)


print "First: "
print "Output List: ", list_dir('/Users/Ronak/Public/', outputlst)
print "Second"