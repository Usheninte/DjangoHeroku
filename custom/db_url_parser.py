def django_heroku_db_url_postgres_parser(database_url):
    db_url = database_url[11:]  # remove "postgres://" from database url
    # print(db_url)

    user_ = ""  # initialize user base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        user_ += el  # add characters to user base variable
        if el == ':':
            break  # break at semicolon character
    user = user_[:-1]  # get username from user base variable

    # print(user)  # USER

    user_gap = len(user_)
    db_url = db_url[user_gap:]  # reassign database url value to string minus with username
    # print(db_url)

    password_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        password_ += el  # add characters to password base variable
        if el == '@':
            break  # break at semicolon character
    password = password_[:-1]  # get password from password base variable

    # print(password)  # PASSWORD

    password_gap = len(password_)
    db_url = db_url[password_gap:]
    # print(db_url)

    host_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        host_ += el  # add characters to password base variable
        if el == ':':
            break  # break at semicolon character
    host = host_[:-1]  # get password from password base variable

    # print(host)  # HOST

    host_gap = len(host_)
    db_url = db_url[host_gap:]
    # print(db_url)

    port_ = ""  # initialize password base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        port_ += el  # add characters to password base variable
        if el == '/':
            break  # break at semicolon character
    port = port_[:-1]  # get password from password base variable

    # print(port)  # PORT

    port_gap = len(port_)
    db_name = db_url[port_gap:]

    # print(db_name)  # NAME

    return dict(user=user, password=password, host=host, port=port, name=db_name)


dummy_db_url_1 = 'postgres://mydatabaseuser:mypassword@127.0.0.1:5432/mydatabase'
dummy_db_url_2 = 'postgres://USER:PASSWORD@HOST:PORT/NAME'
print(django_heroku_db_url_postgres_parser(dummy_db_url_1))
print(django_heroku_db_url_postgres_parser(dummy_db_url_2))
