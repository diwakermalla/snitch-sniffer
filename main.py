from credentials import Credentials


author1 = Credentials('dm')
author2 = Credentials('jc')

print('there are ' + str(Credentials.number_of_credentials) + ' authors')
print('author 1 ' + author1.name)
print('author 2 ' + author2.name)


Credentials.static_method()

Credentials.class_method()

author1.instance_method()