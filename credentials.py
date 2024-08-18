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

    def merge_test(self):
        pass

    def create_config(self):
        author = 1
        pass

    def manual_merge1(self):
        print('test1111')
        pass

    def manual_merge2(self):
        pass

    def manual_merge2_main(self):
        pass

    def merge_test_from_lidar(self):
        print(1)
        print(1)
        print(1)

    