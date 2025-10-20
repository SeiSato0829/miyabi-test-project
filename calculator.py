#!/usr/bin/env python3
"""
Simple Calculator Application
Supports basic arithmetic operations: addition, subtraction, multiplication, division
"""

import sys
from typing import Union


class Calculator:
    """A simple calculator class that performs basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        Divide a by b.

        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def calculate(self, operation: str, a: float, b: float) -> float:
        """
        Perform calculation based on operation.

        Args:
            operation: One of '+', '-', '*', '/'
            a: First number
            b: Second number

        Returns:
            Result of the calculation

        Raises:
            ValueError: If operation is not supported
            ZeroDivisionError: If division by zero is attempted
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}. Use one of: +, -, *, /")

        return operations[operation](a, b)


def main():
    """Main function to run the calculator from command line."""
    calculator = Calculator()

    print("=" * 50)
    print("Simple Calculator")
    print("=" * 50)
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")
    print("Type 'quit' or 'exit' to stop")
    print("=" * 50)

    while True:
        try:
            # Get user input
            user_input = input("\nEnter calculation (e.g., 5 + 3): ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thank you for using the calculator. Goodbye!")
                break

            # Parse input
            parts = user_input.split()

            if len(parts) != 3:
                print("Error: Please enter in format: number operation number")
                print("Example: 5 + 3")
                continue

            # Extract operands and operator
            try:
                num1 = float(parts[0])
                operation = parts[1]
                num2 = float(parts[2])
            except ValueError:
                print("Error: Invalid number format. Please use numbers only.")
                continue

            # Perform calculation
            result = calculator.calculate(operation, num1, num2)

            # Display result
            print(f"Result: {num1} {operation} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
