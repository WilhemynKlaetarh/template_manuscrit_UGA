    Remerciements
  Tables
    Table des matières
    Table des figures
    Liste des tableaux
    Glossaire
  Introduction générale
I Physique & historique
  1 L'énergie nucléaire et la physique des réacteurs nucléaires
    1.1 État des lieux de l'utilisation de l'énergie nucléaire en France et dans le monde
      1.1.1 Une épopée mondiale de l'énergie
        1.1.1.1 « Depuis la nuit des temps... »
        1.1.1.2 Une addiction au carbone
        1.1.1.3 Vers un mix énergétique décarbonné
      1.1.2 L'énergie nucléaire dans le monde
        1.1.2.1 Une énergie récente
        1.1.2.2 Une énergie concentrée
        1.1.2.3 Une filière globalisée
      1.1.3 La France : un pays nucléaire
        1.1.3.1 L'exception française
        1.1.3.2 Une énergie d'avenir et un levier de transition énergétique
    1.2 Éléments de neutronique et de physique des réacteurs nucléaires
      1.2.1 Physique nucléaire simplifiée
        1.2.1.1 Isotopes, isobares et isomères
        1.2.1.2 Énergie de liaison des noyaux
        1.2.1.3 Des noyaux instables
        1.2.1.4 La fission spontanée et induite par neutron
        1.2.1.5 La capture
        1.2.1.6 La diffusion
      1.2.2 Neutronique
        1.2.2.1 Interactions neutron-matière : le concept de sections efficaces
        1.2.2.2 Flux neutronique et taux de réaction
        1.2.2.3 Transport des neutrons
        1.2.2.4 Réactivité
      1.2.3 Effet de spectre
        1.2.3.1 Spectre neutronique
        1.2.3.2 Neutrons prompts et retardés
        1.2.3.3 Contre-réactions
    1.3 Fonctionnement d'un réacteur nucléaire
      1.3.1 Un mot sur le cycle du combustible...
        1.3.1.1 Des actinides mineurs
        1.3.1.2 \emph {All cycles are breedable 
      1.3.2 Principes de base du fonctionnement d'une centrale nucléaire
      1.3.3 Quelques concepts de réacteurs
        1.3.3.1 Les réacteurs à eau présurisée
        1.3.3.2 Les réacteurs à eau bouillante
        1.3.3.3 Les réacteurs à neutrons rapides refroidis au sodium
    1.4 Les REP en France et le cycle du combustible français
      1.4.1 Rappels sur l'historique du déploiement du parc français
      1.4.2 Le cycle du combustible français actuel
      1.4.3 Le futur
    1.5 Objectif incinération des AM
      1.5.1 Les déchets nucléaires
      1.5.2 Transmutation, incinération, conversion
  2 Les réacteurs à sels fondus
    2.1 Historique et état des lieux pré-thèse
    2.2 Principe de fonctionnement
    2.3 Élément de chimie des sels fondus
      2.3.1 Type de sels
      2.3.2 Des sels ternaires
      2.3.3 Propriétés des sels fondus, Rédox
        2.3.3.1 Volume ionique
        2.3.3.2 Densité
    2.4 Les différents projets
      2.4.1 En France
        2.4.1.1 Projets passés
        2.4.1.2 ISAC
        2.4.1.3 Les start-ups
      2.4.2 En Europe
        2.4.2.1 Projets passés
        2.4.2.2 MIMOSA
        2.4.2.3 Projets présents ou futurs
      2.4.3 Dans le monde
    2.5 Les réacteurs à sels fondus dans cette thèse
      2.5.1 Un réacteur multi-physique et multi-échelle
II Codes & outils
  3 Les outils « classiques » autour de la simulation d'un RSF
    3.1 Les codes de transport neutronique
      3.1.1 Principe général
        3.1.1.1 Calculs déterministes
        3.1.1.2 Calculs stochastiques
      3.1.2 Le code MCNP
        3.1.2.1 Principe de fonctionnement d'un calcul de criticité (kcode)
        3.1.2.2 Calcul du keff
        3.1.2.3 Calcul du flux
        3.1.2.4 Calcul des taux de réaction
        3.1.2.5 Calcul rapide du spectre
        3.1.2.6 Remarque sur les sections efficaces
    3.2 Les codes de calculs neutroniques en évolution
      3.2.1 Le schéma de calcul standard
      3.2.2 Le code SMURE
    3.3 Spécificité des RSF et adaptation des codes d'évolution
      3.3.1 Adaptation pour les RSF
        3.3.1.1 Extraction continue des PF insolubles par bullage
        3.3.1.2 Première stratégie : échanges continus
        3.3.1.3 Stratégie alternative : échanges par \emph {batch 
        3.3.1.4 Réflexions préliminaires sur les différentes stratégies d'échanges au regard des simulations numériques
      3.3.2 Le code REM {\color {couleurElsa \it (@Elsa : ajouter que la description est originale dans la thèse ?) 
        3.3.2.1 Initialisation de l'évolution : les usines de traitement
        3.3.2.2 Le pas REM : un pas d'une longueur variable
        3.3.2.3 Le pas ERE : l'ajustement des alimentations
        3.3.2.4 Le pas IME : l'intégration des équations de Bateman
      3.3.3 Autres codes d'évolution adaptés aux RSF
        3.3.3.1 MOSARELA (CEA)
        3.3.3.2 SMURE/CARAPUCE (CNRS/Orano)
        3.3.3.3 PYMS (EDF)
        3.3.3.4 CEREIS (CNRS --- Subatech/LPSC)
    3.4 Les codes de scénario
      3.4.1 Définition pragmatique d'un scénario
      3.4.2 Le code ISF
      3.4.3 Autres codes de scénarios existants
    3.5 Les autres codes utilisés dans la thèse
      3.5.1 Sherlock
      3.5.2 Le constructeur de géométries REM
        3.5.2.1 Imbrication des traducteurs inter-code
        3.5.2.2 La géométrie ERE
        3.5.2.3 Le constructeur Java
  4 Adaptation des outils pour l'étude de RSF convertisseurs
    4.1 Les RSF incinérateurs par rapport aux électrogènes
      4.1.1 Définition d'un incinérateur
      4.1.2 Les critères de performances
    4.2 Contribution à l'adaptation des outils pour les RSF incinérateurs
      4.2.1 Problématique
      4.2.2 Les nouveaux ajouts dans REM (e.g nouvelles contraintes)
      4.2.3 Le nouvel ISF optimisé
    4.3 Outils d'analyse poussée
      4.3.1 Méthodologie de conception d'un réacteur
III Convertisseurs & incinérateurs
  5 Caractérisation de RSF convertisseurs
    5.1 Présentation des concepts utilisés (géométrie + objectif)
      5.1.1 Le MSFR de référence, un régénérateur-incinérateur
        5.1.1.1 Adaptation de la géométrie pour la neutronique
      5.1.2 Le RAPTOr, pour la conversion du plutonium
      5.1.3 ARAMIS-A, pour l'incinération de l'américium
    5.2 Les différents schémas d'alimentation et d'extraction
      5.2.1 Schémas continu vs. par \emph {batch 
      5.2.2 Schémas MIMOSA
      5.2.3 Schémas ISAC
      5.2.4 Exemple d'application : avant/après sur le MSFR
    5.3 Application des critères de performance
      5.3.1 Impact sur la taille : exemple avec RAPTOr
      5.3.2 Impact des matériaux/du spectre : exemple avec ARAMIS
      5.3.3 Impact sur l'isotopie du vecteur d'alim : exemple avec ...
  6 Étude et développements de RSF convertisseurs originaux
    6.1 Esquisses alternatives du concept ARAMIS-A
      6.1.1 Mise en contexte
      6.1.2 ARAMIS-B
      6.1.3 ARAMIS-C
      6.1.4 ARAMIS-D
    6.2 RAPTOrs évolués
      6.2.1 Mise en contexte
    6.3 Études de sensibilités
      6.3.1 Ajout de barres de contrôles mini-raptor+ARAMIS
      6.3.2 ARAMIS chaînés
      6.3.3 Changement de schéma de calcul : plus de PF, ±1000 pcm
IV Scénarios & exploration
  7 Scénarios de déploiement
    7.1 Scénario : définition
      7.1.1 Les usines
    7.2 Intégration des RSF incinérateurs dans des parcs
      7.2.1 Travail sur le scénario de référence du projet ISAC
      7.2.2 Adaptation rapide dans un parc à dimension européenne
  8 Optimisation de scénarios exploratoires
    8.1 Une intégration poussée des incinérateurs
    8.2 Études de sensibilité
      8.2.1 Intégration des esquisses alternatives d'ARAMIS dans un parc français
      8.2.2 Comparaison des concept ARAMIS et RAPTOr dans des parcs français et européens
  Conclusion générale et perspectives
  Bibliographie
Annexes
  A Liste des réacteurs étudiés au cours de cette thèse
  B Éléments de comparaison et autres compléments sur la chimie des sels
    B.1 Différents calculs de la densité des sels (Daniel, Sherlock, CEA)
    B.2 Autres schémas d'extraction (MSFR EVOL, SAMOSAFER)
  C Complément d'information sur les codes ERE et REM
    C.1 Configuration de ERE
    C.2 Configuration de REM
    C.3 Descriptions simplifiées de la géométrie du RAPTOr dans les fichiers d'entrée du Constructeur et des codes ERE et MCNP
      C.3.1 Fichier d'entrée --- Constructeur
      C.3.2 Fichier d'entrée --- Code ERE
      C.3.3 Fichier d'entrée --- Code MCNP
  Z Liste prévisionnelle des annexes (pas dans l'ordre)
    Z.1 Confusions à éviter
    Z.2 Détricotage des notations
    Z.3 Index
