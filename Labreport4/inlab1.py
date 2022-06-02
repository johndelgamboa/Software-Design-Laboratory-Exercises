def minmax(inp_list, i=0, emin=float('inf'), emax=float('-inf')):
    e = inp_list[i]

    if e < emin: emin = e
    if e > emax: emax = e
    if i == len(inp_list) - 1:
        return (emin, emax)
    return minmax(inp_list, i + 1, emin, emax)


print(minmax([5, 10, 20, 25, 40]))