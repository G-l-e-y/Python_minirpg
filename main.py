from random import randint

lista_npcs = []

player = {
    'nome': 'Zelda',
    'level': 1,
    'xp': 0,
    'xp_MAX': 28,
    'vida': 50,
    'vida_max': 50,
    'dano': 10,
}


def criar_npc(level):

    novo_npc = {
        'nome': f'Monstro #{level}',
        'level': level,
        'dano': 5 * level, 
        'vida': 20 * level,
        'vida_max':20 * level,
        'xp': 7 * level,
    }
    
    return novo_npc


def gerar_npcs(n_npcs):

    for x in range(n_npcs):
        npc = criar_npc(x + 1)
        lista_npcs.append(npc)


def exibir_npc(npc):
    for npc in lista_npcs:
        exibir_npc(npc)


def exibir_npcs(npc):
        print(
            f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // Vida: {npc['vida']} // XP: {npc['xp']}"
        )


def exibir_player():
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // Vida: {player['vida']}/{player['vida_max']} // XP: {player['xp']}/{player['xp_MAX']}"        
    )


def reset_player():
    player['vida'] = player['vida_max']

def reset_npc(npc):
    npc['vida'] = npc['vida_max']

def level_up():
    if player['xp'] >= player['xp_MAX']:
        player['level'] += 1
        player['xp'] = 0
        player['xp_MAX'] *= 2
        player['vida_max'] += 20


def iniciar_batalha(npc):
    while player['vida'] > 0 and npc['vida'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)


    if player['vida'] > 0:
        print(f"{player['nome']} venceu a batalha e ganhou {npc['xp']} de Expêriencia!")
        player['xp'] += npc['xp']
        exibir_player()
    else:
        print(f"O {npc['nome']} venceu a batalha!!")
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)


def atacar_npc(npc):
    npc['vida'] -= player['dano']


def atacar_player(npc):
    player['vida'] -= npc['dano']


def exibir_info_batalha(npc):
    print(f"Player HP: {player['vida']}/{player['vida_max']}")
    print(f"NPC: {npc['nome']}: {npc['vida']}/{npc['vida_max']}")
    print('---------------------------------\n')


gerar_npcs(5)

npc_selecionado = lista_npcs[0]
iniciar_batalha(npc_selecionado)

exibir_player()
