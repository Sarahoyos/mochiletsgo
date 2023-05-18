const username = document.getElementById('username')
const password1 = document.getElementById('password1')
const password2 = document.getElementById('password2')
const registro = document.getElementById('signup')  
const signupbtn = document.getElementById('signupbtn')


function enviarDatos(evento) {
    evento.preventDefault(); 
    const datos = {
        username: username.value,
        password1: password1.value, 
        password2: password2.value,
    }   
    console.log('datos',datos)
};
fetch ('https://mochiletsgo.herokuapp.com/signup/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(datos),
})
.then((response) => response.json())
.then(data => {
    // Process the data received from the backend
    console.log(data);
  })

signup.onsubmit = enviarDatos;
signupbtn.onclick = enviarDatos;

