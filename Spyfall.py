from random import randint
jogo = [['Aeroporto', ['Piloto', 'Co-Piloto', 'Aeromoça', 'Passageiro', 'Mecânico', 'Segurança', 'Vip']],
          ['Shopping', ['Vendedor', 'Segurança', 'Comprador', 'Faxineiro', 'Atendente', 'Administrador', 'Manobrista']],
          ['Banco', ['Caixa', 'Segurança', 'Cliente', 'Analista Financeiro', 'Gerente PJ', 'Gerente PF', 'Telemarketing']],
          ['Cassino', ['Crupier', 'Jogador', 'Segurança', 'Técnico de Máquinas', 'Caixa', 'Bartender', 'iretor de Jogos']],
          ['Circo', ['Malabarista', 'Domador', 'Palhaço', 'Contorcionista', 'Mágico', 'Equilibrista', 'Atirador de Facas']],
          ['Spa', ['Massagista', 'Manicure', 'Nutricionista', 'Esteticista', 'Cliente', 'Maquiador', 'Recepcionsita']],
          ['Hospital', ['Médico', 'Enfermeira', 'Cirurgião', 'Recepcionista', 'Técnico de Raio-X', 'Paciente', 'Almoxarife']],
          ['Hotel', ['Hóspede', 'Cozinheiro', 'Recepcionista', 'Ascensorista', 'Carregador de Malas', 'Concierge', 'Porteiro']],
          ['Escola', ['Professor', 'Aluno', 'Diretor', 'Coordenador', 'Inspetor', 'Cozinheira', 'Zelador']],
          ['Supermercado', ['Caixa', 'Estoquista', 'Gerente', 'Auxiliar de Caixa', 'Padeiro', 'Açogueiro', 'Promoter']],
          ['Cruzeiro', ['Capitão', 'Marinheiro', 'Comissário', 'Tripulante', 'Músico', 'Cozinheiro', 'Mecânico']],
          ['Zoológico', ['Zelador', 'Tratador', 'Visitante', 'Atendente de Bilheteria', 'Segurança', 'Guia', 'Biólogo']],
          ['Trem', ['Maquinista', 'Passageiro', 'Controlador de Acesso', 'Ambulante', 'Manobrista', 'Mecânico', 'Catador de Bilhete']],
          ['Restaurante', ['Cozinheiro', 'Chef', 'Garçon', 'Cliente', 'Recepcionista', 'Barman', 'Caixa']]]

local = randint(0, len(jogo)-1)
jogadores = int(input('Quantos jogadores? (3-8) '))

sorteador = list()

while True:
    n = randint(0, 6)
    if n not in sorteador:
        sorteador.append(n)
    if len(sorteador) == jogadores-1:
        break

prof = list()
prof.append('Espião')
for c in sorteador:
    prof.append(jogo[local][1][c])
print(jogo[local][0])
contador = 1
while True:
    if len(prof) > 1:
        n = randint(0, len(prof)-1)
        print(f'Jogador {contador} => {prof[n]}')
        contador += 1
        prof.pop(n)
    elif len(prof) == 1:
        print(f'Jogador {contador} => {prof[0]}')
        prof.pop(0)
    if len(prof) == 0:
        break

