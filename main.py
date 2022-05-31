import yagmail

subject = 'subject here'
spam = int(input("How many emails do you want to spam?\n-> "))
receiver_email = input("Who would you like to spam?\n-> ")

contents = ['1st line', '2nd line', '3rd line', 'https://www.youtube.com/Kxffie']

GMAIL = input('Enter your email address here\n-> ')
PASSWORD = input('Enter your email password here\n-> ')

sentEmails = 0

def sendEmail():
    global sentEmails
    
    sender_email = GMAIL
    yag = yagmail.SMTP(sender_email, PASSWORD)
    yag.send(to=receiver_email, subject=subject, contents=contents)
    sentEmails += 1
    print(f'Email {sentEmails} sent!')

for i in range(spam):
    sendEmail()