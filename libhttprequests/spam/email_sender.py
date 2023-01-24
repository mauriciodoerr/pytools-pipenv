class EmailSender:
    def send(self, email_from, email_to, subject, body):
        if '@' not in email_from:
            raise InvalidEmail(f'Invalid email from: {email_from}')
        return email_from


class InvalidEmail(Exception):
    pass
