class Client:
    clients = 'paul,'

    def list_clients(self):
        print(clients)

    def create_client(self, client_name):
        clients = self.clients
        clients += client_name+','
