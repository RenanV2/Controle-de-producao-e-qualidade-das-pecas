# Controle de Qualidade de Peças

## Sobre o projeto

Este projeto foi desenvolvido em Python como uma solução de automação digital para auxiliar no controle de produção e qualidade de peças em uma linha de montagem industrial.

O sistema recebe os dados de cada peça, realiza automaticamente a verificação dos critérios de qualidade e classifica a peça como aprovada ou reprovada.

As peças aprovadas são organizadas em caixas com capacidade máxima de 10 peças. Quando uma caixa atinge sua capacidade máxima, ela é fechada e uma nova caixa é iniciada.

O sistema também permite consultar as peças cadastradas, remover peças, visualizar as caixas e gerar um relatório final.

## Regras de aprovação

Uma peça é considerada aprovada quando atende simultaneamente aos seguintes critérios:

- Peso entre **95g e 105g**;
- Cor **azul ou verde**;
- Comprimento entre **10cm e 20cm**.

Caso um ou mais critérios não sejam atendidos, a peça é considerada reprovada e o sistema registra os respectivos motivos.

## Funcionalidades

O sistema possui as seguintes opções:

1. **Cadastrar nova peça** — registra peso, cor e comprimento e realiza a avaliação automática;
2. **Listar peças aprovadas/reprovadas** — apresenta os dados das peças e, no caso das reprovadas, seus motivos;
3. **Remover peça cadastrada** — remove uma peça e atualiza a organização das caixas quando necessário;
4. **Listar caixas fechadas** — apresenta as caixas completas e a caixa que ainda está em formação;
5. **Gerar relatório final** — apresenta a quantidade de peças aprovadas, reprovadas, motivos de reprovação e caixas utilizadas;
6. **Persistência dos dados** — salva e recupera automaticamente o estado do sistema.

## Persistência dos dados

O sistema utiliza um arquivo `data.json` para armazenar os dados das peças, das caixas e do próximo identificador de peça.

Os dados são salvos automaticamente após o cadastro de uma peça ou após a remoção de uma peça. Quando o programa é executado novamente, os dados armazenados são carregados automaticamente, permitindo continuar a utilização do sistema a partir do estado anterior.

O arquivo `data.json` é criado automaticamente pelo programa e está incluído no `.gitignore`. Dessa forma, os dados gerados durante a execução permanecem apenas no ambiente local e não são enviados para o repositório GitHub.

## Como executar

### Pré-requisitos

- **Python 3** instalado;
- **Git** instalado caso o projeto seja obtido por meio de um repositório GitHub.

### Execução

1. Clone o repositório ou faça o download do projeto.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal:

```bash
python sistema.py
```

4. O menu principal será exibido no terminal.

Caso o arquivo `data.json` ainda não exista, o sistema inicia com os dados vazios e cria o arquivo automaticamente após a primeira alteração que for salva.

## Exemplos de uso

### Cadastro de uma peça aprovada

**Entrada:**

```text
Escolha uma opção: 1
Digite o peso: 100
Digite a cor da peça: azul
Digite o comprimento da peça: 15
```

**Resultado:**

A peça é aprovada e armazenada na caixa atual.

### Cadastro de uma peça reprovada

**Entrada:**

```text
Escolha uma opção: 1
Digite o peso: 110
Digite a cor da peça: vermelho
Digite o comprimento da peça: 25
```

**Resultado:**

A peça é reprovada e os seguintes motivos são registrados:

```text
Peso fora do intervalo
Cor fora do intervalo
Comprimento fora do intervalo
```

### Listagem de caixas

Quando existem peças aprovadas, elas são armazenadas na caixa atual até atingir a capacidade máxima de 10 peças.

Exemplo:

```text
--- Caixas Completas ---

Não possui nenhuma caixa fechada.

--- Caixa Incompleta ---

Quantidade de peças: 1
- P1
```

Quando uma caixa atinge 10 peças, ela é fechada e uma nova caixa é iniciada.

### Relatório final

O relatório apresenta informações consolidadas sobre o estado atual do sistema, como:

```text
=== Relatório Final ===

Quantidade de peças aprovadas: 8
Quantidade de peças reprovadas: 2

--- Motivos de Reprovação ---

P3:
- Peso fora do intervalo

P7:
- Cor fora do intervalo
- Comprimento fora do intervalo

--- Caixas Utilizadas ---

Quantidade de caixas utilizadas: 1
Caixas fechadas: 0
Caixa incompleta: 1
```

## Tecnologias utilizadas

- **Python 3** — linguagem utilizada no desenvolvimento do sistema;
- **JSON** — utilizado para a persistência dos dados durante a execução;
- **Git** — utilizado para controle de versão do projeto;
- **GitHub** — utilizado para armazenamento e disponibilização do código-fonte.

## Estrutura do projeto

```text
controle-qualidade-python/
├── sistema.py
├── README.md
├── .gitignore
└── data.json
```

### Descrição dos arquivos

- `sistema.py` — arquivo principal contendo a lógica do sistema;
- `README.md` — documentação do projeto, incluindo funcionamento, instruções de execução e exemplos;
- `.gitignore` — define os arquivos que não devem ser enviados para o repositório Git;
- `data.json` — arquivo criado automaticamente pelo sistema para armazenar os dados durante a execução. Não é versionado no GitHub.
