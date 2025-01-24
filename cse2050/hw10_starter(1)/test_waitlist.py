from waitlist import Waitlist, Entry, Time
import unittest

class Test_Waitlist(unittest.TestCase):
    def test_add_customer(self):
        w1 = Waitlist()

        # makes sure list is 0
        self.assertEqual(len(w1._entries), 0)

        # adds customer
        w1.add_customer('Phil', '9:30')

        # list increases
        self.assertEqual(len(w1._entries), 1)
        
        # repeat
        w1.add_customer('Chad', '11:00')
        self.assertEqual(len(w1._entries), 2)

    def test_peek(self):
        w1 = Waitlist()
        
        # peek equals none when no cusomters in waitlist
        self.assertEqual(w1.peek(), None)

        # Adds 2 different customers
        self.assertEqual(len(w1._entries), 0)
        w1.add_customer('Phil', '9:30')
        self.assertEqual(len(w1._entries), 1)
        w1.add_customer('Chad', '11:45')
        self.assertEqual(len(w1._entries), 2)

        # returns highest priority
        self.assertEqual(w1.peek(), ('Phil', '9:30'))

        # adds another customer
        w1.add_customer('Becca', '9:15')
        # returns highest priority
        self.assertEqual(w1.peek(), ('Becca', '9:15'))

        # adds another customer
        w1.add_customer('Ryan', '4:55')
        # returns highest priority
        self.assertEqual(w1.peek(), ('Ryan', '4:55'))

    def test_seat_customer(self):
        w1 = Waitlist()

        # seat_customer equals none when no cusomters in waitlist
        self.assertEqual(w1.seat_customer(), None)

        # adds 2 customers to waitlist
        w1.add_customer('Phil', '9:30')
        w1.add_customer('Chad', '11:45')
        self.assertEqual(len(w1._entries), 2)

        # seat 1st customer
        self.assertEqual(w1.seat_customer(), ('Phil', '9:30'))
        self.assertEqual(len(w1._entries), 1)

        # seat 2nd customer
        self.assertEqual(w1.seat_customer(), ('Chad', '11:45'))
        self.assertEqual(len(w1._entries), 0)

    def test_print_reservation_list(self):
        w1 = Waitlist()

        # adds 4 customers to waitlist
        w1.add_customer('Phil', '9:30')
        w1.add_customer('Chad', '11:45')
        w1.add_customer('Becca', '9:15')
        w1.add_customer('Ryan', '4:55')

        reservation_list = w1.print_reservation_list()

        # prints customers from sorted reservation list
        for i in range(len(reservation_list)):
            customer = reservation_list[i]
            reservation_list[i] = (customer.name, customer.time)

        # sorted reservation list
        self.assertEqual(reservation_list, [('Ryan', '4:55'),('Becca', '9:15'),('Phil', '9:30'),('Chad', '11:45')])

        
    def test_change_reservation(self):
        w1 = Waitlist()

        # adds 2 customers to waitlist
        w1.add_customer('Phil', '9:30')
        w1.add_customer('Becca', '11:45')

        
        
        # Chad not in waitlist
        self.assertEqual(w1.change_reservation('Chad','9:15'), 'Name not found')

        # changes reservations for both customers
        self.assertEqual(w1.change_reservation('Phil','10:00'), ('Phil','10:00'))
        self.assertEqual(w1.change_reservation('Becca', '11:15'), ('Becca', '11:15'))
        


unittest.main()