# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as pp
Datum_to_axle=DTA=2.25
CL=60
EW=692#-8
MFW=42
AFW=66
TFW=108
TWW=27
LP=140
MP=180
HP=220
PAS=100
pp.style.use('seaborn')
#Calculating the Empty Weight Center of Gravity(CG)
CGC=((TWW*168.375)/(EW))#-((49.125*-8)/EW)
EWCG=(DTA)+CGC

#Changes in CG due to Pilot Weights
#Light Pilot
cglp=DTA+(CGC*(EW/(EW+LP)))+((54.375*LP)/(EW+LP))
grosslp=np.linspace(EW,(EW+LP),1000)
CGLP=(grosslp-EW)/(((EW+LP)-EW)/(cglp-EWCG))+EWCG
pp.plot(CGLP,grosslp,color='blue',alpha=1,label='Light Pilot ('+str(LP)+'lbs.)')
pp.plot(cglp,EW+LP,'o',color='black',alpha=0.6)
#Medium Pilot
cgmp=DTA+(CGC*(EW/(EW+MP)))+((54.375*MP)/(EW+MP))
grossmp=np.linspace(EW,(EW+MP),1000)
CGMP=(grossmp-EW)/(((EW+MP)-EW)/(cgmp-EWCG))+EWCG
pp.plot(CGMP,grossmp,color='green',alpha=1,label='Medium Pilot ('+str(MP)+'lbs.)')
pp.plot(cgmp,EW+MP,'o',color='black',alpha=0.6)
#Heavy Pilot
cghp=DTA+(CGC*(EW/(EW+HP)))+((54.375*HP)/(EW+HP))
grosshp=np.linspace(EW,(EW+HP),1000)
CGHP=(grosshp-EW)/(((EW+HP)-EW)/(cghp-EWCG))+EWCG
pp.plot(CGHP,grosshp,color='red',alpha=1,label='Heavy Pilot ('+str(HP)+'lbs.)')
pp.plot(cghp,EW+HP,'o',color='black',alpha=0.6)

#Changes in CG due to Fuel in main
#Light Pilot
cglpm=DTA+(CGC*(EW/(EW+LP+MFW)))+((54.375*LP)/(EW+LP+MFW))-(4.125*MFW)/(EW+LP+MFW)
grosslpm=np.linspace((EW+LP),(EW+LP+MFW),1000)
CGLPM=(grosslpm-(EW+LP))/(((EW+LP+MFW)-(EW+LP))/(cglpm-cglp))+cglp
pp.plot(CGLPM,grosslpm,'',color='gray',label='Main Tank (7gal.)')
pp.plot(cglpm,EW+LP+MFW,'o',color='black',alpha=0.6)
#Medium Pilot
cgmpm=DTA+(CGC*(EW/(EW+MP+MFW)))+((54.375*MP)/(EW+MP+MFW))-(4.125*MFW)/(EW+MP+MFW)
grossmpm=np.linspace((EW+MP),(EW+MP+MFW),1000)
CGMPM=(grossmpm-(EW+MP))/(((EW+MP+MFW)-(EW+MP))/(cgmpm-cgmp))+cgmp
pp.plot(CGMPM,grossmpm,color='gray')
pp.plot(cgmpm,EW+MP+MFW,'o',color='black',alpha=0.6)
#Heavy Pilot
cghpm=DTA+(CGC*(EW/(EW+HP+MFW)))+((54.375*HP)/(EW+HP+MFW))-(4.125*MFW)/(EW+HP+MFW)
grosshpm=np.linspace((EW+HP),(EW+HP+MFW),1000)
CGHP=(grosshpm-(EW+HP))/(((EW+HP+MFW)-(EW+HP))/(cghpm-cghp))+cghp
pp.plot(CGHP,grosshpm,color='gray')
pp.plot(cghpm,EW+HP+MFW,'o',color='black',alpha=0.6)

#Changes in CG due to Fuel in Aux Tank
#Light Pilot
cglpma=DTA+(CGC*(EW/(EW+LP+TFW)))+((54.375*LP)/(EW+LP+TFW))-(4.125*MFW)/(EW+LP+TFW)+((19.375*AFW)/(EW+LP+TFW))
grosslpma=np.linspace(EW+LP+MFW,(EW+LP+TFW),1000)
CGLPMA=(grosslpma-(EW+LP+MFW))/(((EW+LP+TFW)-(EW+LP+MFW))/(cglpma-cglpm))+cglpm
pp.plot(CGLPMA,grosslpma,color='teal',label='Aux. Tank (11gal.)')
pp.plot(cglpma,EW+LP+TFW,'o',color='black',alpha=0.6)
#Medium Pilot
cgmpma=DTA+(CGC*(EW/(EW+MP+TFW)))+((54.375*MP)/(EW+MP+TFW))-(4.125*MFW)/(EW+MP+TFW)+((19.375*AFW)/(EW+MP+TFW))
grossmpma=np.linspace(EW+MP+MFW,(EW+MP+TFW),1000)
CGMPMA=(grossmpma-(EW+MP+MFW))/(((EW+MP+TFW)-(EW+MP+MFW))/(cgmpma-cgmpm))+cgmpm
pp.plot(CGMPMA,grossmpma,color='teal')
pp.plot(cgmpma,EW+MP+TFW,'o',color='black',alpha=0.6)
#Heavy Pilot
cghpma=DTA+(CGC*(EW/(EW+HP+TFW)))+((54.375*HP)/(EW+HP+TFW))-(4.125*MFW)/(EW+HP+TFW)+((19.375*AFW)/(EW+HP+TFW))
grosshpma=np.linspace(EW+HP+MFW,(EW+HP+TFW),1000)
CGHPMA=(grosshpma-(EW+HP+MFW))/(((EW+HP+TFW)-(EW+HP+MFW))/(cghpma-cghpm))+cghpm
pp.plot(CGHPMA,grosshpma,color='teal')
pp.plot(cghpma,EW+HP+TFW,'o',color='black',alpha=0.6)

#Changes in CG due to a Passenger
#Light Pilot
cglpmap=DTA+(CGC*(EW/(EW+LP+TFW+PAS)))+((54.375*LP)/(EW+LP+TFW+PAS))-(4.125*MFW)/(EW+LP+TFW+PAS)+((19.375*AFW)/(EW+LP+TFW+PAS))+(((23.375*PAS)/(EW+LP+TFW+PAS)))
grosslpmap=np.linspace(EW+LP+TFW,(EW+LP+TFW+PAS),1000)
CGLPMAP=(grosslpmap-(EW+LP+TFW))/(((EW+LP+TFW+PAS)-(EW+LP+TFW))/(cglpmap-cglpma))+cglpma
pp.plot(CGLPMAP,grosslpmap,color='salmon',label='Passenger('+str(PAS)+'lbs.)')
pp.plot(cglpmap,EW+LP+TFW+PAS,'o',color='black',alpha=0.6)
#Medium Pilot
cgmpmap=DTA+(CGC*(EW/(EW+MP+TFW+PAS)))+((54.375*MP)/(EW+MP+TFW+PAS))-(4.125*MFW)/(EW+MP+TFW+PAS)+((19.375*AFW)/(EW+MP+TFW+PAS))+(((23.375*PAS)/(EW+MP+TFW+PAS)))
grossmpmap=np.linspace(EW+MP+TFW,(EW+MP+TFW+PAS),1000)
CGMPMAP=(grossmpmap-(EW+MP+TFW))/(((EW+MP+TFW+PAS)-(EW+MP+TFW))/(cgmpmap-cgmpma))+cgmpma
pp.plot(CGMPMAP,grossmpmap,color='salmon')
pp.plot(cgmpmap,EW+MP+TFW+PAS,'o',color='black',alpha=0.6)
#Heavy Pilot
cghpmap=DTA+(CGC*(EW/(EW+HP+TFW+PAS)))+((54.375*HP)/(EW+HP+TFW+PAS))-(4.125*MFW)/(EW+HP+TFW+PAS)+((19.375*AFW)/(EW+HP+TFW+PAS))+(((23.375*PAS)/(EW+HP+TFW+PAS)))
grosshpmap=np.linspace(EW+HP+TFW,(EW+HP+TFW+PAS),1000)
CGHPMAP=(grosshpmap-(EW+HP+TFW))/(((EW+HP+TFW+PAS)-(EW+HP+TFW))/(cghpmap-cghpma))+cghpma
pp.plot(CGHPMAP,grosshpmap,color='salmon')
pp.plot(cghpmap,EW+HP+TFW+PAS,'o',color='black',alpha=0.6)


#Creating the Limit Boxes
y=np.linspace(EW,1200,15)
x=CL*(1/3)*(y/y)
pp.plot(x,y,color='grey',alpha=0.5)
pp.text((1/3)*CL,680,'33% of MAC.',ha='center',fontsize=25)
x=CL*(0.266)*(y/y)
pp.plot(x,y,color='grey',alpha=0.5)
pp.text((0.266)*CL,680,'26.6% of MAC.',ha='center',fontsize=25)
#Plotting the Gross Limit
grossx=np.linspace(x,20.5,10)
grosslim=1200*(grossx/grossx)
pp.plot(grossx,grosslim,':',color='black',alpha=0.7)
pp.text(19.5,1205,'Gross Weight Limit(1200lbs.)',ha='left',fontsize=20)

x1=np.linspace(EWCG,x,100)
m=((1200-EW)/((0.266*60)-EWCG))
y=m*(x1-EWCG)+EW
pp.plot(x1,y,':',color='black')

pp.xlim(0.23*CL,.35*CL)
pp.ylabel('Gross Weight',fontsize=25)
pp.yticks(fontsize=25)
pp.xlabel('CG in Inches Aft of Datum',fontsize=25)
pp.xticks(fontsize=25)
pp.title('CG Plot for $N27DT$ Pietenpol',fontsize=45)
pp.legend(fontsize=23,loc='upper left')
pp.show()
#pp.savefig('peitenpol.png',dpi=600,figsize=(12,8))