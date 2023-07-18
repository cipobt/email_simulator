# email_simulator

This programme simulates an email message with a class Email whit four variables:

has_been_read
email_contents
is_spam
from_address.

The constructor initialises the sender’s email address and also initialise has_been_read and is_spam to false.

A function called mark_as_read has been created in this class which changes has_been_read to true 
Another function in this class called mark_as_spam which changes is_spam to true

A list called inbox stores all emails

The following functions have been defined:

○ add_email - which takes in the contents and email address from the received email tomake a new Email object.
○ get_count - returns the number ofmessages in the store.
○ get_email - returns the contents of an email in the list. For this, allow the user to input an index i.e. get_email(i) returns the email stored
at position i in the list. Once this has been done, has_been_read should now be true.
○ get_unread_emails - should return a list of all the emails that haven’t been read.
○ get_spam_emails - should return a list of all the emails that have been marked as spam.
○ delete - deletes an email in the inbox.
