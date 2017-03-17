__author__ = 'zjb'

def hanoi(n,src,dest,spare):
    '''
    Solves towerof Hanoi
    :param n: Number of disks
    :param src: Name of source location
    :param dest: Name of destination
    :param spare: Name of spare peg
    :return: Number of moves required
    '''
    if n > 0: #something to do here
        fmoves = hanoi(n-1,src,spare,dest)
        print("Moving " + str(n) + " from " + src + " to " + dest)
        smoves = hanoi(n-1,spare,dest,src)
        return fmoves + 1 + smoves;
    else:
        return 0

print(hanoi(5, 'Tower 1', 'Tower 3', 'Tower 2'));

