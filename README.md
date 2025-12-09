Snake Game – Python Turtle Graphics

This project is a full implementation of the classic Snake game using Python’s Turtle Graphics.
It includes smooth snake movement, food spawning, scorekeeping with high-score tracking, wall collision detection, and tail collision logic.
The game is built using an object-oriented approach with separate classes for the snake, food, and scoreboard, making the code modular and easy to expand.

Players control the snake using W, A, S, D keys and try to survive as long as possible while collecting food and increasing their score.

Key Features
1. Fully Functional Snake Movement

The snake is composed of multiple segments that follow the head smoothly.
The Snake class handles:

Movement

Turning (with direction restrictions to avoid 180° flips)

Extending the body when food is eaten

Resetting after collisions

2. Randomly Spawning Food

The Food class generates food at random positions on the screen.
Each time the snake eats the food, a new piece appears instantly.
The snake grows longer and the score increases.
Food logic handled in food.py.

3. Scoreboard with Persistent High Score

The game tracks:

Current score

Highest score stored in an external file

When the snake dies, the scoreboard resets the current score but keeps the high score saved.
Score management handled in scoreboard.py.

4. Collision Detection

The game includes accurate collision checks for:

Snake head hitting food

Snake hitting the wall (game resets)

Snake hitting its own tail (game resets)

This makes the gameplay challenging and realistic.

5. Clean Game Loop

The main file (snake_game.py) manages:

Screen setup (size, background, tracer for smooth animation)

Keyboard controls

Updating movement frame-by-frame

Calling reset functions on collision

Connecting Snake, Food, and Scoreboard together

The game runs until the player closes the window.

Conclusion

This project demonstrates essential game development concepts using Python, including:

Object-oriented programming

Real-time movement and screen updates

Collision detection

Randomized spawning

File handling for persistent high scores

It’s a fun, visually engaging way to practice Python fundamentals and graphical programming.
