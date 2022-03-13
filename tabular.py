def tabular(data = [[""]],error = [[""]], collumnnames = [""], rownames = [""], pivot = "" , unit = ""):
    if collumnnames == [""]:
        columnnames = [""] * len(data)

    if rownames == [""]:
        rownames = [""] * len(data[0])

    print("\\begin{tabular}{c|"+"c" * len(data[0])+"}")
#top row
    print('  '+str(pivot)+ '&',end='')
    for j in range(len(collumnnames)-1):
        print('   '+str(collumnnames[j])+' &',end = '')
    print('   '+str(collumnnames[-1])+" \\\\ \\hline")
#left column
    for i in range(len(data)):
        print("   "+str(rownames[i])+"&",end = '')
#data matrix
        for j in range(len(data[i])-1):
            print("   \\SI{"+str(data[i][j])+"+-"+str(error[i][j])+"}{"+unit+"} & ",end = '')

        print("   \\SI{"+str(data[i][-1])+"+-"+str(error[i][-1])+"}{"+unit+"}  \\\\")
    
    print(" \\end{tabular}")

#Example
tabular([[1,2],[3,4]],[[1,2],[3,4]],["A","B"],["C","D"],"P","\meter")