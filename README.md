# Space Invaders Game - Version 2

This is the second version of the Space Invaders game, a classic arcade-style shooter. In this version, I made several improvements to the previous version, including adding multiple enemies, a scoring system, game over functionality, background music, sound effects, and a nicer display of the score. The game is implemented using the `pygame` library in Python.

## Requirements:
- Python 3
- Pygame library

## How to Play:
1. Run the script, and the game window will appear.
2. Use the arrow keys (left and right) to move the player's ship horizontally.
3. Press the spacebar to shoot bullets.
4. Defeat the enemies by hitting them with your bullets.
5. Each enemy hit earns you one point.
6. Avoid enemy ships coming too close to your ship, or it's game over.
7. The game will display "GAME OVER" when the player loses.
8. You can restart the game by running the script again.

## Controls:
- Left Arrow: Move left
- Right Arrow: Move right
- Spacebar: Shoot bullets

## Game Version 2 Improvements:
1. Added multiple enemies to make the game more challenging.
2. Implemented a scoring system to keep track of the player's score.
3. Display the score on the screen during gameplay.
4. Added a game over functionality when an enemy ship reaches a certain Y-coordinate.
5. Improved the display of the score on the screen using a custom font.
6. Added background music to make the game more engaging.
7. Added sound effects for shooting bullets and when an enemy is hit.

## Game Assets:
The game assets (images and sounds) should be placed in a folder named "spaceinvader" in the same directory as the Python script. The assets include the following:
- Background image: "3.jpg"
- Player's ship image: "battleship.png"
- Enemy ships image: "4.png"
- Bullet image: "bullets.png"
- Game over font: "font.ttf"
- Background music: "background.wav"
- Bullet sound effect: "laser.wav"
- Enemy hit sound effect: "explosion.wav"

Make sure to have these assets available for the game to run correctly.

## Notes:
- The game loop continuously updates the screen and checks for player input and collisions.
- The player can move the ship left and right and fire bullets at the enemies.
- The enemy ships move left and right, and if they reach a certain Y-coordinate, the game ends.
- When the player's bullet collides with an enemy ship, the enemy disappears, and the score is increased by one point.
- The game will display the current score on the top left corner of the screen.
- The game will show "GAME OVER" on the screen if an enemy ship reaches the specified Y-coordinate, and the player can restart the game by running the script again.
