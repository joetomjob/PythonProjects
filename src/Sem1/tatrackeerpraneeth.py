from heapq import *

oliversList = []
colleensList = []

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for i in range(len(h))]

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
            heappush(colleensList,tupleOfStudentWithConfusion)
            # Sorting the list based on the weights, which is the 1st index of the list
            heapsort(colleensList)
            # Reversing the order as we need more weight as first priority
            colleensList.reverse()

        if line == "Oliver ready\n":
            oliverHelpingStudent = oliversList.pop(0)
            print("Oliver helping %s"%(oliverHelpingStudent[0]))
            # remove the element from oliversList as well as colleensList
            colleensList.remove(oliverHelpingStudent)

        elif line == "Colleen ready\n":
            colleenHelpingStudent = heappop(colleensList)
            print("Colleen helping %s"%(colleenHelpingStudent[0]))
            # remove the element from oliversList as well as colleensList
            oliversList.remove(colleenHelpingStudent)

print("Students left unhelped:")

# Olivers list or colleens list both can be used, they'll contain the same data
for i in oliversList:
    print(i[0])
