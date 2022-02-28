import PersonClass as person

def main():

    per = person.Person('Brittney Solorio', '2415 S University Parks Dr', '254-470-0834')
    per.print_person()

    cust = person.Customer('Brittney Solorio', '2415 S University Parks Dr', '254-470-0834', 1, True)
    cust.print_person()

main()