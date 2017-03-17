def Hanoi(n,src,dest,spare):
    if n>0:
        fm = Hanoi(n - 1, src, spare, dest)
        print('Moving '+str(n)+' from ' +src+' to '+dest)
        sm = Hanoi(n - 1, spare, dest, src)
        return fm +sm+1
    else:
        return 0

def main():
    print(Hanoi(3,'Tree1','Tree3','Tree2'))


if __name__ == '__main__':
    main()