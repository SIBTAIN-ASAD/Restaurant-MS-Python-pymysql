import pymysql 
#=========================================================================
# DATABASE HANDLER CLASS
#=========================================================================
class DbRunner:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password = password
        self.database = database
        try:
            connection = pymysql.connect(host=self.host, user= self.user, password = self.password, database=self.database)
            self.connected = connection
            dbCursor = self.connected.cursor()
            self.dcursor = dbCursor
        except:
            print("Error! Database not connected")

    def signupAdmin(self,admin):
        query = "insert into admin(admin_email, admin_pwd,admin_name) values(%s, %s, %s)"
        arg = (admin.email, admin.pwd,admin.name)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True
  
    def signupCustomer(self,customer):
        query = "insert into customer(cus_email, cus_pwd, cus_name) values(%s, %s, %s)"
        arg = (customer.email, customer.pwd,customer.name)
        self.dcursor.execute(query, arg)
        self.connected.commit()
        return True

    def checkCustomerAlreadyExist(self, customer):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from customer")
        emailList=dbCursor.fetchall()
        for e in emailList:
            if e[3]==customer.email:
                return True
            
        return False


    def checkAlreadyExist(self,admin):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from admin")
        emailList=dbCursor.fetchall()
        for e in emailList:
            if e[3]==admin.email:
                return True
            
        return False

    def signInAdmin(self,admin):
        dbCursor = self.dcursor
        if self.isValid(admin) == False:
            print("Invalid Email or password")
            return []
        else:
            dbCursor.execute("Select * from admin where admin_email = %s", admin.email)
            ls = dbCursor.fetchall()
            return ls

    def signInCustomer(self,customer):
        dbCursor = self.dcursor
        if self.isValid2(customer) == False:
            print("Invalid Email or password")
            return []
        else:
            dbCursor.execute("Select * from customer where cus_email = %s", customer.email)
            ls = dbCursor.fetchall()
            return ls


    def isValid2(self, cust):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from customer")
        emailList=dbCursor.fetchall()
        for e in emailList:
            if e[3]==cust.email and e[2] == cust.pwd:
                return True
            
        return False


    def isValid(self, admin):
        dbCursor = self.dcursor
        dbCursor.execute("Select * from admin")
        emailList=dbCursor.fetchall()
        for e in emailList:
            if e[3]==admin.email and e[2] == admin.pwd:
                return True
            
        return False

    def addDish(self, dish):
        arg = (dish.ingredients[0],dish.ingredients[1],dish.ingredients[2])
        self.dcursor.execute("insert into ingredients(first, second, third) values(%s, %s, %s)", arg)
        self.connected.commit()
        self.dcursor.execute("Select i_id from ingredients where first = %s and second = %s and third = %s", arg)
        id = self.dcursor.fetchall()
        arg = (dish.name, id[0], dish.price, dish.category)
        self.dcursor.execute("insert into dish(d_name, d_ingredients, d_price, d_category) values(%s, %s, %s, %s)", arg)
        self.connected.commit()

        return True

    def getDishList(self):
        self.dcursor.execute("Select d.d_name, d.d_price, d.d_category, i.first, i.second, i.third, d.d_id, i.i_id  from dish d inner join ingredients i on  d.d_id = i.i_id ")
        ls = self.dcursor.fetchall()
        return ls

    def storeOrder(self, myorder, dine, payment):
        arg = (myorder[0].cus_email, dine, payment)
        self.dcursor.execute("insert into orders(email, type, payment) values(%s, %s, %s)", arg)
        self.connected.commit()

        arg = (myorder[0].cus_email)
        self.dcursor.execute("Select id from orders where email = %s", arg)
        ls = self.dcursor.fetchall()

        for order in myorder:
            arg = (order.cus_email, order.dish, order.price, order.quantity, ls[-1])
            self.dcursor.execute("insert into data(cus_email, dish, price, quantity, data_id) values(%s, %s, %s, %s, %s)", arg)

        self.connected.commit()
        return True

    def getOrderLists(self, email):
        self.dcursor.execute("Select * from orders where email = %s", email)
        ls = self.dcursor.fetchall()
        return ls

    def getOrderData(self, id):
        self.dcursor.execute("Select * from data where data_id = %s",id)
        ls = self.dcursor.fetchall()
        return ls

    def __del__(self):
        if self.dcursor != None:
            self.dcursor.close()
        if self.connected!=None:
            self.connected.close()
