var demo=[
    {
        'demo':2
    },
    {
        'demo':3
    },
    {
        'demo':7
    },
    {
        'demo':3
    },
    {
        'demo':2
    },
    {
        'demo':5
    }
]
var spacedem=document.getElementById('demo')
spacedem.setAttribute('id','spacedem')
var subspacedmo=document.createElement('div')
subspacedmo.setAttribute('id','spacedemo')
// spacedem.append(subspacedmo)
demo.forEach((demoelement)=>{
    var homebulle=document.createElement('div');
    homebulle.setAttribute('id','homebulle') 
var bulle=document.createElement('div');
bulle.setAttribute('class','bulle');
var baget=document.createElement('div');
    baget.setAttribute('id','baget') 
    bulle.append(baget)
    

bulle.style.position='relative';
bulle.style.top=''+(demoelement.demo*10)+'px';
if(demoelement.demo<4){
    bulle.style.backgroundColor='rgb(70, 41, 41)';

}else{
    bulle.style.backgroundColor='darkgreen';
}
baget.style.height=''+(demoelement.demo*100)+'px';

bulle.style.width='10px';
bulle.style.height='10px';

bulle.onclick=function(){
    if(bulle.style.width=='10px'){
  homebulle.style.width='15%'
    bulle.style.width='90%'
    bulle.style.height='90%'
    bulle.style.position='relative';
bulle.style.top=''+(5)+'px';
    }else{
        bulle.style.position='relative';
        homebulle.style.width='5%';
        bulle.style.width='10px';
        bulle.style.height='10px';
        bulle.style.top=''+(demoelement.demo*10)+'px';
    }
  
}

// homebulle.append(bulle)
// subspacedmo.append(homebulle)



})