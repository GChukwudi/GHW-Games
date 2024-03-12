## Rock Paper Scissors Hand Game

The Rock Paper Scissors Hand Game is an interactive Python application that allows users to play the game of rock-paper-scissors using hand gestures captured through their webcam. This project demonstrates the integration of computer vision techniques with game logic to create a gaming experience.

### Features

- Real-time hand gesture recognition using OpenCV.
- Simple user interface displaying live webcam feed and game interface.
- Computer opponent with randomized moves.
- Score tracking for multiple rounds of gameplay.
- Easy-to-use keyboard controls to start and exit the game.

### Technologies Used

* Python: The core programming language used for developing the application.
* OpenCV: OpenCV (Open Source Computer Vision Library) is utilized for capturing webcam input and processing hand gestures.
* cvzone: The cvzone library is employed for simplified hand tracking and finger counting.
* GitHub: Hosting platform for storing the project repository and source code.
Markdown: Used for writing this README file and providing project documentation.
Installation
Clone this repository to your local machine:



bash
Copy code
git clone https://github.com/your-username/rock-paper-scissors-hand-game.git
Navigate to the project directory:

bash
Copy code
cd rock-paper-scissors-hand-game
Install the required dependencies:

![alt text](<2024-03-12 (1).png>)

Copy code
pip install opencv-python opencv-python-headless cvzone
How to Play
Run the program by executing the main.py file:

bash
Copy code
python main.py
The program will display the live webcam feed along with the game interface.

Press the 's' key on your keyboard to start the game.

Make hand gestures in front of the webcam to represent your choice (rock, paper, or scissors).

The computer will randomly select its move.

The winner of each round will be determined based on the gestures, and the scores will be updated accordingly.

Continue playing until you decide to exit the game by pressing the 'Esc' key.

Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please feel free to open an issue or submit a pull request.