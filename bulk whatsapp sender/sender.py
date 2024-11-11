import pandas as pd
import pywhatkit
import pyautogui
import time

# Load the data from the CSV file
df = pd.read_csv("int_rotich.csv")

# Define the message template
message_template = (
    "Hi {first_name},\n\n"
    "This is just to inform you that there are two JKUELC events this Saturday: a fun day in Karen and a mentorship event at KU. "
    "If you will be attending the KU mentorship event, please fill out this link: "
    "https://docs.google.com/forms/d/e/1FAIpQLScmB3lYQsqvDJqXfnrTdOc2rRnicz6uUKn1uD3KFOGQk5GnaA/viewform?vc=0&c=0&w=1&flr=0\n\n"
    "If you'll be attending the Karen campus event, kindly inform me."
)

# Time interval in seconds between messages
interval = 20

# Iterate over each contact in the DataFrame
for index, row in df.iterrows():
    # Format phone number and extract first name
    phone_number = f"+{int(row['Phone number'])}"
    first_name = row['Full name'].split()[0]
    message = message_template.format(first_name=first_name)

    # Calculate the scheduled time for each message
    current_hour = time.localtime().tm_hour
    current_minute = time.localtime().tm_min + 2  # Set a 2-minute buffer

    # Adjust if minutes exceed 59
    if current_minute >= 60:
        current_hour = (current_hour + 1) % 24
        current_minute = current_minute % 60

    try:
        # Schedule message with pywhatkit
        pywhatkit.sendwhatmsg(phone_number, message, current_hour, current_minute)

        # Allow time for WhatsApp to load and send
        time.sleep(15)

        # Press Enter to send the message
        pyautogui.press("enter")

        # Wait before sending the next message
        time.sleep(interval)

    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")
