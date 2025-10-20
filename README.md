# Miyabi Test Project

## 📝 Overview
This project demonstrates Miyabi's autonomous development capabilities with a simple calculator application.

## 🧮 Calculator Application

A command-line calculator application that supports basic arithmetic operations.

### Features
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- ✅ Error handling (division by zero, invalid inputs)
- 🧪 Comprehensive test suite

### Installation

No installation required! Just Python 3.6+.

### Usage

#### Running the Calculator

```bash
python calculator.py
```

#### Interactive Mode

```
Enter calculation (e.g., 5 + 3): 10 + 5
Result: 10.0 + 5.0 = 15.0

Enter calculation (e.g., 5 + 3): 20 / 4
Result: 20.0 / 4.0 = 5.0

Enter calculation (e.g., 5 + 3): quit
```

#### Supported Operations

- `+` : Addition (e.g., `5 + 3`)
- `-` : Subtraction (e.g., `10 - 3`)
- `*` : Multiplication (e.g., `4 * 5`)
- `/` : Division (e.g., `20 / 4`)

### Running Tests

Run all tests with verbose output:

```bash
python test_calculator.py
```

Or using pytest (if installed):

```bash
pytest test_calculator.py -v
```

Or using Python's unittest:

```bash
python -m unittest test_calculator.py -v
```

### Test Coverage

The test suite includes:
- ✅ 25+ test cases
- ✅ Positive and negative numbers
- ✅ Floating point arithmetic
- ✅ Zero handling
- ✅ Edge cases (very large/small numbers)
- ✅ Error conditions (division by zero, invalid operations)
- ✅ Precision testing

### Examples

```python
# Using the Calculator class programmatically
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 3)  # 7
result = calc.multiply(4, 5)   # 20
result = calc.divide(20, 4)    # 5.0

# Using the calculate method
result = calc.calculate('+', 5, 3)  # 8
result = calc.calculate('*', 4, 5)  # 20
```

### Error Handling

The calculator handles various error conditions gracefully:

```python
# Division by zero
calc.divide(10, 0)  # Raises ZeroDivisionError

# Invalid operation
calc.calculate('%', 10, 3)  # Raises ValueError

# Invalid input format (in CLI mode)
# Input: "5 +"
# Output: "Error: Please enter in format: number operation number"
```

## 🌸 About Miyabi

This project was created to demonstrate Miyabi's autonomous development capabilities. Miyabi is a self-operating AI agent system that uses GitHub as its operating system for persistent memory and task management.

For more information, see [MIYABI_GUIDE.md](MIYABI_GUIDE.md).

## 📄 License

This project is created for demonstration purposes.
