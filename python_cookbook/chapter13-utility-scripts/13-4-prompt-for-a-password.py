import getpass

user = getpass.getuser()
passwd = getpass.getpass()


def svc_login(user, passwd):
    print(user, passwd)


if svc_login(user, passwd):
    print('Yay!')
else:
    print('Boo!')