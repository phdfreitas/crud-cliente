# Crud Cliente

## Escopo do que deve ser realizado
- [x] Criar um projeto com o Django mais atualizado
- [x] Criar um **Login** básico
- [x] Criar um Model com 5 campos _(nome, endereco, telefone, data_nascimento, data_cadastro)_
- [x] Criar um **CRUD** do cliente que só seja acessado via **Login**
- [x] O campo **data_cadastro** deve ser gravado sempre com a data e hora atual e não precisa aparecer no cadastro
- [x] Ao entrar no sistema, o mesmo deve ser direcionado para o **Login**

## Sobre o desenvolvimento do projeto
- [x] O projeto deve usar **VENV**
- [x] O código deve ser commitado no github com o repositório de nome **crud-cliente**

## Como executar o projeto
### Pré-requisitos
- [x] Python 3.9.x
- [x] Pip
- [x] Git

### Passo a Passo
- Caso não tenha o **virtualenv** instalado, faça:
  - Abra o terminal ou CMD do seu sistema operacional e execute:
      >pip install virtualenv
  - Em seguida, faça:
    - Caso você use Windows:
      >pip install virtualenvwrapper-win
    - Caso contrário:
      >pip install virtualenvwrapper
** **
- Se já instalou o **virtualenv** e o **virtualenvwrapper**:
  - Crie seu ambiente virtual:
      >mkvirtualenv nome-do-ambiente  
  
  - Certifique-se de que está usando seu ambiente virtual:
    - Caso use o Windows:
      - Acesse a pasta **Envs**, normalmente:
        > cd \Users\seu-usuário\Envs
      - Dentro de **Envs**, execute o comando abaixo:
        > workon nome-do-ambiente
    - Caso contrário, basta executar o comando abaixo:
      > workon nome-do-ambiente
      
  - Faça o clone do repositório. Sugiro que faça isso na Área de Trabalho.
    - No terminal ou no CMD do seu sistema operacional, execute:
      >git clone https://github.com/phdfreitas/crud-cliente.git
      
  - Entre na pasta do repositório:
    > cd crud-cliente/

  - Usando o ambiente virtual criado e dentro da pasta do projeto, execute:
      >pip install -r requirements.txt
  
  - Feito isso, entre dentro da pasta **cliente:**
      > cd cliente/
  
  - Dentro da pasta **cliente**, execute:
      >python manage.py runserver
  
  - **Neste momento, você estará executando a aplicação.** 
  
  - No navegador de sua preferência, acesse:
      >localhost:8000/
    
  - Para fazer login, utilize o **usuário e senha** *"admin"* sem as aspas. 
  
  - Pronto, você está dentro do sistema. 
  
  - Agora você pode testar o **CRUD** do Cliente. 