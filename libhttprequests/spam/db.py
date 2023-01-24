class Session:
    id = 0
    users = []

    def save(self, user):
        self.id += 1
        user.id = self.id
        self.users.append(user)

    def list(self):
        return self.users

    def roll_back(self):
        self.users.clear()

    def close(self):
        pass


class DBConnection:
    def generate_session(self):
        return Session()

    def close(self):
        pass
