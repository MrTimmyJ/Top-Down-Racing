# Top-Down-Racing
A simple top-down racing game.
Race around a custom track against an AI opponent, pass through all checkpoints, and cross the finish line first!
Customize your track background and define your AI's racing path via a simple text file.

Author: Timothy Johnson <br>
Date: January 2021 to March 2021

## Overview

&nbsp;&nbsp;&nbsp;&nbsp;This is a top-down 2D racing game built with Python and Pygame.
Players control a custom car sprite and race against an AI.
The AI's path is loaded dynamically through a text file (AI.txt), allowing for map modding and custom challenges.
The objective is to pass through all rings (checkpoints) and beat the AI to the finish.

🧩 Features

    🚗 Custom top-down sprites for player and AI

    🧠 AI pathing from external AI.txt file (easy to mod!)

    🌄 Changeable background images for track customization

    ⭕ Power-up / checkpoint ring system to guide gameplay

    🕹️ Keyboard-driven player controls with directional sprite changes

    ⏱️ Finish-time tracking and high score system (written to a file)

🎮 Gameplay

You control a car from a top-down view using arrow keys or WASD. Pass through each power-up ring to progress. Once all rings are passed, the timer stops and your time is saved.

### Controls:

| Key   | Action     |
| ----- | ---------- |
| ↑ / W | Move Up    |
| ↓ / S | Move Down  |
| ← / A | Turn Left  |
| → / D | Turn Right |

📁 Code Structure

. <br>
├── Game.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Main gameplay loop and state logic <br>
├── Player.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Player car movement and sprite handling <br>
├── AIRacer.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; AI movement logic based on coordinates from AI.txt <br>
├── PowerUp.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Checkpoint ring logic and victory condition <br>
├── States.py &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; State machine for game scenes <br>
├── highscore_list.txt &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Saves top times <br>
├── AI.txt &nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp; Custom AI Positional Coordinates <br>
├── res/ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;---&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Resources folder (sprites, backgrounds, AI.txt) <br>
│   ├── Car_Down.png <br>
│   ├── Car_Left.png <br>
│   ├── Car_Right.png <br>
│   ├── Car_Up.png <br>
│   ├── Logo.png <br>
│   ├── PowerUp.png <br>
│   ├── Truck_Down.png <br>
│   ├── Truck_Left.png <br>
│   ├── Truck_Right.png <br>
│   ├── Truck_Up.png <br>
│   ├── track1.png <br>


⚙️ How It Works <br>
Player Initialization

    Loads directional car sprites and places the player on the track

    Handles input to update position and sprite direction

AI Movement

    AI.txt contains a list of X,Y coordinates

    AI moves through these points in order, simulating a racing path

Power-Ups / Rings

    Represent checkpoints around the track

    The player must pass through all to finish the race

    Once completed, the timer ends, and the high score is recorded

Timer and Scoring

    The timer starts on game load

    Stops once all rings are passed

    High score saved to highscore_list.txt in hh:mm:ss.ss format
    
🖼️ Screenshots / Visuals

![tdrbanner](https://github.com/user-attachments/assets/4bc1b66f-b1fe-4cdd-9c5a-782068c63305)

🧰 Technologies Used

    🐍 Python

    🎮 Pygame

    🖼️ Custom sprites and background images

    🧠 Text-based AI scripting (AI.txt)

    📄 File I/O: Reads from AI.txt, writes to highscore.txt

🚀 Getting Started

    To run this project on your machine:

    1. Clone this repository

        git clone https://github.com/MrTimmyJ/top-down-racing.git
        cd top-down-racing

    2. Install Pygame

       pip install pygame

    3. Run the game
    
       python Game.py

📝 Make sure AI.txt and all image assets are in the correct /res/ folder or update the file paths in code.

🌱 Planned Features

    🧭 Minimap showing player and AI progress

    🏎️ Drift mechanics or acceleration system

    🛠️ Editor for visually setting up AI.txt points

    🧊 Obstacles and power-down tiles

    🧍 2-player local multiplayer

    🧪 Better collision detection and track limits

🪪 License

This open-source project is available under the [MIT License](https://opensource.org/license/mit).

