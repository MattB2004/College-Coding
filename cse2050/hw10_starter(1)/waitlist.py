import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, item, priority):
        #TODO add customers to the waiting list.

        # make customer an opject and add it to the list of entries
        customer = Entry(item, priority)
        self._entries.append(customer)


    def peek(self):
        #TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        # Return a tuple of the extracted item (customer, time). Return None if the heap is empty
        index = 0

        # base case if there are no customers in waitlist
        if len(self._entries) == 0:
            return None

        # Looks through every customer in waitlist to find and return the one with highest priority
        for i in range(len(self._entries)):
            customer = self._entries[i]
            priority_customer = self._entries[index]

            # splits the time into hours and minutes
            value = customer.time.split(':')
            priority_value = priority_customer.time.split(':')

            # Looks at the hour reservation
            if int(value[0]) < int(priority_value[0]):
                index = i

            # Looks at the minute reservation
            if int(value[0]) == int(priority_value[0]):
                if int(value[1]) < int(priority_value[1]):
                    index = i

            # if reservation time the same then peak alphabedically
            if int(value[0]) == int(priority_value[0]) and int(value[1]) == int(priority_value[1]):
                if customer.name < priority_customer.name:
                    index = i

        customer = self._entries[index]

        return (customer.name, customer.time)


    def seat_customer(self):
        #TODO The program should extract the customer with the highest priority 
        # (i.e., the earliest reservation time) from the priority queue.
        # Return a tuple of the extracted item (customer, time)
        index = 0

        # base case if there are no customers in waitlist
        if len(self._entries) == 0:
            return None

        # Looks through every customer in waitlist to find and return and remove the one with highest priority
        for i in range(len(self._entries)):
            customer = self._entries[i]
            priority_customer = self._entries[index]

            # splits the time into hours and minutes
            value = customer.time.split(':')
            priority_value = priority_customer.time.split(':')

            # Looks at the hour reservation
            if int(value[0]) < int(priority_value[0]):
                index = i

            # Looks at the minute reservation
            if int(value[0]) == int(priority_value[0]):
                if int(value[1]) < int(priority_value[1]):
                    index = i

            # if reservation time the same then seat alphabedically
            if int(value[0]) == int(priority_value[0]) and int(value[1]) == int(priority_value[1]):
                if customer.name < priority_customer.name:
                    index = i

        # index where the customer has highest priority
        customer = self._entries[index]

        self._entries.pop(index)

        return (customer.name, customer.time)


    def print_reservation_list(self):
        #TODO Prints all customers in order of their priority (reservation time).
        #Maintain the heap property

        # creats seperate list to not change entries directly
        reservation_list = self._entries
        
        # Sorts the customer where highest priority is first (bubble sort)
        for i in range(len(reservation_list)):
            for j in range(len(reservation_list)-i-1):
                customer = reservation_list[j]
                next_customer = reservation_list[j+1]

                # splits the time into hours and minutes
                value = customer.time.split(':')
                next_value = next_customer.time.split(':')

                # compares hour reservation
                if int(value[0]) > int(next_value[0]):
                    reservation_list[j], reservation_list[j + 1] = reservation_list[j + 1], reservation_list[j]

                # compares minute reservation
                if int(value[0]) == int(next_value[0]):
                    if int(value[1]) > int(next_value[1]):
                        reservation_list[j], reservation_list[j + 1] = reservation_list[j + 1], reservation_list[j]

        # returns sorted reservation list
        return reservation_list
    
    def change_reservation(self, name, new_priority):
        #TODO Change the reservation time (priority) for the customer with the given name

        # makes customer with new priority (reservation time)
        customer = Entry(name, new_priority)

        # for every customer in waitlist
        for i in range(len(self._entries)):

            change_customer = self._entries[i]

            # if customer name matches a customer name in waitlist already, then replace
            if name == change_customer.name:
                self._entries[i] = customer
                return (name, new_priority)

        # else return that no names match
        return 'Name not found'

    #Add other methods you may need



