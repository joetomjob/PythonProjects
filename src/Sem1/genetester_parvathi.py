"""
file: DNALIst.py
language: python3
author: pvc8661@rit.edu by  Pallavi Chandanshive
author: pan7447@rit.edu by  Paravthi Nair
description: Implementation of LinkedList
"""

import dnalist

""" This class consiste of all the test cases
"""
class genetester:

     def init_tester(self):
         """
            Testing the  constuctor of DNA_List class
            precondition: LinkedList is created
            postcondition: hLinkedlist is crated with teh avlues passed in the constructor

         """
         DNA1 = dnalist
         print('Testing the init tester....')
         print('Testing Passing Empty String')
         t = DNA1.DNAList("")
         print(t.__str__())
         print('Passing String')
         t = DNA1.DNAList("ACGT")
         print(t.__str__())
         print("Pssing invalid characters")
         t= DNA1.DNAList("AABT")


     def append_tester(self):
         """
            Testing the  append method of DNA_List class
            precondition:LinkedList is created
            postcondition: various dff arguments are tetested for appending char

         """
         DNA1 = dnalist
         print('Testing the append method....')
         print('Passing Empty string')
         t = DNA1.DNAList('ACGT')
         t.append('')
         print(t.__str__())
         print('Passing IllegalArguments ')
         t.append(1)
         print('Appending When LinkedList is Null')
         t = DNA1.DNAList('')
         t.append('A')
         print(t.__str__())
         print('Appending at the end of the list')
         t = DNA1.DNAList('ACGTT')
         t.append('G')
         print(t.__str__())
         print('Appending more characters')
         t.append('AA')
         print('Appending invalid character')
         t.append('B')


     def join_Tester(self):
         """
             Testing the  join method of DNA_List class
             precondition: LinkedList is created
             postcondition: checks various joining condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the join method....')
         print('Join When LinkedList is Null')
         t = DNA1.DNAList('')
         t1 = DNA2.DNAList('ACGT')
         t.join(t1)
         print(t.__str__())
         print('Joining at the end of the list')
         t = DNA1.DNAList('ACG')
         t2 = DNA2.DNAList('TTA')
         t.join(t2)
         print(t.__str__())


     def splice_Tester(self):
         """
            Testing the  splice method of DNA_List class
            precondition: LinkedList is created
            postcondition: checks various splicing condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the splice method....')
         print('Testing when index is not in range')
         t = DNA1.DNAList('ACGGT')
         t2 = DNA2.DNAList('ACGT')
         t.splice(6,t2)
         #print(t.__str__())
         print('splice at last index')
         t = DNA1.DNAList('GACT')
         t2 = DNA2.DNAList('ACGT')
         t.splice(4, t2)
         print(t.__str__())
         print('splice at middle index')
         t = DNA1.DNAList('ACGTT')
         t2 = DNA2.DNAList('ACGT')
         t.splice(1, t2)
         print(t.__str__())
         print('Illegal passing of arguments')
         t = DNA1.DNAList('ACGT')
         t2 = DNA2.DNAList('GGCCT')
         t.splice('A', t2)
         print('Negative value of arguments')
         t = DNA1.DNAList('ACGT')
         t2 = DNA2.DNAList('GACT')
         t.splice(-1, t2)
         print('if the list on which splice is being done is empty ')
         t = DNA1.DNAList('')
         t2 = DNA2.DNAList('GACTT')
         t.splice(0, t2)
         print(t.__str__())
         print('if the list with which splice is being done is empty ')
         t = DNA1.DNAList('ACCAT')
         t2 = DNA2.DNAList('')
         t.splice(2, t2)
         print(t.__str__())
         print('if other list has invalid characters')
         t = DNA1.DNAList('ACCAT')
         t.splice(2, t2)
         t2 = DNA2.DNAList('BGT')

     def snip_Tester(self):
         """
            Testing the  join method of DNA_List class
            precondition: LinkedList is created
            postcondition: checks various joining condition

         """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the snip method....')
         print('Indices in range')
         t = DNA1.DNAList('ACCTTG')
         t.snip(2, 3)
         print(t.__str__())
         print('Index is not in range')
         t = DNA1.DNAList('ACCTTG')
         t.snip(8,9)
         #print(t.__str__())
         print('Snip using boundary indices')
         t = DNA1.DNAList('GACTT')
         t.snip(0,4)
         print(t.__str__())
         print('Illegal passing of arguments')
         t = DNA1.DNAList('ACCTTG')
         t.snip('A', 4)
         print('Negative value of arguments')
         t = DNA1.DNAList('ACCTTG')
         t.snip(-1, 4)
         print('i1 is greater than i2 ')
         t = DNA1.DNAList('ACCTTG')
         t.snip(4, 1)
         print('i1 equal to i2 ')
         t = DNA1.DNAList('ACCTTG')
         t.snip(2, 2)
         print(t.__str__())
         print('i1 and i2 equals to 0')
         t = DNA1.DNAList('ACCTTG')
         t.snip(0, 0)
         print(t.__str__())


     def replace_Tester(self):
         """
        Testing the  replace method of DNA_List class
        precondition: LinkedList is created
        postcondition: checks various replacing conditions
        """
         DNA1 = dnalist
         DNA2 = dnalist
         print('Testing the replace method....')
         print('Normal case')
         t = DNA1.DNAList('ACCTTG')
         t.replace('CT',t2)
         t2 = DNA2.DNAList('AC')
         print(t.__str__())
         print('Replacing the starting elements')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('GG')
         t.replace('AC', t2)
         print(t.__str__())
         print('Replacing the ending elements')
         t = DNA1.DNAList('ACCTTG')
         t.replace('TG', t2)
         t2 = DNA2.DNAList('TT')
         print(t.__str__())
         print('Replacing the first element')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('C')
         t.replace('A', t2)
         print(t.__str__())
         print('Replacing the last element')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('T')
         t.replace('G', t2)
         print(t.__str__())
         print('List 1 is empty')
         t = DNA1.DNAList('')
         t2 = DNA2.DNAList('CG')
         t.replace('AC', t2)
         print('List 2 is empty')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('')
         t.replace('CT', t2)
         print(t.__str__())
         print('String and list length not equal')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('GGG')
         t.replace('TT', t2)
         print(t.__str__())
         print('Invalid string')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('TTT')
         t.replace(123, t2)
         print('String not found')
         t = DNA1.DNAList('CCGTAAT')
         t2 = DNA2.DNAList('ACGTTT')
         print(t.replace('CT', t2))
         print('Invalid characters in the list 2')
         t = DNA1.DNAList('ACCTTG')
         t2 = DNA2.DNAList('PQG')
         t.replace('CC', t2)



     def copy_Tester(self):
         """
         Testing the  replace method of DNA_List class
         precondition: LinkedList is created
         postcondition: checks various copying conditions
         """
         DNA1 = dnalist
         print('Testing the copy method....')
         print('Normal Case')
         t = DNA1.DNAList('ACCGGT')
         print(t.__str__())
         print("copy of the list is as below:")
         t.copy()
         print('Copy of empty list')
         t = DNA1.DNAList('')
         print(t.__str__())
         print("copy of the list is as below:")
         t.copy()


     def str_Tester(self):
         """
        Testing the  replace method of DNA_List class
        precondition: LinkedList is created
        postcondition: checks various test cases
                     """
         DNA1 = dnalist
         print('Testing the str method....')
         print('Normal Case')
         t = DNA1.DNA_List('ACCGT')
         s=t.__str__()
         print(s)
         print('Testing if list is empty')
         t = DNA1.DNA_List('')
         s = t.__str__()
         print(s)




g = genetester()

g.init_tester()
g.append_tester()
g.join_Tester()
g.splice_Tester()
g.snip_Tester()
g.replace_Tester()
g.copy_Tester()
g.str_Tester()







