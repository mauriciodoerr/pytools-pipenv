from libhttprequests.spam.db import Session
from libhttprequests.spam.email_sender import EmailSender


class SpamSender:
    def __init__(self, session: Session, email_sender: EmailSender):
        self.session = session
        self.email_sender = email_sender

    def send_email(self, email_from, email_subject, email_body):
        for user in self.session.list():
            self.email_sender.send(
                email_from,
                user.email,
                email_subject,
                email_body
            )
