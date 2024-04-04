## ui.py
import sys

class UI:
    def get_input(self) -> tuple:
        """
        Prompts the user for input and returns a tuple containing a list of numbers and a list of requests.
        Each request is a tuple of three integers (l, v, k).

        Returns:
            tuple: A tuple containing two elements:
                - A list of integers representing the numbers.
                - A list of tuples, each representing a request with three integers (l, v, k).
        """
        while True:
            try:
                numbers_input = input("Enter numbers separated by space or type 'exit' to quit: ").strip()
                if numbers_input.lower() == 'exit':
                    sys.exit(1)
                numbers = list(map(int, numbers_input.split()))
                num_requests_input = input("Enter number of requests or type 'exit' to quit: ").strip()
                if num_requests_input.lower() == 'exit':
                    sys.exit(1)
                num_requests = int(num_requests_input)
                requests = []
                for _ in range(num_requests):
                    request_input = input("Enter l, v, k for request separated by space or type 'exit' to quit: ").strip()
                    if request_input.lower() == 'exit':
                        sys.exit(1)
                    l, v, k = map(int, request_input.split())
                    requests.append((l, v, k))
                return numbers, requests
            except ValueError as e:
                self.display_error(f"Invalid input: {e}. Please try again.")

    def display_result(self, result: str) -> None:
        """
        Displays the result to the user.

        Args:
            result (str): The result to be displayed.
        """
        print(f"Result: {result}")

    def display_error(self, message: str) -> None:
        """
        Displays an error message to the user.

        Args:
            message (str): The error message to be displayed.
        """
        print(f"Error: {message}")
