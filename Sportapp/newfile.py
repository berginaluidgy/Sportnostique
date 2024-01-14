import requests
import pprint
import time
def callstatsPronostics(fixtureparent,league):
  id=str(fixtureparent)
  envleague=league
  def base(endpoint):
    time.sleep(1)
    url ="https://v3.football.api-sports.io/"+endpoint
    headers={
      'x-rapidapi-key': '2f554e59b05daef4304c2752e4fff0a8',
      'x-rapidapi-host': 'v3.football.api-sports.io'}
    response = requests.request("GET", url, headers=headers)
    resjson=response.json()
    
    return resjson['response']


  def scrapedatafixture():
   
    rencontre=base('fixtures?id='+id)
   
    responseone=rencontre[0]
    etude={
    'stade':responseone['fixture']['venue']['name'],
    'satus':responseone['fixture']['status']['short'],
    'league-id':responseone['league']['id'],
    'league-name':responseone['league']['name'],
    'league-logo':responseone['league']['logo'],
    'teamhomeid':responseone['teams']['home']['id'],
    'teamawayid':responseone['teams']['away']['id'],
    'teamhomename':responseone['teams']['home']['name'],
    'teamawayname':responseone['teams']['away']['name'],
  }
    return etude

  standing=base('standings?league='+str(envleague)+'&season=2023')
 
  scrap=scrapedatafixture()

  statsAndpronostics=[]


  def statteam(scrapid):
    
  # standteam1=base('standings?league=140&season=2023&team='+str(scrap[scrapid]))
    standteam1=base('standings?league='+str(envleague)+'&season=2023&team='+str(scrapid))
    print('standings?league='+str(envleague)+'&season=2023&team='+str(scrapid))
    print('ok')
    team1stat={
    'rank':standteam1[0]['league']['standings'][0][0]['rank'],
    'buttotal':standteam1[0]['league']['standings'][0][0]['all']['goals']['for'],
    'butencaisser':standteam1[0]['league']['standings'][0][0]['all']['goals']['against'],
    'buttotalalamaison':standteam1[0]['league']['standings'][0][0]['home']['goals']['for'],
    'butencaisseralamaison':standteam1[0]['league']['standings'][0][0]['home']['goals']['against'],
    'buttotalalexterieur':standteam1[0]['league']['standings'][0][0]['away']['goals']['for'],
    'butencaisseralexterieur':standteam1[0]['league']['standings'][0][0]['away']['goals']['against'],
    'matchplay':standteam1[0]['league']['standings'][0][0]['all']['played'],
    'matchplaywin':standteam1[0]['league']['standings'][0][0]['all']['win'],
    'matchplaylose':standteam1[0]['league']['standings'][0][0]['all']['lose'],
    'matchplaynull':standteam1[0]['league']['standings'][0][0]['all']['draw'],
    
    'matchplayalamaison':standteam1[0]['league']['standings'][0][0]['home']['played'],
    'matchplaywinalamaison':standteam1[0]['league']['standings'][0][0]['home']['win'],
    'matchplaylosealamaison':standteam1[0]['league']['standings'][0][0]['home']['lose'],
    'matchplaynullalamaison':standteam1[0]['league']['standings'][0][0]['home']['draw'],
    'buttotalalamaison':standteam1[0]['league']['standings'][0][0]['home']['goals']['for'],
    'butencaisseralamaison':standteam1[0]['league']['standings'][0][0]['home']['goals']['against'],
    
    'matchplayalexterieur':standteam1[0]['league']['standings'][0][0]['away']['played'],
    'matchplaywinalexterieur':standteam1[0]['league']['standings'][0][0]['away']['win'],
    'matchplaylosealexterieur':standteam1[0]['league']['standings'][0][0]['away']['lose'],
    'matchplaynullalexterieur':standteam1[0]['league']['standings'][0][0]['away']['draw'],
    'buttotalalexterieur':standteam1[0]['league']['standings'][0][0]['away']['goals']['for'],
    'butencaisseralexterieur':standteam1[0]['league']['standings'][0][0]['away']['goals']['against'],
 
}
    return team1stat
#--------------------------------------------------------------------------------------
  body=base('fixtures?id='+id)
  res=body

  scrapidteam1=res[0]['teams']['home']['id']
  scrapidteam2=res[0]['teams']['away']['id']

  
  tabteam=[scrapidteam1,scrapidteam2]
  test=[]
  for team in tabteam:
    nameteam=''
    if team ==res[0]['teams']['home']['id']:
      nameteam=res[0]['teams']['home']['name']
      
    else:
      nameteam=res[0]['teams']['away']['name']
      
    
    print(team)
    teamdata=base('fixtures?league='+str(envleague)+'&season=2023&team='+str(team)+'&status=FT')
    tailleteamdata=len(teamdata)
    round="Regular Season - "
    indicedata=tailleteamdata-1
    tab3event=[]
    nbrbut=[]
    nbrdebut=[]
    nbrbutencaisse=[]
    nbrcartonjaune=[]
    nbrcartonrouge=[]
    nbrdecorner=[]
    nbrdebutmitan=[]
    nbrdebut2mitan=[]
    win=[]
    lose=[]
    draw=[]
    arretdegardien=[]
    TotalShotstab=[]
    Foulstab=[]
    Cornertab=[]
    BallPossessiontab=[]
    #----------------------------------------------------------------------------
    tab3event5=[]
    nbrbut5=[]
    nbrdebut5=[]
    nbrbutencaisse5=[]
    nbrcartonjaune5=[]
    nbrcartonrouge5=[]
    nbrdecorner5=[]
    nbrdebutmitan5=[]
    nbrdebut2mitan5=[]
    win5=[]
    lose5=[]
    draw5=[]
    arretdegardien5=[]
    TotalShotstab5=[]
    Foulstab5=[]
    BallPossessiontab5=[]
    
    
    print('fixtures?'+str(envleague)+'&season=2023&team='+str(team)+'&status=FT')
    for event in teamdata:
      
      roundteam=event['league']['round']
      if roundteam == (round+str(len(teamdata))) or roundteam == (round+str(len(teamdata)-1)) or  roundteam ==(round+str(len(teamdata)-2)) :
        
        idfix=event['fixture']['id']
        scraperescueevent=base('fixtures?id='+str(idfix)) 
        direct1='home'
        direct2='away'
        if scraperescueevent[0]['teams'][direct1]['id']==team:
          nameteam=scraperescueevent[0]['teams'][direct1]['name']
          print(team,'ok',nameteam)
          goaldeam=scraperescueevent[0]['score']['fulltime'][direct1]
          nbrbut.append(goaldeam)
          goaldeammitan=scraperescueevent[0]['score']['halftime'][direct1]
          nbrdebutmitan.append(goaldeammitan)
          nbrdebut2mitan.append((goaldeam-goaldeammitan))
          nbrbutencaisse.append((scraperescueevent[0]['score']['halftime'][direct2]))
        
          if scraperescueevent[0]['teams'][direct1]['winner']== True :
            win.append(True)
          
          elif scraperescueevent[0]['teams'][direct1]['winner']==None:
            draw.append(None)
          
          elif scraperescueevent[0]['teams'][direct1]['winner'] == False:
            lose.append(False)
          
          else:
            pass
          stats= scraperescueevent[0]['statistics']
          
          for sts in stats:
            if sts['team']['id']==team:
                substat= sts['statistics']
                for substs  in substat:
                  if substs['type']=="Corner Kicks":
                    if substs['value']==None:
                      nbrdecorner.append(0)
                    else:
                      kikscorner=substs['value']
                      nbrdecorner.append(kikscorner)
                  elif substs['type']=="Total Shots":  
                    if substs['value']==None:
                      TotalShotstab.append(0)
                    else:
                      totalshots=substs['value']
                      TotalShotstab.append(totalshots)
                    
                  elif substs['type']=="Fouls": 
                    if substs['value']==None:
                      Foulstab.append(0)
                    else: 
                      fouls=substs['value']  
                      Foulstab.append(fouls)
                  elif substs['type']=="Yellow Cards": 
                    if substs['value']==None:
                      nbrcartonjaune.append(0)
                    else:  
                      YellowCard=substs['value'] 
                      nbrcartonjaune.append(YellowCard)
                  elif substs['type']=="Red Cards":   
                    if substs['value']==None:
                      nbrcartonrouge.append(0)
                    else: 
                      RedCards=substs['value'] 
                      nbrcartonrouge.append(RedCards)
                  elif substs['type']=="Ball Possession": 
                    if substs['value']==None:
                      BallPossessiontab.append(0)
                    else: 
                      bps=substs['value']
                      BallPossessiontab.append(bps)
                  else:
                    pass
           
                  
        else:
          goaldeam= event['score']['fulltime'][direct2]
          goaldeam=scraperescueevent[0]['score']['fulltime'][direct2]
          nbrbut.append(goaldeam)
          goaldeammitan=scraperescueevent[0]['score']['halftime'][direct2]
          nbrdebutmitan.append(goaldeammitan)
          nbrdebut2mitan.append((goaldeam-goaldeammitan))
          nbrbutencaisse.append((scraperescueevent[0]['score']['halftime'][direct2]))
          if scraperescueevent[0]['teams'][direct2]['winner']== True :
            win.append(True)
          
          elif scraperescueevent[0]['teams'][direct2]['winner']==None:
            draw.append(None)
          
          elif scraperescueevent[0]['teams'][direct2]['winner'] == False:
            lose.append(False)
          
          else:
            pass 
        
          stats= scraperescueevent[0]['statistics']
          
          for sts in stats:
            if sts['team']['id']==team:
                substat= sts['statistics']
                for substs  in substat:
                  if substs['type']=="Corner Kicks":
                    if substs['value']==None:
                      nbrdecorner.append(0)
                    else:
                      kikscorner=substs['value']
                      nbrdecorner.append(kikscorner)
                  elif substs['type']=="Total Shots":  
                    if substs['value']==None:
                      TotalShotstab.append(0)
                    else:
                      totalshots=substs['value']
                    
                  elif substs['type']=="Fouls": 
                    if substs['value']==None:
                      Foulstab.append(0)
                    else: 
                      fouls=substs['value']  
                      Foulstab.append(fouls)
                  elif substs['type']=="Yellow Cards": 
                    if substs['value']==None:
                      
                      nbrcartonjaune.append(0)
                    else:  
                      YellowCard=substs['value'] 
                      nbrcartonjaune.append(YellowCard)
                      print(nbrcartonjaune)
                  elif substs['type']=="Red Cards":   
                    if substs['value']==None:
                      nbrcartonrouge.append(0)
                    else: 
                      RedCards=substs['value'] 
                      nbrcartonrouge.append(RedCards)
                  elif substs['type']=="Ball Possession": 
                    if substs['value']==None:
                      BallPossessiontab.append(0)
                    else: 
                      bps=substs['value']
                      BallPossessiontab.append(bps)
                  else:
                    pass
    
          
          
    detailall=statteam(team)    
    dataanalitics={
        'Team':team,
        'nameteam':nameteam,
      
        'all':detailall,
        'moyenne3':{
        
        'but':{
          'nombredebut':sum(nbrbut),
        'moyenne_nombredebut':sum(nbrbut)/3,
          },
        'butencaisser':{
          'nombre_de_but_encaisse':sum(nbrbutencaisse),
        'moyenne_de_but_encaisse':sum(nbrbutencaisse)/3,
          },
        'butmitan':{
          'nombre_de_but_mitan':sum(nbrdebutmitan),
        'moyenne_de_but_mitan':sum(nbrdebutmitan)/3,
          },
        'butmitan2':{
          'nombre_de_but_2mitan':sum(nbrdebut2mitan),
        'moyenne_de_but_2mitan':sum(nbrdebut2mitan)/3,
          },
        'cartonjaune':{
          'nombre_de_carton_jaune':sum(nbrcartonjaune),
        'moyenne_de_carton_jaune':sum(nbrcartonjaune)/3,
          },
      
        'corner':{
          'nombre_de_corner':sum(nbrdecorner),
        'moyenne_de_corner':sum(nbrdecorner)/3,
          },
        'nbrwin':{
          'nombre_de_win':len(win),
        'pourcentage_de_win':(len(win)/3)*100,
          },
        'nbrlose':{
          'nombre_de_lose':len(lose),
        'pourcentage_de_lose':(len(lose)/3)*100,
          },
        'nbrdraw':{
          'nombre_de_draw':len(draw),
        'pourcentage_de_draw':(len(draw)/3)*100,
          
          },
        # 'nbrardugardien':{
        #   'nombre_de_arretdegardien':sum(arretdegardien),
        # 'moyenne_de_arretdegardien':sum(arretdegardien)/3,
        #   },
        'faute':{
          'nombre_de_faute':sum(Foulstab),
        'moyenne_de_faute':sum(Foulstab)/3,
          },
        # 'possession':{
        #   'nombre_de_possession':sum(BallPossessiontab),
        # 'moyenne_de_possession':sum(BallPossessiontab)/3,
        #   },

        
      },
      
      
      
    }
    rankattaque=statteam(team)['buttotal']
    rankdefense=statteam(team)['butencaisser']

    numberang=[]
    numberang2=[]
    tabattaque=[]
    tabdefense=[]
    for stand in standing:
      recup=stand['league']['standings']
      # pprint.pprint(recup)
      
      for teamstat1 in recup:
        for teamstat in teamstat1:
          
          attaque=teamstat['all']['goals']['for']
          defense=teamstat['all']['goals']['against']
          if attaque>rankattaque:
            numberang.append(teamstat)
          if defense<rankdefense:
            numberang2.append(teamstat)  
    classementAttaque=len(numberang)+1
    classementdefense=len(numberang2)+1
    
    dataanalitics['force']={
      'classementdefense':classementdefense,
      'classementAttaque':classementAttaque,
      
    }
    statsAndpronostics.append(dataanalitics)
    
    
    
  return statsAndpronostics
        
       
      


def pronossafe(integerfix,leagueid):
  integerfixx=integerfix
  leagueidd=leagueid
  print(type(integerfixx))
  if type(integerfixx)==int:
      
    statsAndpronostics=callstatsPronostics(integerfixx,leagueidd)
    
    buildStat={"stats":statsAndpronostics}
    print(buildStat)
    teamSensible={
      'team0':{ 
        'allpercentlose0':(statsAndpronostics[0]['all']['matchplaylose']/statsAndpronostics[0]['all']['matchplay'])*100,
        'allpercentwin0':(statsAndpronostics[0]['all']['matchplaywin']/statsAndpronostics[0]['all']['matchplay'])*100,
      'allpercentdraw0':(statsAndpronostics[0]['all']['matchplaynull']/statsAndpronostics[0]['all']['matchplay'])*100,     
      },
      'team1':{
          'allpercentlose0':(statsAndpronostics[1]['all']['matchplaylose']/statsAndpronostics[1]['all']['matchplay'])*100,
        'allpercentwin0':(statsAndpronostics[1]['all']['matchplaywin']/statsAndpronostics[1]['all']['matchplay'])*100,
    'allpercentdraw0':(statsAndpronostics[1]['all']['matchplaynull']/statsAndpronostics[1]['all']['matchplay'])*100,     
      }
    }
    def firstpronos():
      
      
      print(teamSensible)  
      teamSensible['team0']['allpercentlose0']
    #-----------------------------champs regle win and double win and --------------------------------------------
      if statsAndpronostics[0]['all']['rank']>statsAndpronostics[1]['all']['rank']and statsAndpronostics[0]['force']['classementAttaque']<7 and statsAndpronostics[0]['force']['classementdefense']<7 and  statsAndpronostics[1]['force']['classementAttaque']>7 and statsAndpronostics[1]['force']['classementdefense']>7 and statsAndpronostics[0]['moyenne3']['nbrlose']['pourcentage_de_lose']<=20 and statsAndpronostics[0]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=20  and statsAndpronostics[1]['moyenne3']['nbrwin']['pourcentage_de_win']>50 and teamSensible['team0']['allpercentlose0']<40 and teamSensible['team0']['allpercentdraw0']<40:
        buildStat['Pronos']=[str(statsAndpronostics[0]) + ' gagne']
        return buildStat
      elif statsAndpronostics[1]['all']['rank']>statsAndpronostics[0]['all']['rank'] and statsAndpronostics[1]['force']['classementAttaque']<7 and statsAndpronostics[1]['force']['classementdefense']<7 and  statsAndpronostics[0]['force']['classementAttaque']>7 and statsAndpronostics[0]['force']['classementdefense']>7 and statsAndpronostics[1]['moyenne3']['nbrlose']['pourcentage_de_lose']<=20 and statsAndpronostics[1]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=20  and statsAndpronostics[0]['moyenne3']['nbrwin']['pourcentage_de_win']>50 and teamSensible['team1']['allpercentlose0']<40 and teamSensible['team1']['allpercentdraw0']<40:
        
        buildStat['Pronos']=[str(statsAndpronostics[1]) + ' gagne']
        return buildStat
      
      elif statsAndpronostics[0]['all']['rank']>statsAndpronostics[1]['all']['rank'] and statsAndpronostics[0]['force']['classementAttaque']<9 and statsAndpronostics[0]['force']['classementdefense']<9 and  statsAndpronostics[1]['force']['classementAttaque']>9 and statsAndpronostics[1]['force']['classementdefense']>9  and statsAndpronostics[0]['moyenne3']['nbrlose']['pourcentage_de_lose']<=20 and statsAndpronostics[0]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=40  and statsAndpronostics[1]['moyenne3']['nbrwin']['pourcentage_de_win']>30 and teamSensible['team0']['allpercentlose0']<60 and teamSensible['team0']['allpercentdraw0']<60 :
        
        buildStat['Pronos']=[str(statsAndpronostics[0]) + ' gagne ou match null']
        return buildStat
      elif statsAndpronostics[1]['all']['rank']>statsAndpronostics[0]['all']['rank'] and statsAndpronostics[1]['force']['classementAttaque']<9 and statsAndpronostics[1]['force']['classementdefense']<9 and  statsAndpronostics[0]['force']['classementAttaque']>9 and statsAndpronostics[0]['force']['classementdefense']>9 and statsAndpronostics[1]['moyenne3']['nbrlose']['pourcentage_de_lose']<=20 and statsAndpronostics[1]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=40  and statsAndpronostics[0]['moyenne3']['nbrwin']['pourcentage_de_win']>30 and teamSensible['team1']['allpercentlose0']<60 and teamSensible['team1']['allpercentdraw0']<60:
        
        buildStat['Pronos']=[str(statsAndpronostics[1 ]) + ' gagne ou match null']
        return buildStat
    #-------------------------------------------champs 12-----------------------------------------------------------------------------------
    
      elif statsAndpronostics[0]['all']['rank']>statsAndpronostics[1]['all']['rank'] and  statsAndpronostics[0]['force']['classementAttaque']<12 and statsAndpronostics[1]['force']['classementAttaque']<15 and statsAndpronostics[0]['moyenne3']['nbrwin']['pourcentage_de_win']>30 and statsAndpronostics[0]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=30  or statsAndpronostics[1]['all']['rank']>statsAndpronostics[0]['all']['rank'] and  statsAndpronostics[1]['force']['classementAttaque']<12 and statsAndpronostics[0]['force']['classementAttaque']<15 and statsAndpronostics[1]['moyenne3']['nbrwin']['pourcentage_de_win']>30 and statsAndpronostics[1]['moyenne3']['nbrdraw']['pourcentage_de_draw']<=30 and teamSensible['team0']['allpercentdraw0']<40 and teamSensible['team1']['allpercentdraw0']<40: 
        
        buildStat['Pronos']=['Une des deux equipes gagne (    12    )']
        return buildStat
    #-----------------------------------------------champs les deux equipes marquent---------------------------------- 
      elif (statsAndpronostics[0]['moyenne3']['butencaisser']['nombre_de_but_encaisse']/3)>=1 and (statsAndpronostics[0]['moyenne3']['butencaisser']['nombre_de_but_encaisse']/3)>=1  and ((statsAndpronostics[0]['all']['butencaisser']/statsAndpronostics[0]['all']['matchplay'])*100)>70 and (statsAndpronostics[1]['moyenne3']['butencaisser']['nombre_de_but_encaisse']/3)>=1 and (statsAndpronostics[1]['moyenne3']['butencaisser']['nombre_de_but_encaisse']/3)>=1  and ((statsAndpronostics[1]['all']['butencaisser']/statsAndpronostics[1]['all']['matchplay'])*100)>70 :
        buildStat['Pronos']=['Les deux equipes marquent']
        return buildStat
        return 'Les deux equipes marquent'
      #-----------------------------------------------champs nombre de but-------------------------------------------------------------------
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>0 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<3:
        goal=[' TOTAL +0.5','TOTAL -2.5']
        buildStat['Pronos']= goal
        return buildStat
        
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=2 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<4:
        goal=['TOTAL +1.5',' TOTAL -4.5']
        buildStat['Pronos']= goal
        return buildStat
        
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=3 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<5:
        goal=['TOTAL +2.5','TOTAL -5.5']
        buildStat['Pronos']= goal
        return buildStat
        
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=4 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<6:
        goal=['TOTAL +3.5','TOTAL -6.5']
        buildStat['Pronos']= goal
        return buildStat
    
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=5 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<7:
        goal=['TOTAL +4.5']
        buildStat['Pronos']= goal
        return buildStat
        
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=6 and  (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])<8:
        goal=['TOTAL +5.5']
        buildStat['Pronos']= goal
        return buildStat
        
      elif (statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut'])>=7 :
        goal=['TOTAL +6.5']
        buildStat['Pronos']= goal
        return buildStat
      
    #---------------------------------------------------champs marge du vainqueur--------------------------------------------------------------------------------------------------------- 
      else :
        print((statsAndpronostics[0]['moyenne3']['but']['moyenne_nombredebut']+statsAndpronostics[1]['moyenne3']['but']['moyenne_nombredebut']))
        return 'NoneAgain'
    def secondpronos():
      if ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>1 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<3:
        carton=[' carton +2']
        buildStat['Pronos2']=carton
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>3 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<5:
        carton=[' carton +3']
        buildStat['Pronos2']=carton
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>4 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<6:
        carton=[' carton +4']
        buildStat['Pronos2']=carton
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>5 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<7:
        carton=['carton +5']
        buildStat['Pronos2']=carton
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>6 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<8:
        carton=['carton +6']
        buildStat['Pronos2']=carton
        return buildStat  
      
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>7 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<9:
        carton=['carton +7']
        buildStat['Pronos2']=carton
        return buildStat 
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>8 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<10:
        carton=[' carton +8']
        buildStat['Pronos2']=carton
        return buildStat
      
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>9 and ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)<11:
        carton=['carton +9']
        buildStat['Pronos2']=carton
        return buildStat
      
      
      elif ((statsAndpronostics[0]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune']+statsAndpronostics[1]['moyenne3']['cartonjaune']['moyenne_de_carton_jaune'])/2)>10 :
        carton=['carton +10']
        buildStat['Pronos2']=carton
        return buildStat
      else:
        pass
    def thirdpronos():
      if ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>3 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<5:
        corner=['corner  +5.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>4 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<6:
        corner=['corner +6.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>5 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<7:
        corner=['corner +7.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>6 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<8:
        corner=['corner +8.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>7 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<9:
        corner=['corner +9.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>8 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<10:
        corner=['corner +10.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>9 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<11:
        corner=['corner +11.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>10 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<12:
        corner=['corner +12.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>11 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<13:
        corner=['corner +13.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>12 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<14:
        corner=['corner +14.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>13 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<15:
        corner=['corner +15.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>14 and ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)<17:
        corner=['corner +16.5']
        buildStat['Pronoscorner']=corner
        return buildStat
      elif ((statsAndpronostics[0]['moyenne3']['corner']['moyenne_de_corner']+statsAndpronostics[1]['moyenne3']['corner']['moyenne_de_corner'])/2)>17 :
        corner=['corner +17.5']
        buildStat['Pronoscorner']=corner
        return buildStat
    def notsafe10():
      if statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']<1:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -0.5 but'
        buildStat['Pronosnosafe']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=1 and statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']<2:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -1.5 but'
        buildStat['Pronosnosafe']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=2 and statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']<3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=2 and statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']<3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan']['moyenne_de_but_mitan']>3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN +2.5 but'
        buildStat['Pronosnosafe']=[nosafe]
        return buildStat
    def notsafe11():  
      if statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']<1:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -0.5 but'
        buildStat['Pronosnosafe1']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=1 and statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']<2:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -1.5 but'
        buildStat['Pronosnosafe1']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=2 and statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']<3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe1']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']>=2 and statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']<3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe1']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan']['moyenne_de_but_mitan']>3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN +2.5 but'
        buildStat['Pronosnosafe1']=[nosafe]
        return buildStat
    def notsafe20():
      if statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<1:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -0.5 but'
        buildStat['Pronosnosafe2']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=1 and statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<2:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -1.5 but'
        buildStat['Pronosnosafe2']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=2 and statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe2']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=2 and statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe2']=[nosafe]
        return buildStat
      elif statsAndpronostics[0]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>3:
        nosafe=statsAndpronostics[0]['nameteam'] +'1er MITAN +2.5 but'
        buildStat['Pronosnosafe2']=[nosafe]
    def notsafe21():
      if statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<1:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -0.5 but'
        buildStat['Pronosnosafe3']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=1 and statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<2:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -1.5 but'
        buildStat['Pronosnosafe3']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=2 and statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe3']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>=2 and statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']<3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN -2.5 but'
        buildStat['Pronosnosafe3']=[nosafe]
        return buildStat
      elif statsAndpronostics[1]['moyenne3']['butmitan2']['moyenne_de_but_2mitan']>3:
        nosafe=statsAndpronostics[1]['nameteam'] +'1er MITAN +2.5 but'
        buildStat['Pronosnosafe3']=[nosafe]
        return buildStat   
    def notmestudy():
      import requests
      def base(endpoint):
        time.sleep(1)
        url ="https://v3.football.api-sports.io/"+endpoint
        headers={
          'x-rapidapi-key': '2f554e59b05daef4304c2752e4fff0a8',
          'x-rapidapi-host': 'v3.football.api-sports.io'}
        response = requests.request("GET", url, headers=headers)
        resjson=response.json()
        
        return resjson['response']
      urlname=base('predictions?fixture='+str(integerfixx))
      robotpronos=urlname[0]['predictions']['advice']
      buildStat['Pronosnotmestudy']=[robotpronos]
      return buildStat
    firstpronos()  
    secondpronos()
    thirdpronos()
    notsafe10()
    notsafe11()
    notsafe20()
    notsafe21()
    notmestudy()
    
    
    return buildStat
  else:
    return 'l identifiant doit etre un nombre'



# pronossafe(1038145,140)
print(int(123.3))





















