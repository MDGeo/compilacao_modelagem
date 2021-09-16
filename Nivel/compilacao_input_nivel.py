'''
###################################################################
            COMPILADOR DE INPUTS PARA NÍVEL D'ÁGUA
###################################################################
                    OS INPUTS PARA A FUNÇÃO
###################################################################
    
----------------------------------------------------------------------
    
arquivo = arquivo em que contém as informações sobre os instrumentos
(nome, data, por exemplo)
    
----------------------------------------------------------------------
aba = a mesma aba utilizada na função coletando_dados_colunas
    
----------------------------------------------------------------------
    
cordcolect = arquivo em que estão as informações das coordenadas e cota do
filtro de cada instrumento
    
----------------------------------------------------------------------
    
abacord = nome da aba em que está
    
---------------------------------------------------------------------
    
inst = tipo de instrumento (nivel dágua, poços...)
    
---------------------------------------------------------------------
    
'''

import pandas as pd
import numpy as np
import os, glob, time
from datetime import datetime
 
print('-------------------------------------------------------')
print('''Bem-Vindo ao Compilador de Dados de Nível D'Água da MDGeo! \n
    \nIniciando o sistema...''')
print('-------------------------------------------------------')
    
time.sleep(5)
print(' ')
    
print('Será solicitado que você preencha 5 variáveis. Certifique-se de preencher corretamente igual aos arquivos. ')

print('')
    
print('Algumas vezes aparecerão opções  para confirmação.\nEscolha uma delas escrevendo o número indicado. Depois pressione enter para prosseguir')
    
print(' ')
time.sleep(5)
    
print('Insira o nome do arquivo quem contém as informações \n dos instrumentos (nome, data) com sua extensão (.xlsx): ')
print('----------------------------------')
arquivo = str(input('Nome do Arquivo:'))
    
print(' ')
time.sleep(2)
    
print('Agora, insira o nome da aba que contém os dados dos instrumentos')
print('----------------------------------')
aba = str(input('Nome da aba:'))
    
print(' ')

time.sleep(2)
    
print('Agora, é preciso inserir o nome do arquivo que contém as coordenadas e cota do filtro')
print('----------------------------------')
cordcolect = str(input('Nome do Arquivo:'))
    
print(' ')
time.sleep(2)
    
print('Penultimo item: preencha o nome da aba em que se encontram as informações de coordenadas e do filtro')
print('----------------------------------')
abacord = str(input('Nome da aba:'))
  
print('')    
inst = 'nivel'

print(' ')
time.sleep(2)
    
print('Se você tiver preenchido tudo certo, o processamento iniciará. Caso contrário, o programa será interrompido.')
print('-------------------------------------------------------')
    
#função de coletar dados das colunas
    
print(' ')
time.sleep(2)
    

path = os.getcwd()
if not os.path.exists(path + '/empilhamento/'):
        os.makedirs(path + '/empilhamento/')
pasta = './empilhamento'

df = pd.read_excel(io = arquivo, sheet_name = aba)
df.head()
#criando uma lista com todas as colunas no dataframe, exceto a primeira, que é a data
lst = []
print('Empilhando as colunas')
for i in df.columns:
        lst.append(i)

lst = lst[1:]
#criando arquivos csv na pasta "csv_pedro"
for i in lst:
    DF2 = df.filter([df.columns[0], i])
    DF2['Instrumento'] = DF2.columns[1]
    DF2.rename(columns={DF2.columns[1]: 'Vazao'}, inplace = True)
    DF2.to_excel(f'{pasta}/{i}.xlsx', index = False)
print('Empilhamento Concluído')

#função para concatenar os arquivos

files = glob.glob(pasta + f'/*.xlsx')  # pegando os arquivos com o seu path

filename = []  # criando lista vazia
# criando loop para criar uma lista com todos os paths dos arquivos
for file in files:
    file_List = (file)
    filename.append(file_List)
# lista vazia
frames = []

# criando loop para concatenar todos os arquivos dentro de filename
for arquivo in filename:
    # lendo o arquivo
    df2 = pd.read_excel(arquivo)
    # appending
    frames.append(df2)

# concatenando todos os arquivos
df = pd.concat(frames, axis=0, ignore_index=True)


# salvando o aquivo em apenas um
df.to_excel('tabela_empilhada.xlsx', index=False)

#excluindo arquivos da pasta
for f in files:
    os.remove(f)

print('Processamento feito. Os arquivos foram gerados, por favor, verifique a sua pasta')

#função que junta dados de X, Y, Cota do Filtro e a diferença em dias a partir
#do início do modelo


emp = df.copy()

cc = pd.read_excel(cordcolect, sheet_name = abacord)
cc.rename(columns = {cc.columns[0]:'Instrumento'},inplace = True)

#loop para pegar os valores em que o nome do instrumento da planilha
#empilhada seja igual ao nome do instrumento na planilha CC.
#Em seguida, coloca em uma lista

print('Juntando os dados das tabelas')
row = []
for i in emp['Instrumento']:
    line = cc.loc[cc['Instrumento'] == i].reset_index()
    row.append(line)
#criando listas vazias
xm = []
ym =[]
zm = []

#a lista row possui uma série de informações. Para retirar os dados que queremos, é preciso
#criar sublistas com o que realmente importa. O X, Y e a Cota do instrumento.
print('Separando os dados por tipo')
for i in range(len(row)):
    X = row[i]['E-W'].to_list()
    Y = row[i]['N-S'].to_list()
    Z = row[i]['Cota do Filtro (m)'].to_list()
    xm.append(X)
    ym.append(Y)
    zm.append(Z)

#as lista criadas acima (zm, xm e ym) são na verdade, listas de listas.
#Agora, para extrair apenas o valor de dentro das listas, vamos passar, mais uma vez
#por um for loop, e criar mais listas. Dessa vez, com os valores em números.
print('Transformando os dados para tipo numérico')
xmnew = []
for x in xm:
    att = xm[i][0]
    xmnew.append(att)

ymnew = []
for x in xm:
    att = ym[i][0]
    ymnew.append(att)

zmnew = []
for x in zm:
    att = zm[i][0]
    zmnew.append(att)
#uma vez que as listas numéricas foram criadas, podemos colocá-las no dataframe
emp['X (m)'] = xmnew
emp['Y (m)'] = ymnew
emp['Cota do Filtro (m)']= zmnew

#calculando datas a partir da data de início do modelo

emp['Data'] = pd.to_datetime(emp['Data'])

print('Insira a data de início do modelo? [AAAA-MM-DD]')
data_input = input()
print(f'A data escolhida foi {data_input}.')
time.sleep(1)
print('''-----------Deseja Confirmar?---------
Sim - 1
Não - 0
------------------------
''')

resposta = int(input())
if resposta == 1:
    print('Ok, calculando a diferença de datas.')
elif resposta == 0:
    print('Por favor, insira a data novamente')
    data_input = input('Nova Data:')
else:
    while resposta > 1.1:
        print('Valor incorreto. Digite 1 para Sim e 0 para Não')
        resposta = int(input())
        if resposta == 1:
            print(f'A data escolhida foi {data_input}')
            print('Ok, calculando a diferença de datas.')
        elif resposta == 0:
            print('Por favor, insira a data novamente')
            data_input = input('Nova Data:')
            


lst_days = []
date_fmt = "%Y-%m-%d"


#data de início formatado
start_modelo = datetime.strptime(data_input, date_fmt)

#aqui, o código itera por cada data, e se a data for anterior ao
#start_modelo, o valor será 0. Caso seja após, será feito um cálculo
for date in emp['Data']:
    if date < start_modelo:
        days = 0
        lst_days.append(days)
    else:
        date_str = str(date)
        date_cut = date_str[:10]
        data_col = datetime.strptime(date_cut, date_fmt)
        timedelta =  data_col - start_modelo
        days = timedelta.days
        lst_days.append(days)

#o resultado do cálculo é uma lista, que logo em seguida é adicionada ao df
emp['Dias'] = lst_days
emp['Câmara'] = 'A'
emp.replace(0, np.nan, inplace=True)
emp = emp[['Data',
            'Instrumento',
            'X (m)',
            'Y (m)',
            'Câmara',
            'Cota do Filtro (m)',
            'Dias','Vazao']]

print('Salvando o arquivo na pasta...')

emp.to_excel(f'modelo_input_{inst}_{aba}.xlsx')

print('Arquivo salvo! Fim do processamento.')

os.remove('tabela_empilhada.xlsx')