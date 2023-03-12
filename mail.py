import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


gmail_smtp = "smtp.gmail.com"
gmail_imap = "imap.gmail.com"
login = 'login@gmail.com'
password = 'qwerty'
subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message = 'Message'
header = None


class MailAssistant:

    def __init__(self, user_login, user_password):
        self.login = user_login
        self.password = user_password

    def send_message(self, _recipients, _subject, _message, _gmail_smtp):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(_recipients)
        msg['Subject'] = _subject
        msg.attach(MIMEText(_message))

        ms = smtplib.SMTP(_gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

        return 'msg sent'

    def receive_message(self, message_header, _gmail_imap):
        mail = imaplib.IMAP4_SSL(_gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % message_header if message_header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return 'msg receive'


if __name__ == '__main__':
    mail = MailAssistant(login, password)

    mail.send_message(recipients, subject, message, gmail_smtp)

    mail.receive_message(header, gmail_imap)
