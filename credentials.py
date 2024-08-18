class Credentials:

    number_of_credentials = 0
    author = 'dm_credential'
    def __init__(self, name):
        self.name = name        
        Credentials.number_of_credentials = Credentials.number_of_credentials + 1

    @staticmethod
    def static_method():
        print('static method')

    @classmethod
    def class_method(cls):
        print(cls.author)

    def instance_method(self):
        print('instance method')

    def create_config(self):
        author = 1
        pass