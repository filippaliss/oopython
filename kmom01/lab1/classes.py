"""
Module docstring: Defines classes for cat and duration representations.
"""

class Cat:
    """
    A cat with attributes such as eye color, name, and lives left.

    Attributes:
        nr_of_paws (int): A class with the number of paws a cat has (default 4).
        eye_color (str): The eye color of the cat.
        name (str): The name of the cat.
        _lives_left (int): The number of lives the cat has left.

    Methods:
        get_lives_left(): Get the current number of lives.
        set_lives_left(new_lives): Set the number of lives.
        description(): Get a description of the cat, including its attributes.
    """
    nr_of_paws = 4

    def __init__(self, eye_color, name, lives_left=-1):
        """
        Initializes a new Cat object.

        Args:
            eye_color (str): The eye color of the cat.
            name (str): The name of the cat.
            lives_left (int, optional): The number of lives the cat has left (default -1).
        """
        self.eye_color = eye_color
        self.name = name
        self._lives_left = lives_left

    def get_lives_left(self):
        """
        Get the current number of lives.

        Returns:
            int: The number of lives the cat has left.
        """
        return self._lives_left

    def set_lives_left(self, new_lives):
        """
        Set the number of lives.

        Args:
            new_lives (int): The new number of lives.
        """
        self._lives_left = new_lives

    def description(self):
        """
        Get a description of the cat including the information given to the cat.

        Returns:
            str: A descriptive string of the cat.
        """
        return (
            f"My cat's name is {self.name}, "
            f"has {self.eye_color} eyes and "
            f"{self._lives_left} lives left to live."
        )

class Duration:
    """
    Represents a duration with hours, minutes, and seconds.

    Attributes:
        hours (int): The number of hours.
        minutes (int): The number of minutes.
        seconds (int): The number of seconds.

    Methods:
        display(): Get a formatted string representation of the duration.
        duration_to_sec(duration_string): Convert a duration string to the total number of seconds.
    """
    def __init__(self, hours, minutes, seconds):
        """
        Initializes a new Duration object.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
            seconds (int): The number of seconds.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        """
        Get a formatted string representation of the duration.

        Returns:
            str: A formatted string in the format "hh-mm-ss".
        """
        formatted_hours = f"{self.hours:02d}"
        formatted_minutes = f"{self.minutes:02d}"
        formatted_seconds = f"{self.seconds:02d}"

        return f"{formatted_hours}-{formatted_minutes}-{formatted_seconds}"

    @staticmethod
    def duration_to_sec(duration_string):
        """
        Convert a duration string to the total number of seconds.

        Returns:
            int: The total number of seconds.
        """
        duration_list = duration_string.split('-')
        hours = int(duration_list[0])
        minutes = int(duration_list[1])
        seconds = int(duration_list[2])

        return hours * 3600 + minutes * 60 + seconds

    def __add__(self, other):
        return Duration.duration_to_sec(self.display()) + Duration.duration_to_sec(other.display())

    def __iadd__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60

        return self
