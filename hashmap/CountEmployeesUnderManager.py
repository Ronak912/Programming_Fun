# http://www.geeksforgeeks.org/find-number-of-employees-under-every-manager/
#
# Find number of Employees Under every Employee
# Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs like below.
#
# { "A", "C" },
# { "B", "C" },
# { "C", "F" },
# { "D", "E" },
# { "E", "F" },
# { "F", "F" }
#
# In this example C is manager of A,
# C is also manager of B, F is manager
# of C and so on.

# ToDo: output it incorrect and need to come up with better approach


def countEmployees(indict):

    mgrempldict = {}
    for empl, mgr in indict.iteritems():
        if mgr == empl:
            continue

        if mgr not in mgrempldict:
            mgrempldict[mgr] = [empl]
        else:
            tmplst = mgrempldict.get(mgr, [])
            tmplst.append(empl)
            mgrempldict[mgr] = tmplst

    result = {}
    for key, val in indict.iteritems():
        countEmployeesUtil(key, mgrempldict, result)
    return result

def countEmployeesUtil(mngr, mgrempldict, result):
    count = 0
    if mngr not in mgrempldict:
        result[mngr] = 0
        return count
    elif mngr in result:
        count = result.get(mngr, 0)
    else:
        directempllist = mgrempldict.get(mngr, [])
        for empl in directempllist:
            count = countEmployeesUtil(empl, mgrempldict, result)

    return count


if __name__ == '__main__':
    recorddict = {"A": "C", "B": "C", "C": "F", "D": "E","E": "F", "F": "F"}
    print countEmployees(recorddict)