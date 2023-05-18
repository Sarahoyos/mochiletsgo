const username = document.getElementById('username')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
const signinbtn = document.getElementById('signinbtn')


function enviarDatos(evento) {
    evento.preventDefault();
    const datos = {
        username: username.value,
        password1: password1.value,
        password2: password2.value,

    }
    console.log('datos',datos)
};

login.onsubmit = enviarDatos;
signinbtn.onclick = enviarDatos;