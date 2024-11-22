    
class A:
    def __init__(self,name,age,passid,password,ticketsb,status,bt):
        self.name=name
        self.age=age
        self.passid=passid
        self.password=password
        self.ticketsb='no flights booked'
        self.status='not yet booked'
        self.bt=0
    def show(self):
        print(self.name,'\t',self.age,'\t','\t',self.passid,'\t',self.password,'\t',self.ticketsb,'\t',self.status,'\t',self.bt,'\t')
class B:
    def __init__ (self):
        self.tickets=100
        self.vel=100
        self.us=100
        self.passid=100
        self.password=10
        self.l=[]
y=B()
def passenger():
    while True:
        print("\n1.Signup\n2.Login\n3.Exit")
        n=int(input("enter your choice:"))
        if n==1:
            name=input("enter your name:")
            age=int(input("enter your age:"))
            print("\nyour id is:",y.passid)
            print("\nyour password is:",y.password)
            status=''
            bt=0
            ticketsb='no fligths booked'
            x=A(name,age,y.passid,y.password,ticketsb,status,bt)
            y.l.append(x)
            y.passid+=1 
            y.password+=1 
        elif n==2:
            n=int(input('Enter your id:'))
            m=int(input('Enter your password:'))
            r=''
            for i in range (len(y.l)):
                if y.l[i].passid==n and y.l[i].password==m:
                    print("\n\t\t.....logined successfully......")
                    while True:
                        print("\n1.book tickets\n2.cancel tickets\n3.Availability\n4.logout")
                        nm=int(input("enter your choice:"))
                        if nm==1:
                            print("\nFlight availabile:")
                            print("\nFlight choices:")
                            print("1.Trichy to coimbatore-₹5000")
                            print("2.Trichy to vellore-₹3500")
                            print("3.Trichy to USA-₹25000")
                            choice=int(input("enter your choice:"))
                            if choice==1:
                                r="Trichy to coimbatore"
                            elif choice==2:
                                r="Trichy to vellore"
                            elif choice==3:
                                r="Trichy to USA"
                            mn=int(input("enter no of tickets you want to book:"))
                            if mn<y.tickets and choice==1:
                                for i in range(len(y.l)):
                                    if y.l[i].passid==n:
                                        y.l[i].bt=mn
                                        y.l[i].status='pending'
                                        y.l[i].ticketsb=r
                                        print("\n \t \...wait for the moment....")
                            elif mn<y.vel and choice==2:
                                for i in range(len(y.l)):
                                    if y.l[i].passid==n:
                                        y.l[i].bt=mn
                                        y.l[i].status='pending'
                                        y.l[i].ticketsb=r
                                        print("\n \t \t...wait for the moment....")
                            elif mn<y.us and choice==3:
                                for i in range(len(y.l)):
                                    if y.l[i].passid==n:
                                        y.l[i].bt=mn
                                        y.l[i].status='pending'
                                        y.l[i].ticketsb=r
                                        print("\n \t \t...wait for the moment....")
                            else:
                                print("\n... Not Availabile...")
                        elif nm==2:
                            for i in range(len(y.l)):
                                if y.l[i].status=='not yet booked' or y.l[i].status=='approved':
                                    y.l[i].status='cancelled'
                                    if y.l[i].ticketsb=='Trichy to coimbatore':
                                        y.tickets+=y.l[i].bt
                                    elif y.l[i].ticketsb=='Trichy to vellore':
                                        y.vel+=y.l[i].bt
                                    elif y.l[i].ticketsb=='Trichy to USA':
                                        y.us+=y.l[i].bt
                                    print("\tThe tickets are successfully cancelled")
                                else:
                                    print("You are not booked any tickets to cancel")
                        elif nm==4:
                            break
                        elif nm==3:
                            print("\n \t\tAvailabile tickets")
                            print("1.Trichy to coimbatore =",y.tickets)
                            print("2.Trichy to vellore =",y.vel)
                            print("3.Trichy to USA =",y.us)
                        else:
                            print("\t\t....Invalid choice....")
        elif n==3:
            break
        else:
            print("....Erukura choice podu...")
            passenger()
def cashier():
    while True:
        print("\n1.show details\n2.approved tickets\n3.cancel tickets\n4.logout")
        n=int(input("enter your choice:"))
        if n==1:
            for j in range(len(y.l)):
                y.l[j].show()
        elif n==2:
            f=True
            print("\nwhom to approve tickets??")
            i=int(input("enter the id:"))
            for j in range (len(y.l)):
                if y.l[j].passid==i and y.l[j].bt<y.tickets:
                    f=False
                    y.l[j].status="approved"
                    if y.l[j].ticketsb=='Trichy to coimbatore':
                        y.tickets-=y.l[j].bt
                    elif y.l[j].ticketsb=='Trichy to vellore':
                        y.vel-=y.l[j].bt
                    elif y.l[j].ticketsb=='Trichy to USA':
                        y.us-=y.l[j].bt
                    print("\t..... The tickets are successfully approved....")
            if f:
                print("\n sorry... no tickets to approve")
        elif n==3:
            f=1
            print("\nwhich one passenger to get a cancelled tickets??")
            z=int(input("enter your id:"))
            for j in range(len(y.l)):
                if y.l[j].passid==z:
                    f=0
                    y.l[j].status='cancelled'
                    if y.l[j].ticketsb=='Trichy to coimbatore':
                        y.tickets+=y.l[j].bt
                    elif y.l[j].ticketsb=='Trichy to vellore':
                        y.vel+=y.l[j].bt
                    elif y.l[j].ticketsb=='Trichy to USA':
                        y.us+=y.l[j].bt
                    print("\t.....The tickets are successfully cancelled....")
            if f:
                print("\t....No tickets to cancel....")
        elif n==4:
            break
        else:
            print("\t\t...Erukura choice podu...")
print("\t \t WELCOME TO NAMMA AIRLINES")
while True:
    print("1.passenger\n2.cashier\n3.exit")
    n=int(input("enter your choice:"))
    if n==1:
        passenger()
    elif n==2:
        cashier()
    elif n==3:
        print("\n\t\t....THANKS FOR COMING....")
        break
    else:
        print("Enter the correct choices 1 or 2 or 3")



