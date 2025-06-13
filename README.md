-----

# Auri Assistant

Auri is a versatile desktop assistant built with Python, capable of performing various tasks through both voice and text commands. It can provide information from Wikipedia, search the web using Google, tell you the current time, and even open applications on your system.

-----

## Features

  * **Voice and Text Commands**: Interact with Auri using your microphone or by typing commands.
  * **Intelligent Command Handling**: Auri prioritizes Wikipedia for information retrieval and falls back to Google search if a Wikipedia summary isn't available.
  * **Time Teller**: Quickly get the current time.
  * **Application Launcher**: Open applications installed on your Windows, macOS, or Linux system.
  * **Cross-Platform Compatibility**: Designed to work on major operating systems.
  * **User-Friendly GUI**: A simple and intuitive graphical interface built with Tkinter.

-----

## How it Works

Auri leverages several Python libraries to deliver its functionalities:

  * `pyttsx3`: For text-to-speech capabilities, allowing Auri to speak its responses.
  * `speech_recognition`: To process your voice commands through your microphone.
  * `wikipedia`: To fetch summaries directly from Wikipedia.
  * `webbrowser`: To open web pages for Google searches.
  * `subprocess` and `os`: For interacting with your operating system to open applications and manage paths.
  * `tkinter`: To create the graphical user interface.

-----

## Installation

To get Auri up and running, follow these steps:

1.  **Clone the repository (or download the code):**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

      * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
      * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**

    ```bash
    pip install pyttsx3 wikipedia speechrecognition
    ```

      * **Note for `pyttsx3`**: Depending on your operating system, you might need additional system-level speech packages.
          * **On Windows**: `pyttsx3` generally works out of the box.
          * **On macOS**: You might need `pyobjus`.
          * **On Linux**: You might need `espeak` and `ffmpeg` (e.g., `sudo apt-get install espeak ffmpeg` on Debian/Ubuntu).

-----

## Usage

Once the GUI appears:

  * **To give a voice command**: Click the "**Start Listening**" button or press the **Page Down** key.
  * **To give a text command**: Type your command in the input box and press **Enter** or click the "**Submit**" button.
  * **To quit Auri**: Click the "**Quit**" button or press the **Escape** key.

-----

## Commands Auri Understands

Here are some examples of commands you can give Auri:

  * "What is the time?"
  * "Search for information about [topic]" (e.g., "Search for information about quantum physics")
  * "Tell me about [topic]" (e.g., "Tell me about the Eiffel Tower")
  * "Open Chrome" (or any other application like "Firefox", "Calculator", "Notepad", etc.)

-----

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome\!

----
