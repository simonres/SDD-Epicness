# Configuration of  `cgi-bin` module in Apache server
For debian (see [here](https://www.server-world.info/en/note?os=Debian_9&p=httpd&f=2) for details)
* Install Apache
```bash
sudo apt-get install apache2
```
* For test purposes, install also `curl`
```bash
sudo apt-get install curl
```
* Try the server
```bash
$ curl http://localhost
```
* Enable CGI module
```bash
sudo a2enmod cgid
```
* Assuming that the repository was copied in the server like
```
sudo cp -r REPODIR/* /var/www/html
```
it is then necessary to configure the CGI directory of Apache to point to `/var/www/html/cgi-bin`. For that the `IfDefine` tag of the CGI configuration file at `/etc/apache2/conf-available/serve-cgi-bin.conf`, must looks like
```xhtml
       <IfDefine ENABLE_USR_LIB_CGI_BIN>
                ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/
                <Directory "/var/www/html/cgi-bin">
                  <!-- default contents here -->
                  ...
                </Directory>
        </IfDefine>
```
* Restart Apache and [check script permissions](https://askubuntu.com/a/932719/678974) of the exectuable scripts. For example `cgi-bin/forward.py`
```bash
systemctl restart apache2
sudo chmod 755 /var/www/html/cgi-bin/forwards.cgi
```
* Test that the script is working
```bash
$ curl http://localhost/cgi-bin/forwards.cgi
```
For a general Linux system check https://code-maven.com/set-up-cgi-with-apache
