from database import Database
class Customer:
    def __init__(self):
        self.db=Database()
        self.con=self.db.connect()
        self.cursor=self.con.cursor()
        
    def add_customer(self):
        name=input("Enter customer name:")
        mobile=input("Enter Mobile Number")
        
        sql= "Insert Into customers(customer_name,mobile) values (%s,%s)"
        value=(name,mobile)
        
        self.cursor.execute(sql,value)
        self.con.commit()
        
        print("Customer added successfully")
    def view_customers(self):

        sql="Select * from customers"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        
        print("\n-------Customer List-------")
        
        for row in data:
            print(row)
    def add_vehicle(self):
        
        customer_id=int(input("Enter Customer ID:"))
        vehicle_number=input("Enter Vehicle Number:")
        vehicle_name=input("Enter Vehicle Name:")
        
        sql='''
        Insert into vehicles(customer_id,vehicle_number,vehicle_name)
        values(%s,%s,%s)
        '''
        
        value=(customer_id,vehicle_number,vehicle_name)
        self.cursor.execute(sql,value)
        self.con.commit()
        print("Vehcile added successfully")
        
    def view_vehicles(self):
        sql="""
        Select vehicles.vehicle_id,
        customers.customer_name,
        vehicles.vehicle_number,
        vehicles.vehicle_name
        From vehicles
        Inner Join customers
        On customers.customer_id=vehicles.customer_id
        """
        
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        
        print("\n-----Vehicle List") 
        for row in data:
            print(row)
        
        
        
        
        
        
 
 
    