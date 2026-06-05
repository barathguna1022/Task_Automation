# Task 3 - Task Automation with Python Scripts
# Sub-task: Extract all email addresses from a .txt file
# Concepts used: re, file handling (text mode + binary mode), OOP (class, object)

import re

# ----------------------------------------
# CLASS - EmailExtractor
# Handles reading the file, finding emails,
# and saving them — all in one class
# ----------------------------------------
class EmailExtractor:

    # __init__ stores the file names and an empty list for found emails
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.emails = []   # will store all found email addresses

    # Method to read the file in BINARY mode
    # Binary mode reads the file as raw bytes (0s and 1s)
    # We then decode it to a normal string for processing
    def read_file_binary(self):
        print("Reading file in binary mode...")

        # "rb" means read binary — file is read as bytes, not text
        binary_file = open(self.input_filename, "rb")
        raw_bytes = binary_file.read()
        binary_file.close()

        print("Raw bytes (first 60):", raw_bytes[:60])   # show a preview of binary data

        # Decode bytes to a regular string so we can search for emails
        content = raw_bytes.decode("utf-8")
        print("\nDecoded to text successfully.\n")
        return content

    # Method to find all emails using regular expression
    def find_emails(self, content):
        # Email pattern: characters @ domain . extension
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        self.emails = re.findall(email_pattern, content)

    # Method to show found emails on screen
    def show_emails(self):
        if len(self.emails) == 0:
            print("No email addresses found in the file.")
        else:
            print("Emails found:", len(self.emails))
            for email in self.emails:
                print("-", email)

    # Method to save extracted emails to an output text file
    def save_emails(self):
        if len(self.emails) == 0:
            print("Nothing to save.")
            return

        output_file = open(self.output_filename, "w")
        output_file.write("Extracted Email Addresses\n")
        output_file.write("--------------------------\n")
        for email in self.emails:
            output_file.write(email + "\n")
        output_file.close()

        print("\nAll emails saved to", self.output_filename)

    # Method to run all steps together
    def run(self):
        print("Email Extractor - Automation Script")
        print("-------------------------------------")

        content = self.read_file_binary()   # Step 1: read file in binary mode
        self.find_emails(content)            # Step 2: find emails using regex
        self.show_emails()                   # Step 3: print on screen
        self.save_emails()                   # Step 4: save to output file


# ----------------------------------------
# Create an object and run the extractor
# ----------------------------------------
extractor = EmailExtractor("sample_text.txt", "extracted_emails.txt")
extractor.run()
