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