#Get one dynamic array of given size and do all the operations of DS (Insert,Delete,Search,Sort)

a=[]
def func():
    print("Enter the type of operation")
    print("1.Create\n2.Insert\n3.Delete\n4.Search\n5.Sort\n6.Abort")
    e=int(input())
    if e==1:
        create()
    elif e==2:
        insert()
    elif e==3:
        delete()
    elif e==4:
        search()
    elif e==5:
        sort()
    else:
        print("Thank You")
    

def create():  
    n=int(input("Enter size"))
    for i in range(1,n+1):
        t=int(input("Enter Num"))
        a.append(t)
    print(a)
    func()

def insert():
    print("Enter the num to insert")
    ins=int(input())
    
    a.append(ins)
    print(a)
    func()
    
def delete():
    print("Enter the num to del")
    d=int(input())
    a.remove(d)
    print(a)
    func()
    
def search():
    print("Enter the num to search")
    s=int(input())
    f=0
    for i in a:
        if i==s:
            f=1
    if f==1:
        print("Found")
    if f==0:
        print("Not Found")
    func()
def sort():
    a.sort()
    print(a)
    func()

func()
