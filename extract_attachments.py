import argparse
import logging
import mailbox
import os
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    parser = argparse.ArgumentParser(
        description='Extract attachments from an mbox file.',
        usage='%(prog)s -m <mbox_file> -o <output_dir> [-d]'
    )
    parser.add_argument(
        '-m',
        '--mbox',
        required=True,
        metavar='mbox_file',
        help='Path to the mbox file'
    )
    parser.add_argument(
        '-o',
        '--output',
        required=True,
        metavar='output_dir',
        help='Path to the output directory'
    )
    parser.add_argument(
        '-d',
        '--dry-run',
        action='store_true',
        help='Enable dry-run mode (don\'t extract attachments)'
    )
    args = parser.parse_args()

    mbox_file = args.mbox
    output_dir = args.output
    dry_run = args.dry_run

    # Create the output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f'Created output directory: {output_dir}')

    # Open the mbox file and iterate over the messages
    mbox = mailbox.mbox(mbox_file)
    logging.info(f'Opened mbox file: {mbox_file}')
    for i, message in enumerate(mbox):
        logging.info(f'Processing message {i + 1}')
        # Iterate over the message's attachments
        for part in message.walk():
            # Check if the part is an attachment
            if part.get_filename():
                # Construct the output filename
                filename = os.path.join(output_dir, part.get_filename())
                if dry_run:
                    logging.info(f'Dry run: Would save attachment {filename}')
                else:
                    # Open the output file and write the attachment to disk
                    with open(filename, 'wb') as f:
                        f.write(part.get_payload(decode=True))
                    logging.info(f'Saved attachment: {filename}')

    logging.info('Done.')

if __name__ == '__main__':
    main()
