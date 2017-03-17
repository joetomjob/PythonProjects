class Task:

    __slots__ = ('name','age')

    def __init__(self,n,a):
        self.name = n;
        self.age = a;

    def work_on(self,some_year):
        self.age = self.age-some_year

k = Task('Joe',12)

print(k)
print(k.age)
print(k.name)

k.work_on(2)

print(k.age)

