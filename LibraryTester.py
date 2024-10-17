from Library import Library, Book, Album, Movie, Patron

class LibraryTester:
    """
    A class to test the Library system functionality.
    """

    def __init__(self):
        """
        Initializes the tester and sets up the library.
        """
        self.library = None
        self.patrons = []
        self.items = []

        self.setup()

    def setup(self):
        """
        Sets up the library, patrons, and items for testing.
        """
        # Initialize library
        self.library = Library()

        # Create library items
        self.b1 = Book("B1009653", "Brave New World", "Aldous Huxley")
        self.b2 = Book("B4275142", "The Great Gatsby", "F. Scott Fitzgerald")
        self.a1 = Album("A888751199729", "Up All Night", "One Direction")
        self.m1 = Movie("M024543617907", "Fight Club", "David Fincher")

        # Create patrons
        self.p1 = Patron("459786", "Harry Styles")
        self.p2 = Patron("126453", "Niall Horan")

        # Add items and patrons to the library
        self.library.add_library_item(self.b1)
        self.library.add_library_item(self.b2)
        self.library.add_library_item(self.a1)
        self.library.add_library_item(self.m1)
        self.library.add_patron(self.p1)
        self.library.add_patron(self.p2)

        # Store items and patrons for later use
        self.items = [self.b1, self.b2, self.a1, self.m1]
        self.patrons = [self.p1, self.p2]

    def test_check_out_library_item(self):
        """
        Test checking out a library item.
        """
        print("\nTesting Check Out Library Item:")
        print(self.library.check_out_library_item("126453", "A888751199729"))  # Should succeed
        print(self.library.check_out_library_item("126453", "B1009653"))  # Should succeed
        print(self.library.check_out_library_item("126453", "M024543617907"))  # Should fail (item already checked out)
        print(self.library.check_out_library_item("xyz", "A888751199729"))  # Should fail (patron not found)
        print(self.library.check_out_library_item("459786", "999"))  # Should fail (item not found)

    def test_return_library_item(self):
        """
        Test returning a library item.
        """
        print("\nTesting Return Library Item:")
        print(self.library.return_library_item("A888751199729"))  # Should succeed
        print(self.library.return_library_item("999"))  # Should fail (item not found)
        print(self.library.return_library_item("M024543617907"))  # Should fail (item already in library)

    def test_request_library_item(self):
        """
        Test requesting a library item.
        """
        print("\nTesting Request Library Item:")
        print(self.library.request_library_item("459786", "A888751199729"))  # Should succeed
        print(self.library.request_library_item("126453", "A888751199729"))  # Should fail (item already on hold)
        print(self.library.request_library_item("xyz", "A888751199729"))  # Should fail (patron not found)
        print(self.library.request_library_item("459786", "999"))  # Should fail (item not found)

    def test_pay_fine(self):
        # """
        # Test paying fines.
        # """
        # print("\nTesting Pay Fine:")
        # print(self.library.pay_fine("459786", 5))  # Should succeed (patron exists)
        # print(self.library.pay_fine("xyz", 5))  # Should fail (patron not found)

        """Test paying fines."""
        print("\nTesting Pay Fine:")
        # Check initial fine amount
        print(f"Initial fine amount: ${round(self.p2.get_fine_amount(), 2):.2f} for Patron {self.p2.get_patron_id()}")
        assert round(self.p2.get_fine_amount(), 2) == 0.00, "Initial fine amount should be $0.00"

        # Simulate overdue item for p1
        self.library.check_out_library_item("126453", "B1009653")
        for _ in range(25):  # Simulate 25 days of being overdue
            self.library.increment_current_date()

        # Check fine amount after overdue
        expected_fine = round(0.10 * (25 - 21), 2) # 4 days overdue at 10 cents per day
        print(f"Expected fine for Patron {self.p2.get_patron_id()} is ${expected_fine:.2f}")
        print(f"Fine amount: ${round(self.p2.get_fine_amount(), 2):.2f} for Patron {self.p2.get_patron_id()}")
        print(f"Patron ID: {self.p2.get_patron_id()}, Patron name: {self.p2.get_patron_name()}")
        assert round(self.p2.get_fine_amount(), 2) == expected_fine, f"Fine should be ${expected_fine:.2f}"

        # Test payment
        print(f"Attempting to pay $5.00 to cover ${round(self.p2.get_fine_amount(), 2):.2f} fine for Patron p2")
        print(self.library.pay_fine("126453", 5))  # Should succeed (patron exists)
        assert round(self.p2.get_fine_amount(), 2) == round(expected_fine - 5, 2), f"Fine amount should be ${expected_fine - 5:.2f}"
        result = self.library.pay_fine("126453", 5)
        print(f"pay_fine result: {result}")



    def test_overpayment(self):
        """Test handling of overpayments on fines."""
        # Simulate checkout and overdue days
        print("\nTesting Overpayment:")
        self.library.check_out_library_item("459786", "B1009653")
        for _ in range(25):  # Simulate 25 days of being overdue
            self.library.increment_current_date()

        # Calculate expected fine after overdue
        expected_fine = round(0.10 * (25 - 21), 2)  # Fine should be $0.40
        self.p1.amend_fine(expected_fine)  # Manually set the fine for the test

        # Print the initial fine amount
        print(f"Initial fine for Patron {self.p1.get_patron_id()}: ${self.p1.get_fine_amount():.2f}")

        # Test overpayment
        payment_amount = 10.00  # Simulating a payment of $10.00
        result = self.library.pay_fine("459786", payment_amount)
        print(result)  # This should print "payment successful"
        assert result == "payment successful", "Second payment should be successful"

        # After the payment, the fine should be zero
        final_fine = self.p1.get_fine_amount()

        # Assert final fine amounts, expecting it to be zero after overpayment
        assert final_fine == 0, f"Fine amount should be reset to $0, but got ${final_fine:.2f}"

    def test_increment_current_date(self):
        """
        Test incrementing the current date.
        """
        print("\nTesting Increment Current Date:")
        for _ in range(5):
            self.library.increment_current_date()
        print(f"Current date after increment: {self.library._current_date}")

    def run_tests(self):
        """
        Run each of the tests above.
        """
        self.test_check_out_library_item()
        self.test_return_library_item()
        self.test_request_library_item()
        self.test_pay_fine()
        self.test_overpayment()
        self.test_increment_current_date()


def main():
    """
    Main function to run the library tests.
    """
    tester = LibraryTester()
    tester.run_tests()


if __name__ == "__main__":
    main()
