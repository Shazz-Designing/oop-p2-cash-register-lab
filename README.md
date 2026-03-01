# Cash Register – OOP Part 2

## Overview

This project implements a `CashRegister` class using Object-Oriented Programming principles in Python.

The class simulates core functionality of an e-commerce checkout system, including:

- Adding items with an optional quantity
- Tracking a running total
- Applying percentage-based discounts
- Voiding the last transaction
- Maintaining a list of all added items (including duplicates)

The project was developed using Test-Driven Development (TDD). All functionality was implemented to satisfy the provided automated tests.

---

## Concepts Demonstrated

- Class creation and initialization
- Instance attributes and state management
- Method implementation
- Optional parameters
- Percentage calculations
- Transaction tracking
- Test-driven development workflow

---

## Features

### Initialization

- Optional discount percentage (default is 0)
- `total` initialized to `0`
- `items` initialized as an empty list
- Tracks the last transaction amount for voiding

### Methods

#### `add_item(title, price, quantity=1)`

- Adds item(s) to the register
- Updates the running total
- Tracks the last transaction amount

#### `apply_discount()`

- Applies a percentage discount to the total
- Prints the updated total
- Prints an error message if no discount exists

#### `void_last_transaction()`

- Subtracts the last transaction from the total
- Prevents incorrect totals

---

## How to Run

Install dependencies and activate the environment:

```bash
pipenv install
pipenv shell
```

Run tests:

```bash
pytest
```

---

## Test Results

All automated tests pass successfully:

```
14 passed in 0.xx seconds
```

---

## Project Structure

```
lib/
 └── cash_register.py
lib/testing/
 └── cash_register_test.py
```