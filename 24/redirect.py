#grep texte monfichier
#grep -i alias .bashrc #ne fait pas attention à la casse
#grep -n alias .bashrc #renvoit les numéros de lignes
#grep -v alias .bashrc inversion de recherche
#grep -r "Site du Zéro" code/


#grep -E ^Alias .bashrc
# .  Caractère quelconque
# ^  Début de ligne
# $  Fin de ligne
# [] Un des caractères entre les crochets
# ?  L'élément précédent est optionnel (peut être présent 0 ou 1 fois)
# *  L'élément précédent peut être présent 0, 1 ou plusieurs fois
# +  L'élément précédent doit être présent 1 ou plusieurs fois
# |  Ou
# () Groupement d'expressions

# sort noms.txt 
# sort -o noms_tries.txt noms.txt
# sort -r noms.txt # reverse
# sort -R noms.txt # random 
# sort -n nombres.txt #trier les nombres

# wc noms.txt # lignes mots bits
# wc -l noms.txt
# wc -w noms.txt
# wc -c noms.txt
# wc -m noms.txt

#uniq doublons.txt sans_doublons.txt
#uniq -c doublons.txt #compte occurence 
#uniq -d doublons.txt  #nombre d'occurence

#cut -c 2-5 noms.txt #keep 2 to 5 caracteres
#cut -c -3 noms.txt 
#cut -c 3- noms.txt 
#cut -d , -f 1 notes.csv #keep first side of cut
#cut -d , -f 1,3 notes.csv

#cut -d , -f 1 notes.csv > eleves.txt #overwrite if exists
#cut -d , -f 1 notes.csv >> eleves.txt #append and create if not exist
#2>, 2>> et 2>&1  
#cut -d , -f 1 fichier_inexistant.csv > eleves.txt 2> erreurs.log
#cut -d , -f 1 fichier_inexistant.csv >> eleves.txt 2>&1
#<,<<
#cat < notes.csv
#sort -n << FIN #lit pogressivement
#wc -m << FIN

#sort -n << FIN > nombres_tries.txt 2>&1

#cut -d , -f 1 notes.csv | sort > noms_tries.txt
#du | sort -nr
#du | sort -nr | head
#sudo grep log -Ir /var/log  | cut -d : -f 1  | sort | uniq #-I exclu les fichiers binaires

#w
#date
#
#