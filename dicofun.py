from math import *
f = open('text.txt')

text = f.read()
text = text.replace('.','')
text = text.replace(',','')
text = text.replace(';','')
text = text.replace('(','')
text = text.replace(')','')
text = text.replace('/','')
text = text.replace('"','')
text = text.lower()
mots = text.split()
lst_mot_freq = []

#print(mots)
m_total = 0

freq_mots = dict()
mot_demander = str(input("Donnée moi un mot à cherché dans le text (en minuscule)"))
for mot in mots:
    if len(mot) > 3:
        if mot not in freq_mots:
            freq_mots[mot] = 0
        freq_mots[mot] += 1
        m_total += 1


cur_max = 0
mot_plus_frequent = ''


for key in freq_mots:
    if freq_mots[key] > cur_max:
        mot_plus_frequent = key
        cur_max = freq_mots[key]
#Nombre d'apparition d'un mot donné par l'intulisateur en input
if mot_demander not in freq_mots:
    print('le mot', (mot_demander),"n'est pas dans le text")
else:
    print('Le mot' + "'" + mot_demander + "'",'appaarait', freq_mots[mot_demander],"fois")
print("Il y a",m_total," mots au total dans le text")
print("Le mot le plus fréquent est " + "'" + (mot_plus_frequent)+ "'" + " il apparait ", (cur_max), "fois")
# Pourcentage d'apparation du mot le plus fréquent
pourcentage_m_plus_fréquent = ceil((cur_max/m_total)*100)
print("Soit",pourcentage_m_plus_fréquent, "%")

