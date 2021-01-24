# Crud Cliente

### Escopo do que deve ser realizado
- [x] Criar um projeto com o Django mais atualizado
- [x] Criar um Login básico
- [x] Criar um Model com 5 campos (nome, endereco, telefone, data_nascimento, data_cadastro)
- [x] Criar um CRUD do cliente que só seja acessado via Login
- [x] O campo **data_cadastro** deve ser gravado sempre com a data e hora atual e não precisa aparecer no cadastro
- [x] Ao entrar no sistema, o mesmo deve ser direcionado para o **Login**

### Sonre o desenvolvimento do projeto
- [x] O projeto deve usar **VENV**
- [x] O código deve ser commitado no github com o repositório de nome **crud-cliente**

### Como executar o projeto
### Pré-requisitos
- [x] Python 3.9
- [x] Pip

### Passo a Passo
** **
**Caso não tenha o **virtualenv** instalado, faça:**
- No terminal do seu sistema operacional
    >pip install virtualenv
- Em seguida, faça:
    >pip install virtualenvwrapper
** **
- Crie seu ambiente virtual:
    >mkvirtualenv nome-do-ambiente
- Com o seu ambiente virtual criado e dentro da pasta do projeto, execute:
    >pip install -r requirements.txt
- Feito isso, entre dentro da pasta **cliente** e execute o seguinte comando:
    >python manage.py runserver

- Ao executar o comando acima, você pode ir no navegador e digitar:
    >localhost:8000/
  
- Neste momento, você estará executando a aplicação. 
- Para fazer login, utilize o **usuário e senha** *"admin"* sem as aspas. 
- Pronto, você está dentro do sistema. 
- Agora você pode testar o CRUD do Cliente. 