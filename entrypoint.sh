#!/bin/sh

set -e

export PATH="/venv/bin:$PATH"

# Mensahem de boas-vindas
echo "🚀 Iniciando o container do Django..."
echo "Ajustando as permissões do diretório /dashboard-covid/staticfiles"

# Cria a pasta staticfiles se não existir
mkdir -p /dashboard-covid/staticfiles
# Ajusta as permissões para o usuário appuser
chown -R appuser:appuser /dashboard-covid


echo "Me ajuda senhor, eu não sei o que fazer"
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done
echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"


echo "✅ Conexão com $POSTGRES_HOST $POSTGRES_PORT estabelecida com sucesso!"
#---------Fim das mensagens de status do banco de dados PostgreSQL--------#

# Executa os comandos do Django como o usuário appuser
echo "🔧 Executando comandos do Django..."
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py test

echo "✅ Servidor Django iniciado com sucesso!"

python manage.py runserver 0.0.0.0:8000