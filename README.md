# Template pour la rédaction de thèse

## README.md version Loulou

J'ai récupéré ce template par mes prédécesseurs. J'ai fais quelques modifications personnelles d'ordre esthétique et pour avoir la nouvelle page de garde UGA (version 2025).
Important :
* Remplir son ED, son labo, son nom, son titre, son encadrement et son jury dans le fichier `Page_de_garde/Page_de_garde_new.tex`
* Remplir son résumé et son abstract dans le fichier `Page_de_garde/Page_de_couverture.tex`
* Les liens ont des couleurs pouvant être changées à la toute fin du fichier `Manuscrit/Packages.tex` (ctrl f "Pour changer les couleurs des liens")
* Les parties ont leur numéro en arrière-plan, la couleur de ce numéro est à changer dans le fichier `Manuscrit/Packages.tex` ligne 173 (ctrl f "Changer la couleur par celle de son choix")
* Les chapitres ont aussi un numéro en couleur, elle se trouve dans le fichier `Manuscrit/Packages.tex` ligne 152 (ctrl f "Changer la couleur des numéros de chapitre")
* Pour la moindre question : louiliam.clot@lpsc.in2p3.fr
* gl;hf

-------------------------------------------------------------------------

## README.md orginal (plus forcément à jour)

Dossier issu des templates de David Leh et Florian Huet (docteurs au laboratoire SYMME).
Ce dossier final est une fusion des fonctionnalités de chacun des templates (regroupement de fonctionnalités) et avec la mise à jour des packages devenus obsolètes.


## Fonctionnement

* Le fichier "manuscrit.tex" (dossier manuscrit) est le document maître.
* Il suffit de rédiger des les fichiers .tex de chacun des dossiers, puis d'excécuter le fichier maître.
* Il est possible d'ajouter ou de supprimer des dossiers/fichiers (par exemple des chapitres). Il suffit d'ajouter/désactiver les lignes correspondantes dans le fichier "manuscrit.tex".

## Modifications autres
* Logo de l'université (Grenoble Alpes) peut être modifié dans le fichier "meta-donnees.sty".
* Spécialité du doctorat peut être modifiée dans le fichier "meta-donnees.sty".
* Laboratoire peut être modifié dans le fichier "meta-donnees.sty".
* Ecole doctorale peut être modifiée dans le fichier "meta-donnees.sty".
* Des packages peuvent être ajoutés dans le fichier "packages.tex".
* Les couleurs (Tableaux, références, liens ...) peuvent être modifiés dans le fichier "packages.tex" via le package "hyperref".

