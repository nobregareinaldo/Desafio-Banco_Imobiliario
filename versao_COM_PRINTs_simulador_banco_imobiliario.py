import json
from pathlib import Path
import configparser as cp
import time
import random
from os import system
from datetime import datetime
import utilities

# Exemplo de chamada por linha de comando
# python simulador_banco_imobiliario.py

# Rotulando a janela de execucao do programa simulador_banco_imobiliario.py
system("title " + "Desafio BrasilPrev x Capitani - por Reinaldo Nobrega")

# Controle de tempo de execucao do programa
start_t = time.time()
start = time.ctime()

def configurar_partida():
    """
    Carregar a configuracao inicial do jogo atribuindo saldo, carregando propriedades e parametros de simulacao
    Retorna os parametros atribuidos no arquivo de configuracao 'application.cfg'.
    Jogadores por perfil, propriedades, quantidade de simulacoes, limite de rodadas e bonus.
    """
    path = Path(__file__).parent.absolute() / "application.cfg"

    # Configuracao properties
    props = cp.RawConfigParser()
    props.read(path)

    # Atribuindo os parametros de configuracao de perfis aos jogadores
    perfil = "perfis"
    saldo_inicial = props.get(perfil, "saldo_inicial")
    impulsivo = json.loads(props.get(perfil, "perfil_impulsivo"))
    exigente = json.loads(props.get(perfil, "perfil_exigente"))
    cauteloso = json.loads(props.get(perfil, "perfil_cauteloso"))
    aleatorio = json.loads(props.get(perfil, "perfil_aleatorio"))

    # Inicializando o saldo inicial dos jogadores
    impulsivo['saldo']=saldo_inicial
    exigente['saldo']=saldo_inicial
    cauteloso['saldo']=saldo_inicial
    aleatorio['saldo']=saldo_inicial

    # Definindo a sequencia de turno entre os jogadores
    ordem = [1,2,3,4]
    random.shuffle(ordem)
    # Distribuindo a sequencia de turno para os jogadores
    impulsivo['turno']=ordem[0]
    exigente['turno']=ordem[1]
    cauteloso['turno']=ordem[2]
    aleatorio['turno']=ordem[3]

    # Atribuindo os parametros de configuracao de simulacao
    simula = "simulacoes"
    qtd_simula = props.get(simula, "qtd_simulacoes")
    max_rodadas = props.get(simula, "max_rodadas")
    bonus = props.get(simula,"bonus_volta_completa")

    # Atribuindo os parametros de propriedades
    propriedades = [
        {'posicao':1,'desc':'Av. 9 de julho','valor_venda':90,'valor_aluguel':10,'disponivel':True,'dono':None},
        {'posicao':2,'desc':'Avenida Paulista','valor_venda':90,'valor_aluguel':10,'disponivel':True,'dono':None},
        {'posicao':3,'desc':'Rua 25 de marco','valor_venda':90,'valor_aluguel':10,'disponivel':True,'dono':None},
        {'posicao':4,'desc':'Av. Rio Branco','valor_venda':90,'valor_aluguel':10,'disponivel':True,'dono':None},
        {'posicao':5,'desc':'Av. do Estado','valor_venda':110,'valor_aluguel':20,'disponivel':True,'dono':None},
        {'posicao':6,'desc':'Rua Jose Paulino','valor_venda':110,'valor_aluguel':20,'disponivel':True,'dono':None},
        {'posicao':7,'desc':'Av. Reboucas','valor_venda':110,'valor_aluguel':20,'disponivel':True,'dono':None},
        {'posicao':8,'desc':'Av. Santo Amaro','valor_venda':110,'valor_aluguel':20,'disponivel':True,'dono':None},
        {'posicao':9,'desc':'Rua da Consolacao','valor_venda':140,'valor_aluguel':30,'disponivel':True,'dono':None},
        {'posicao':10,'desc':'Av. Morumbi','valor_venda':140,'valor_aluguel':30,'disponivel':True,'dono':None},
        {'posicao':11,'desc':'Av. Higienopolis','valor_venda':140,'valor_aluguel':30,'disponivel':True,'dono':None},
        {'posicao':12,'desc':'Av. Sao Joao','valor_venda':140,'valor_aluguel':30,'disponivel':True,'dono':None},
        {'posicao':13,'desc':'Av. Ipiranga','valor_venda':170,'valor_aluguel':50,'disponivel':True,'dono':None},
        {'posicao':14,'desc':'Av. Brigadeiro Faria Lima','valor_venda':170,'valor_aluguel':50,'disponivel':True,'dono':None},
        {'posicao':15,'desc':'Av. Paulista','valor_venda':170,'valor_aluguel':50,'disponivel':True,'dono':None},
        {'posicao':16,'desc':'Rua Augusta','valor_venda':170,'valor_aluguel':50,'disponivel':True,'dono':None},
        {'posicao':17,'desc':'Rua Santa Ifigenia','valor_venda':200,'valor_aluguel':80,'disponivel':True,'dono':None},
        {'posicao':18,'desc':'Rua Oscar Freire','valor_venda':200,'valor_aluguel':80,'disponivel':True,'dono':None},
        {'posicao':19,'desc':'Av. Ibirapuera','valor_venda':200,'valor_aluguel':80,'disponivel':True,'dono':None},
        {'posicao':20,'desc':'Rua dos Pinheiros','valor_venda':200,'valor_aluguel':80,'disponivel':True,'dono':None}
    ]

    # Ajustando tipagem de dados dos jogadores
    impulsivo["compra"] = int(impulsivo["compra"])
    impulsivo["aluguel_min"] = int(impulsivo["aluguel_min"])
    impulsivo["saldo_min"] = int(impulsivo["saldo_min"])
    impulsivo["posicao"] = int(impulsivo["posicao"])
    impulsivo["saldo"] = int(impulsivo["saldo"])
    impulsivo["turno"] = int(impulsivo["turno"])

    exigente["compra"] = int(exigente["compra"])
    exigente["aluguel_min"] = int(exigente["aluguel_min"])
    exigente["saldo_min"] = int(exigente["saldo_min"])
    exigente["posicao"] = int(exigente["posicao"])
    exigente["saldo"] = int(exigente["saldo"])
    exigente["turno"] = int(exigente["turno"])

    cauteloso["compra"] = int(cauteloso["compra"])
    cauteloso["aluguel_min"] = int(cauteloso["aluguel_min"])
    cauteloso["saldo_min"] = int(cauteloso["saldo_min"])
    cauteloso["posicao"] = int(cauteloso["posicao"])
    cauteloso["saldo"] = int(cauteloso["saldo"])
    cauteloso["turno"] = int(cauteloso["turno"])

    aleatorio["compra"] = int(aleatorio["compra"])
    aleatorio["aluguel_min"] = int(aleatorio["aluguel_min"])
    aleatorio["saldo_min"] = int(aleatorio["saldo_min"])
    aleatorio["posicao"] = int(aleatorio["posicao"])
    aleatorio["saldo"] = int(aleatorio["saldo"])
    aleatorio["turno"] = int(aleatorio["turno"])

    return impulsivo, exigente, cauteloso, aleatorio, qtd_simula, max_rodadas, bonus, propriedades

def iniciar_partida():
    """
    Inicializar as partidas atribuindo os valores default para jogadores, propriedades e variaveis de sistema.
    Retorna os valores carregados pela funcao configurar_partida() e inicializa a variavel timeout.
    """
    # Inicializando controle de partida encerrada por timeout
    timeout = True
    # Configurando a partida
    configurar = configurar_partida()
    
    return configurar, timeout

def jogar_dado():
    """
    Simular o arremesso de um dado equiprovavel de seis faces.
    Retorna o valor da face sorteada.
    """
    return random.randint(1,6)

def main():
    # O log de execucao sera armazenado no diretorio abaixo
    log = 'C:\\Users\\Usuario\\Desktop\\BrasilPrev\\build\\'
    now = datetime.now()
    data_hora = now.strftime("%Y%m%d-%H%M%S")

    print("\nInicializando Desafio - Simulacoes Banco Imobiliario ...")
    print("Desenvolvido por Reinaldo Nobrega - https://www.linkedin.com/in/reinaldo-nobrega/ \n")
    msg = 'Inicializando Desafio - Simulacoes Banco Imobiliario ...\nDesenvolvido por Reinaldo Nobrega - https://www.linkedin.com/in/reinaldo-nobrega/'
    
    print('#########################################################################')
    print('Simulando turnos ...')
    msg +='\n#########################################################################\nSimulando turnos ...'

    # Iniciando a primeira partida
    iniciar = iniciar_partida()
    impulsivo = iniciar[0][0]
    exigente = iniciar[0][1]
    cauteloso = iniciar[0][2]
    aleatorio = iniciar[0][3]
    qtd_simula = int(iniciar[0][4])
    max_rodadas = int(iniciar[0][5])
    bonus = int(iniciar[0][6])
    propriedades = iniciar[0][7]
    timeout = iniciar[1]

    # Inicializando totalizadores de execucao
    partida = 0
    total_turnos = 0
    simulacao = 0
    qtd_timeout = 0
    impulsivo_perdeu = 0
    exigente_perdeu = 0
    cauteloso_perdeu = 0
    aleatorio_perdeu = 0
    impulsivo_ganhou=0
    exigente_ganhou=0
    cauteloso_ganhou=0
    aleatorio_ganhou=0

    # Processamento das simulacoes e respectivas turnos
    while simulacao < qtd_simula:
        while partida < max_rodadas:
            # Checando a ordem de turnos dos jogadores
            for turno in range(1,5):
                # Tratamentos para o jogador IMPULSIVO
                if impulsivo['turno'] == turno and impulsivo['saldo'] > 0 and impulsivo['jogar'] == "True":
                    dado = jogar_dado()
                    impulsivo['posicao'] += dado

                    print(f"IMPULSIVO jogou o dado e tirou {dado}")
                    print(f"A posicao do IMPULSIVO eh {impulsivo['posicao']}"
                    
                    if impulsivo['posicao'] > 20:
                        print("\nIMPULSIVO ganhou bonus!")
                        impulsivo['saldo'] += bonus
                        print(f"Saldo do IMPULSIVO eh {impulsivo['saldo']}\n")
                        impulsivo['posicao'] -= 20

                    for propriedade in propriedades:
                        if impulsivo["posicao"] == propriedade["posicao"]:
                            print("IMPULSIVO entrou na propriedade ", propriedade['desc'])
                            
                            if propriedade["disponivel"] == True:
                                print(f"\n*** Propriedade {propriedade['desc']} disponivel *****")

                                if propriedade['valor_venda'] <= impulsivo['saldo']:
                                    impulsivo['saldo'] -= propriedade['valor_venda']
                                    propriedade["disponivel"] = False
                                    propriedade["dono"] = "IMPULSIVO"
                                    print(f'Novo dono... {propriedade["dono"]}')
                                    print('IMPULSIVO comprou a propriedade ', propriedade["desc"])
                                    print(f"Saldo do IMPULSIVO eh {impulsivo['saldo']}\n")
                                    
                            else:
                                impulsivo['saldo'] -= propriedade['valor_aluguel']
                                if propriedade['dono'] == 'exigente':
                                    exigente['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'cauteloso':
                                    cauteloso['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'aleatorio':
                                    aleatorio['saldo'] += propriedade['valor_aluguel']
                            
                            if impulsivo['saldo'] <= 0:
                                print("Jogador IMPULSIVO faliu: ",impulsivo['saldo'])
                                impulsivo['jogar'] = False
                                impulsivo_perdeu += 1
                            break

                if impulsivo['jogar'] == False:
                    for propriedade in propriedades:
                        if propriedade['dono'] == 'impulsivo':
                           propriedade['dono'] = None
                           propriedade['disponivel'] = True
                           print(f"### IMPULSIVO devolveu a propriedade {propriedade['desc']} ###")    

                if exigente['turno'] == turno and exigente['saldo'] > 0 and exigente['jogar'] == "True":
                    dado = jogar_dado()
                    exigente['posicao'] += dado

                    print(f"EXIGENTE jogou o dado e tirou {dado}")
                    print(f"A posicao do EXIGENTE eh {exigente['posicao']}")

                    if exigente['posicao'] > 20:
                        print("\nEXIGENTE ganhou bonus!")
                        exigente['saldo'] += bonus
                        print(f"Saldo do EXIGENTE eh {exigente['saldo']}\n")
                        exigente['posicao'] -= 20

                    for propriedade in propriedades:                        
                        if exigente["posicao"] == propriedade["posicao"]:
                            print("EXIGENTE caiu na propriedade ", propriedade['desc'])
                            
                            if propriedade["disponivel"] == True:
                                print(f"\n*** Propriedade {propriedade['desc']} disponivel *****")

                                if propriedade['valor_venda'] <= exigente['saldo'] and propriedade['valor_aluguel'] > exigente['aluguel_min']:
                                    exigente['saldo'] -= propriedade['valor_venda']
                                    propriedade["disponivel"] = False
                                    propriedade["dono"] = "exigente"
                                    print(f'Novo dono... {propriedade["dono"]}')
                                    print('EXIGENTE comprou a propriedade ', propriedade["desc"])
                                    print(f"Saldo do EXIGENTE eh {exigente['saldo']}\n")
                                    
                            else:
                                exigente['saldo'] -= propriedade['valor_aluguel']
                                if propriedade['dono'] == 'impulsivo':
                                    impulsivo['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'cauteloso':
                                    cauteloso['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'aleatorio':
                                    aleatorio['saldo'] += propriedade['valor_aluguel']
                            
                            if exigente['saldo'] <= 0:
                                print("Jogador EXIGENTE faliu: ",exigente['saldo'])
                                exigente['jogar'] = False
                                exigente_perdeu += 1
                            break

                if exigente['jogar'] == False:
                    for propriedade in propriedades:
                        if propriedade['dono'] == 'exigente':
                           propriedade['dono'] = None
                           propriedade['disponivel'] = True
                           print(f"### EXIGENTE devolveu a propriedade {propriedade['desc']} ###")

                if cauteloso['turno'] == turno and cauteloso['saldo'] > 0 and cauteloso['jogar'] == "True":
                    dado = jogar_dado()
                    cauteloso['posicao'] += dado

                    print(f"CAUTELOSO jogou o dado e tirou {dado}")
                    print(f"A posicao do CAUTELOSO eh {cauteloso['posicao']}")

                    if cauteloso['posicao'] > 20:
                        print("\nCAUTELOSO ganhou bonus!")
                        cauteloso['saldo'] += bonus
                        print(f"Saldo do CAUTELOSO eh {cauteloso['saldo']}\n")
                        cauteloso['posicao'] -= 20

                    for propriedade in propriedades:    
                        if cauteloso["posicao"] == propriedade["posicao"]:
                            print("CAUTELOSO caiu na propriedade ", propriedade['desc'])
                            
                            if propriedade["disponivel"] == True:
                                print(f"\n*** Propriedade {propriedade['desc']} disponivel *****")

                                if propriedade['valor_venda'] <= (cauteloso['saldo'] - cauteloso['saldo_min']):
                                    cauteloso['saldo'] -= propriedade['valor_venda']
                                    propriedade["disponivel"] = False
                                    propriedade["dono"] = "cauteloso"
                                    print(f'Novo dono... {propriedade["dono"]}')
                                    print('CAUTELOSO comprou a propriedade ', propriedade["desc"])
                                    print(f"Saldo do CAUTELOSO eh {cauteloso['saldo']}\n")
                                else:
                                    diferenca = propriedade['valor_venda'] - cauteloso['saldo'] + cauteloso['saldo_min']
                                    print(f'CAUTELOSO nao tem reserva suficiente ... Faltou {diferenca} para comprar dentro da margem')
                            else:
                                cauteloso['saldo'] -= propriedade['valor_aluguel']
                                if propriedade['dono'] == 'impulsivo':
                                    impulsivo['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'exigente':
                                    exigente['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'aleatorio':
                                    aleatorio['saldo'] += propriedade['valor_aluguel']
                                
                            if cauteloso['saldo'] <= 0:
                                print("Jogador CAUTELOSO faliu: ",cauteloso['saldo'])
                                cauteloso['jogar'] = False
                                cauteloso_perdeu += 1
                            break

                if cauteloso['jogar'] == False:
                    for propriedade in propriedades:
                        if propriedade['dono'] == 'cauteloso':
                           propriedade['dono'] = None
                           propriedade['disponivel'] = True
                           print(f"### CAUTELOSO devolveu a propriedade {propriedade['desc']} ###")

                if aleatorio['turno'] == turno and aleatorio['saldo'] > 0 and aleatorio['jogar'] == "True":
                    dado = jogar_dado()
                    aleatorio['posicao'] += dado

                    print(f"ALEATORIO jogou o dado e tirou {dado}")
                    print(f"A posicao do ALEATORIO eh {aleatorio['posicao']}")

                    if aleatorio['posicao'] > 20:
                        print("\nALEATORIO ganhou bonus!")
                        aleatorio['saldo'] += bonus
                        print(f"Saldo do ALEATORIO eh {aleatorio['saldo']}\n")
                        aleatorio['posicao'] -= 20

                    for propriedade in propriedades:
                                               
                        if aleatorio["posicao"] == propriedade["posicao"]:
                            print("ALEATORIO caiu na propriedade ", propriedade['desc'])
                            
                            if propriedade["disponivel"] == True:
                                print(f"\n*** Propriedade {propriedade['desc']} disponivel *****")

                                if propriedade['valor_venda'] <= aleatorio['saldo'] and random.randint(0,1) == 1:
                                    aleatorio['saldo'] -= propriedade['valor_venda']
                                    propriedade["disponivel"] = False
                                    propriedade["dono"] = "aleatorio"
                                    print(f'Novo dono... {propriedade["dono"]}')
                                    print('ALEATORIO comprou a propriedade ', propriedade["desc"])
                                    print(f"Saldo do ALEATORIO eh {aleatorio['saldo']}\n")
                                    
                            else:
                                aleatorio['saldo'] -= propriedade['valor_aluguel']
                                if propriedade['dono'] == 'impulsivo':
                                    impulsivo['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'exigente':
                                    exigente['saldo'] += propriedade['valor_aluguel']
                                if propriedade['dono'] == 'cauteloso':
                                    aleatorio['saldo'] += propriedade['valor_aluguel']

                            if aleatorio['saldo'] <= 0:
                                print("Jogador ALEATORIO faliu: ",aleatorio['saldo'])
                                aleatorio['jogar'] = False
                                aleatorio_perdeu += 1
                            break

                if aleatorio['jogar'] == False:
                    for propriedade in propriedades:
                        if propriedade['dono'] == 'aleatorio':
                           propriedade['dono'] = None
                           propriedade['disponivel'] = True
                           print(f"### ALEATORIO devolveu a propriedade {propriedade['desc']} ###")    
            partida += 1
            total_turnos += 1
            if (impulsivo_perdeu + exigente_perdeu + cauteloso_perdeu + aleatorio_perdeu) == 3:
                print(f'Temos um vencedor na partida {partida} !!!!!!')
                if impulsivo_perdeu == 0:
                    impulsivo_ganhou += 1
                    print(f"### IMPULSIVO venceu com saldo de {impulsivo['saldo']} ###")
                if exigente_perdeu == 0:
                    exigente_ganhou += 1
                    print(f"### EXIGENTE venceu com saldo de {exigente['saldo']} ###")
                if cauteloso_perdeu == 0:
                    cauteloso_ganhou += 1
                    print(f"### CAUTELOSO venceu com saldo de {cauteloso['saldo']} ###")
                if aleatorio_perdeu == 0:
                    aleatorio_ganhou += 1
                    print(f"### ALEATORIO venceu com saldo de {aleatorio['saldo']} ###")

                # Inicializando derrotas por partida
                impulsivo_perdeu,exigente_perdeu,cauteloso_perdeu,aleatorio_perdeu=0,0,0,0
                timeout = False
                break
        simulacao += 1
        partida = 0
        
        if timeout:
            # Simulacao encerrada por time-out
            qtd_timeout += 1
            print(f'Temos um vencedor por timeout na simulacao {simulacao} !!!!!!')
            # Dicionario com o saldo dos jogadores
            saldo_jogadores = {'IMPULSIVO':impulsivo['saldo'],'EXIGENTE':exigente['saldo'],'CAUTELOSO':cauteloso['saldo'],'ALEATORIO':aleatorio['saldo']}

            # Encontrando o jogador com maior saldo
            ganhador_saldo = max(saldo_jogadores, key=saldo_jogadores.get)
            maior_saldo = max(saldo_jogadores)

            if ganhador_saldo == 'IMPULSIVO':
                impulsivo_ganhou += 1
                print(f"### IMPULSIVO venceu POR TIMEOUT com saldo de {impulsivo['saldo']} ###")
            if ganhador_saldo == 'EXIGENTE':
                exigente_ganhou += 1
                print(f"### EXIGENTE venceu POR TIMEOUT com saldo de {exigente['saldo']} ###")
            if ganhador_saldo == 1:
                cauteloso_ganhou += 1
                print(f"### CAUTELOSO venceu POR TIMEOUT com saldo de {cauteloso['saldo']} ###")
            if ganhador_saldo == 1:
                aleatorio_ganhou += 1
                print(f"### ALEATORIO venceu POR TIMEOUT com saldo de {aleatorio['saldo']} ###")
        
        # Iniciando nova partida
        iniciar = iniciar_partida()
        impulsivo = iniciar[0][0]
        exigente = iniciar[0][1]
        cauteloso = iniciar[0][2]
        aleatorio = iniciar[0][3]
        qtd_simula = int(iniciar[0][4])
        max_rodadas = int(iniciar[0][5])
        bonus = int(iniciar[0][6])
        propriedades = iniciar[0][7]
        timeout = iniciar[1]

    print(f'\nForam executadas {simulacao} simulacoes, jogados {total_turnos} turnos e {qtd_timeout} partidas foram encerradas por timeout !')
    media_turnos = total_turnos / simulacao
    perc_impulsivo = (impulsivo_ganhou / simulacao) * 100
    perc_exigente = (exigente_ganhou / simulacao) * 100
    perc_cauteloso = (cauteloso_ganhou / simulacao) * 100
    perc_aleatorio = (aleatorio_ganhou / simulacao) * 100

    # Dicionario com o percentual de vitorias por perfil
    vitorias = {'IMPULSIVO':perc_impulsivo,'EXIGENTE':perc_exigente,'CAUTELOSO':perc_cauteloso,'ALEATORIO':perc_aleatorio}

    print(f'\nImpulsivo ganhou {impulsivo_ganhou} vezes!')
    print(f'Exigente ganhou {exigente_ganhou} vezes!')
    print(f'Cauteloso ganhou {cauteloso_ganhou} vezes!')
    print(f'Aleatorio ganhou {aleatorio_ganhou} vezes!')

    # Encontrando o perfil que venceu mais vezes
    maior_vencedor = max(vitorias, key=vitorias.get)
            
    print('\n#########################################################################')
    print('##################### ESTATISTICAS DE PROCESSAMENTO #####################')
    print('#########################################################################')
    print('Quantas partidas terminam por time out (1000 rodadas) ?')
    print(f'Resposta...: {qtd_timeout} partidas foram encerradas por timeout !')
    print('\nQuantos turnos em media demora uma partida ?')
    formatted = '{:.0f}'.format(media_turnos)
    print(f'Resposta...: Uma partida demora em media {formatted} turnos !')
    print('\nQual a porcentagem de vitorias por comportamento de jogadores ?')
    formatted = '{0:.2g}'.format(perc_impulsivo)
    print(f'Resposta...: A porcentagem de vitorias do perfil IMPULSIVO eh de {formatted}% !')
    formatted = '{0:.2g}'.format(perc_exigente)
    print(f'Resposta...: A porcentagem de vitorias do perfil EXIGENTE eh de {formatted}% !')
    formatted = '{0:.2g}'.format(perc_cauteloso)
    print(f'Resposta...: A porcentagem de vitorias do perfil CAUTELOSO eh de {formatted}% !')
    formatted = '{0:.2g}'.format(perc_aleatorio)
    print(f'Resposta...: A porcentagem de vitorias do perfil ALEATORIO eh de {formatted}% !')
    print('\nQual o comportamento que mais vence ?')
    print(f'Resposta...: O comportamento que mais vence eh o {maior_vencedor} !!!!')
    print('#########################################################################\n')

    # Registrando o log
    utilities.append_file(log, f"{data_hora}-log-desafio-por-RNobrega.txt", msg)

    end_t = time.time()
    end = time.ctime()
    msg_log = f"""
    RUNNING DETAILS INFO:
    start_time (UTC) = {start}
    end_time (UTC) = {end}
    \n{100 * '-'}
    """
    print(msg_log)
    print('Elapsed time: ', end="")
    print(end_t - start_t, end="")
    print(' secs')

    input()

if __name__ == "__main__":
    main()