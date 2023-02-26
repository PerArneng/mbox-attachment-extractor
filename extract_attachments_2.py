# Import the mailbox, argparse and logging modules
import mailbox
import argparse
import logging

# Define a function to extract attachments from a message
def extract_attachments(message):
    # Loop through all the parts of the message
    for part in message.walk():
        # Check if the part is an attachment
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # Get the filename and sender of the attachment
        filename = part.get_filename()
        sender = message['From']
        if filename is None or sender is None:
            continue

        # Create a subfolder for each sender in the output folder
        subfolder = os.path.join(args.output, sender)
        os.makedirs(subfolder, exist_ok=True)

        # Save the attachment to a file in the subfolder
        filepath = os.path.join(subfolder, filename)
        logging.info(f'Saving {filename} from {sender} to {filepath}')
        if not args.dry_run:
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))

# Create an argument parser
parser = argparse.ArgumentParser(description='Extract attachments from an mbox file.')
parser.add_argument('-i', '--input', required=True, help='The path to the mbox file.')
parser.add_argument('-o', '--output', required=True, help='The path to the output folder.')
parser.add_argument('-d', '--dry-run', action='store_true', help='Do not save any files.')
args = parser.parse_args()

# Configure logging with date and time format
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Open the mbox file
logging.info(f'Opening {args.input}')
mbox = mailbox.mbox(args.input)

# Loop through all the messages in the mbox file
for message in mbox:
    # Extract attachments from each message
    extract_attachments(message)
