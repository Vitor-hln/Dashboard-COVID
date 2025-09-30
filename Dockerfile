# Define a imagem base - Python 3.15.3 com Alpine Linux 3.18
FROM python:3.11-alpine3.18 


# Evita a criação de arquivos binários 
ENV PYTHONDONTWRITEBYTECODE 1 
# Garante que o output do Python seja exibido em tempo real no console
# Ou seja não armazena mensagems em buffers
ENV PYTHONUNBUFFERED 1

# Faz as copias dos aquivos de requisitos para o container
COPY ./dashboard-covid /dashboard-covid
COPY ./scripts /scripts
COPY ./entrypoint.sh /entrypoint.sh

# Define o diretorio de trabalho dentro do container
WORKDIR /dashboard-covid

# Porta que a aplicação irá rodar
# 8000 é a porta padrão do Django
EXPOSE 8000


# Cria ambiente virtual Python isolado no diretório /venv
RUN python -m venv /venv && \
    # Atualiza o pip dentro do ambiente virtual para a versão mais recente
    /venv/bin/pip install --upgrade pip && \
    # Instala todas as dependências listadas no requirements.txt usando o pip do venv
    /venv/bin/pip install -r /dashboard-covid/requirements.txt && \
    # Instala o cliente PostgreSQL sem salvar cache (economia de espaço)
    apk add --no-cache postgresql-client&& \
    # Cria um usuário do sistema chamado appuser sem senha
    adduser --disabled-password appuser && \
    # Cria o diretório para arquivos estáticos do Django (CSS, JS, imagens)
    mkdir -p /dashboard-covid/staticfiles && \
    # Define o usuário appuser como dono de todos os arquivos do projeto
    chown -R appuser:appuser /dashboard-covid && \
    # Da acesso aos arquivos dentro de /scripts 
    chmod -R +x /scripts && \
    # Garante permissão de execução para todos os arquivos dentro de /scripts
    chmod +x /scripts/* && \
    # Dá permissão de execução ao script de inicialização do container
    chmod +x /entrypoint.sh


# roda os scripts dentro da pasta scripts
RUN /scripts/example.sh

ENV PATH="scripts/venv/bin:$PATH"

# Define o script de entrada do container
# Esse script será executado toda vez que o container iniciar
# Ele configura o ambiente e inicia o servidor Django
# O script cuida de tarefas como aplicar migrações do banco de dados
ENTRYPOINT [ "/entrypoint.sh" ]