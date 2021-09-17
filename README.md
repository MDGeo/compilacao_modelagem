# MDGeoApps: Compilador de Dados de Input Modflow

Compilar dados em planilhas custa muito tempo. Por isso, desenvolveu-se este compilador. De agora em diante, você não gastará mais tanto tempo, mas apenas alguns instantes para poder ajustar o arquivo de acordo com os requisitos.

## Índice

[1. Como Instalar](#ci)

[2. Requisitos da Sua Tabela](#rst)

[3. Usando o Programa](#uop)

[4. Sobre o Programa](#sop)

_______

<a name = "ci" ></a>
## 1. Como Instalar?

A instalação é bastante simples. Siga os passos abaixo:

`1.` Escolha o tipo de dado que você quer processar `VAZÃO` ou `NÍVEL D'ÁGUA`

`2.` Acesse a pasta e realize o download do arquivo com extensão `.exe`

`3.` Uma vez que tiver baixado, escolha uma pasta, de preferência vazia, para colocar seu `.exe`
_________________________

<a name = 'rst' ></a>
## 2. Requisitos da Sua Tabela

#### Compilação de Dados de Vazão

- `Tabela com os Dados de Vazão`
	
	Caso você queira compilar os dados de vazão, é necessário obedecer um tipo de formatação. Para isso, basta seguir o modelo abaixo (é **muito recomendável** que o nome das colunas também sejam iguais):
	
	
	| Data | Intrsumento 1 | Instrumento 2|
	|------|---------------|--------------|
	|01/02/2000| 2000 | 5000 |
	
	
- `Tabela com os dados de Coordenadas dos Instrumentos`
	
	A mesma coisa se aplica para a tabela de instrumentos
	
	| Código | E-W | N-S | Cota do Filtro (m) |
	|--------|-----|-----|--------------------|
	|Instrumento 1| 000000 | 0000000 | 850 |
	
	
`Observação` : esses duas tabelas podem estar dentro do mesmo arquivo, porém, em abas com nomes diferentes. Mais detalhes sobre isso em [Como Utilizar o Programa](#uop)
	

#### Compilação de Dados de Nível D'água

- `Tabela com os dados de Nível D'água`
	
	A formatação correta da tabela é assim:
	
	| Início | Fim | N dias| Instrumento 1|
	|------|-------|--------|--------------|
	|01/02/2000| 01/05/2000 | 90 | 0|

- `Tabela com os dados de Coordenadas dos Instrumentos`

	A tabela para as coordenadas dos instrumentos é bastante semelhante, tendo algumas mudanças:
	
	
	| Código | E-W | N-S | Topo (m) | Base (m) |
	|--------|-----|-----|----------|---------|
	|Instrumento 1| 000000 | 0000000 | 850 | 700|

___________________________________________

<a name = "uop" ></a>
## 3. Usando o Programa

`1.` Colocando os arquivos dentro da pasta com o **.exe**

 - No início, lembra que você colocou o **.exe** dentro de uma pasta vazia? Pois bem, é nessa pasta que o processamento ocorrerá.
 
 - Antes de você rodar o programa, é fundamental que coloque o arquivo dentro da pasta. Mas atente-se ao tipo de instrumento que os dados da planilha possui! 
 
 - Dados de Nível devem sempre estar dentro da pasta com o **compilacao_input_nivel.exe** , e Dados de Vazao/Poço devem sempre estar dentro da pasta com o **compilacao_input_vazao.exe**.

`2.` Rodando o programa

 - Para rodar o programa, dê um duplo clique sobre o arquivo com final **.exe**. Isso abrirá uma janela preta.

`3.` Lendo linhas numa tela preta

 - Infelizmente, por enquanto, o programa não tem uma interface bonita, mas ele é funcional. Você precisa inserir uma série de informações, conforme os passos abaixo, feito com o `compilacao_input_vazao`, porém, o processo para `compilacao_input_nivel` é o mesmo, o que muda é o processamento do código.
 
 `a.` Ao iniciar o programa, aparecerão algumas informações. Leia com atenção!
 
 ![image](https://user-images.githubusercontent.com/53950449/133777425-e95eb5c3-c804-48d9-b660-85719ba90f15.png)

________________________
 
 `b.` Depois, aparecerá um campo para inserir o nome do arquivo. No caso, a minha planilha se chama `INPUT_VAZAO_POCOS_TRANS.xlsx`. É fundamental que você coloque o nome idêntico, além da extensão do arquivo, que no caso deve sempre ser `XLSX`. Ao preencher, basta apertar a tecla enter.
 
 ![image](https://user-images.githubusercontent.com/53950449/133780558-0ccad2e0-632d-4abf-8ca9-5314fb7ea341.png)

________________________

`c.` Em seguida, será solicitado o nome da aba. No caso da minha tabela, os dados de vazão dos poços se encontram na aba `Vazao_trimestral_m3dia`.

 ![Captura de tela de 2021-09-17 08-53-09](https://user-images.githubusercontent.com/53950449/133778446-c9831f3b-64cc-4c1f-adfd-22010e401eb7.png)

Copie o nome integralmente, preencha o espaço e pressione a tecla enter.

![image](https://user-images.githubusercontent.com/53950449/133778578-375b1126-cdab-4e3b-87bc-a589bf789ceb.png)

________________________

`d.` O próximo passo é inserir as informações onde estão as coordenadas, topo e base do poço (no caso de poço/vazão). Esses dados podem estar na mesma planilha que você já inseriu o nome no passo `a.`, ou em planilha diferente. No caso desse exemplo, os dados se encontram no mesmo arquivo, porém em aba diferente. 

![Captura de tela de 2021-09-17 09-05-44](https://user-images.githubusercontent.com/53950449/133779990-0b4bb0cf-9bf5-4de7-9b40-5acf52c6f186.png)

Então, basta inserir o nome do arquivo, e dar enter.

![image](https://user-images.githubusercontent.com/53950449/133780677-0fad2e87-e561-401d-964d-9a8d1b140aa4.png)

________________________

**Nota**: tem um pequeno erro na linha de código `...que contém as coordenadas e a cota do filtro`. Apesar de indicar `cota do filtro`, é a planilha deve ser igual a mostrada no passo `d.`.

________________________

`e.` A penúltima entrada é o nome da aba em que se encontram tais informações. No caso do exemplo, é simplesmente `coordenadas`.

![image](https://user-images.githubusercontent.com/53950449/133780704-650022dd-8ab6-48b9-ab0e-6082cb6cee84.png)

________________________

`f.` Um aviso aparecerá. Se você tiver preenchido tudo certo, o programa irá processar normalmente. Caso contrário, ele irá apresentar um erro. Caso queira rodar, feche a janela, e abra o programa novamente.

________________________

`g.` Depois, aparecerão uma série de confirmações de que o código está rodando, até o momento que haverá uma solicitação para inserir a data de início do modelo. O formato da data necessariamente é **AAAA-MM-DD**.

![image](https://user-images.githubusercontent.com/53950449/133781006-d02bf575-7419-4b32-afbd-352fabf468ad.png)

________________________

`h.` Será solicitada uma confirmação. Aperte 1 caso sua data esteja correta ou 0 caso queira corrigir. 

![image](https://user-images.githubusercontent.com/53950449/133781087-cfe8072a-6e47-43ed-b683-297f8bfaa004.png)

________________________

`i.` Em seguida, haverá uma mensagem dizendo que o processamento foi concluído, e a janela se fechará muito rapidamente. 
Confira a pasta em que se encontra o **.exe** e veja a planilha recém-criada.

![image](https://user-images.githubusercontent.com/53950449/133781227-089fc9c5-8f72-49df-bf2b-75b87ce4899e.png)
 
________________________

`4.` Vendo o arquivo de saída na pasta

A planilha processada será direcionada para a pasta que você colocou o **.exe**. 

No caso do processamento de dados de poços/vazão, a planilha terá esse início como nome `modelo_input_poco...`.
Se os dados forem de nível d'água, terá o nome de `modelo_input_nivel...`

<a name = "sop" ></a>
## 4. Sobre o Programa

 - FAQ
 
 	- Esse programa vai ficar assim com essa janela feia? 
 	
 	`Resposta:` Por ora sim, mas futuramente será desenvolvida uma interface para deixar o programa mais amigável
	
	- Preciso seguir a formatação das planilhas igual apontada no [Capítulo 2](#rst)
	
	`Resposta:` Para evitar erros no processamento, sim. Infelizmente o código não é muito flexivel.
	
 
 - Autor: Rodrigo Brust
 
 	  Leonardo Pereira
 
 - Empresa: MDGeo
 
	- Setor: Modelagem Numérica

- Coordenadores: Julio Yasbek & Roberto Delfim
