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
        b1 = Book("B1009653", "Brave New World", "Aldous Huxley")
        b2 = Book("B4275142", "The Great Gatsby", "F. Scott Fitzgerald")
        a1 = Album("A888751199729", "Up All Night", "One Direction")
        m1 = Movie("M024543617907", "Fight Club", "David Fincher")

        # Create patrons
        p1 = Patron("459786", "Harry Styles")
        p2 = Patron("126453", "Niall Horan")

        # Add items and patrons to the library
        self.library.add_library_item(b1)
        self.library.add_library_item(b2)
        self.library.add_library_item(a1)
        self.library.add_library_item(m1)
        self.library.add_patron(p1)
        self.library.add_patron(p2)

        # Store items and patrons for later use
        self.items = [b1, b2, a1, m1]
        self.patrons = [p1, p2]

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
        """
        Test paying fines.
        """
        print("\nTesting Pay Fine:")
        print(self.library.pay_fine("459786", 5))  # Should succeed (patron exists)
        print(self.library.pay_fine("xyz", 5))  # Should fail (patron not found)

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
        self.test_increment_current_date()


def main():
    """
    Main function to run the library tests.
    """
    tester = LibraryTester()
    tester.run_tests()


if __name__ == "__main__":
    main()
