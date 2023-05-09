const username = document.getElementById('username')
const email = document.getElementById('email')
const password = document.getElementById('password')
const registro = document.getElementById('registro')
const signupbtn = document.getElementById('signupbtn')


function enviarDatos(evento) {
    evento.preventDefault();
    const datos = {
        username: username.value,
        email: email.value,
        password: password.value,
    }
    console.log('datos',datos)
};

registro.onsubmit = enviarDatos;
signupbtn.onclick = enviarDatos;