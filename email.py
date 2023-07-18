# Features for the output menu and messages

PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# * Global variable: list of Email objects
inbox = []

class Email:
    '''
    class deﬁnition for an Email
    '''
    def __init__(self, email_contents, from_address):
        '''
        Initialising Email class with four variables, two boolean and two string type given by the user
        :param email_contents: User's input
        :param from_address: User's input
        '''
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    def mark_as_read(self):
        '''
        Method to change value of attribute has_been_read
        :return: Nothing
        '''
        self.has_been_read = True

    def mark_as_spam(self):
        '''
        Method to change value of attribute is_spam
        :return: Nothing
        '''
        self.is_spam = True

def add_email(contents, sender):
    '''
    Function that adds new email input by User to global list inbox
    :param contents: User's input
    :param sender: User's input
    :return: Nothing
    '''
    new_email = Email(contents, sender)
    inbox.append(new_email)

def get_count():
    '''
    Determines the number of emails in the inbox
    :return: number of emails in the inbox
    '''
    return len(inbox)

def get_email(index):
    '''
    Takes an especific email from the inbox, calls the function mark_as_read and returns the email chosen
    :param index: Number assigned to email
    :return: Specific email according to index
    '''
    email = inbox[index]
    email.mark_as_read()
    return email.email_contents

def get_unread_emails():
    '''
    Uses list comprehension to count all emails in inbox that haven't been read
    :return: Total of unread emails in inbox
    '''
    return [email for email in inbox if not email.has_been_read]

def get_spam_emails():
    '''
    Uses list comprehension to count all emails in inbox that are spam
    :return: Total of spam emails in inbox
    '''
    return [email for email in inbox if email.is_spam]

def delete(index):
    '''
    Deletes an especific email chosen by user from the inbox
    :param index: Number assigned to email
    :return: Nothing
    '''
    del inbox[index]

def print_separator(COLOUR):
    '''
    Prints out a decoration line to frame display messages
    :param COLOUR: Colour selected in the display option
    :return: Decoration line
    '''
    print(f'{BOLD}{COLOUR}─────────────────────────────────────────{WHITE}')


# An Email Simulation
# I've added error handling features to prevent the program from crashig and there are a few inbox display messages
# that help the user to check the inbox and select a particular email. Also I initiated the list with some dummy data

inbox.append(Email("This is a first sample", "test@test.com"))
inbox.append(Email("This is the second sample", "test@test.com"))
inbox.append(Email("I'm still working on this program", "test@test.com"))

user_choice = ""

print(f"\n{BOLD}{YELLOW}Welcome to your email inbox!{WHITE}")

while user_choice != "q":
    try:
        user_choice = input(f"\nPlease choose one option:\n"
                            f"{BOLD}{UNDERLINE}{BLUE}C{WHITE}heck inbox\n"
                            f"{BOLD}{UNDERLINE}{PINK}R{WHITE}ead\n"
                            f"{BOLD}{UNDERLINE}{BLUE}M{WHITE}ark spam\n"
                            f"{BOLD}{UNDERLINE}{GREEN}S{WHITE}end\n"
                            f"{BOLD}{UNDERLINE}{RED}D{WHITE}elete\n"
                            f"{BOLD}{UNDERLINE}{RED}Q{WHITE}uit: ").lower()
    except ValueError:
        print("Invalid input!")

    total_inbox = len(inbox)

    if user_choice == "c":
        for i in range(total_inbox):
            print_separator(YELLOW)
            email_contents = get_email(i)
            print(f"Email {i}: {email_contents}")
        print_separator(YELLOW)

    elif user_choice == "r":
        if total_inbox == 0:
            print("\nNo unread emails in your inbox")
        else:
            total_unread = len(get_unread_emails())
            print(f"\n{total_unread} unread emails from {total_inbox} emails in your inbox")
            try:
                index = int(input(f"\nWhich email you wanna read? (input a number betwen 0-{total_inbox-1}) "))
                if index <= total_inbox:
                    email_contents = get_email(index)
                    print(f"\nEmail {index}: {email_contents}")

                else:
                    continue
            except ValueError:
                print("Invalid input!")

    elif user_choice == "m":  # The user can see the email before confirming it goes to spam
        if total_inbox == 0:
            print(F"\nNo spam: {BOLD}{CYAN}CONGRATULATIONS!")
        else:
            print(f"\n{total_inbox} emails in your inbox")
            try:
                index = int(input(f"\nWhich email goes to spam? (input a number betwen 0-{total_inbox-1}) "))
                email_contents = get_email(index)
                print(f"\nEmail {index}: {email_contents}")

                if input("\nConfirm this is spam (Y/N) ").lower() == 'y':
                    email = inbox[index]
                    email.mark_as_spam()
                    print(f"\nThe email from {email.from_address} marked as spam.")
                else:
                    continue
            except ValueError:
                print("Invalid input!")

    elif user_choice == "s":
        user_email = input("\nWrite your email: ")
        user_address = input("Sender address: ")
        add_email(user_email, user_address)
        print("Email added to the inbox")

    elif user_choice == "d":
        print(f"\n{total_inbox} emails in your inbox")
        try:
            index = int(input(f"\nWhat email you wish to delete? (input a number betwen 0-{total_inbox-1}) "))
            email_contents = get_email(index)
            print(f"\nEmail {index}: {email_contents}")

            if input("\nConfirm deletion (Y/N) ").lower() == 'y':
                delete(index)
                print(f"\nThe email has been deleted.")
            else:
                continue
        except ValueError:
            print("Invalid input!")


    elif user_choice == "q":
        print("That's all!")

    else:
        print(f"{BOLD}{UNDERLINE}{RED}Invalid input")
