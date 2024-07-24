Introduction
The Snake game is a classic arcade game that has been recreated using Python programming language, leveraging the Tkinter library for the graphical user interface (GUI) and employing Object-Oriented Programming (OOP) principles for modularity and reusability. This version of the game maintains the core mechanics of the original while demonstrating the capabilities of Python and Tkinter.

Libraries and Tools
Python: A versatile high-level programming language known for its readability and simplicity.
Tkinter: The standard GUI toolkit in Python, which is used to create windows, dialogs, and various widgets.
OOP (Object-Oriented Programming): A programming paradigm that uses objects and classes to structure the code, enhancing code modularity and reusability.
Game Features
Graphical Interface:

Window Creation: The game window is created using Tkinter, with a defined size and title.
Canvas Widget: The game board is a Tkinter canvas where the snake and food items are drawn.
Game Logic:

Snake Movement: The snake moves in four directions (up, down, left, right) based on user input.
Food Consumption: The snake grows in length when it eats food, which randomly appears on the board.
Collision Detection: The game detects collisions with the walls or the snake’s own body, which ends the game.
OOP Design:

Class Structure: The game is designed using multiple classes:
Game: Manages the overall game state, including the start, pause, and reset functionalities.
Snake: Represents the snake, handling its movement, growth, and collision detection.
Food: Manages the food's position and ensures it appears in a valid location.
Encapsulation and Modularity: Each class encapsulates specific functionalities, promoting code reuse and easy maintenance.
User Interaction:

Keyboard Controls: The game captures keyboard events to change the snake’s direction.
Real-time Updates: The game board is updated in real-time to reflect the snake’s movement and interactions.
