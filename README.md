# Sistemas Distribuídos - Projeto Final

Este repositório contém um projeto de Sistemas Distribuídos utilizando Docker e agentes inteligentes. O sistema consiste em dois agentes que interagem entre si e com um cliente web.

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados e configurados:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Além disso, é necessário que o Docker esteja instalado e **iniciado** no seu sistema.

## Instalação e Execução

1. Clone este repositório:
   ```sh
   git clone https://github.com/RibeiroEduardo8/Sistemas-Distribuidos-Final.git
   cd Sistemas-Distribuidos-Final
   ```

2. Construa e inicie os containers com Docker Compose:
   ```sh
   docker-compose build
   docker-compose up
   ```

   Aguarde até que os dois servidores iniciem completamente. Dependendo da sua conexão com a internet, esse processo pode demorar um pouco.

3. O sistema iniciará dois serviços principais:
   - **Agente Principal** rodando em `http://localhost:8000`
   - **Cliente** rodando em `http://localhost:8001`

4. Para interagir com o sistema:
   - Se estiver usando o **VS Code**, você pode executar o arquivo HTML (`template/index.html`) usando o **Live Server** ou **Live Share**.
   - Caso contrário, basta abrir o arquivo `template/index.html` diretamente no seu navegador.

5. Insira as informações necessárias na interface web e aguarde cerca de **2 minutos** para o programa processar a resposta.

6. Para encerrar os containers, pressione `CTRL+C` no terminal onde o Docker Compose está rodando ou execute o seguinte comando:
   ```sh
   docker-compose down
   ```

## Estrutura do Projeto

```
Sistemas-Distribuidos-Final/
│── agentes/
│   ├── agente1/
│   ├── agente2/
│── Relatório RIPD/
│── template/
│   ├── index.html
│   ├── style.css
│── docker-compose.yml
```

- **agentes/**: Contém os códigos dos agentes distribuídos.
- **template/**: Contém os arquivos da interface web.
- **docker-compose.yml**: Arquivo de configuração para orquestração dos containers.

## Observações

- Certifique-se de que o Docker esteja em execução antes de iniciar o projeto.
- O tempo de processamento pode variar dependendo da complexidade das informações inseridas e da capacidade do seu sistema.
- Em caso de problemas, verifique os logs dos containers para mais detalhes.
