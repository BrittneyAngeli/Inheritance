
class Person:

    def __init__(self, name, address, tele_num):
        self.__name = name 
        self.__address = address
        self.__tele_num = tele_num

    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Number:", self.__tele_num)        

    
class Customer(Person):
    def __init__(self, name, address, tele_num, cust_num, mail_list):
        Person.__init__(self, name, address, tele_num)

        self.__cust_num = cust_num
        self.__mail_list = mail_list

    def print_person(self):
        Person.print_person(self)
        print("Customer name:", self.__cust_num)
        print("Mailing list:", self.__mail_list)