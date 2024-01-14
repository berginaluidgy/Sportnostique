
  var boyy=document.body;

    var childparent=document.createElement('div')
    childparent.setAttribute('id','childparend')
   















    
      var childparentx=document.createElement('div')
      childparentx.setAttribute('id','childparentx')
     var childparentxp=document.createElement('p')
       childparentxp.innerHTML='Sortir'
      childparentxp.style.fontSize='17px'
      childparentxp.style.fontWeight='bolder'
      childparent.style.position='absolute';
      childparent.style.top='0%';
      childparent.style.left='0%';
      childparent.style.width='100%';
      childparent.style.height='100%';
      childparent.style.background='white';
      childparent.style.display='none';

    
      var childparentcontainer=document.createElement('div')
      childparentxp.onclick=()=>{
        childparent.style.display='none'
      }
      childparentx.append(childparentxp)
     childparent.append(childparentx,childparentcontainer)
     boyy.appendChild(childparent)
//--------------------------------------------

var generateparent=document.getElementById('subgenerate')

console.log(generateparent.childNodes)
generateparent.childNodes.forEach(element => {
    if(element.childNodes.length==1){
        console.log(element.id)

var elements=document.getElementById(element.id)
elements.onclick=()=>{
  
 
    childparent.style.display='block';

}


    }
    
});