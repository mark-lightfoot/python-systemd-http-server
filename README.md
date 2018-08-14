# python-systemd-http-server
A simple Python HTTP Server that serves static content and can be deployed as a Systemd Service
### Running as a Systemd Service
- In the [Service File](python-systemd-http-server), change the `User` property to the user that is going to be running the server, the default is jenkins:
	```systemd
	[Service]
	User=jenkins
	```
- Install the server
	```bash
	sudo make install
	```
- Start the Server with `systemctl`
	```bash
	sudo systemctl start python-systemd-http-server
	```
- The server can be accessed on the default port of `9000`:
	```bash
	http://localhost:9000
	```
