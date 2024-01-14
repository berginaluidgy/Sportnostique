var login=document.getElementById('login')
var signup=document.getElementById('signup')
var labelnom=document.getElementById('forname')
var nom=document.getElementById('nom')
var prenom=document.getElementById('Prenom')
var labelprenom=document.getElementById('labelprenom')
var labelphone=document.getElementById('labelphone')
var what=document.getElementById('what')
var csn=document.getElementById('csn')
csn.name='choose'
var authparent=document.getElementById('authsystemparent')
// authparent.style.display='none'
form=document.getElementById('formauth')
form.method='post';

// var email=document.getElementById('email')
var tel=document.getElementById('phone')
var password=document.getElementById('passe')
var submit=document.getElementById('submit')
var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
// submit.onclick=()=>{
 
//      form.method='post';}
    
login.onclick=()=>{

    what.innerHTML='CONNEXION'
    tel.style.display='none';
    labelphone.style.display='none';
    prenom.style.display='none';
    labelprenom.style.display='none';
    console.log(login,nom,submit)
    submit.innerHTML='Se Connecter';
    console.log(submit)
    csn.value='login';
    form.method='post';
    
    
    authparent.style.display='flex';
    
}
signup.onclick=()=>{
    what.innerHTML='INSCRIPTION'
    nom.style.display='block';
    labelnom.style.display='block';
    prenom.style.display='block';
    labelprenom.style.display='block';
    console.log(login,nom,submit)
   
    submit.innerHTML="S'Inscrire";
    console.log(submit)
    csn.value='signup';
   
    authparent.style.display='flex';
    
    
// // const xhr = new XMLHttpRequest();
// // xhr.open("POST", "http://localhost:8000/signup");
// // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
// // xhr.setRequestHeader('X-CSRFToken',csrfToken);
// // const body = JSON.stringify({
// //     name:nom.value,
// //     prenom:prenom.value,
// //     password:password.value,
// // });
// // xhr.onload = () => {
// //     console.log(JSON.parse(xhr.responseText));
// // };
// // xhr.send(body);

// // console.log(body)

//     }


}




