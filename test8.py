# username Request
# password request

# correct both User Name and Passwork
# show result (login)

uname = 'hlainghtoo'
pwd = '1234'
username = input (" Enter username: ")
password = input ("Enter password: ")
name = ' Saw Hlaing Htoo'
if username == uname and password == pwd:
    print( "Dear" + name + " Welcome to SEF community")
elif username == uname and password !=pwd:
    print(" Wrong Password")
elif username != uname or password !=pwd:
    print (" Wrong Username or Password")
