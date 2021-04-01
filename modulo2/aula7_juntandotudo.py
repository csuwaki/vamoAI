class Restaurante:
    def __init__(self, cardapio, funcionamento, nome, pagamento):
        self.cardapio = cardapio
        self.funcionamento = funcionamento
      
    def mostra_info(self):
        print(f'Nome do Restaurante: {self.nome} \nCardápio: {self.cardapio} \nFuncionamento: {self.funcionamento} \nFormas de Pagamento: {self.pagamento}')
    
    def pula_linha(self):
        print('-='*30)

class Outback(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, pagamento):
        super().__init__(cardapio, funcionamento, nome, pagamento)
        self.nome = nome
        self.pagamento = pagamento

class Sukiya(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, pagamento):
        super().__init__(cardapio, funcionamento, nome, pagamento)
        self.nome = nome
        self.pagamento = pagamento

class Burgerking(Restaurante):
    def __init__(self, cardapio, funcionamento, nome, pagamento):
        super().__init__(cardapio, funcionamento)
        self.nome = nome
        self.pagamento = pagamento

class Pessoa:
    def __init__(self, nome, rg, cpf, telefone):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone

    def perfil(self):
        self.perfil = perfil

    def entrega(self, entrega):
        self.entrega = entrega
        return self.entrega

    def pula_linha(self):
        print('-='*30)
   
    def status(self):
        return status

class Entregador(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, avaliacao):
        super().__init__(nome, rg, cpf, telefone)
        self.avaliacao = avaliacao

    def entrega(self, entrega):
        self.entrega = entrega 
        print(f'Boa noite, {self.nome}. Você tem {self.entrega} minutos para finalizar a entrega!')

    def perfil(self):
        print(f'Nome do entregador: {self.nome} \nRG: {self.rg} \nCPF: {self.cpf} \nTelefone: {self.telefone} \nAvaliação: {self.avaliacao} estrelas.')

    def status(self):
        print("O entregador está chegando... \nPedido entregue. Não se esqueça de deixar uma avaliação!")

class Cliente(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, cupons):
        super().__init__(nome, rg, cpf, telefone)
        self.cupons = cupons
    
    def perfil(self):
        print(f'Cliente: {self.nome} \nRG: {self.rg} \nCPF: {self.cpf} \nTelefone: {self.telefone} \nCupons: {self.cupons} cupons disponiveis.')
      
    def entrega(self, entrega):
        self.entrega = entrega 
        print(f'Boa noite, {self.nome}! Prato está sendo preparado. Você receberá seu pedido em até {self.entrega} minutos!')

    def status(self):
        print("Pedido recebido! \nAguardando restaurante aceitar... ")

class Proprietario(Pessoa):
    def __init__(self, nome, rg, cpf, telefone, cnpj):
        super().__init__(nome, rg, cpf, telefone)
        self.cnpj = cnpj
    
    def entrega(self, entrega):
        self.entrega = entrega
        print(f'Boa noite, {self.nome}, seu restaurante acabou de receber um pedido! Você terá 40 minutos para preparar o pedido e adicionalmente {self.entrega} minutos para entregá-lo!')

    def perfil(self):
        print(f'Nome do proprietário (a): {self.nome} \nRG: {self.rg} \nCPF: {self.cpf} \nTelefone: {self.telefone}, \nCNPJ: {self.cnpj}.')

outback = Outback({'seg': 'costela', 'ter': 'cebola', 'qua': 'batata frita', 'qui': 'pizza', 'sex': 'lasanha', 'sab': 'churrasco', 'dom': 'macarronada'}, 'Seg à dom das 18 às 0h', 'Outback Steakhouse', 'Dinheiro, cartão de crédito e débito')
outback.mostra_info()
outback.pula_linha()


cliente = Cliente('Joao', '12.345.678-9', "213.456.789-0", "1234-5678", 3)
cliente.perfil()
cliente.status()
cliente.pula_linha()

prop = Proprietario('Caroline', '12.345.678-9', "213.456.789-0", "1234-5678", "123456987/0000")
prop.perfil()
prop.entrega('40')
prop.pula_linha()

cliente.entrega('40')
cliente.pula_linha()

entregador = Entregador('José', '12.345.678-9', "213.456.789-0", "1234-5678", 5)
entregador.perfil()
entregador.entrega('40')
entregador.pula_linha()
entregador.status()