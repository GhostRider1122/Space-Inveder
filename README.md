## My First Game - A Space Invader Game

![Spaceship dodging enemy fire](assets/icons/gameplay_screenshot.png)  This is a simple space invader game developed using the Pygame library. 

### How to Play

* Use the arrow keys (`a` and `d`) to move your spaceship left and right.
* Click your mouse to fire a bullet.
* Shoot down enemies to score points.
* Avoid being hit by the enemies or their bullets.

### Game Over

The game ends when an enemy reaches the bottom of the screen.

### Running the Game

1. Make sure you have Pygame installed (`pip install pygame`).
2. Download the game files and place them in the same directory.
3. Run the game using Python (`python main.py`).

### Files

* `main.py`: The main game script.
* `assets/`: This directory contains the game assets such as images and sounds.
    * `assets/icons/`: This directory contains game icons.
        * `game_icon.png`: The game icon.
        * `background.jpg`: The game background image.
        * `spaceship.png`: The spaceship image.
        * `enemy.png`: The enemy image.
        * `bullet.png`: The bullet image.
    * `assets/sounds/`: This directory contains game sounds.
        * `bgm.mp3`: The background music.
        * `shoot.wav`: The sound effect for shooting a bullet.
        * `invaderkilled.wav`: The sound effect for killing an enemy.
