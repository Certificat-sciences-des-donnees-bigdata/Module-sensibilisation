# Module-sensibilisation
Retrouvez ici les contenus à étudier en autonomie du module *sensibilisation*.
_____
**Planning de travail** :

- Du 10 septembre au 3 octobre 2018 : faire les paragraphes 1, 2 et 3.
- Séance en présenciel le 4 octobre 2018 après-midi.
- Du 5 octobre au 28 octobre 2018 : faire les paragraphes 4, 5 et 6.
- Séance en présenciel le lundi 29 octobre 2018 matin et après-midi.
______

Les ressources pédagogiques offrent plusieurs niveaux de lecture ou d'utilisation afin d'être au mieux adaptées à un public hétérogène. Plus précisément il faut voir ce certificat comme une introduction à la *Science des Données* qui propose des pistes et références pour des approfondissements ultérieurs.

1. Le premier niveau est constitué des documents de cours de base (format `.pdf`) ci-dessous présentant les 
*grands principes* des méthodes ainsi que de nombreux exemples d'utilisation. Ils suffisent à une compréhension générale.
2. Ces documents pointent (liens hypertextes) vers des ressources de *deuxième niveau* ou d'approfondissement car intégrant les formulatons mathématiques des méthodes et algorithmes. Ces ressources sont celles du site collaboratif [`wikistat`](http://wikistat.fr/).
3. Le troisième niveau, appliqué, est composé des tutoriels (calepins ou jupyter notebooks) explicitant le traitement élémentaire de données "jouet", les exemples illustrant les documents de cours et d'autres exemples sur des données réelles. Ils servent de base de travail durant les phases de présenciel. 
4. Un quatrième niveau est à rechercher avec d'autres exemples d'utilisation disponibles dans les dépôts: [`github-wikistat`](https://github.com/wikistat/).

**Attention** : logiciels à installer

Pour les parties 1. Introduction à R, 2. Eléments d'analyse statistique de données et 3. Modélisation statistique, il faut installer le logiciel R. Il s'installe à partir du lien [R-project](https://www.r-project.org/) en choisissant la version qui correspond au système d’exploitation de la machine de l’utilisateur (Windows, ios, Linux). L’interface conseillée pour l’utilisation de R s’appelle [RStudio Desktop](http://www.rstudio.com/products/rstudio/download) en choisissant la version Open Source License.

Pour les parties suivantes, l'installation de Python 3 est requise pour la bonne exécution des tutoriels. Le plus simple est de l'installer à partir de la distribution [Anaconda](https://www.anaconda.com/download/). R nécessite également l'installation du noyau [IRkernel](https://irkernel.github.io/installation/).

Pour **exécuter les tutoriels**, il *suffit* de cloner ce dépôt, si vous avez un compte (gratuit) et les compétences nécessaires *GitHub*, ou encore, plus simplement, de [télécharger l'archive](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/archive/master.zip) puis de la dézipper. Lancer enfin *jupyter notebook* avant d'ouvrir les différents calepins (fichiers d'extension.ipynb) dans le navigateur par défaut qui exécute *jupyter*. L'exécution de chaque cellule d'un calepin est obtenue en cliquant sur le bouton `run`.

## 1 Introduction à R
*A faire sur la période du 10/09 au 3/10*

Le langage de programmation R est un langage reconnu pour l’analyse statistique de données, massives ou non.  L’acquisition de compétences dans l’utilisation de R est aujourd’hui un atout professionnel pour ceux qui le maîtrisent.

### 1.1 Documents de base à consulter en autonomie
- Cours introductif intitulé Logiciel R de [`wikistat.fr`](http://wikistat.fr/).
- [*Shortcut reference card*](https://cran.r-project.org/doc/contrib/Short-refcard.pdf) de Tom Short.
- [R pour les débutants](https://cran.r-project.org/doc/contrib/Paradis-rdebuts_fr.pdf) d’Emmanuel Paradis. 

### 1.2 Travail personnel demandé 
L’exercice qui vous est proposé vous permettra d’acquérir des compétences en langage R. Vous êtes invités à contacter vos enseignants (florent.bourgeois@ensiacet.fr et pascal.floquet@ensiacet.fr) pour vous aider dans la réalisation de ce travail. L’exercice porte sur la manipulation de variables aléatoires et leurs distributions statistiques, un des socles de l’analyse statistique de données.

Soit X1 et X2 deux variables aléatoires indépendantes qui suivent une loi normale. Écrivez en langage R les 6 fonctions (p, d, q, r, e et v) `bigdata`, dans un même script R, qui permettent de calculer la fonction de répartition CDF (*Cumulative Distribution Function*), la fonction densité de probabilité PDF (*Probability Density Function*), les quartiles, la génération de nombres aléatoires, la moyenne et la variance des variables 

Y = X1+X2 et Z = X1*X2. 

Les dites fonctions produiront les graphes pertinents qui permettent de visualiser les résultats de chacune des 6 fonctions.

## 2 Éléments d’analyse statistique de données
*A faire sur la période du 10/09 au 3/10*

Cette section vous permettra d’acquérir les notions élémentaires de l’analyse statistique de données. Elles sont la base des méthodes d’inférence et de modélisation mises en œuvre dans la suite.

### 2.1. Documents de base à consulter en autonomie sur [`wikistat.fr`](http://wikistat.fr/)

- [Statistique élémentaire : Introduction](http://wikistat.fr/pdf/st-l-Intro-statElem.pdf)
- [Statistique descriptive unidimensionnelle](http://wikistat.fr/pdf/st-l-des-uni.pdf)
- [Statistique descriptive bidimensionnelle](http://wikistat.fr/pdf/st-l-des-bi.pdf)
- [Estimation statistique](http://wikistat.fr/pdf/st-l-inf-estim.pdf)
- [Tests statistiques](http://wikistat.fr/pdf/st-l-inf-tests.pdf)

### 2.2. Travail personnel demandé

Le travail attendu est un travail personnel d’autoévaluation de votre maîtrise des concepts et méthodes d’analyse statistique étudiées dans les documents de base, en les appliquant au jeu de données du pic d’ozone de la ville de Rennes. Vous êtes invités à consulter le [tutoriel en R](https://github.com/wikistat/StatElem/blob/master/StatElem-R-Ozone.ipynb) sur lequel vous pourrez aussi récupérer le jeu de données. Vous trouverez ci-après, sans caractère limitatif, une liste de thèmes auxquels vous pouvez réfléchir en y apportant une ou plusieurs réponses basées sur les concepts étudiés dans cette section, comme par exemple:

- Décrire (type de données, moyenne, variance, moments,...) et tracer la distribution statistique des variables;
- Tester la normalité des variables;
- Calculer l’incertitude de la moyenne et de l’écart-type des variables;
- Analyser la corrélation entre 2 variables; 
- Tester la nullité du coefficient de corrélation linéaire ;
- ...

Toutes ces études feront l’objet d’une restitution en groupe lors de la séance en présentiel et de discussions lors des séances hors présentiel (contactez alors les enseignants florent.bourgeois@ensiacet.fr et pascal.floquet@ensiacet.fr) ou en présentiel.


## 3 Modélisation statistique
*A faire sur la période du 10/09 au 3/10*

Cette section vous permettra d’acquérir et de mettre en œuvre 2 méthodes de régression couramment utilisées dans l’analyse de données massives : la régression linéaire multiple et la régression logistique.

### 3.1. Documents de base à consulter en autonomie [`wikistat.fr`](http://wikistat.fr/)
 
- [Introduction à la modélisation statistique](http://wikistat.fr/pdf/st-m-modlin-intro.pdf)
- [Modèle gaussien: régression linéaire multiple](http://wikistat.fr/pdf/st-m-modlin-regmult.pdf)
- [Modèle binomial ou régression logistique](http://wikistat.fr/pdf/st-m-modlin-reglog.pdf)
 
### 3.2. Travail personnel demandé

Le travail attendu est un travail personnel d’autoévaluation de votre maîtrise de la régression linéaire multiple et de la régression logistique, en les appliquant à la prédiction du pic d’ozone de la ville de Rennes.
Vous trouverez ci-après, sans caractère limitatif, une liste de sujets auxquels vous êtes invité à réfléchir en y apportant une ou plusieurs réponses basées sur les concepts étudiés dans cette section: 

- Calculer les paramètres des modèles de régression (linéaire multiple et logistique) liant la variable pic d’ozone aux autres variables explicatives;
- Calculer l’intervalle de confiance de ces paramètres;
- Tester la significativité des paramètres;
- Examiner la qualité des modèles de régression, en ajustement et en prédiction;
- Quelles sont les incertitudes associées à la prédiction ?;
- Quel est le « bon » modèle à choisir : nombre de paramètres, valeurs des paramètres,... ?;
- ...

_____
#### **Corrigé de la séance du 4 octobre 2018 :**

Vous trouverez le fichier R utilisé en séance dans le fichier Calepins : [Analyse et modélisation statistique avec R](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/Analyse%20et%20modelisation%20statistique%20sur%20R%20Ozone_4-10-2018.r)
_____

## 4 Introduction à Python
*A faire sur la période du 5/10 au 28/10*

*Python* et ses librairies produisent moins de résultat utiles que R à l'interprétation statistique mais fournissent des codes généralement plus efficaces pour aborder le traitement de données massives.

Des [tutoriels](https://github.com/wikistat/Intro-Python) proposent une introduction à Python et une sélection des commandes utiles au statisticien et / ou *data scientist*.  

Une connaissance experte de Python n'est pas indispensbale au suivi de ce module; ces tutoriels peuvent être sautés en première lecture. 


## 5 Exploration Multidimensionnelle
*A faire sur la période du 5/10 au 28/10*

Le choix a été fait de mettre plus particulièrement l'accent sur des exemples d'application issus du monde industriel (données physiques quantitatives) plutôt que des applications (données qualitatives) de type sondage,  marketing ou fouille de textes... Comme écrit plus haut, l'introduction à d'autres méthodes et d'autres exemples d'application sont à rechercher dans les ressources des autres niveaux (2 et 4) d'approfondissement.


### 5.1 Documents de base à consulter en autonomie

- [Introduction](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsIntro.pdf): De la statistique à la *Science des Données* en passant par la fouille de données (*Data Mining*).
- [Exploration ](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsExplo.pdf) en grande dimension avec l'analyse en composantes Principales (ACP), l'analyse factorielle discriminante (AFD); classification non supervisée (*clustering*) avec *k-means*.

### 5.2 Tutoriels à réaliser en automnomie
Profiter du présenciel pour exécuter les calepins (*jupyer notebooks*) et **surtout poser les questions** relatives au cours et aux traitements présentés dans les différents tutoriels.

[**Télécharger**](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/archive/master.zip) l'ensemble de l'archive du dépôt ou *cloner* le dépôt si vous avez déjà un compte GitHub pour exécuter les tutoriels.

1. [Intro-ACP-AFD](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Intro-ACP-AFD-Python.ipynb)
2. [Adaptation statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Pic-Ozone-Python.ipynb) et prévision de la concentration en ozone. Traiter la première partie: *Exploration*.
3. [Segmentation d'image](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Cluster-Mars-Python.ipynb) et cartographie de la surface de Mars.

### 5.3 Tutoriel à réaliser en présenciel
4. [Reconnaissance d'activité](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-ML4IoT-Har-Python.ipynb) à partir des enregistrements d'un smartphone. Traiter la première partie: *Exploration*.

Profiter du présenciel pour poser les questions sur les parties de cours mal comprises et approfondir la compréhension des tutoriels notamment les interprétations des résultats obtenus. 

D'autres exemples sont disponibles dans le dépôt [`github - wikistat - Exploration`](https://github.com/wikistat/Exploration).



## 6 Principes de l'Apprentissage Statistique
*A faire sur la période du 5/10 au 28/10*

### 6.1 Document de base à consulter en autonomie

- [Principes de l'Apprentissage Statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsApprent.pdf) 

### 6.2 Tutoriels à réaliser en autonomie

- [Classification supervisée](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Intro-Apprent-Python.ipynb) de données synthétiques dans **R**²
- [Adaptation statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Pic-Ozone-Python.ipynb) et prévision de la concentration en ozone. Deuxième partie: *Apprentissage et Prévision*.


### 6.3 Tutoriel à réaliser en présenciel
- [Reconnaissance d'activité](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-ML4IoT-Har-Python.ipynb) à partir des enregistrements d'un smartphone. Deuxième partie: *Apprentissage et Reconnaissance*.

Profiter du présenciel pour poser les questions sur les parties de cours mal comprises et approfondir la compréhension des tutoriels notamment les interprétations des résultats obtenus. 

D'autres exemples sont disponibles dans le dépôt [`github-wikistat-Apprentissage`](https://github.com/wikistat/Apprentissage).



## 7 Infrastructures du big data

*Le cours est disponible dans le fichier Documents*
[Infrastructures](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/Cours%20infrastructure%20301018.pdf)

## 8 Optimisation

*Le cours est disponible dans le fichier Documents*
[Optimisation](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/Cours%20optimisation%20301018.pdf)

*Le TP est disponible dans le fichier Calepins - c'est un jupyter notebook*
[TP Optimisation](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/tp1_certificat_etudiant.ipynb)

## 9 Projet de fin de module

Pour conclure ce premier module, vous devez réaliser un projet en binôme. Le projet est à rendre au plus tard le **21 décembre à midi**.
La composition des binômes doit être envoyée par email aux 2 enseignants mentionnés dans le sujet, au plus tard le **21 novembre à midi**. Lisez attentivement les conditions de travail indiquées dans le sujet.

Toutes les questions concernant le projet doivent être posées via le **forum google groupe** mis en place au début du certificat.

*Le sujet est disponible dans le fichier Documents.* [Sujet Projet](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/project-subject.pdf)

*Le jupyter notebook associé est dans le fichier Calepins.* [Projet optimisation](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/Projet-Optimisation.ipynb)

*Le fichier ratings.dat est dans le fichier data du même dossier.*

Bon travail à tous !
