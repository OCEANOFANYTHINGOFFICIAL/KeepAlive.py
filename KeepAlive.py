import pyautogui  # Importing the pyautogui module for controlling the mouse and keyboard
import time  # Importing the time module to add delays in the code
import threading  # Importing the threading module to run code concurrently
import keyboard  # Importing the keyboard module to detect key presses
import random  # Importing the random module to generate random numbers

# Global variable to control the thread
running = False  # This variable is used to start and stop the mouse movement

def move_mouse_smooth_random(interval_seconds):
    global running  # Refers to the global variable 'running'
    while running:  # Loop runs as long as 'running' is True
        # Generate a random time interval between mouse movements (not more than 10 seconds)
        interval_seconds = random.uniform(0.1, 10.0)  # Choose a random number between 0.1 and 10.0 seconds
        # Generate random coordinates within the screen boundaries
        target_x = random.randint(0, pyautogui.size()[0])  # Choose a random x-coordinate within the screen width
        target_y = random.randint(0, pyautogui.size()[1])  # Choose a random y-coordinate within the screen height
        current_x, current_y = pyautogui.position()  # Get the current position of the mouse
        steps = 20  # Number of steps for interpolation
        for i in range(steps):  # Loop to move the mouse in small steps
            # Calculate the intermediate position
            x = current_x + (target_x - current_x) * (i + 1) / steps  # Calculate the x-coordinate for the current step
            y = current_y + (target_y - current_y) * (i + 1) / steps  # Calculate the y-coordinate for the current step
            pyautogui.moveTo(x, y, duration=0.05)  # Move the mouse smoothly to the intermediate position
            time.sleep(0.02)  # Adjust the sleep time for smoother movement
        # Wait for the specified interval
        time.sleep(interval_seconds)  # Pause for the random interval before the next movement

def start_mouse_movement():
    global running  # Refers to the global variable 'running'
    if not running:  # Check if the movement is not already running
        running = True  # Set running to True to start the movement
        # Start the thread to move the mouse smoothly in random movements
        thread = threading.Thread(target=move_mouse_smooth_random, args=(0,))  # Create a new thread for mouse movement
        thread.start()  # Start the new thread
        print("Mouse smooth random movement started.")  # Print a message indicating the movement has started

def stop_mouse_movement():
    global running  # Refers to the global variable 'running'
    running = False  # Set running to False to stop the movement
    print("Mouse movement stopped.")  # Print a message indicating the movement has stopped

def on_key_press(event):
    if event.name == 's':  # If the 's' key is pressed
        start_mouse_movement()  # Start the mouse movement
    elif event.name == 'q':  # If the 'q' key is pressed
        stop_mouse_movement()  # Stop the mouse movement

if __name__ == "__main__":
    try:
        # Register the keypress event handler
        keyboard.on_press(on_key_press)  # Set up the function to be called when a key is pressed
        print("Press 's' to start mouse smooth random movement, 'q' to quit.")  # Print instructions for the user
        # Keep the program running
        keyboard.wait()  # Wait indefinitely for a key press
    except KeyboardInterrupt:
        stop_mouse_movement()  # Stop the mouse movement if the program is interrupted
