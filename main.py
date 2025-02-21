import time
import threading
import tkinter as tk
from tkinter import messagebox
from plyer import notification

# Function to trigger a notification
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Reminder App",
        timeout=10  
    )

# Function to start the reminder countdown
def start_reminder():
    try:
        reminder_text = message_entry.get()
        reminder_time = int(time_entry.get())  # Convert input time to an integer

        if reminder_time <= 0:
            messagebox.showerror("Error", "Time must be greater than 0")
            return

        # Notify user that the reminder has started
        messagebox.showinfo("Reminder Set", f"Reminder set for {reminder_time} seconds.")

        # Run countdown in a separate thread so the UI doesn't freeze
        threading.Thread(target=reminder_countdown, args=(reminder_time, reminder_text), daemon=True).start()
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for time.")

# Function that waits for the reminder time and shows a notification
def reminder_countdown(reminder_time, reminder_text):
    time.sleep(reminder_time)  # Wait for the specified time
    show_notification("Reminder", reminder_text)

# GUI Setup using Tkinter
root = tk.Tk()
root.title("Reminder App")
root.geometry("300x200")

# Title Label
tk.Label(root, text="Notification Reminder", font=("Arial", 14)).pack(pady=10)

# Message Entry
tk.Label(root, text="Enter Reminder Message:").pack()
message_entry = tk.Entry(root, width=30)
message_entry.pack(pady=5)

# Time Entry
tk.Label(root, text="Enter Time (seconds):").pack()
time_entry = tk.Entry(root, width=10)
time_entry.pack(pady=5)

# Set Reminder Button
tk.Button(root, text="Set Reminder", command=start_reminder, height=5).pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
