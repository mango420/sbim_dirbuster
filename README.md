# sbim_dirbuster

To build the container, use the following command:

`sudo docker build -t flask-hidden . `

Now the container can be started with this command:

`sudo docker build -t flask-hidden .`



After its up, we can discover the hidden paths wir gobuster:

`sudo gobuster dir -u http://localhost:6969 -w /path/to/wordlist`