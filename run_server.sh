#!/bin/sh
#杀掉所有 gunicorn进程
#killall gunicorn
#杀掉所有包含有关键字 “106.15.136.219:8001” 的进程
echo ==============killall gunicorn
ps -ef|grep 192.168.0.246:8002|grep -v grep|cut -c 9-15|xargs kill -9
set -e

export PYTHONPATH=$PYTHONPATH:.
export DJANGO_SETTINGS_MODULE=server_settings

mkdir -p /home/www/sso_server/media
mkdir -p /home/www/sso_server/static

#wait_for_psql.py -u "${POSTGRES_USER}" -w "${POSTGRES_PASSWORD}" -h postgres
# echo ==============collect static
# manage.py collectstatic --no-input --no-color
# echo ==============makemigrations
# manage.py makemigrations --no-input --no-color
# echo ==============migrate
# manage.py migrate --no-input --no-color
echo ==============start gunicorn
gunicorn -w 4 -b 192.168.0.246:8002  sso.apps.sso.wsgi
;;


$@
