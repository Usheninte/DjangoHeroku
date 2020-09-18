def django_heroku_db_url_postgres_parser(database_url):
    db_url = database_url[11:]  # remove "postgres://" from database url

    user_ = ""  # initialize user base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        user_ += el  # add characters to user base variable
        if el == ':':
            break  # break at selected character
    user = user_[:-1]  # get username from user base variable

    user_gap = len(user_)
    db_url = db_url[user_gap:]  # reassign database url value to string minus username

    password_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        password_ += el  # add characters to password base variable
        if el == '@':
            break  # break at selected character
    password = password_[:-1]  # get password from password base variable

    password_gap = len(password_)
    db_url = db_url[password_gap:]  # reassign database url value to string minus password

    host_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        host_ += el  # add characters to password base variable
        if el == ':':
            break  # break at selected character
    host = host_[:-1]  # get password from password base variable

    host_gap = len(host_)
    db_url = db_url[host_gap:]  # reassign database url value to string minus host

    port_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        port_ += el  # add characters to password base variable
        if el == '/':
            break  # break at selected character
    port = port_[:-1]  # get password from password base variable

    port_gap = len(port_)
    db_name = db_url[port_gap:]  # database name value is the string of database value minus host port

    return dict(user=user, password=password, host=host, port=port, name=db_name)


dummy_db_url_1 = 'postgres://mydatabaseuser:mypassword@127.0.0.1:5432/mydatabase'
dummy_db_url_2 = 'postgres://USER:PASSWORD@HOST:PORT/NAME'
print(django_heroku_db_url_postgres_parser(dummy_db_url_1))
# {'user': 'mydatabaseuser', 'password': 'mypassword', 'host': '127.0.0.1', 'port': '5432', 'name': 'mydatabase'}
print(django_heroku_db_url_postgres_parser(dummy_db_url_2))
# {'user': 'USER', 'password': 'PASSWORD', 'host': 'HOST', 'port': 'PORT', 'name': 'NAME'}
