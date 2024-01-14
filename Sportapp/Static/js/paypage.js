var clickunder=document.getElementById('inf')
var clickbtn=document.getElementById('btn')
clickbtn.onclick=()=>{
if(clickunder.style.display=='none'){
    clickunder.style.display='block';

}else{
    clickunder.style.display='none'
}
}


// async function postJSON(data) {
//   try {
//     const response = await fetch('http://localhost:8000/pay', {
//       method: "POST", // or 'PUT'
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify(data),
//     });

//     const result = await response.json();
//     console.log("Success:", result);
//   } catch (error) {
//     console.error("Error:", error);
//   }
// }

// const data = { username: "example" };
// postJSON(data);
var payclick=document.getElementById('pay')
payclick.onclick=()=>{
window.location.href='https://surveyheart.com/form/6599d92c2b329e09602ea625';
}
