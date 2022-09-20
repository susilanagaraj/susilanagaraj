import mysql.connector
#import datetime
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="keerthi",
    database="TOURISM"
  
)
mycursor=mydb.cursor()
#mycursor.execute("create database TOURISM")
#mycursor.execute("create table tour_details (customers_name varchar(225),place varchar(225),days int,budjet int)")
#print("completed")




vellore=1000
velloreac=1500
coibatore=500
coibatoreac=800
madurai=400
maduraiac=600
valliyur=150
valliyurac=300
salem=1300
salemac=800
tuticorin=150
tuticorinac=300
virudhunagar=500
virudhunagarac=700

def travel(Name,Phone_No,From_loc,To_loc,Tickets,Price):
    sql="insert into tickets_details (Name,Phone_No,From_loc,To_loc,Tickets,Price) values (%s,%s,%s,%s,%s,%s)"
    val=(Name,Phone_No,From_loc,To_loc,Tickets,Price)
    mycursor.execute(sql,val)
    mydb.commit()

def ticketdetailes():
        print("")
        print("***************************************************")
        print("\t\t |**Ticket Detailes**|")
        print(f"Name:{Name}")
        print(f"Phone_No:{Phone_No}")
        print(f"From:{From_loc}")
        print(f"To:{To_loc}")
        print(f"Tickets:{Tickets}")
        print(f"Totel Price:{Price}")
        print("Your Tickets Was Booked \n Happy Journey")
        print("***************************************************")

user=input("Type **start** To Book Tickets:").lower().strip()
if user=="start":
    print("***Welcome To Ticket Booking***")
    Name=input("Enter Your Name:")
    Phone_No=int(input("Enter Your Phone_No:"))
    From_loc="Tirunelveli"
    print("")
    print("Tirunelveli To:\n1.Chennai\n2.Coibatore\n3.Madurai\n4.Nagercoil\n5.Salem\n6.Tuticorin\n7.Virudhunagar\n")
    To_loc=input("Enter Your place name:").lower().strip()
    print("")
    print("1.A/c\n2.NON-A/C")
    print("")
    Type=int(input("Select Your Choice:"))
    if To_loc=="chennai" and Type==1:
        print(f"{From_loc}->Chennai")
        print(f"Ticket Price:{vellore}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*1500
        ticketdetailes()
    elif To_loc=="chennai" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{vellore}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*vellore
        ticketdetailes()
    elif To_loc=="coibatore" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{coibatore}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*coibatore
        ticketdetailes()
    elif To_loc=="coibatore" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{coibatoreac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*coibatoreac
        ticketdetailes()
    elif To_loc=="madurai" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{madurai}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*madurai
        ticketdetailes()
    elif To_loc=="madurai" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{maduraiac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*maduraiac
        ticketdetailes()
    elif To_loc=="nagercoil" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{valliyur}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*valliyur
        ticketdetailes()
    elif To_loc=="nagercoil" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{valliyur}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*valliyur
        ticketdetailes()
    elif To_loc=="salem" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{salem}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*salem
        ticketdetailes()
    elif To_loc=="coibatore" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{salemac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*salemac
        ticketdetailes()
    elif To_loc=="tuticorin" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{tuticorin}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*tuticorin
        ticketdetailes()
    elif To_loc=="tuticorin" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{tuticorinac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*tuticorinac
        ticketdetailes()
    elif To_loc=="virudhunagar" and Type==1:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{virudhunagar}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*virudhunagar
        ticketdetailes()
    elif To_loc=="virudhunagar" and Type==2:
        print(f"{From_loc}->{To_loc}")
        print(f"Ticket Price:{virudhunagarac}")
        Tickets=int(input("Enter how many tickets you want:"))
        Price=Tickets*virudhunagarac
        ticketdetailes()
    else:
        print("")
        print("Enter Destination Correctly")
        print("")

else:
    print("")
    print("Enter Start Correctly")
    print("")



