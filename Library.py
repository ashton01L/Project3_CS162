# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/16/2024
# Description: You will be writing a Library simulator involving multiple classes.
class LibraryItem:
    """
    A LibraryItem object represents a library item that a patron can check out from a library. It has six data members.

    Attributes:
        _library_item_id (str): a unique identifier for a LibraryItem
        _title (str): the title of the LibraryItem
        _location (str): the state of the LibraryItem - "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        _checked_out_by (Patron): refers to the name of the Patron who has LibraryItem "CHECKED_OUT", if any.
        _requested_by (Patron): refers to the name of the Patron who has requested LibraryItem "ON_HOLD_SHELF", if any.
        _date_checked_out (int): date the LibraryItem was "CHECKED_OUT", set to current_date of the Library
    """

    def __init__(self, library_item_id, title):
        """
        Initializes LibraryItem object with the provided library_item_id and title. Additionally, initializes
        checked_out_by and requested_by to None, location to "ON_SHELF"

        :param:
            library_item_id (str):
            title (str):
        """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"  # Initial location
        self._checked_out_by = None  # No patron checked it out initially
        self._requested_by = None  # No patron has requested it initially
        self._date_checked_out = None  # Not checked out

    def get_library_item_id(self):
        """
        Gets the uniques identifier of the LibraryItem

        :return:
            str: The unique identifier (id) of the LibraryItem
        """
        return self._library_item_id

    def get_title(self):
        """
        Gets the title of the LibraryItem

        :return:
            str: The title of the LibraryItem
        """
        return self._title

    def get_location(self):
        """
        Gets the location of the LibraryItem

        :return:
            str: The location of the LibraryItem
        """
        return self._location

    def set_checked_out_by(self, patron):
        """
        Sets the name of the Patron who has checked_out the LibraryItem

        :param:

        :return:
            Patron: The name of the Patron who has checked_out the LibraryItem
        """
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        """
        Sets the name of the Patron who has requested the LibraryItem

        :return:
            Patron: The name of the Patron who has requested the LibraryItem
        """
        self._requested_by = patron

    def set_location(self, location):
        """
        Sets the location of the LibraryItem

        :param:
            location (str): The new location of the item, "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT".
        """
        self._location = location

    def set_date_checked_out(self, date):
        """
        Sets the date_checked_out of the LibraryItem

        :param:
            date (int): The date to set as date LibraryItem was checked_out
        :return:
            int:  The date to set as checked_out date for LibraryItem
        """
        self._date_checked_out = date

    def get_checked_out_by(self):
        """
        Gets the name of the Patron who has checked_out the LibraryItem

        :return:
            Patron: The name of the Patron who has checked_out the LibraryItem
        """
        return self._checked_out_by

    def get_requested_by(self):
        """
        Gets the name of the Patron who has requested the LibraryItem

        :return:
            Patron: The name of the Patron who has requested the LibraryItem
        """
        return self._requested_by

    def get_date_checked_out(self):
        """
        Gets the date_checked_out of the LibraryItem

        :return:
            int: The date the LibraryItem was checked_out
        """
        return self._date_checked_out


class Book(LibraryItem):
    """
    A Book object that represents an object that can be checked out by a Patron, inheriting from libraryItem. It has a
    single data member.

    Attributes:
        _author (str): The author of the book.
    """

    def __init__(self, library_item_id, title, author):
        """
        Initializes a new Book object with a library_item_id, title, and the new attribute, author.

        :param:
            library_item_id (str): The unique identifier for the book.
            title (str): The title of the book.
            author (str): The author of the book.
        """
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """
        Gets the name of the author of the book

        :return:
            str: The name of the author of the book.
        """
        return self._author

    def get_check_out_length(self):
        """
        Gets the length, in number of days, that a book can be checked_out (21 days)

        :return:
            int: The number of days allowable for a Book object to be checked_out (21 days)
        """
        return 21


class Album(LibraryItem):
    """
    An Album object that represents an object that can be checked out by a Patron, inheriting from LibraryItem. It has a
    single data member.

    Attributes:
        _artist (str): The main artist of the album.
    """

    def __init__(self, library_item_id, title, artist):
        """
        Initializes a new Album with a library_item_id, title, and artist.

        :param:
            library_item_id (str): The unique identifier for the album.
            title (str): The title of the album.
            artist (str): The artist of the album.
        """
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """
        Gets the name of the artist of the Album

        :return:
            str: The name of the artist to whom the album is attributed.
        """
        return self._artist

    def get_check_out_length(self):
        """Gets the length, in number of days, that an album can be checked_out (14 days)

        :return:
            int: The number of days allowable for an Album object to be checked_out (14 days)
        """
        return 14


class Movie(LibraryItem):
    """
    A Movie object that represents an object that can be checked out by a Patron, inheriting from LibraryItem. It has a
    single data member.


    Attributes:
        _director (str): The name of the director of the movie.
    """

    def __init__(self, library_item_id, title, director):
        """
        Initializes a new Movie with a library_item_id, title, and director.

        :param:
            library_item_id (str): The unique identifier for the movie.
            title (str): The name of the title of the movie.
            director (str): The name of the director of the movie.
        """
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """
        Gets the name of the director of the Movie

        :return:
            str: The name of the director to whom the movie is attributed.
        """
        return self._director

    def get_check_out_length(self):
        """
        Gets the length, in number of days, that a movie can be checked_out (7 days)

        :return:
            int: The number of days allowable for a Movie object to be checked_out (7 days)
        """
        return 7


class Patron:
    """
    A Patron object represents a patron of a library. It has four data members.

    Attributes:
        _patron_id (str): a unique identifier for a LibraryItem
        _name (str): the name of the Patron
        _checked_out_items (list): a list of LibraryItem's the patron currently has checked_out
        _fine_amount (float): refers to the amount the patron owes in fines
    """

    def __init__(self, patron_id, name):
        """
        Initializes a new Patron with an ID and name.

        :param:
            patron_id (str): The unique identifier for the patron.
            name (str): The name of the patron.
        """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []  # List of currently checked out LibraryItems
        self._fine_amount = 0.0  # Initial fine amount

    def get_patron_id(self):
        """
        Gets the patron_id, the unique identifier for each patron

        :return:
            str: The patron_id, the unique identifier for each patron
        """
        return self._patron_id

    def get_patron_name(self):
        """
        Gets the name of the patron, patron_name.

        :return:
            str: The patron_name.
        """
        return self._name

    def get_fine_amount(self):
        """
        Gets the amount of the current fine

        :return:
            float: The amount of fines the patron currently owes.
            """
        if self._fine_amount < 0:
            self._fine_amount = 0.0

        return round(self._fine_amount, 2)

    def add_library_item(self, library_item):
        """
        Adds a LibraryItem to the list of items checked_out to Patron
        """
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """
        Removes a LibraryItem from the list of items checked_out to Patron
        """
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        """
        Amends the amount of the fine by the specified additional amount
        """
        self._fine_amount += amount

        if self._fine_amount < 0:
            self._fine_amount = 0.0


class Library:
    """
    A Library object represents a library that holds LibraryItems and serves each Patron. It has three additional data
    members.

    Attributes:
        _holdings (dict): A list of library items in the library.
        _members (dict): A list of patrons who are members of the library.
        _current_date (int): The current date, tracked as an integer.
    """

    def __init__(self):
        """
        Initializes a new Library with empty holdings and members, and sets the current date to 0.
        """
        self._holdings = []  # List of LibraryItems in the Library
        self._members = []  # List of Patrons who are members of the Library
        self._current_date = 0  # Days since the Library object was created

    def add_library_item(self, library_item):
        """
        Adds a LibraryItem to the Library's list of holdings.
        """
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """
        Adds a Patron to the Library's list of members.
        """
        self._members.append(patron)


    def lookup_library_item_from_id(self, library_item_id):
        """
        Searches for a library item by its library_item_id and returns it, or None if not found.

        :return:
            str: the library_item_id, a unique identifier for each individual item
            OR
            None, if no library_item_id is found
        """
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """
        Searches for a patron by their patron_id and returns them, or None if not found.

        :return:
            str: the patron_id, a unique identifier for each individual patron
            OR
            None, if no patron_id is found
        """
        for member in self._members:
            if member._patron_id == patron_id:
                return member
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        Checks out a LibraryItem to a patron, if library_item_id is available, ON_SHELF.

        :param:
            patron_id (str): The patron_id of the patron checking out the LibraryItem.
            library_item_id (str): The library_item_id of the item being checked out by the patron.

        :return:
            str: The result of the checkout attempt.
        """
        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)

        if patron is None:
            return "patron not found"
        if library_item is None:
            return "item not found"
        if library_item.get_checked_out_by() is not None:
            return "item already checked out"
        if library_item.get_requested_by() is not None and library_item.get_requested_by() != patron:
            return "item on hold by other patron"

        # Update the library item and patron
        library_item.set_checked_out_by(patron)
        library_item.set_date_checked_out(self._current_date)
        library_item.set_location("CHECKED_OUT")
        patron.add_library_item(library_item)

        # If the item was on hold by this patron, update requested_by
        if library_item.get_requested_by() == patron:
            library_item.set_requested_by(None)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """
        Returns a LibraryItem to the Library.

        :param:
            library_item_id (str): The library_item_id of the item to be returned.

        :return:
            str: A string message return of the result of the item return attempt.
        """
        library_item = self.lookup_library_item_from_id(library_item_id)

        if library_item is None:
            return "item not found"
        if library_item.get_checked_out_by() is None:
            return "item already in library"

        # Update the patron's checked out items
        patron = library_item.get_checked_out_by()
        patron.remove_library_item(library_item)

        # Check if the item is on hold
        if library_item.get_requested_by() is not None:
            library_item.set_location("ON_HOLD_SHELF")
        else:
            library_item.set_location("ON_SHELF")

        # Update the checked_out_by
        library_item.set_checked_out_by(None)
        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        Requests a LibraryItem to be held for a patron, if available, and places LibraryItem to ON_HOLD_SHELF.

        :param:
            patron_id (str): The unique identifier, patron_id, of the patron requesting the item be placed on hold.
            library_item_id (str): The unique identifier, library_item_id, of the item that the patron is requesting to
            be placed on hold.

        :return:
            str: A message indicating the result of the request for the item to be placed on hold.
        """
        patron = self.lookup_patron_from_id(patron_id)
        library_item = self.lookup_library_item_from_id(library_item_id)

        if patron is None:
            return "patron not found"
        if library_item is None:
            return "item not found"
        if library_item.get_requested_by() is not None:
            return "item already on hold"

        # Update the library item
        library_item.set_requested_by(patron)
        if library_item.get_location() == "ON_SHELF":
            library_item.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self, patron_id, amount):
        """
        Processes a fine payment for a Patron.

        The amount specified will reduce the patron's outstanding fines. If the amount exceeds the current fine,
        the fine amount will be reduced to zero (no refunds are given for overpayment).

        :param:
            patron_id (str): The unique identifier for the Patron paying the fine.
            amount (float): The amount of money the Patron is paying toward their fine.

        :return:
            str: A message indicating the result of the fine payment
        """
        patron = self.lookup_patron_from_id(patron_id)
        print(f"Lookup for patron '{patron_id}' resulted in: {patron}")

        if patron is None:
            return "patron not found"

        # Amend the fine
        print(f"Amending fine for patron '{patron_id}' by ${amount:.2f}")
        patron.amend_fine(-amount)
        print(f"New fine amount: ${patron.get_fine_amount():.2f}")
        return "payment successful"

    def increment_current_date(self):
        """
        Advances the current date for the library.

        Upon each incremented date, the function checks all LibraryItems that are checked out. If an item has been
        checked out beyond its allowed check-out length, the patron's fine is increased by $0.10 per day overdue.
        """
        self._current_date += 1
        for patron in self._members:
            for item in patron._checked_out_items:
                if item.get_location() == "CHECKED_OUT":
                    if (self._current_date - item._date_checked_out) > item.get_check_out_length():
                        fine_days = self._current_date - item._date_checked_out - item.get_check_out_length()
                        if fine_days > 0:
                            patron.amend_fine(0.10)
