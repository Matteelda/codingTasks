class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address 
        self.subject_line = subject_line 
        self.email_content = email_content
        self.has_been_read = False   # Initialize to False by default

    # Instance method to mark the email as read
    def mark_as_read(self):
        self.has_been_read = True  # Change has_been_read to True

# Inbox list to store email instances
inbox = []

def populate_inbox():
    # Clear inbox to avoid duplicates
    inbox.clear()
    # Add sample emails to the inbox list
    inbox.append(Email("dev@email.com", "Welcome to HyperionDev!", "Should you need any further support, please click the link below to submit a query and our support team will aim to respond timeously."))
    inbox.append(Email("techme@email.com", "Great Work on the bootcamp!", "Your Unit 1 submission was successful. Please do not hesitate to reach out if you need anything."))
    inbox.append(Email("hyper@email.com", "Your excellent marks!", "Congratulations on your outstanding performance! Keep up the great work."))

def list_emails():
    # Print each email's subject line with its corresponding index
    for index, email in enumerate(inbox):
        print(f"{index}: {email.subject_line}")

def read_email(index):
    # Check if the index is valid
    if 0 <= index < len(inbox):
        email = inbox[index]
        # Display the email's details
        print(f"Email Address: {email.email_address}")
        print(f"Subject Line: {email.subject_line}")
        print(f"Email Content: {email.email_content}")
        # Mark the email as read
        email.mark_as_read()  # Sets has_been_read to True
        
        print(f"\nEmail from {email.email_address} marked as read.\n") # Confirmation message for marking as read
    else:
        print("Invalid email index.")

def list_unread_emails():
    # Print only unread emails with their index and subject line
    for index, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{index}: {email.subject_line} (Unread)")

def print_subject_lines():
    # Loop through each email in the inbox and print only the subject line
    for email in inbox:
        print(email.subject_line)

# Main function to run the email application
def email_app():
    populate_inbox()    # Populate inbox with sample emails

    while True:
        print("\nOptions:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            # List emails and prompt user to select one by index
            list_emails()
            try:
                index = int(input("Enter the index of the email to read: "))
                read_email(index)
            except ValueError:
                print("Please enter a valid index number.")
        
        elif choice == "2":
            # Display only unread emails
            print("Unread Emails:")
            list_unread_emails()
        
        elif choice == "3":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the application
email_app()

# Example call to print only the subject lines after the main application
print("\nAll Subject Lines:")
print_subject_lines()