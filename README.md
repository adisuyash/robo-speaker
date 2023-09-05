# RoboSpeaker
Welcome to RoboSpeaker, a simple text-to-speech (TTS) tool created by [AdiSuyash](https://github.com/adisuyash).

## About 
- RoboSpeaker is a Python program that converts text input into speech.
- It allows you to interact with the program by entering text commands, and it will read aloud whatever you input.
- This tool can be useful for various applications, including accessibility, automation, or just for fun.

## Getting Started
To run RoboSpeaker locally, follow these steps:

### Prerequisites
Make sure you have [Python](https://www.python.org/) and [VS Code](https://code.visualstudio.com/) installed on your computer.

### Installation
Clone this repository to your local machine (or download and extract the ZIP file).
```bash
git clone https://github.com/adisuyash/robo-speaker.git
```

Navigate to the project directory.
```bash
cd robo-speaker
```

Install the required `pyttsx3` Python library, using pip.
```bash
pip install pyttsx3
```
### Running the Program
To start RoboSpeaker, run the following command:

```bash
python roboSpeaker.py
```

You will see the welcome message, and the program will be ready to accept your text commands.

### Usage
- Enter the text you want the Robo Speaker to say and press Enter.
- To exit the program, enter one of the following commands: `exit`, `Exit` or `EXIT`.

### Example
Here's an example of how to use RoboSpeaker :
```bash
Welcome to RoboSpeaker 1.0.0 Created by AdiSuyash
Enter your command to speak: Hello, this is a test.
# The program will speak "Hello, this is a test".
Enter your command to speak: How are you today?
# The program will speak "How are you today?".
Enter your command to speak: exit
Terminated RoboSpeaker 1.0.0
```