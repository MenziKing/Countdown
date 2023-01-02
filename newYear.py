import tkinter as tk
from datetime import datetime, timedelta

# Create the main window
window = tk.Tk()
window.title("New Year's Countdown")

# Set the font for the clock
font = ('Helvetica', 80)

# Create a label to display the clock
clock = tk.Label(window, text='', font=font)
clock.pack()
clock.config(bg='red')
# Set the current time
now = datetime.now()

# Calculate the number of seconds until New Year's Day
new_year = datetime(now.year + 1, 1, 1)
seconds_left = (new_year - now).total_seconds()

# Function to update the clock
def update_clock():
  global seconds_left
  seconds_left -= 1
  time_left = timedelta(seconds=seconds_left)
  clock.config(text=time_left)
  clock.after(1000, update_clock)

# Start the clock
update_clock()

# Run the main loop
window.mainloop()
