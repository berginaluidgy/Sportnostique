
var countryparent=document.getElementById('containerleague')

// var previewsparent=document.getElementById('stars')

// var previewsgoldparent=document.createElement('div')
// previewsgoldparent.setAttribute('id','previewsgoldparent')
// var previewsgoldparentbis=document.createElement('div')
// previewsgoldparentbis.setAttribute('id','previewsgoldparentbis')

// var statspreviews=document.createElement('div')
// statspreviews.setAttribute('id','statspreviews')
// var statspreviewtext=document.createElement('p')
// statspreviewtext.innerHTML='Stats';
// var pronospreviewtext=document.createElement('p')
// pronospreviewtext.innerHTML='Autre Pronos';

// statspreviews.append(statspreviewtext,pronospreviewtext)
// console.log(statspreviews)

// var previewsgoldfirst=document.createElement('div')
// previewsgoldfirst.setAttribute('id','previewsgoldfirst')
// var previewsgoldfirstcountryname=document.createElement('p')
// previewsgoldfirstcountryname.innerHTML='Spain';
// previewsgoldfirstcountryname.setAttribute('id','previewsgoldfirstcountryname')
// var previewsgoldfirstdate=document.createElement('p')
// previewsgoldfirstdate.innerHTML='12h:30'
// previewsgoldfirstdate.setAttribute('id','previewsgoldfirstdate')
// previewsgoldfirst.append(previewsgoldfirstcountryname,previewsgoldfirstdate)

// var previewsgoldsecond=document.createElement('div')
// previewsgoldsecond.setAttribute('id','previewsgoldsecond')
// var previewsgoldsecondconname=document.createElement('div')
// previewsgoldsecondconname.setAttribute('id','previewsgoldsecondconname')
// var previewsgoldsecondname1=document.createElement('p')
// previewsgoldsecondname1.innerHTML='Barcaelona'
// previewsgoldsecondname1.setAttribute('id','previewsgoldsecondname1')
// var previewsgoldsecondseparator=document.createElement('p')
// previewsgoldsecondseparator.innerHTML='VS';
// previewsgoldsecondseparator.setAttribute('id','previewsgoldsecondseparator')
// var previewsgoldsecondname2=document.createElement('p')
// previewsgoldsecondname2.setAttribute('id','previewsgoldsecondname2')
// previewsgoldsecondname2.innerHTML='Real Madrid'

// previewsgoldsecondconname.append(previewsgoldsecondname1,previewsgoldsecondname2)


// var previewsgoldsecondpronos=document.createElement('div')
// previewsgoldsecondpronos.setAttribute('id','previewsgoldsecondpronos')
// var previewsgoldsecondinfo=document.createElement('p')
// previewsgoldsecondinfo.innerHTML='PRONOSTIQUE'
// previewsgoldsecondinfo.setAttribute('id','previewsgoldsecondinfo')
// var previewsgoldseconddefinitive=document.createElement('p')
// previewsgoldseconddefinitive.innerHTML='TOTAL +1.5'

// previewsgoldseconddefinitive.setAttribute('id','previewsgoldseconddefinitive')

// previewsgoldsecondpronos.append(previewsgoldsecondinfo,previewsgoldseconddefinitive)

// previewsgoldsecond.append(previewsgoldsecondconname,previewsgoldsecondpronos);


// previewsgoldparent.append(previewsgoldfirst,previewsgoldsecond)
// previewsgoldparentbis.append(previewsgoldparent,statspreviews)
// previewsparent.append(previewsgoldparentbis)


// console.log(previewsparent)







var xhr = new XMLHttpRequest();
xhr.withCredentials =false;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
   var  respons=JSON.parse(this.responseText)
    var  restrue=respons.response
    restrue.forEach((element)=>{
      console.log(element.name)
      if(element.name !='Antigua-And-Barbuda' || element.name !='Haiti' || element.name !='Myanmar'){

   
      var bigparent=document.createElement('div')
        var country=document.createElement('div')
        country.setAttribute('id','country')
        var countryflag=document.createElement('div')
        countryflag.setAttribute('id','countryflag')

        var countryflagimage=document.createElement('img')
        countryflagimage.setAttribute('id','countryflagimage')
        countryflagimage.src=element.flag;
        var countrypcon=document.createElement('div')
        countrypcon.setAttribute('id','countrypcon')
        var countryp=document.createElement('p')
        countryp.setAttribute('id','countryp')
        countryp.innerHTML=element.name;

        var league=document.createElement('div');
       
       league.setAttribute('id','league')
        
       league.style.display='none'
        countryflag.append(countryflagimage)
        countrypcon.append(countryp)
        country.append(countryflag,countrypcon)
bigparent.append(country,league)
        countryparent.append(bigparent)
        console.log(league.style.display)
country.onclick=()=>{
  if(league.style.display=='none'){
    league.style.display='block'
    var xhr = new XMLHttpRequest();
xhr.withCredentials =false;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
   var  respons=JSON.parse(this.responseText)
    var  restrue2=respons.response
console.log(restrue2.length)
    restrue2.forEach((element2)=>{
      console.log(element2)
 console.log(element2.seasons[0].coverage.standings,0) 
 if (element2.seasons[0].coverage.standings==true){

 
      var text=document.createElement('p')

text.innerHTML=element2.league.name;
league.append(text) 
console.log(element2)
var id=element2.league.id
console.log(id)
text.onclick=()=>{
     var containerallbet=document.createElement('div')
     containerallbet.setAttribute('id','containerallbet')
     var childparentx=document.createElement('div')
      childparentx.setAttribute('id','childparentx2')

     var childparentxp=document.createElement('p')
       childparentxp.innerHTML='Sortir'
      childparentxp.style.fontSize='17px'
      childparentxp.style.fontWeight='bolder'
      childparent.style.position='absolute';
      childparent.style.top='0%';
      childparent.style.left='0%';
      childparent.style.width='100%';
      childparent.style.height='100%';
      childparent.style.background='whitesmoke';
      childparent.style.display='none';
      containerallbet.append(childparentx)
      childparentx.append(childparentxp)

    childparentx.onclick=()=>{
      if(containerallbet.style.display=='block'){
        containerallbet.style.display='none';
      }else{
        containerallbet.style.display='block';
      }
    }
    var bodybet=document.body;
    
    
    bodybet.append(containerallbet)
    var xhr = new XMLHttpRequest();
    xhr.withCredentials =false;
    
    xhr.addEventListener("readystatechange", function() {
      if(this.readyState === 4) {
       var  respons=JSON.parse(this.responseText)
        var  restrue=respons.response
        console.log(restrue)
             
        var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;  



    }
console.log('res')

      restrue.forEach((fix)=>{
      
        var betid=fix.fixture.id;
        var betidleague=fix.league.id;
 console.log(betid,betidleague)
        console.log(betid)
        async function getdata() {
          setTimeout(()=>{

          },10000)
          const response = await fetch('https://'+window.location.host+"/Pronos/"+betid+"/"+betidleague);
          const data = await response.json();
          console.log(data);
            console.log(data.stats,data.Pronos)
            var corps=document.createElement('div')
corps.setAttribute('id','corps')
var entete=document.createElement('div')
entete.setAttribute('id','entete')
var pricipale=document.createElement('div')
pricipale.setAttribute('id','pricipale')
corps.append(entete,pricipale)

var names=document.createElement('div')
names.setAttribute('id','names')
var stats=document.createElement('div')
stats.setAttribute('id','stats')
entete.append(names,stats)
var namesp=document.createElement('p')
namesp.setAttribute('id','namesp')
var statsp=document.createElement('p')
statsp.setAttribute('id','statsp')
namesp.innerHTML=data.stats[0].nameteam + '  VS   '+ data.stats[1].nameteam ;
namesp.setAttribute('id','namesp')
statsp.innerHTML='Stats';
names.append(namesp)
stats.append(statsp)
var pronosall=[data.Pronos,data.Pronos2,data.Pronoscorner,data.Pronosnosafe,data.Pronosnosafe1,data.Pronosnosafe2,data.Pronosnosafe2,data.Pronosnotmestudy]

pronosall.forEach((unique)=>{
  var pricipalechilds=document.createElement('div')
  pricipalechilds.setAttribute('id','pricipalechilds')
  var plchild=document.createElement('p')
  plchild.setAttribute('id','plchild')
  plchild.innerHTML=unique[0];
  pricipalechilds.append(plchild)
  pricipale.append(pricipalechilds)

})


containerallbet.append(corps)

var pagecontainer=document.getElementById('allstats')
  
stats.onclick=()=>{
  if(pagecontainer.style.display=='none'){

    pagecontainer.style.display='block'
  var tabstast=["rank",
"buttotal",
"butencaisser",
"buttotalalamaison",
"butencaisseralamaison",
"buttotalalexterieur",
"butencaisseralexterieur",
"matchplay",
"matchplaywin",
"matchplaylose",
"matchplaynull",
"matchplayalamaison",
"matchplaywinalamaison",
"matchplaylosealamaison",
"matchplaynullalamaison",
"matchplayalexterieur",
"matchplaywinalexterieur",
"matchplaylosealexterieur",
"matchplaynullalexterieur"]
tabstast.forEach((unique)=>{
    if(unique=="rank"){
    var setcontainerdiv=document.getElementById(unique)
    setcontainerdiv.childNodes[0].innerHTML= 'Classement :'+data.rank

    }
    else if(unique=="buttotal"){
      var setcontainerdiv=document.getElementById(unique)
      setcontainerdiv.childNodes[0].innerHTML='But Total marques:'+data.buttotal
  
      }
      else if(unique=="butencaisser"){
        var setcontainerdiv=document.getElementById(unique)
        setcontainerdiv.childNodes[0].innerHTML='But Total Encaisser: '+data.buttotal
    
        }
        else if(unique=="buttotalalamaison"){
          var setcontainerdiv=document.getElementById(unique)
          setcontainerdiv.childNodes[0].innerHTML='But Total marquer a la maison :'+buttotalalamaison
      
          }
          else if(unique=="butencaisseralamaison"){
            var setcontainerdiv=document.getElementById(unique)
            setcontainerdiv.childNodes[0].innerHTML= 'But Total encaisser a la maison :  '+data.butencaisseralamaison
        
            }
            else if(unique=="buttotalalexterieur"){
              var setcontainerdiv=document.getElementById(unique)
              setcontainerdiv.childNodes[0].innerHTML= "But total marquer a l'eterieur : "+data.buttotalalexterieur
          
              }
              else if(unique=="butencaisseralexterieur"){
                var setcontainerdiv=document.getElementById(unique)
                setcontainerdiv.childNodes[0].innerHTML="But total encaisser a l'eterieur : " + data.butencaisseralexterieur
            
                }
                else if(unique=="matchplay"){
                  var setcontainerdiv=document.getElementById(unique)
                  setcontainerdiv.childNodes[0].innerHTML='Match Total Jouer: '+data.buttotal
              
                  }
                  else if(unique=="matchplaywin"){
                    var setcontainerdiv=document.getElementById(unique)
                    setcontainerdiv.childNodes[0].innerHTML='Total gagner: '+data.matchplaywin
                
                    }
                    else if(unique=="matchplaylose"){
                      var setcontainerdiv=document.getElementById(unique)
                      setcontainerdiv.childNodes[0].innerHTML='Total Perdu :'+data.buttotal
                  
                      }
                      else if(unique=="matchplaynull"){
                        var setcontainerdiv=document.getElementById(unique)
                        setcontainerdiv.childNodes[0].innerHTML='Total null: '+data.matchplaynull
                    
                        }
                        else if(unique=="matchplayalamaison"){
                          var setcontainerdiv=document.getElementById(unique)
                          setcontainerdiv.childNodes[0].innerHTML='Match Jouer a la maison : '+data.matchplayalamaison
                      
                          }
                          else if(unique=="matchplaywinalamaison"){
                            var setcontainerdiv=document.getElementById(unique)
                            setcontainerdiv.childNodes[0].innerHTML='Match gagner a la maison : '+data.matchplaywinalamaison
                        
                            }
                            else if(unique=="matchplaylosealamaison"){
                              var setcontainerdiv=document.getElementById(unique)
                              setcontainerdiv.childNodes[0].innerHTML='Match perdu a la maison :' +data.matchplaylosealamaison
                          
                              }
                              else if(unique=="matchplaynullalamaison"){
                                var setcontainerdiv=document.getElementById(unique)
                                setcontainerdiv.childNodes[0].innerHTML= 'Match null a la Maison :'+ data.matchplaynullalamaison
                            
                                }
                                else if(unique=="matchplayalexterieur"){
                              var setcontainerdiv=document.getElementById(unique)
                              setcontainerdiv.childNodes[0].innerHTML='match jouer a l exterieur :'+data.matchplayalexterieur
                          
                              }
                              else if(unique=="matchplaywinalexterieur"){
                                var setcontainerdiv=document.getElementById(unique)
                                setcontainerdiv.childNodes[0].innerHTML='Match jouer et Gagner : '+ matchplaywinalexterieur
                            
                                }
                                else if(unique=="matchplaylosealexterieur"){
                                  var setcontainerdiv=document.getElementById(unique)
                                  setcontainerdiv.childNodes[0].innerHTML='Match jouer et perdu : '+data.matchplaylosealexterieur
                              
                                  }
                                  else if(unique=="matchplaynullalexterieur"){
                                    var setcontainerdiv=document.getElementById(unique)
                                    setcontainerdiv.childNodes[0].innerHTML='Match jouer et null a l exterieur : '+data.matchplaynullalexterieur
                                
                                    }
                                    else{
                                      
                                    }
                                    var tabstast=["rank2",
                                    "buttotal2",
                                    "butencaisser2",
                                    "buttotalalamaison2",
                                    "butencaisseralamaison2",
                                    "buttotaalexterieur2",
                                    "butencaisseralexterieur2",
                                    "matchplay2",
                                    "matchplaywin2",
                                    "matchplaylose2",
                                    "matchplaynull2",
                                    "matchplayalamaison2",
                                    "matchplaywinalamaison2",
                                    "matchplaylosealamaison2",
                                    "matchplaynullalamaison2",
                                    "matchplayalexterieur2",
                                    "matchplaywinalexterieur2",
                                    "matchplaylosealexterieur2",
                                    "matchplaynullalexterieur2"]
                                    tabstast.forEach((unique)=>{
                                        if(unique=="rank2"){
                                        var setcontainerdiv=document.getElementById(unique)
                                        setcontainerdiv.childNodes[0].innerHTML= 'Classement :'+data.rank
                                    
                                        }
                                        else if(unique=="buttotal2"){
                                          var setcontainerdiv=document.getElementById(unique)
                                          setcontainerdiv.childNodes[0].innerHTML='But Total marques:'+data.buttotal
                                      
                                          }
                                          else if(unique=="butencaisser2"){
                                            var setcontainerdiv=document.getElementById(unique)
                                            setcontainerdiv.childNodes[0].innerHTML='But Total Encaisser: '+data.buttotal
                                        
                                            }
                                            else if(unique=="buttotalalamaison2"){
                                              var setcontainerdiv=document.getElementById(unique)
                                              setcontainerdiv.childNodes[0].innerHTML='But Total marquer a la maison :'+buttotalalamaison
                                          
                                              }
                                              else if(unique=="butencaisseralamaison2"){
                                                var setcontainerdiv=document.getElementById(unique)
                                                setcontainerdiv.childNodes[0].innerHTML= 'But Total encaisser a la maison :  '+data.butencaisseralamaison
                                            
                                                }
                                                else if(unique=="buttotalalexterieur2"){
                                                  var setcontainerdiv=document.getElementById(unique)
                                                  setcontainerdiv.childNodes[0].innerHTML= "But total marquer a l'eterieur : "+data.buttotalalexterieur
                                              
                                                  }
                                                  else if(unique=="butencaisseralexterieur2"){
                                                    var setcontainerdiv=document.getElementById(unique)
                                                    setcontainerdiv.childNodes[0].innerHTML="But total encaisser a l'eterieur : " + data.butencaisseralexterieur
                                                
                                                    }
                                                    else if(unique=="matchplay2"){
                                                      var setcontainerdiv=document.getElementById(unique)
                                                      setcontainerdiv.childNodes[0].innerHTML='Match Total Jouer: '+data.buttotal
                                                  
                                                      }
                                                      else if(unique=="matchplaywin2"){
                                                        var setcontainerdiv=document.getElementById(unique)
                                                        setcontainerdiv.childNodes[0].innerHTML='Total gagner: '+data.matchplaywin
                                                    
                                                        }
                                                        else if(unique=="matchplaylose2"){
                                                          var setcontainerdiv=document.getElementById(unique)
                                                          setcontainerdiv.childNodes[0].innerHTML='Total Perdu :'+data.buttotal
                                                      
                                                          }
                                                          else if(unique=="matchplaynull2"){
                                                            var setcontainerdiv=document.getElementById(unique)
                                                            setcontainerdiv.childNodes[0].innerHTML='Total null: '+data.matchplaynull
                                                        
                                                            }
                                                            else if(unique=="matchplayalamaison2"){
                                                              var setcontainerdiv=document.getElementById(unique)
                                                              setcontainerdiv.childNodes[0].innerHTML='Match Jouer a la maison : '+data.matchplayalamaison
                                                          
                                                              }
                                                              else if(unique=="matchplaywinalamaison2"){
                                                                var setcontainerdiv=document.getElementById(unique)
                                                                setcontainerdiv.childNodes[0].innerHTML='Match gagner a la maison : '+data.matchplaywinalamaison
                                                            
                                                                }
                                                                else if(unique=="matchplaylosealamaison2"){
                                                                  var setcontainerdiv=document.getElementById(unique)
                                                                  setcontainerdiv.childNodes[0].innerHTML='Match perdu a la maison :' +data.matchplaylosealamaison
                                                              
                                                                  }
                                                                  else if(unique=="matchplaynullalamaison2"){
                                                                    var setcontainerdiv=document.getElementById(unique)
                                                                    setcontainerdiv.childNodes[0].innerHTML= 'Match null a la Maison :'+ data.matchplaynullalamaison
                                                                
                                                                    }
                                                                    else if(unique=="matchplayalexterieur2"){
                                                                  var setcontainerdiv=document.getElementById(unique)
                                                                  setcontainerdiv.childNodes[0].innerHTML='match jouer a l exterieur :'+data.matchplayalexterieur
                                                              
                                                                  }
                                                                  else if(unique=="matchplaywinalexterieur2"){
                                                                    var setcontainerdiv=document.getElementById(unique)
                                                                    setcontainerdiv.childNodes[0].innerHTML='Match jouer et Gagner : '+ matchplaywinalexterieur
                                                                
                                                                    }
                                                                    else if(unique=="matchplaylosealexterieur2"){
                                                                      var setcontainerdiv=document.getElementById(unique)
                                                                      setcontainerdiv.childNodes[0].innerHTML='Match jouer et perdu : '+data.matchplaylosealexterieur
                                                                  
                                                                      }
                                                                      else if(unique=="matchplaynullalexterieur2"){
                                                                        var setcontainerdiv=document.getElementById(unique)
                                                                        setcontainerdiv.childNodes[0].innerHTML='Match jouer et null a l exterieur : '+data.matchplaynullalexterieur
                                                                    
                                                                        }
                                                                        else{
                                                                          
                                                                        }
                                                                      
                                                                    
                                    })
                                
})
  }else{
    pagecontainer.style.display='none'
  }
}

        }
        getdata()

        
        
          
           
      })
       
  
    });
    
    xhr.open("GET", 'https://v3.football.api-sports.io/fixtures?league='+id+'&season=2023&status=NS');
    xhr.setRequestHeader("x-rapidapi-key", "2f554e59b05daef4304c2752e4fff0a8");
    xhr.setRequestHeader("x-rapidapi-host", "v3.football.api-sports.io");
    
    xhr.send();
}

   






 }

})
   









  }
});

xhr.open("GET", 'https://v3.football.api-sports.io/leagues?country='+element.name+'&season=2023');
xhr.setRequestHeader("x-rapidapi-key", "2f554e59b05daef4304c2752e4fff0a8");
xhr.setRequestHeader("x-rapidapi-host", "v3.football.api-sports.io");

xhr.send();



  }else{
    league.style.display='none';
    console.log(league.childNodes)
    league.removeChild

    league.childNodes.forEach((pelement)=>{
pelement.innerHTML=''

    })
console.log(league.childNodes)
  }
}
        /*--------------------------------------------------------- */

     } })
    console.log(respons.response)

  }
});

xhr.open("GET", "https://v3.football.api-sports.io/countries");
xhr.setRequestHeader("x-rapidapi-key", "2f554e59b05daef4304c2752e4fff0a8");
xhr.setRequestHeader("x-rapidapi-host", "v3.football.api-sports.io");

xhr.send();
