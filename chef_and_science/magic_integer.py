## magic_integer.py
import numpy as np

class MagicInteger:
    def __init__(self):
        self.numbers = np.array([], dtype=np.int64)

    def generate_magic_integer(self, l: int, v: int) -> None:
        """
        Generates a magic integer based on the provided length and value and updates self.numbers.
        
        Args:
            l (int): The length of the sequence to generate.
            v (int): The value to be concatenated to generate the sequence.
        """
        sequence = np.full((l,), v, dtype=np.int64)
        self.numbers = np.concatenate((self.numbers, sequence))

    def find_kth_digit(self, k: int) -> str:
        """
        Finds the kth digit in the concatenated magic integer sequence.
        
        Args:
            k (int): The position of the digit to find.
        
        Returns:
            str: The kth digit as a string, or 'So sad' if the position is out of bounds.
        """
        if k > self.numbers.size or k < 1:
            return 'So sad'
        else:
            # Convert the array to a single number string to ensure correct digit extraction
            concatenated_sequence = ''.join(map(str, self.numbers))
            return concatenated_sequence[k - 1]

    def process_requests(self, requests):
        """
        Processes a list of requests to generate magic integers and populate self.numbers.
        
        Args:
            requests (list of tuples): Each tuple contains two integers (l, v) representing the length and value for generating a magic integer.
        """
        for l, v in requests:
            self.generate_magic_integer(l, v)
