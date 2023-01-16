

# Challenge: Develop a simple e-mail scheduler with randomized messages

## Make sure to contact gencayar.tx@gmail.com for any kidn of help. I have added .env file deliberately for demo purpose. Although it is kept hidden in Actual Production Systems ##


***Clone the Repository through following command***
```sh
git clone https://github.com/GencayAr/copenotes_gencay/
```
***Use sudo before git if you are on linux***



### Requirements
1.	There should be an API endpoint to register new users (with their e-mail address)
2.	There should be ten hardcoded messages (feel free to choose the content)
3.	Every minute, every user receives one of these messages at random, but never the same one twice.
4.	Once a user has received all messages, they shouldn't receive any more.
5.	Data storage can be in memory.

Please develop an application that fulfills all these requirements. Feel free to creatively work around missing information, as in, if these requirements don't answer all your questions, do what you think is the best solution. Should you have any additional questions, please ask. 

### Deliverable:
1.	Fully runnable application with instructions on how to run in a **GitHub** or **Bitbucket** repository. (_**I have done in Github**_)
2.	Use any programming language applicable. Frameworks are allowed and encouraged.
3.	Write well-structured, clean code. This is a small system, but feel free to over-engineer and show off your skills. Please employ all methods of modern, high-quality software engineering.



### Installation

Requirements are given below: 
- Python >= 3.10
- RabitMQ
- Erlang
- Follow the document given in it

#### For Linux OS on Google Cloud Console

Please open **https://shell.cloud.google.com/** and in the console. Upload the **run_script.sh** as file and run 
 ```sh
 source run_script.sh
 ```
 
 If it does not work then run these commands one by one
 
 ```sh

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
sudo python manage.py collectstatic
sudo python manage.py makemigrations
sudo python manage.py migrate
sudo python manage.py createsuperuser
sudo python3 manage.py runserver 0.0.0.0:8080


 ```
 

Then visualize by clicking **Web preview** icon on the top right with settings **gear icon** and click **Preview on port 8080**


#### For Windows OS

It is recommended from developer to use **Anaconda** for running the program. You can install from **https://repo.anaconda.com/archive/Anaconda3-2022.05-Windows-x86_64.ex/**

Please setup your python environment and then once you clone the repository, please make sure to run following commands given below in the Anaconda Terminal: 

```sh
conda create -n copenotes python=3.10
conda activate copenotes
cd copenotes_gencay
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```



Run the following each command in separate terminals under same environment:


```sh
celery -A copenotes_gencay beat
celery -A copenotes_gencay  worker --pool=solo -l INFO
python manage.py runserver 0.0.0.0:8080
```



##### While creating superuser, make sure to keep the username and password _admin_ and _admin_ only respectively. Use your own email #####










