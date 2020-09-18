def django_heroku_db_url_postgres_parser(database_url):
    db_url = database_url[11:]  # remove "postgres://" from database url

    user_ = ""  # initialize user base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        user_ += el  # add characters to user base variable
        if el == ':':
            break  # break at selected character
    user = user_[:-1]  # get user from user base variable

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

    host_ = ""  # initialize host base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        host_ += el  # add characters to host base variable
        if el == ':':
            break  # break at selected character
    host = host_[:-1]  # get host from host base variable

    host_gap = len(host_)
    db_url = db_url[host_gap:]  # reassign database url value to string minus host

    port_ = ""  # initialize port base variable to empty string
    for el in db_url:  # iterate through trimmed database url
        port_ += el  # add characters to port base variable
        if el == '/':
            break  # break at selected character
    port = port_[:-1]  # get port from port base variable

    port_gap = len(port_)
    db_name = db_url[port_gap:]  # database name value is the string of database value minus port

    return dict(user=user, password=password, host=host, port=port, name=db_name)
