# Mbox Attachment Extractor

A Python script that extracts all attachments from an mbox file and saves them to disk.

## Features

- Extracts all attachments from an mbox file and saves them to disk.
- Supports specifying the mbox file path and output directory path as command-line arguments.
- Supports a `--dry-run` option to simulate the extraction without actually saving the attachments.
- Logs messages to the console to indicate the progress and status of the extraction process.
- Written in Python 3 using the built-in `mailbox` module.

## Requirements

- Python 3.6 or higher.
- The built-in `mailbox` module.

## Usage

```
python extract_attachments.py -m <mbox_file> -o <output_dir> [-d]
```


- `-m` or `--mbox`: the path to the mbox file to extract attachments from (required).
- `-o` or `--output`: the path to the output directory where attachments will be saved (required).
- `-d` or `--dry-run`: enable dry-run mode, which simulates the extraction without saving the attachments (optional).

## Examples

Extract attachments from `example.mbox` and save them to `attachments/`:

```
python extract_attachments.py -m example.mbox -o attachments/
```

Simulate the extraction from `example.mbox` without saving the attachments:

```
python extract_attachments.py -m example.mbox -o attachments/ -d
```


## License

This script is licensed under the MIT License. See the `LICENSE` file for details.

## Author

This script was written by [Per Arneng](https://github.com/PerArneng/).


