# Lire adresse url
url = input("Saisir une url : ")
# Lire le texte du lien hypertexte
text_lien = input("saisir le texte du lien ")
# convert the url text to a link 
url = "<a href='"+ url + "'> " + text_lien + "</a>"
print(url)
