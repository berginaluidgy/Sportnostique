var taksearch=document.getElementById('search')
var btn=document.getElementById('btn')
var form=document.getElementById('form')
var solissearch=document.getElementById('containersolissearch')
console.log(window.location.host)
    form.onsubmit=()=>{
console.log(btn.value)

async function getdata() {
     console.log('https://'+window.location.host+'/getuser/'+taksearch.value)
    const response = await fetch('http://'+window.location.host+'/getuser/'+taksearch.value);
    const data = await response.json();
    var nameusergetparent=document.createElement('div')
    var nameusergetparentw=document.createElement('div')
    var nameusergetparentclique=document.createElement('div')


    var nameusergetname=document.createElement('div')
    var nameusergetprenom=document.createElement('div')
    var nameusergetdate=document.createElement('div')
    var nameusergetisactif=document.createElement('div')
    var nameusergetclique=document.createElement('div')


    var nameusergetnamep=document.createElement('p')
    nameusergetnamep.innerHTML=data.name
    var nameusergetprenomp=document.createElement('p')
    nameusergetprenomp.innerHTML=data.prenom
    var nameusergetdatep=document.createElement('p')
    nameusergetdatep.innerHTML=data.date

    var nameusergetisactifp=document.createElement('p')
    if(data.isactif==true){
      nameusergetisactifp.innerHTML='ACTIVER' 
    }else{
        nameusergetisactifp.innerHTML='DESACTIVER'
    }
    

    
    console.log(data)
    nameusergetname.append(nameusergetnamep)
    nameusergetprenom.append(nameusergetprenomp)
    nameusergetdate.append(nameusergetdatep)
    nameusergetisactif.append(nameusergetisactifp)
    

    nameusergetparentclique.append(nameusergetclique)
    nameusergetparentw.append(nameusergetname,nameusergetprenom,nameusergetdate,nameusergetisactif)
    nameusergetparent.append(nameusergetparentw)
    solissearch.append(nameusergetparent)
    nameusergetisactifp.onclick=()=>{
        console.log(nameusergetclique)
    async function getdata() {
     
        const response = await fetch('https://'+window.location.host+'/checking/'+taksearch.value);
        const data = await response.json();
        console.log(data)
        if(data.isactif==true){
            nameusergetisactifp.innerHTML='ACTIVER' 
          }else{
              nameusergetisactifp.innerHTML='DESACTIVER'
          }
          
    }
    getdata()

}
     
}
getdata()



console.log(3)

return false
    }


   
