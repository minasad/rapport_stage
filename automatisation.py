from tkinter import *
import pandas as pd
import numpy as np
import sys, os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

A=0 
C=1
T=2
G=3
COV=4
freqA=0
freqT=0
freqC=0
freqG=0
COVJOK1=9
global tab_concatenate

def manipFile(namefile):
	global barreEtat
	df = pd.read_csv(namefile, skiprows=2, delimiter=';')
	barreEtat.config(text=namefile + ' chargé')
	return df


def calculFrequence():
	if df is None:
		messagebox.showerror('File Error', 'Please open a csv file first')
		return

	nA=df['A']
	nC=df['C']
	nG=df['G']
	nT=df['T']
	
	tab_freq = [[0] * 5 for _ in range(len(nA))]
	for i in range(len(nA)):
		cov1=nA[i]+nC[i]+nG[i]+nT[i]
		if cov1 ==0 :
			tab_freq[i][A]=0
			tab_freq[i][C]=0
			tab_freq[i][T]=0
			tab_freq[i][G]=0
			tab_freq[i][COV]=0
		else:
			tab_freq[i][A]=nA[i]/cov1
			tab_freq[i][C]=nC[i]/cov1
			tab_freq[i][G]=nG[i]/cov1
			tab_freq[i][T]=nT[i]/cov1
			tab_freq[i][COV]=cov1
	return tab_freq

	
def readSensRev(tab_freq):
	global df
	if df is None:
		messagebox.showerror('File Error', 'Please open a csv file first')
		return
	nAs=df['Asens ']
	nCs=df['Csens ']
	nGs=df['Gsens ']
	nTs=df['Tsens ']
	read_sr = [[0] * 6 for _ in range(len(nAs))]
	for i in range(len(nAs)):
		cov2=nAs[i]+nCs[i]+nGs[i]+nTs[i]
		if cov2 == 0:
			read_sr[i][0]=0
			read_sr[i][1]=0
			read_sr[i][2]=0
			read_sr[i][3]=0
			read_sr[i][4]=0
		
		else:
			read_sr[i][0]=nAs[i]/cov2
			read_sr[i][1]=nCs[i]/cov2
			read_sr[i][2]=nGs[i]/cov2
			read_sr[i][3]=nTs[i]/cov2
			read_sr[i][4]=cov2
			quotient_nucl_nuclsens=tab_freq[i][COV]/cov2
		
			print(quotient_nucl_nuclsens)
	return quotient_nucl_nuclsens


def readSensRev1(tab_freq):
	nA_1=df['A.1']
	nC_1=df['C.1']
	nG_1=df['G.1']
	nT_1=df['T.1']
	read_sr_1 = [[0] * 6 for _ in range(len(nA_1))]
	for i in range(len(nA_1)):
		cov2_1=df['Asens .1'][i]+df['Tsens .1'][i]+df['Gsens .1'][i]+df['Csens .1'][i]
		if cov2_1 == 0:
			read_sr_1[i][0]=0
			read_sr_1[i][1]=0
			read_sr_1[i][2]=0
			read_sr_1[i][3]=0
			read_sr_1[i][4]=0
		else:
			read_sr_1[i][0]=nA_1[i]/cov2_1
			read_sr_1[i][1]=nC_1[i]/cov2_1                                                                              
			read_sr_1[i][2]=nG_1[i]/cov2_1
			read_sr_1[i][3]=nT_1[i]/cov2_1
			read_sr_1[i][4]=cov2_1
			quotient_nucl_nuclsens_1=tab_freq[i][COV]/cov2_1
		
			print(quotient_nucl_nuclsens_1)
	return quotient_nucl_nuclsens_1
		
			
def lettreMaj(tab_freq):
	global df
	global freqA
	global freqT
	global freqC
	global freqG
	global cov1
	nA=df['A']
	nC=df['C']
	nG=df['G']
	nT=df['T']
	nAs=df['Asens ']
	nCs=df['Csens ']
	nGs=df['Gsens ']
	nTs=df['Tsens ']
	tab_LetrMaj=[[0]*4 for _ in range(len(tab_freq))]
	for i in range(len(tab_freq)):
		
		freqA=tab_freq[i][A]
		freqT=tab_freq[i][T]
		freqG=tab_freq[i][G]
		freqC=tab_freq[i][C]
		freq_max=max(freqA,freqT,freqG,freqC)
		tab_LetrMaj[i][0]=freq_max
		if freq_max == 0:
			tab_LetrMaj[i][1]=0
			tab_LetrMaj[i][2]=0 
		elif freqA == freq_max:
			tab_LetrMaj[i][1]="A"
			tab_LetrMaj[i][2]= df["A"][i]/ df['Asens '][i]
			
		elif freqT == freq_max:
			tab_LetrMaj[i][1]="T"
			tab_LetrMaj[i][2]= df["T"][i]/ df['Tsens '][i]
		elif freqG == freq_max :
			tab_LetrMaj[i][1]="G"
			tab_LetrMaj[i][2]= df["G"][i]/ df['Gsens '][i]
		elif freqC == freq_max :
			tab_LetrMaj[i][1]="C"
			tab_LetrMaj[i][2]= df["C"][i]/ df['Csens '][i]
			
		if tab_freq[i][COV] > 1.2 * 112.67 or tab_freq[i][COV]< 0.8*112.67 :
			tab_LetrMaj[i][3]="pb cov general1"
		else:
			tab_LetrMaj[i][3]=0
		
	print(tab_LetrMaj)
		freq_letr_maj = freq_max
		
		
	return tab_LetrMaj,tab_freq

	
def lettreMaj1(tab_freq):
	global df
	nA1=df['A.1']
	nC1=df['C.1']
	nT1=df['T.1']
	nG1=df['G.1']
	tab_freq1 = [[0] * 5 for _ in range(len(nA1))]
	for i in range(len(nA1)):
		covjok1=nA1[i]+nC1[i]+nT1[i]+nG1[i]
		if covjok1 ==0 :
			tab_freq1[i][A]=0
			tab_freq1[i][C]=0
			tab_freq1[i][T]=0
			tab_freq1[i][G]=0
			tab_freq1[i][COV]=0
		else:
			tab_freq1[i][A]=nA1[i]/covjok1
			tab_freq1[i][C]=nC1[i]/covjok1
			tab_freq1[i][T]=nG1[i]/covjok1
			tab_freq1[i][G]=nT1[i]/covjok1
			tab_freq1[i][COV]=covjok1
	tab_LetrMaj1=[[0]*3 for _ in range(len(tab_freq1))]	
	for i in range(len(tab_freq1)):
		freqA1=tab_freq1[i][A]
		freqT1=tab_freq1[i][T]
		freqG1=tab_freq1[i][G]
		freqC1=tab_freq1[i][C]
		freq_max1=max(freqA1,freqT1,freqG1,freqC1)
		tab_LetrMaj1[i][0]=freq_max1
		if freq_max1 == 0:
			tab_LetrMaj1[i][1]=0
			tab_LetrMaj1[i][2]=0 
		elif freqA1 == freq_max1:
			tab_LetrMaj1[i][1]="A"
			tab_LetrMaj1[i][2]= df['A.1'][i]/ df['Asens .1'][i]
			
		elif freqT1 == freq_max1:
			tab_LetrMaj1[i][1]="T"
			tab_LetrMaj1[i][2]= df['T.1'][i]/ df['Tsens .1'][i]
		elif freqG1 == freq_max1 :
			tab_LetrMaj1[i][1]="G"
			tab_LetrMaj1[i][2]= df['G.1'][i]/ df['Gsens .1'][i]
		elif freqC1 == freq_max1 :
			tab_LetrMaj1[i][1]="C"
			tab_LetrMaj1[i][2]= df['C.1'][i]/ df['Csens .1'][i]
	
	print(tab_LetrMaj1)
		freq_letr_maj1 = freq_max1
		print(freq_letr_maj1)
	
	return tab_LetrMaj1,tab_freq1
	
def lettreMin(tab_freq):
	global df
	global freqA
	global freqT
	global freqC
	global freqG
	nA=df['A']
	nC=df['C']
	nG=df['G']
	nT=df['T']
	nAs=df['Asens ']
	nCs=df['Csens ']
	nGs=df['Gsens ']
	nTs=df['Tsens ']
	
	tab_LetrMin=[[0]*4 for _ in range(len(tab_freq))]
	for i in range(len(tab_freq)):
		freqA=tab_freq[i][A]
		freqT=tab_freq[i][T]
		freqG=tab_freq[i][G]
		freqC=tab_freq[i][C]
		freq_min=min(freqA,freqT,freqG,freqT)
		tab_LetrMin[i][0]=freq_min
		if freq_min == 0:
			tab_LetrMin[i][1]=0
			tab_LetrMin[i][2]=0 
		elif freqA == freq_min:
			tab_LetrMin[i][1]="A"
			tab_LetrMin[i][2]= df["A"][i]/ df['Asens '][i]
			
		elif freqT == freq_min:
			tab_LetrMin[i][1]="T"
			tab_LetrMin[i][2]= df["T"][i]/ df['Tsens '][i]
			
		elif freqG == freq_min :
			tab_LetrMin[i][1]="G"
			tab_LetrMin[i][2]= df["G"][i]/ df['Gsens '][i]
			
		elif freqC == freq_min :
			tab_LetrMin[i][1]="C"
			tab_LetrMinl[i][2]= df["C"][i]/ df['Csens '][i]
			
		if freq_min>= 0.01:
			tab_LetrMin[i][3]= "v"
		else:
			tab_LetrMin[i][3]= 0
		freq_letr_min=tab_LetrMin[i][0]
		
		
	print(tab_LetrMin)
		
	return tab_LetrMin
	
def lettreMin1(tab_freq):
	global df
	nA1m=df['A.1']
	nC1m=df['C.1']
	nT1m=df['T.1']
	nG1m=df['G.1']
	tab_freq1m = [[0] * 5 for _ in range(len(nA1m))]
	for i in range(len(nA1m)):
		covjok1m=nA1m[i]+nC1m[i]+nT1m[i]+nG1m[i]
		if covjok1m ==0 :
			tab_freq1m[i][A]=0
			tab_freq1m[i][C]=0
			tab_freq1m[i][T]=0
			tab_freq1m[i][G]=0
			tab_freq1m[i][COV]=0
		else:
			tab_freq1m[i][A]=nA1m[i]/covjok1m
			tab_freq1m[i][C]=nC1m[i]/covjok1m
			tab_freq1m[i][T]=nG1m[i]/covjok1m
			tab_freq1m[i][G]=nT1m[i]/covjok1m
			tab_freq1m[i][COV]=covjok1m
	print(tab_freq1m)
	tab_LetrMin1m=[[0]*3 for _ in range(len(tab_freq1m))]	
	for i in range(len(tab_freq1m)):
		
		freqA1m=tab_freq1m[i][A]
		freqT1m=tab_freq1m[i][T]
		freqG1m=tab_freq1m[i][G]
		freqC1m=tab_freq1m[i][C]
		freq_min1m=min(freqA1m,freqT1m,freqG1m,freqC1m)
		
		tab_LetrMin1m[i][0]=freq_min1m
		if freq_min1m == 0:
			tab_LetrMin1m[i][1]=0
			tab_LetrMin1m[i][2]=0 
		elif freqA1m == freq_min1m:
			tab_LetrMin1m[i][1]="A"
			tab_LetrMin1m[i][2]= df['A.1'][i]/ df['Asens .1'][i]
			
		elif freqT1m == freq_min1m:
			tab_LetrMin1m[i][1]="T"
			tab_LetrMin1m[i][2]= df['T.1'][i]/ df['Tsens .1'][i]
		elif freqG1m == freq_min1m :
			tab_LetrMin1m[i][1]="G"
			tab_LetrMin1m[i][2]= df['G.1'][i]/ df['Gsens .1'][i]
		elif freqC1m == freq_min1m :
			tab_LetrMin1m[i][1]="C"
			tab_LetrMin1m[i][2]= df['C.1'][i]/ df['Csens .1'][i]
	
	
		freq_letr_min1m=tab_LetrMin1m[i][0]
		
	return tab_LetrMin1m,tab_freq1m


def sommeCoverage(tab_freq):
	global df
	nA=df['A']
	nC=df['C']
	nG=df['G']
	nT=df['T']
	nAs=df['Asens ']
	nCs=df['Csens ']
	nGs=df['Gsens ']
	nTs=df['Tsens ']
	nAr=df['Arev ']
	nCr=df['Crev ']
	nGr=df['Grev ']
	nTr=df['Trev ']
	tab_coverage=[[0]*9 for _ in range(len(nA))]
	for i in range(7,len(tab_freq)-7):
		condition = True
		for j in range(1,8):
			if condition and tab_freq[i][COV]>tab_freq[i-j][COV] and tab_freq[i][COV]>tab_freq[i+j][COV]:	
				condition = True
				tab_coverage[i][2]="x"
			else:
		
				condition = False
		

	for i in range(len(nAs)):
		cov2=nAs[i]+nCs[i]+nGs[i]+nTs[i]
		COVERAGE=nA[i]+nC[i]+nG[i]+nT[i]+nAs[i]+nCs[i]+nGs[i]+nTs[i]
		tab_coverage[i][0]=COVERAGE
		if nA[i]==nT[i] and nAs[i]==nTs[i] and nAr[i]==nTr[i] and nC[i]==nG[i] and nCs[i]==nGr[i] and nCr[i]==nGs[i]:
			tab_coverage[i][1] ="palind"
			
		if tab_coverage[i][0]> 1.2*1112.67 or tab_coverage[i][0]<0.8*1112.67 :
			tab_coverage[i][3]= "pb cov general2"
		else:
			tab_coverage[i][3]= 0
	for i in range(7,len(tab_freq)-7):
		condition = True
		for k in range(1,6):
			if condition and tab_coverage[i][0] > 1.2*tab_coverage[i-k][0] or tab_coverage[i][0]< 1.2 * tab_coverage[i+k][0]:
				condition =True
				tab_coverage[i][4]="pb cov1"
			else:
				condition=False
		for l in range(1,3):
			if condition and tab_coverage[i][0] > 1.1 *tab_coverage[i-l][0] or tab_coverage[i][0]< 1.1 * tab_coverage[i+l][0]:
				condition =True
				tab_coverage[i][5]="pb cov3"
			else:
				condition=False
		for m in range(1,4):
			if condition and (tab_coverage[i+m][0]/3 )*0.9 > tab_coverage[i][0]  or (tab_coverage[i+m][0]/3 )* 1.1 < tab_coverage[i][0]:
				condition =True
				tab_coverage[i][6]="pb cov2"
			else:
				condition=False
			
		if tab_coverage[i][4]=="pb cov1" and tab_coverage[i][6]=="pb cov2" and tab_coverage[i][5]=="pb cov3" :
			tab_coverage[i][7]= "s"
		else:
			tab_coverage[i][7]= 0
		if (tab_coverage[i][7]=="s" and tab_coverage[i][6] != "pb cov2") or( tab_coverage[i][4] !="pb cov1" and tab_coverage[i][7] != "s") :
			tab_coverage[i][8]="t"
		else:
			tab_coverage[i][8]=0
		
				
			
	print(tab_coverage)
		
	return tab_coverage

		
def condition1(tab_LetrMaj,tab_LetrMaj1,tab_coverage):
	global COVERAGE
	tab_condition1=[[0]*1 for _ in range(len(tab_coverage))]
	for i in range(len(tab_LetrMaj)):
		if tab_LetrMaj[i][1] != tab_LetrMaj1[i][1] and tab_coverage[i][0] < 1.5*(22+858) and tab_coverage[i][0] >30 :
			
			tab_condition1[i][0]="y"
		else:
			tab_condition1[i][0]=0
			
	print(tab_condition1)		

	return tab_condition1
	
	
def condition2(tab_LetrMin,readSensRev,condition1,tab_LetrMaj1,readSensRev1):
	tab_condition2=[[0]*2 for _ in range(len(tab_LetrMin))]	
	for i in range(len(tab_LetrMin)):
		if tab_LetrMin[i][3]=="v" and tab_LetrMin[i][2]> 0.5*quotient_nucl_nuclsens and tab_LetrMin[i][2]< 1.5*quotient_nucl_nuclsens  :
			tab_condition2[i][0]= "w"
	else:
		tab_condition2[i][1]= 0
		
	if condition1[i][0]=="y" and tab_LetrMaj1[i][2]>0.5*quotient_nucl_nuclsens_1 and tab_LetrMaj1[i][2]<1.5* quotient_nucl_nuclsens_1 :
		tab_condition2[i][0]= "w"
	else:
		tab_condition2[i][1]= 0
		
	return tab_condition2
	
	
def concatenate(tab_coverage,tab_condition1,tab_LetrMin):
		
		for i in range(len(tab_LetrMin)):
			tab_concatenate=str(tab_coverage[i][2])+str(tab_condition1[i][0])+str(tab_LetrMin[i][3])
			
			
			
		return tab_concatenate
			
def resultat(tab_coverage,tab_condition2):
	global tab_concatenate
	tab_resultat=[[0]*2for _ in range(len(tab_coverage))]
	for i in range(len(tab_coverage)):
		if tab_coverage[i][8] != "t" and tab_coverage[i][1] != "palind" and tab_condition2[i][0]== "w" and tab_coverage[i][0] >500 :
			tab_resultat[i][0]= tab_concatenate
		else:
			pass
			
			
		if tab_resultat[i][0] =="xv" or tab_resultat[i][0] == "v" or tab_resultat[i][0] == "xy" :
			tab_resultat[i][1] ="u"
		else:
			pass 
			
			
		return tab_resultat

	
def main():
	tabFreq = calculFrequence()
	tabSens = readSensRev(tabFreq)
	tabLetMaj=lettreMaj(tabFreq)
	tabLetMin=lettreMin(tabFreq)
	tabCoverage=sommeCoverage(tabFreq)
	tabLetMaj1=lettreMaj1(tabFreq)
	tableCondition1=condition1(tabLetMaj,tabLetMaj1,tabCoverage)
	tabLetMin1=lettreMin1(tabFreq)
	tabSens1=readSensRev1(tabFreq)
	tableCondition2=condition2(tabLetMin,tabSens,tableCondition1,tabLetMaj1,tabSens1)
	tableconcaten=concatenate(tabCoverage,tableCondition1,tabLetMin)
	tableResultat=resultat(tabCoverage,tableCondition2)
	
	
	
	
def recupererCsv():
	global df

	nomTable = askopenfilename()
	try:
		df = manipFile(nomTable)
	except IOError:
		messagebox.showerror('''Aucun fichier de ce nom, vous devez saisir un nom de fichier valide''')
		return


def hello():
	messagebox.showinfo('About', 'Developed by Amina SADIO - 2019')


if __name__ == '__main__':
	df = None

	fenetre = Tk()
	fenetre.geometry("800x600")
	fenetre.title('Automatisation')
	menubar = Menu(fenetre)

	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Open", command=recupererCsv)
	filemenu.add_command(label="Exit", command=fenetre.quit)
	menubar.add_cascade(label="File", menu=filemenu)

	statsmenu = Menu(menubar, tearoff=0)
	statsmenu.add_command(label="Calcul Fréquence", command=main)
	menubar.add_cascade(label="Stats", menu=statsmenu)
	

	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About", command=hello)
	menubar.add_cascade(label="Help", menu=helpmenu)

	fenetre.config(menu=menubar)

	barreEtat = Label(fenetre, text='', bd=1, relief=SUNKEN, anchor=W)                                          
	barreEtat.pack(side=BOTTOM, fill=X)                                           

	fenetre.mainloop()
