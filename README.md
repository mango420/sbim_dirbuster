# sbim_dirbuster

### Pt. 0: Setup

To build the container, use the following command:

`sudo docker build -t flask-hidden . `

Now the container can be started with this command:

`sudo docker run -d -p 6969:5000 flask-hidden`

The docker container port `5000` should be exposed to the port `6969`!

---

### Pt. 1: Gobuster

After its up, we can discover the hidden paths wir gobuster:

`sudo gobuster dir -u http://localhost:6969 -w /path/to/wordlist`

---

### Pt. 2: Password Cracking

Go to the discovered `/admin` path. There you can read: `haha here is the password, but hashed: ec0e2603172c73a8b644bb9456c1ff6e`.

To crack it, you can use hashcat:

`echo "ec0e2603172c73a8b644bb9456c1ff6e" > hashes.txt`

`hashcat -m 0 -a 0 -o cracked.txt hashes.txt /usr/share/wordlists/rockyou.txt`

`echo cracked.txt`

---

### Pt. 3: XSS

Go to the discovered `/secret` route. 