oliversList = []
colleensList = []

# Opening the file
with open('students.txt') as f:
    for line in f:
        # Split each line at the space
        tupleOfStudentWithConfusion = tuple(line.split())
        # Append the tuple of students to each of the TA's lists
        if tupleOfStudentWithConfusion[0] != "Oliver" and tupleOfStudentWithConfusion[0] != "Colleen":
            print("%s is looking for help!"%(tupleOfStudentWithConfusion[0]))
            oliversList.append(tupleOfStudentWithConfusion)
            # Duplicating oliversList to colleensList
            colleensList = oliversList[:]
            # Sorting the list based on the weights, which is the 1st index of the list
            colleensList.sort(key=lambda tup: tup[1])
            # Reversing the order as we need more weight as first priority
            colleensList.reverse()

        if line == "Oliver ready\n":
            oliverHelpingStudent = oliversList[0]
            print("Oliver helping %s"%(oliverHelpingStudent[0]))
            # remove the element from oliversList as well as colleensList
            alreadyHelpedStudent = oliversList.pop(0)
            colleensList.remove(alreadyHelpedStudent)

        elif line == "Colleen ready\n":
            colleenHelpingStudent = colleensList[0]
            print("Colleen helping %s"%(colleenHelpingStudent[0]))
            # remove the element from oliversList as well as colleensList
            alreadyHelpedStudent = colleensList.pop(0)
            oliversList.remove(alreadyHelpedStudent)

print("Students left unhelped:")

# Olivers list or colleens list both can be used, they'll contain the same data
for i in oliversList:
    print(i[0])
