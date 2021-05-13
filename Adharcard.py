import sqlite3
class AddressBook:
    def init(self):
        self.contactName=""
        self.emailid=""
        self.address=""
        self.Adharno=""
        self.DOB=""
        self.GENDER=""
        self.CITY=""
        self.pincode=""
    def giveContactDetails(self):
        self.contactName = input("Enter person name: ")
        self.Adharno= int(input ("Enter Aharno:"))
        self.DOB=input ("Enter your Date of Birth:")
        self.GENDER=input("Enter your Gender:")
        self.emailid = input("Enter email id: ")
        self.address = input("Enter Address: ")
        self.CITY=input("Enter your city name:")
        self.pincode=int(input("Enter you pincode:"))
        return self.contactName,self.emailid, self.address,self.Adharno,self.DOB,self.GENDER,self.CITY,self.pincode 

contactList=[]
choice='yes'

while(choice.lower()=='yes'):
    print("1.Add New Contact \n2.Display Contacts\n3.Update Contacts\n4.Delete Contacts\n5.Select Display Columnwise")
    response = int(input("Enter your choice : "))

    if(response==1):
        contact = AddressBook()
        (name, emailid, address,Adharno,DOB,GENDER,CITY,pincode) = contact.giveContactDetails()
        with sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db") as con:
            cur = con.cursor()
            cur.execute("INSERT into Adhardetails (name, emailid, address,Adharno,DOB,GENDER,CITY,pincode) values (?,?,?,?,?,?,?,?)",(name, emailid, address,Adharno,DOB,GENDER,CITY,pincode))
            con.commit()
            msg = "Contact successfully Added"
            print(msg)
    
    elif(response==2):
        con = sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
        cur = con.cursor()
        cur.execute("select * from Adhardetails")   
        result = cur.fetchall()
        for i in result:
            print(i)
    elif (response==3):
        id=input("ENTER your id")
        contact = AddressBook()
        (name, emailid, address,Adharno,DOB,GENDER,CITY,pincode) = contact.giveContactDetails()        
        con=sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
        cur=con.cursor()
        cur.execute("update Adhardetails SET name=?,emailid=?,address=?,Adharno=?,DOB=?,GENDER=?,CITY=?,pincode=? where id=? ",(name, emailid, address,Adharno,DOB,GENDER,CITY,pincode,id))
        con.commit()
        print("updated sucessfully")
    elif (response==4):
        id=input("ENTER your id")
              
        con=sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
        cur=con.cursor()
        cur.execute("Delete from Adhardetails where id=? ",(id))
        con.commit()
        print("Deleted sucessfully")
    elif (response==5):
        print("1.name\n2.adharno\n3.emailid")
        i=int(input("Give your column option:"))
        if (i==1):
            con = sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
            cur = con.cursor()
            cur.execute("select id,name from Adhardetails")   
            result = cur.fetchall()
            for j in result:
                print(j)
        if (i==2):
            con = sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
            cur = con.cursor()
            cur.execute("select * from Adhardetails")   
            result = cur.fetchall()
            for j in result:
                print(j)
        if (i==3):
            con = sqlite3.connect("C:\\Users\\Asus\\Desktop\\Database\\Adharcard.db")
            cur = con.cursor()
            cur.execute("select id,emailid from Adhardetails")   
            result = cur.fetchall()
            for j in result:
                print(j)
    
    else:
        print("Please check your response")
    
    choice = input("Press 'yes' to continue ")
