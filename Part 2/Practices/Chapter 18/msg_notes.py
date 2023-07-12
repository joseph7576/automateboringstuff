# fuck this country
# we should setup OAuth Client felan belan to get credentials.json 
'''
Module by the author -> EZGmail :D

'''

import smtplib

''' Overview of smtplib

>>> import smtplib
>>> smtpObj = smtplib.SMTP('smtp.example.com', 587) #? this is the default port of smtp
#? smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465) - ssl however is 465 
>>> smtpObj.ehlo()
(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')

>>> smtpObj.starttls() #? you should call this for security to be established
(220, b'2.0.0 Ready to start TLS')

>>> smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
(235, b'2.7.0 Accepted')

>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: Solong.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
{}

>>> smtpObj.quit()
(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')


Once you have the SMTP object, call its oddly named ehlo() method to “say hello” to the SMTP email server. 
250 (the code for “success” in SMTP) on the response of calling ehlo() method on SMTP object.
'''

''' Overivew of  imapclient and pyzmail -> i having problems installing this packages

>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.example.com', ssl=True) #? require SSL encryption
>>> imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
'my_email_address@example.com Jane Doe authenticated (Success)'

>>> imapObj.select_folder('INBOX', readonly=True) #? The readonly=True keyword argument prevents you from accidentally making changes or deletions to any of the emails in this folder during the subsequent method calls.

>>> pprint.pprint(imapObj.list_folders()) ->
- A tuple of the folder’s flags. (Exactly what these flags represent is beyond the scope of this book, and you can safely ignore this field.)
- The delimiter used in the name string to separate parent folders and subfolders.
- The full name of the folder.

>>> UIDs = imapObj.search(['SINCE 05-Jul-2019'])
>>> UIDs
[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]

>>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
>>> message.get_subject()

'Hello!'
>>> message.get_addresses('from')
[('Edward Snowden', 'esnowden@nsa.gov')]

>>> message.get_addresses('to')
[('Jane Doe', 'jdoe@example.com')]

>>> message.get_addresses('cc')
[]

>>> message.get_addresses('bcc')
[]

>>> message.text_part != None
True

>>> message.text_part.get_payload().decode(message.text_part.charset)
'Follow the money.\r\n\r\n-Ed\r\n'

>>> message.html_part != None
True

>>> message.html_part.get_payload().decode(message.html_part.charset)
'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'

>>> imapObj.logout()

>>> imaplib._MAXLINE = 10000000 #? search matches size limit -> default is 10000 bytes.

#? (Note that the b prefix means this is a bytes value, not a string value.
#? The difference isn’t too important; just remember to include the b prefix in your code.)
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])

'''

'''SMS!!! can send sms via email!!!

While SMS email gateways are free and simple to use, there are several major disadvantages to them:

- You have no guarantee that the text will arrive promptly, or at all.
- You have no way of knowing if the text failed to arrive.
- The text recipient has no way of replying.
- SMS gateways may block you if you send too many emails, and there’s no way to find out how many is “too many.”
- Just because the SMS gateway delivers a text message today doesn’t mean it will work tomorrow.

Sending texts via an SMS gateway is ideal when you need to send the occasional, nonurgent message.
If you need more reliable service, use a non-email SMS gateway service, as described next.
'''

'''Twilio
Twilio is an SMS gateway service, which means it allows you to send text messages from your programs via the internet.


'''