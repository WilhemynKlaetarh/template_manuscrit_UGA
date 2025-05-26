# Programme Python créant un .md avec la table des matières (peut être utile mais bug quand il y a des $ $ dans les titres oups)

import os

fichier_input = "Manuscrit.toc"
fichier_output = "../toc.md"

if not os.path.isfile(fichier_input) :
    print("Compiler le LaTeX. Arrêt.")
    quit()

lines = [line for line in open(fichier_input).readlines() if "\\contentsline" in line]

tosend = []

for line in lines :
    if (div := line.split("{")[1].split("}")[0]) == "part" :
        tosend.append(line.split("}{")[1].replace("\\hspace {1em}"," ").replace("\\&","&")+"\n")
    elif div != "xpart" :
        line2print = "  "*{"chapter":1, "section":2, "subsection":3, "subsubsection":4}[div]+line.split("}{")[1].replace("\\numberline {","").replace("}"," ")
        tosend.append(line2print+"\n")
        #tosend.append("  "+line.split("}{")[1].replace("\\numberline {","").replace("}"," ")+"\n")

with open(fichier_output, "w") as f :
    f.writelines(tosend)

