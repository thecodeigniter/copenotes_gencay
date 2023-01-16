sudo git clone https://github.com/GencayAr/copenotes_gencay.git
cd copenotes_gencay
sudo apt-get update
sudo apt-get install erlang
sudo apt-get install rabbitmq-server
sudo -b unshare --pid --fork --mount-proc /lib/systemd/systemd --system-unit=basic.target
sudo -E nsenter --all -t $(pgrep -xo systemd) runuser -P -l $USER -c "exec $SHELL"
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl status rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl set_user_tags admin administrator
sudo rabbitmqctl set_permissions -p / admin "." "." "."
sudo pip3 install -r requirements.txt
sudo celery -A copenotes_gencay beat &
sudo celery -A copenotes_gencay  worker --pool=solo -l INFO &
sudo python3 manage.py runserver 0.0.0.0:8080
