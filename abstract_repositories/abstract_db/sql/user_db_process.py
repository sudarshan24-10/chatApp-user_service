from abc import ABC, abstractmethod

class AbstractUserDB(ABC):
    
    @abstractmethod
    def find_by_email(self, email: str):
        """
        Find and return a user by email.
        :param email: The email address to search for.
        :return: A user object if found, otherwise None.
        """
        pass

    @abstractmethod
    def find_by_id(self, user_id: int):
        """
        Find and return a user by their unique identifier.
        :param user_id: The unique identifier of the user.
        :return: A user object if found, otherwise None.
        """
        pass

    @abstractmethod
    def create(self, user_data: dict):
        """
        Save a new user to the database.
        :param user: The user object to save.
        :return: The saved user object (possibly with an assigned ID).
        """
        pass

    @abstractmethod
    def update(self, user):
        """
        Update an existing user's information in the database.
        :param user: The user object with updated data.
        :return: The updated user object.
        """
        pass

    @abstractmethod
    def delete(self, user):
        """
        Delete a user from the database.
        :param user: The user object to delete.
        :return: True if deletion was successful, otherwise False.
        """
        pass
