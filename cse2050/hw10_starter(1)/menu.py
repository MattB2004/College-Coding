from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                print()
                name = input('Enter customers Name: ')
                time = input('Enter time reservastion: ')
                print()
                self.waitlist.add_customer(name, time)
                print(name,'with reservation of',time,'has been added to waitlist')
                print()

            elif choice == "2":
                #TODO"""Seat the next customer"""
                if len(self.waitlist._entries) == 0:
                    print()
                    print('No customers in waitlist')
                    print()

                else:
                    customer = list(self.waitlist.seat_customer())
                    print()
                    print('Now seating', customer[0], 'with reservation', customer[1])
                    print()

            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                print()
                name = input('Enter customers Name: ')
                time = input('Enter new reservation: ')
                if self.waitlist.change_reservation(name, time) == 'Name not found':
                    print()
                    print('Customer not found in waitlist')
                else:
                    print()
                    self.waitlist.change_reservation(name, time)
                    print(name, 'reservation successfully changed to', time)
                    print()


            elif choice == "4":
                #TODO"""Peek at the next customer"""
                if self.waitlist.peek() == None:
                    print()
                    print('No customers in waitlist')
                    print()
                else:
                    customer = list(self.waitlist.peek())
                    print()
                    print('next customer on the waitlist is', customer[0],'with reservation time', customer[1])
                    print()
                

            elif choice == "5":
                #TODO"""Print the waitlist"""
                print()
                print('Customers on the waitlist: ')
                print()
                reservation_list = self.waitlist.print_reservation_list()
                print('Name      Reservation')
                for i in range(len(reservation_list)):
                    customer = reservation_list[i]
                    print(f'{customer.name}      {customer.time}')

                print()
                
            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

