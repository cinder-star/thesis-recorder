# Installation

- First install apache and start

```bash
sudo yum install httpd
sudo systemctl start httpd
```

- Then install httpd devel

```bash
sudo yum install httpd-devel
```

- Install mod_wsgi

```bash
sudo yum install mod_wsgi
sudo systemctl restart httpd
```

- Check if it is working

```bash
$ sudo httpd - M | grep wsgi
wsgi_module (shared) # The okay response
```

- If the server didn't load the mod_wsgi module, add the following line in the /etc/httpd/conf/httpd.conf file along with the other loadmodule sections:

```bash
LoadModule wsgi_module modules/mod_wsgi.so
```

- Then restart the apache server again:

```bash
sudo systemctl restart httpd
```

- Extract the source code and copy the thesis-recorder folder into /var/www folder

```bash
sudo cp -r /path/to/your/extracted/thesis-recorder /var/www/thesis-recorder
```

- Give permission of the folder

```bash
sudo chmod 777 -R /var/www/thesis-recorder
```

- Go to /var/www and create virtualenv

```bash
cd /var/www/thesis-recorder
python3 -m venv venv
```

- Install the dependencies for the virtual env:

```bash
source /venv/bin/activate
pip3 install -r requirements.txt
```

- Create database and grant permission:

```bash
python3 manage.py migrate
sudo chmod 777 /var/www/thesis-recorder/db.sqlite3
```

- Add these line into the /etc/httpd/conf/httpd.conf file under vitualhost section

```bash
<VirtualHost *:80>
    ServerName localhost
    WSGIDaemonProcess thesis-recorder user=http group=http threads=2 python-path=/var/www/thesis-recorder/venv/lib/python3.6/site-packages
    WSGIScriptAlias / /var/www/thesis-recorder/thesis_recorder/wsgi.py
    <Directory /var/www/thesis-recorder>
        Require all granted
    </Directory>
    <Directory /var/www/thesis-recorder/media>
        Require all granted
    </Directory>
</VirtualHost>
```

- Restart the apache server and go to <http://127.0.0.1> in the browser:

```bash
sudo systemctl restart httpd
```

if SELinux Policy is Enforcing
```bash
[root@cse thesis-recorder]# semanage fcontext -a -t httpd_exec_t '<absolute path to venv>/.*\.so(\..*)?'
[root@cse thesis-recorder]# restorecon -r <<absolute path to venv>>
```
