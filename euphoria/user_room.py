from . import connection as cn

from . import room

class UserRoom(room.Room):
    """
    A user room contains a list of all the current users in the room.
    """

    def __init__(self, roomname, password=None, attempts=None):
        super().__init__(roomname, password, attempts)

        self.connection.add_callback("nick-event", self.handle_change)
        self.connection.add_callback("join-event", self.handle_join)
        self.connection.add_callback("part-event", self.handle_part)
        self.connection.add_callback("snapshot-event", self.handle_snapshot)

        self.people = []

    def handle_change(self, data):
        """
        handle_user(data) -> None

        Change a user's name.
        """

        info = data["data"]

        if info["from"] in self.people:
            self.people.remove(info["from"])

        self.people.append(info["to"])

    def handle_join(self, data):
        """
        handle_join(data) -> None

        Add a new user when they join.
        """

        self.people.append(data["data"]["name"])

    def handle_part(self, data):
        """
        handle_part(data) -> None

        Remove a user when they leave.
        """

        if data["data"]["name"] in self.people:
            self.people.remove(data["data"]["name"])

    def handle_snapshot(self, data):
        """
        handle_who(data) -> None

        Get a complete list of who is in the room.
        """

        self.people.clear()

        for user in data["data"]["listing"]:
            self.people.append(user["name"])
