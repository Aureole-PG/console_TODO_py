import Client
clients = 'paul,Dayana,'

def _add_comma():
    global clients
    clients += ','


def list_clients():
    print(clients)


def create_client(client_name):
    global clients
    clients += client_name
    _add_comma()


def _update_client(client_name):
    global clients

    if client_name in clients:
        update_client_name = input('Enter new name ')
        clients = clients.replace(client_name + ',', update_client_name)
    else:
        print('User not exist')


def _delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client not exist')


def _get_client():
    return input('Enter client name ')


def print_welcome():
    print('crud')
    print('press [ C ] to create client')
    print('press [ R ] to read client')
    print('press [ U ] to update client')
    print('press [ D ] to delete client')
    print('press [ E ] to Exit')


if __name__ == '__main__':
    print_welcome()
    op = input()
    op = op.upper()
    if op == 'C':
        client_name = _get_client()
        Client.create_client(client_name)
        Client.list_clients()
    elif op == 'R':
        list_clients()
    elif op == 'U':
        client_name = _get_client()
        _update_client(client_name)
    elif op == 'D':
        pass
    # list_clients()
    # create_client('uwu')
    # list_clients()
