### My first OOP practice with Python

This is the first part of a project to learn how to create classes, and to help me understand basic OOP with Python.

#### Instalation

Clone this repository and run main *duh*

#### What does this button do?

Best Buy (this program) is a CLI that simulates a self-checkout TPV.
A store object is generated along with product objects when the program runs (hard coded).
The user interface prints a menu of actions available in a command dispatcher.
Users can check inventory from a store class object, which contains product class objects.
Users can check the total amount of units across all products in the store.
Users can order: grand total is shown and product quantity is updated.


##### Making nice code:

+ Type Hinting: Improved code readability, it will facilitate static analysis of each class module.
+ Docstrings: Explaining the purpose of each class, and the behaviour of each method, will improve maintainability.
+ More Docstrings: Explaining what each function does and returns, or at least trying to get used to it.
+ Error Handling: Type checking, empty strings and negative values will cause errors when running the program.
+ Assertions: Since this is a project for learning and not for production, some assertions can be found for checking input.
+ Exception messages: Each error and assertion will raise different error messages, making debugging easier and to guide the user during interaction.

* Product class dynamic attribute: The instantiation will contain an "active" (bool) attribute, which will be initialized as True if the "quantity" (int) attribute is higher than zero, otherwise its value will be set to False.