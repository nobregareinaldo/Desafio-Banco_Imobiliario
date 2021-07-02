# Desafio-Banco_Imobiliario
Desafio Banco Imobiliario

Considere o seguinte jogo hipotético muito semelhante a Banco Imobiliário, onde várias de suas mecânicas
foram simplificadas. Numa partida desse jogo, os jogadores se alteram em rodadas, numa ordem definida
aleatoriamente no começo da partida. Os jogadores sempre começam uma partida com saldo de 300 para
cada um...

Desenvolvido em 01/07/2021 por Reinaldo Nobrega

Para realizar as simulacoes do desafio com sucesso:
1 - Atualize o fonte 'simulador_banco_imobiliario.py' na linha 137, substituindo na variavel log = 'C:\\Users\\Usuario\\Desktop\\BrasilPrev\\build\\' para o diretorio em que deseja armazenar o log de execucao.

2 - O programa python pode ser executado de diversas formas:
  - Seja por linha de comando: python simulador_banco_imobiliario.py 
  - Seja por dois cliques do mouse...

3 - No arquivo 'application.cfg' estao armazenados os parametros para configuracao das simulacoes.
  Por exemplo: saldo inicial dos jogadores, caracteriticas dos perfil e quantidade de simulacoes

4 - O programa 'utilities.py' eh utilizado para realizar operacoes de sistema opecional.
  Por exemplo: criacao de diretorio ou criacao de arquivos em disco

5 - Disponibilizei uma versao do simulador contendo print de cada movimentacao durante as partidas.
  Pode ser executado pela linha de comando: python versao_COM_PRINTs_simulador_banco_imobiliario.py

6 - A cada execucao sera criado um arquivo texto com o log da execucao
  - Exemplo: 20210701-205919-log-desafio-por-RNobrega.txt
  - Sendo AAAAMMDD-HHMMSS-log-desafio-por-RNobrega.txt

************************************
LOG DE EXECUCAO:
************************************
    Inicializando Desafio - Simulacoes Banco Imobiliario ...
    Desenvolvido por Reinaldo Nobrega - https://www.linkedin.com/in/reinaldo-nobrega/ 

    #########################################################################
    Simulando turnos ...
    ...
    Simulacao encerrada ...
    Calculando estatisticas ...

    Foram executadas 300 simulacoes, jogados 14037 turnos e 0 partidas foram encerradas por timeout !

    Vitorias por perfil de jogador:
    -- Impulsivo ganhou 0 vezes! --
    -- Exigente ganhou 194 vezes! --
    -- Cauteloso ganhou 67 vezes! --
    -- Aleatorio ganhou 39 vezes! --

    *************************************************************************
    ********************* ESTATISTICAS DE PROCESSAMENTO *********************
    *************************************************************************
    Quantas partidas terminam por time out (1000 rodadas) ?
    Resposta...: 0 partidas foram encerradas por timeout !

    Quantos turnos em media demora uma partida ?
    Resposta...: Uma partida demora em media 47 turnos !

    Qual a porcentagem de vitorias por comportamento de jogadores ?
    Resposta...: A porcentagem de vitorias do perfil IMPULSIVO eh de 0% !
    Resposta...: A porcentagem de vitorias do perfil EXIGENTE eh de 65% !
    Resposta...: A porcentagem de vitorias do perfil CAUTELOSO eh de 22% !
    Resposta...: A porcentagem de vitorias do perfil ALEATORIO eh de 13% !

    Qual o comportamento que mais vence ?
    Resposta...: O comportamento que mais vence eh o EXIGENTE !!!!
    #########################################################################

    RUNNING DETAILS INFO:
    start_time (UTC) = Thu Jul  1 20:59:19 2021
    end_time (UTC) = Thu Jul  1 20:59:20 2021
    
----------------------------------------------------------------------------------------------------
    
