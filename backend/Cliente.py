class Cliente:

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login
    
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email