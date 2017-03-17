from dnalist import DNAList


def init_tester():
    tester = DNAList("")
    print("Testing Passing Empty String" +" " + tester.__str__())
    tester = DNAList("AACCGGTT")
    print("Passing String" +" "+ tester.__str__())




def append_tester():
    tester=DNAList('ACGT')
    tester.append("")
    print('Passing Empty string' + " "+ tester.__str__() )
    tester.append("%^&^@")
    print('Passing IllegalCharacters ' + " " +tester.__str__())
    tester=DNAList("")
    tester.append("A")
    print('Appending When List is Null' + " " + tester.__str__())


def join_Tester():
    tester=DNAList("AACCGGTT")
    tester2=DNAList("")
    tester.join(tester2)
    print('Join When List is Null' + " " + tester.__str__() )
    tester=DNAList('AACCGGTT')
    tester2=DNAList("AAA")
    tester.join(tester2)
    print('Joining at the end of the list' + " " + tester.__str__() )


def splice_Tester():
    test = DNAList('AACCGGTT')
    tester = DNAList('ACGT')
    test.splice(1,tester)
    print('Testing when index is not in range'+" "+test.__str__())
    test = DNAList('AACCGGTT')
    tester = DNAList('ACGT')
    test.splice(7,tester)
    print('splice at last index'+" "+test.__str__())
    test = DNAList('AACCGGTT')
    tester = DNAList('ACGT')
    test.splice(3,tester)
    print('splice at middle index'+" "+test.__str__())
    test = DNAList('AACCGGTT')
    tester = DNAList('ACGT')
    test.splice(0,tester)
    print('splice at the first index'+" " +test.__str__())
    test = DNAList('AACCGGTT')
    tester = DNAList('ACGT')
    test.splice(-1,tester)
    print('Negative index'+" "+test.__str__())
    test = DNAList('AACCGGTT')
    tester = DNAList('')
    test.splice(1,tester)
    print('if the list is empty '+" "+test.__str__())



def snip_Tester():
    test = DNAList('AACCGGTT')
    test.snip(1, 4)
    print('Indices in range'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(1,8)
    print('Index is not in range'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(0,7)
    print('Snip using boundary indices'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(1, 1)
    print('Illegal passing of arguments'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(1, -4)
    print('Negative value of arguments'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(4,1)
    print('i1 is greater than i2 '+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(3,3)
    print('i1 equal to i2 '+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    test.snip(0, 0)
    print('i1 and i2 equals to 0'+ " "+ test.__str__())


def replace_Tester():
    test = DNAList('AACCGGTT')
    r = DNAList('TTGGCC')
    test.replace('AA',r)
    print('Normal case'+ " "+ test.__str__())
    test = DNAList('')
    r = DNAList('TTGGCC')
    test.replace('AA',r)
    print('List 1 is empty'+ " "+ test.__str__())
    test = DNAList('AACCGGTT')
    r = DNAList('')
    test.replace('AA',r)
    print('List 2 is empty'+ " "+ test.__str__())



def copy_Tester():
    test = DNAList("AACCTTGG")
    test.copy()
    print('Normal Case'+ " "+ test.__str__())
    test = DNAList("")
    print('Copy of empty list'+" "+test.__str__())


def str_Tester():
    test = DNAList("AACCTTGG")
    print('Testing the str method....'+ " "+ test.__str__())
    test = DNAList("")
    print('Testing if list is empty'+" "+test.__str__())


def main():
    # init_tester()
    # append_tester()
    # join_Tester()
    # splice_Tester()
    # snip_Tester()
     replace_Tester()
    # copy_Tester()
    # str_Tester()

main()