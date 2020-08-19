#connect to gmail
import imaplib

#set up socket connection with imap gmail server
con=imaplib.IMAP4_SSL('imap.gmail.com')

#login to gmail
email= input('Enter email:')
passwd= input('Enter password:')

con.login(email,passwd)

#check the no. of unread messages
#select the mailbox
status,mes=con.status('INBOX','(UNSEEN)')


mes=str(mes[0])
print(mes[18:22]+' unseen messages')

