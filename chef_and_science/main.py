## main.py
import numpy as np
from typing import List, Tuple

class MagicInteger:
    def __init__(self, numbers: List[int]):
        self.numbers = numbers
        self.requests = []
        self.last_magic_integer = ""  # Initialize last_magic_integer
        self.filtered_numbers = {}  # Dictionary to hold filtered numbers by value

    def generate_magic_integer(self, l: int, v: int) -> str:
        """
        Generates a magic integer based on the provided length and value.
        Efficiently filters and concatenates numbers using preprocessed data.
        
        Args:
            l (int): The length of the magic integer.
            v (int): The value to filter the numbers.

        Returns:
            str: The magic integer or "So sad" if it cannot be generated.
        """
        if v not in self.filtered_numbers:
            self.filtered_numbers[v] = [n for n in self.numbers if n % v == 0]
        filtered_arr = self.filtered_numbers[v]
        if len(filtered_arr) < l:
            return "So sad"
        else:
            magic_integer = ''.join(map(str, filtered_arr[:l]))
            self.last_magic_integer = magic_integer
            return magic_integer

    def find_kth_digit(self, k: int) -> str:
        """
        Finds the kth digit of the last generated magic integer.
        
        Args:
            k (int): The position of the digit to find.

        Returns:
            str: The kth digit or "So sad" if it cannot be found.
        """
        if k <= len(self.last_magic_integer):
            return self.last_magic_integer[k-1]
        else:
            return "So sad"

class UI:
    @staticmethod
    def get_input() -> Tuple[List[int], List[Tuple[int, int, int]]]:
        """
        Gets input from the user, including numbers and requests.
        
        Returns:
            Tuple[List[int], List[Tuple[int, int, int]]]: The numbers and requests.
        """
        numbers = list(map(int, input("Enter numbers separated by space: ").strip().split()))
        n_requests = int(input("Enter number of requests: "))
        requests = []
        for _ in range(n_requests):
            l, v, k = map(int, input("Enter l, v, k separated by space for request: ").strip().split())
            requests.append((l, v, k))
        return numbers, requests

    @staticmethod
    def display_result(result: str) -> None:
        """
        Displays the result to the user.
        
        Args:
            result (str): The result to display.
        """
        print(f"Result: {result}")

    @staticmethod
    def display_error(message: str) -> None:
        """
        Displays an error message to the user.
        
        Args:
            message (str): The error message.
        """
        print(f"Error: {message}")

class Main:
    @staticmethod
    def main() -> None:
        """
        The main method to run the application.
        """
        ui = UI()
        numbers, requests = ui.get_input()
        magic_integer = MagicInteger(numbers)

        for request in requests:
            l, v, k = request
            magic_integer_str = magic_integer.generate_magic_integer(l, v)
            if magic_integer_str != "So sad":
                kth_digit = magic_integer.find_kth_digit(k)
                if kth_digit != "So sad":
                    ui.display_result(kth_digit)
                else:
                    ui.display_error("So sad")
            else:
                ui.display_error("So sad")

if __name__ == "__main__":
    Main.main()
