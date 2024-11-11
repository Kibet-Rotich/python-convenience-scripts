```markdown
# Bulk Message Sender

This script automates the process of sending customized WhatsApp messages to a list of recipients. It’s useful for notifying multiple contacts with personalized messages, ideal for announcements, event notifications, or other group communications.

## Requirements

- **Python 3.7+**
- **Libraries**: Install required libraries using:
  ```bash
  pip install pandas pywhatkit pyautogui
  ```
  
- **WhatsApp Web**: The script uses WhatsApp Web, so ensure you’re logged in to WhatsApp Web on your default browser.

## Input Data

The script reads a CSV file containing the recipients' names and phone numbers. The CSV file should have the following columns:

- **Full name**: Full name of the recipient (used to extract the first name for personalization)
- **Phone number**: Phone number of the recipient, formatted without the '+' (e.g., '254712345678' for a Kenyan number)

### Example CSV Format (int_rotich.csv)

| Full name        | Phone number |
|------------------|--------------|
| Asbel Rotich     | 254712345678 |
| Jane Doe         | 254798765432 |

## Usage

1. Place your CSV file with recipient data in the same directory as the script and name it `int_rotich.csv`.
2. Customize the message template in the script as needed. The `{first_name}` placeholder will be replaced by the recipient's first name.
3. Run the script:
   ```bash
   python bulk_message_sender.py
   ```

4. The script will open WhatsApp Web and start sending messages based on the scheduled intervals.

## Message Sending

The script calculates the next available time slot for each message and schedules it using `pywhatkit`. The `interval` setting allows you to specify a delay between messages to avoid overwhelming WhatsApp Web.

## Important Notes

- **Ensure WhatsApp Web is open**: The script relies on WhatsApp Web, so make sure your computer and browser remain active during the process.
- **Privacy**: Use this script responsibly and ensure you have permission from all recipients.
- **Error Handling**: If a message fails to send, the script will print an error message and continue to the next recipient.

---

This script is provided for educational and personal use. Modify it as needed for your requirements!
```
