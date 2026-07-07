from database import Database
from datetime import date
class Billing:
    def __init__(self):
        self.db=Database()
        self.con=self.db.connect()
        self.cursor=self.con.cursor()
        
    def generate_bill(self):
        vehicle_id=int(input("Enter Vehicle ID:"))
        
        print("\n------ Services------")
        print("1.Car Wash         Rs 500")
        print("2.Oil change       Rs 200 ")
        print("3.Brake Service    Rs 5500")
        print("4.Wheel Alignment  Rs 5400")
        print("5.Full Service     Rs 10000")
        
        choice=int(input("\nSelect Service:"))
        if choice==1:
            service="Car Wash"
            amount=500
        elif choice==2:
           service=" Oil change"
           amount=200
        elif choice==3:
            service="Brake Service"
            amount=5500
        elif choice==4:
            service="Wheel Alignment"
            amount=5400
        elif choice==5:
            service="Full Service"
            amount=10000
        else:
            print("Invalid Choice")
        
        sql="""
        Insert into bills(vehicle_id,service,amount,bill_date)
        values(%s,%s,%s,%s)
        """
        value=(vehicle_id,service,amount,date.today())
        self.cursor.execute(sql,value)
        
        self.con.commit()
        
        print("======Bill=====")
        print("Service:",service)
        print("Amount:",amount)
        print("Date:",date.today())
        print("========")
        print("Bill generated successfully")
        
        
    def view_bills(self):
      

        sql = '''
        SELECT
        bills.bill_id,
        customers.customer_name,
        vehicles.vehicle_number,
        bills.service,
        bills.amount,
        bills.bill_date
        FROM bills
        INNER JOIN vehicles
        ON bills.vehicle_id = vehicles.vehicle_id
        INNER JOIN customers
        ON vehicles.customer_id = customers.customer_id;
        '''
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        
        print("\n------Bills-----")
        
        for row in data:
            print(row)
    