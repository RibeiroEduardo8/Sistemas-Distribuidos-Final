# Sistemas Distribuídos - Projeto Final

Este repositório contém um projeto de Sistemas Distribuídos utilizando Docker e agentes inteligentes. O sistema consiste em dois agentes que interagem entre si e com um cliente web.

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação e Execução

1. Clone este repositório:
   ```sh
   git clone https://github.com/RibeiroEduardo8/Sistemas-Distribuidos-Final.git
   cd Sistemas-Distribuidos-Final
   ```

2. Construa e inicie os containers com Docker Compose:
   ```sh
   docker-compose up --build
   ```

3. O sistema iniciará dois serviços principais:
   - **Agente Principal** rodando em `http://localhost:8000`
   - **Cliente** rodando em `http://localhost:8001`

4. Para encerrar os containers, pressione `CTRL+C` ou rode:
   ```sh
   docker-compose down
   ```

## Estrutura do Projeto

```
Sistemas-Distribuidos-Final/
│── agentes/
│   ├── agente1/
│   ├── agente2/
│── template/
│   ├── index.html
│   ├── style.css
│── docker-compose.yml
```

- **agentes/**: Contém os códigos dos agentes distribuídos.
- **template/**: Contém os arquivos da interface web.
- **docker-compose.yml**: Arquivo de configuração para orquestração dos containers.

