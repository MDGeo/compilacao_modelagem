# MDGeoApps: Compilador de Dados de Input Modflow

Compilar dados em planilhas custa muito tempo. Por isso, desenvolveu-se este compilador. De agora em diante, você não gastará mais tanto tempo, mas apenas alguns instantes para poder ajustar o arquivo de acordo com os requisitos.

## Índice

[1. Como Instalar](#ci)

[2. Requisitos da Sua Tabela](#rst)

[3. Usando o Programa](#uop)

[4. Sobre o Programa](#sop)

_______

<a name = "ci" />
### 1. Como Instalar? 

A instalação é bastante simples. Siga os passos abaixo:

`1. Escolha o tipo de dado que você quer processar **VAZÃO** ou **NÍVEL D'ÁGUA**`

`2. Acesse a pasta e realize o download do arquivo com extensão **.exe**`

`3. Uma vez que tiver baixado, escolha uma pasta, de preferência vazia, para colocar seu **.exe**`

<a name = 'rst' />
### 2. Requisitos da Sua Tabela

- Compilação de Dados de Vazão

	- Tabela com os Dados de Vazão
	
	Caso você queira compilar os dados de vazão, é necessário obedecer um tipo de formatação. Para isso, basta seguir o modelo abaixo (é **muito recomendável** que o nome das colunas também sejam iguais):
	
	| Data | Intrsumento 1 | Instrumento 2|
	|------|---------------|--------------|
	|01/02/2000| 2000 | 5000 |
	
	
	- Tabela com os dados de Coordenadas dos Instrumentos
	
	A mesma coisa se aplica para a tabela de instrumentos
	
	| Código | E-W | N-S | Cota do Filtro (m) |
	|--------|-----|-----|--------------------|
	|Instrumento 1| 000000 | 0000000 | 850 |
	
	**Observação** : esses duas tabelas podem estar dentro do mesmo arquivo, porém, em abas com nomes diferentes. Mais detalhes sobre isso em [Como Utilizar o Programa](#uop)

- Compilação de Dados de Nível D'água

	- Tabela com os dados de Nível D'água
	
	A formatação correta da tabela é assim:
	
	| Início | Fim | N dias| Instrumento 1|
	|------|-------|--------|--------------|
	|01/02/2000| 01/05/2000 | 90 | 0|

	- Tabela com os dados de Coordenadas dos Instrumentos

	A tabela para as coordenadas dos instrumentos é bastante semelhante, tendo algumas mudanças:
	
	| Código | E-W | N-S | Topo (m) | Base (m) |
	|--------|-----|-----|----------|---------|
	|Instrumento 1| 000000 | 0000000 | 850 | 700|

<a name = "uop" />

### 3. Usando o Programa

`1.` Colocando os arquivos dentro da pasta com o **.exe**

 No início, lembra que você colocou o **.exe** dentro de uma pasta...

`2.` Rodando o programa

 De um duplo clique sobre o arquivo com final **.exe**

`3.` Lendo linhas numa tela preta

 Infelizmente, por enquanto, o programa não tem uma interface bonita, mas ele é funcional.
 Você precisa inserir uma série de informações...

`4.` Vendo o arquivo de saída na pasta

<a name = "sop" />
### 4. Sobre o Programa

 - FAQ
 
 
 - Autor: Rodrigo Brust
 
 - Empresa: MDGeo
 
	- Setor: Modelagem Numérica

- Coordenadores: Julio Yasbek & Roberto Delfim