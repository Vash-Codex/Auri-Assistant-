import pyttsx3
import webbrowser
import subprocess
import os
import platform
import wikipedia
import tkinter as tk
import threading
import time
from datetime import datetime
from math import cos, sin, pi
import speech_recognition as sr
import random

#adding the shutdown
end = random.randint(1, 5)
if end == 1:
    o = "Goodbye! Have a great day"
elif end == 2:
    o = "Shutting Down, Master"
elif end == 3:
    o = "Powering Down, See you soon"
elif end == 4:
    o = "Survive without me, live long"
elif end == 5:
    o = "Goodbye God Father"
print(end, o)


# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_wikipedia_summary(topic):
    """Fetch a summary from Wikipedia."""
    try:
        summary = wikipedia.summary(topic, sentences=2)  # Get a 2-sentence summary
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found for '{topic}': {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return None
    except Exception as e:
        return f"An error occurred while fetching Wikipedia information: {e}"

def search_google(query):
    """Search for a query on Google."""
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return f"Searching Google for {query}..."

def tell_time():
    """Get the current time."""
    now = datetime.now()
    return now.strftime("The current time is %I:%M %p.")

def handle_command(command):
    """Handle commands by prioritizing Wikipedia and falling back to Google."""
    command = command.lower()
    if "time" in command:
        return tell_time()
    elif "search" in command or "information" in command:
        topic = command.replace("search", "").replace("information", "").strip()
        response = get_wikipedia_summary(topic)
        if response:
            return response
        else:
            return search_google(topic)
    elif "open" in command:
        app_name = command.replace("open", "").strip()
        return open_app(app_name)
    else:
        return search_google(command)

def open_app(app_name):
    """Open the specified application."""
    app_paths = find_app(app_name)
    if app_paths:
        app_path = app_paths[0]
        try:
            if platform.system() == "Windows":
                os.startfile(app_path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", app_path])
            elif platform.system() == "Linux":
                subprocess.run([app_path])
            return f"Opening {app_name}."
        except Exception as e:
            return f"Failed to open {app_name}. Error: {e}"
    else:
        return f"Sorry, I couldn't find {app_name} on your system."

def find_app(app_name):
    """Search for an application on the system."""
    os_name = platform.system()
    app_paths = []

    if os_name == "Windows":
        search_dirs = [os.getenv("ProgramFiles"), os.getenv("ProgramFiles(x86)"), os.getenv("LOCALAPPDATA")]
        for directory in search_dirs:
            if directory:  # Ensure the directory is not None
                for root, _, files in os.walk(directory):
                    for file in files:
                        if app_name.lower() in file.lower() and file.endswith(".exe"):
                            app_paths.append(os.path.join(root, file))
    elif os_name == "Darwin":  # macOS
        for root, _, files in os.walk("/Applications"):
            for file in files:
                if app_name.lower() in file.lower() and file.endswith(".app"):
                    app_paths.append(os.path.join(root, file))
    elif os_name == "Linux":
        result = subprocess.run(["which", app_name], stdout=subprocess.PIPE, text=True)
        if result.stdout:
            app_paths.append(result.stdout.strip())

    return app_paths

# Create a GUI with Tkinter
def create_gui():
    """Create a Tkinter-based GUI for the assistant."""
    def start_listening(event=None):
        """Handle voice commands."""
        print("Listening")
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        try:
            with microphone as source:
                speak("Listening...")
                output_text.insert(tk.END, "Auri: Listening...\n")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                output_text.insert(tk.END, f"You: {command}\n")
                response = handle_command(command)
                output_text.insert(tk.END, f"Auri: {response}\n\n")
                output_text.see(tk.END)
                speak(response)
        except sr.UnknownValueError:
            output_text.insert(tk.END, "Auri: Sorry, I couldn't understand that.\n")
            speak("Sorry, I couldn't understand that.")
        except Exception as e:
            output_text.insert(tk.END, f"Auri: An error occurred: {e}\n")
            speak("An error occurred.")

    def process_text_command():
        """Handle text-based commands."""
        command = user_input.get().strip()
        if command:
            response = handle_command(command)
            output_text.insert(tk.END, f"You: {command}\n")
            output_text.insert(tk.END, f"Auri: {response}\n\n")
            output_text.see(tk.END)
            user_input.delete(0, tk.END)
            speak(response)

   #program end
    def quit_program(event=None):
        """Quit the program gracefully."""
        speak(o)
        window.quit()

    window = tk.Tk()
    window.title("Auri Assistant")
    window.geometry("250x450")
    window.configure(bg="black")

    # Output display area
    output_text = tk.Text(window, bg="black", fg="magenta", font=("Helvetica", 12), wrap="word", height=15, width=50)
    output_text.pack(pady=10)

    # User input area
    user_input = tk.Entry(window, bg="black", fg="magenta", font=("Helvetica", 14), insertbackground="magenta")
    user_input.pack(pady=10)
    user_input.bind("<Return>", lambda event: process_text_command())

    # Buttons
    listen_button = tk.Button(window, text="Start Listening", command=start_listening, bg="green", fg="black", width=15)
    listen_button.pack(pady=5)

    window.bind("<Next>", start_listening)

    submit_button = tk.Button(window, text="Submit", command=process_text_command, bg="magenta", fg="black", width=15)
    submit_button.pack(pady=5)

    quit_button = tk.Button(window, text="Quit", command=quit_program, bg="red", fg="black", width=15)
    quit_button.pack(pady=5)
    window.bind("<Escape>", quit_program)

    # Greeting and time announcement
    greeting = "Hello! I am Auri, your assistant. " + tell_time()
    output_text.insert(tk.END, f"Auri: {greeting}\n\n")
    speak(greeting)

    window.mainloop()

# Main function
def main():
    create_gui()

if __name__ == "__main__":
    main()
