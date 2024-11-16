import random

# Itens da loja
itens_loja = {
    "Poção de Cura": {"preço": 20.00, "estoque": 10},
    "Espada": {"preço": 50.00, "estoque": 5},
    "Escudo": {"preço": 30.00, "estoque": 5},
}

# Classe Personagem
class Personagem:
    def __init__(self, nome, tipo, vida, ataque, defesa, arma, tipo_ataque="físico"):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.arma = arma
        self.tipo_ataque = tipo_ataque
        self.inventario = []
        self.dinheiro = 100  # Dinheiro inicial

    def atacar(self, oponente):
        dano = max(0, self.ataque - oponente.defesa)
        oponente.vida -= dano
        print(f"{self.nome} ataca {oponente.nome} e causa {dano} de dano!")
        if oponente.vida <= 0:
            print(f"{oponente.nome} foi derrotado!")

    def usar_item(self, item):
        if item in self.inventario and item == "Poção de Cura":
            cura = random.randint(15, 30)
            self.vida += cura
            self.inventario.remove(item)
            print(f"{self.nome} usou {item} e recuperou {cura} de vida!")
        else:
            print(f"Item inválido ou não disponível no inventário.")

    def exibir_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"  Tipo: {self.tipo}")
        print(f"  Vida: {self.vida}")
        print(f"  Ataque: {self.ataque}")
        print(f"  Defesa: {self.defesa}")
        print(f"  Dinheiro: {self.dinheiro}")
        print(f"  Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}")

# Funções específicas para as novas classes
def habilidade_especial(jogador, inimigo):
    if jogador.tipo == "Mago Oculto":
        dano_magico = jogador.ataque
        inimigo.vida -= dano_magico
        jogador.vida -= 6  # O mago toma dano ao usar magia
        print(f"{jogador.nome} usa magia! Causa {dano_magico} de dano, mas perde 6 de vida.")
    elif jogador.tipo == "Ladrão":
        if inimigo.inventario:
            item_roubado = inimigo.inventario.pop()
            jogador.inventario.append(item_roubado)
            print(f"{jogador.nome} roubou {item_roubado} de {inimigo.nome}!")
        else:
            print(f"{inimigo.nome} não tem nada para ser roubado!")
    elif jogador.tipo == "Cristão" and inimigo.tipo == "Mago":
        inimigo.vida = 0  # Queima o mago automaticamente
        print(f"{jogador.nome} invoca a ira divina e queima {inimigo.nome} instantaneamente!")

# Função da Loja
def loja(jogador):
    print("\n=== Bem-vindo à Loja ===")
    print("Itens disponíveis:")
    for item, detalhes in itens_loja.items():
        print(f"{item}: R$ {detalhes['preço']} (Estoque: {detalhes['estoque']})")
    
    while True:
        print("\nEscolha uma ação:")
        print("1. Comprar item")
        print("2. Sair da loja")
        escolha = int(input("Digite o número da ação: "))

        if escolha == 1:
            item_escolhido = input("Digite o nome do item que deseja comprar: ")
            if item_escolhido not in itens_loja:
                print("Item não encontrado. Tente novamente.")
                continue
            
            quantidade = int(input("Digite a quantidade desejada: "))
            if itens_loja[item_escolhido]['estoque'] < quantidade:
                print("Estoque insuficiente. Tente novamente.")
                continue
            
            custo_total = itens_loja[item_escolhido]['preço'] * quantidade
            if jogador.dinheiro < custo_total:
                print("Dinheiro insuficiente. Tente novamente.")
                continue

            # Atualiza o jogador e a loja
            jogador.dinheiro -= custo_total
            for _ in range(quantidade):
                jogador.inventario.append(item_escolhido)
            itens_loja[item_escolhido]['estoque'] -= quantidade
            print(f"Você comprou {quantidade}x {item_escolhido}.")
        elif escolha == 2:
            print("Você saiu da loja.")
            break
        else:
            print("Escolha inválida.")

# Funções Auxiliares
def criar_personagem():
    print("Escolha uma classe:")
    print("1. Cavaleiro (100 vida, 50 ataque, 50 defesa, arma: Espada)")
    print("2. Mago (80 vida, 120 ataque mágico, 20 defesa, arma: Cajado/Magias)")
    print("3. Bárbaro (120 vida, 70 ataque, 30 defesa, arma: Machado)")
    print("4. Mago Oculto (60 vida, 150 ataque mágico, perde 6 vida por magia, arma: Magias)")
    print("5. Ladrão (90 vida, 40 ataque, 40 defesa, arma: Adaga, rouba do inimigo)")
    print("6. Cristão (110 vida, 30 ataque, 50 defesa, arma: Fé, queima magos)")

    escolha = int(input("Digite o número da classe desejada: "))
    nome = input("Digite o nome do seu personagem: ")

    if escolha == 1:
        return Personagem(nome, "Cavaleiro", 100, 50, 50, "Espada")
    elif escolha == 2:
        return Personagem(nome, "Mago", 80, 120, 20, "Cajado/Magias", "mágico")
    elif escolha == 3:
        return Personagem(nome, "Bárbaro", 120, 70, 30, "Machado")
    elif escolha == 4:
        return Personagem(nome, "Mago Oculto", 60, 150, 10, "Magias", "mágico")
    elif escolha == 5:
        return Personagem(nome, "Ladrão", 90, 40, 40, "Adaga")
    elif escolha == 6:
        return Personagem(nome, "Cristão", 110, 30, 50, "Fé")
    else:
        print("Escolha inválida.")
        return criar_personagem()

def criar_inimigo():
    inimigos = [
        Personagem("Goblin", "Inimigo", 50, 15, 5, "Adaga"),
        Personagem("Orc", "Inimigo", 80, 20, 10, "Machado"),
        Personagem("Dragão Bebê", "Inimigo", 120, 30, 20, "Fogo"),
        Personagem("Mago das Trevas", "Mago", 70, 100, 15, "Magias")
    ]
    return random.choice(inimigos)

def batalha(jogador, inimigo):
    print(f"\nA batalha começa entre {jogador.nome} e {inimigo.nome}!")
    jogador.exibir_status()
    print(f"{inimigo.nome} (Inimigo): {inimigo.vida} vida, {inimigo.ataque} ataque, {inimigo.defesa} defesa.")

    while jogador.vida > 0 and inimigo.vida > 0:
        print("\nEscolha uma ação:")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Usar habilidade especial")
        print("4. Fugir")

        escolha = int(input("Digite o número da ação: "))
        if escolha == 1:
            jogador.atacar(inimigo)
            if inimigo.vida > 0:
                inimigo.atacar(jogador)  # Agora o inimigo ataca após o jogador
        elif escolha == 2:
            jogador.exibir_status()
            item = input("Digite o nome do item que deseja usar: ")
            jogador.usar_item(item)
            if inimigo.vida > 0:  # Inimigo ataca após o uso do item
                inimigo.atacar(jogador)
        elif escolha == 3:
            habilidade_especial(jogador, inimigo)
            if inimigo.vida > 0:  # Inimigo ataca após o uso da habilidade especial
                inimigo.atacar(jogador)
        elif escolha == 4:
            print("Você fugiu da batalha!")
            break
        else:
            print("Escolha inválida.")

    if jogador.vida <= 0:
        print(f"{jogador.nome} foi derrotado!")
    elif inimigo.vida <= 0:
        print(f"{jogador.nome} venceu a batalha!")


# Jogo
def main():
    print("=== Bem-vindo ao Jogo de RPG ===")
    jogador = criar_personagem()

    while True:
        print("\nEscolha uma ação:")
        print("1. Ir para a batalha")
        print("2. Visitar a loja")
        print("3. Exibir status")
        print("4. Sair do jogo")

        escolha = int(input("Digite o número da ação: "))
        if escolha == 1:
            inimigo = criar_inimigo()
            batalha(jogador, inimigo)
        elif escolha == 2:
            loja(jogador)
        elif escolha == 3:
            jogador.exibir_status()
        elif escolha == 4:
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Escolha inválida.")

if __name__ == "__main__":
    main()
