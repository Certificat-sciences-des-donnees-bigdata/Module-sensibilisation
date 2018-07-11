# Module-sensibilisation
Retrouvez ici les contenus à étudier en autonomie du module *sensibilisation*.

Les ressources pédagogiques offrent plusieurs niveaux de lecture ou d'utilisation afin d'être au mieux adaptées à un public hétérogène. Plus précisément il faut voir ce certificat comme une introduction à la *Science des Données* qui propose des pistes et références pour des approfondissements ultérieurs.

1. Le premier niveau est constitué des documents de cours de base (format `.pdf`) ci-dessous présentant les 
*grands principes* des méthodes ainsi que de nombreux exemples d'utilisation. Ils suffisent à une compréhension générale.
2. Ces documents pointent (liens hypertextes) vers des ressources de *deuxième niveau* ou d'approfondissement car intégrant les formulatons mathématiques des méthodes et algorithmes. Ces ressources sont celles du site collaboratif [`wikistat`](http://wikistat.fr/).
3. Le troisième niveau, appliqué, est composé des tutoriels (calepins ou jupyter notebooks) explicitant le traitement élémentaire de données "jouet", les exemples illustrant les documents de cours et d'autres exemples sur des données réelles. Ils servent de base de travail durant les phases de présenciel. 
4. Un quatrième niveau est à rechercher avec d'autres exemples d'utilisation disponibles dans les dépôts: [`github - wikistat`](https://github.com/wikistat/).

**Attention**  l'installation de Python 3 est requise pour la bonne exécution des tutoriels. Le plus simple est de l'installer à partir de la distribution [Anaconda](https://www.anaconda.com/download/). R nécessite également l'installation du noyau [IRkernel](https://irkernel.github.io/installation/).

Pour **exécuter les tutoriels**, il *suffit* de cloner ce dépôt, si vous avez un compte (gratuit) et les compétences nécessaires *GitHub*, ou encore, plus simplement, de [télécharger l'archive](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/archive/master.zip) puis de la dézipper. Lancer enfin *jupyter notebook* avant d'ouvrir les différents calepins (fichiers d'extension.ipynb) dans le navigateur par défaut qui exécute *jupyter*. L'exécution de chaque cellule d'un calepin est obtenue en cliquant sur le bouton `run`.

## 1 Introduction à R

## 2 Statistique élémentaire

## 3 Modélisation statistique


## 4 Introduction à Python
*Python* et ses librairies produisent moins de résultat utiles que R à l'interprétation statistique mais fournissent des codes généralement plus efficaces pour aborder le traitement de données massives.

Des [tutoriels](https://github.com/wikistat/Intro-Python) proposent une introduction à Python et une sélection des commandes utiles au statisticien et / ou *data scientist*.  

Une connaissance experte de Python n'est pas indispensbale au suivi de ce module; ces tutoriels peuvent être sautés en première lecture. 


## 5 Exploration Multidimensionnelle

Le choix a été fait de mettre plus particulièrement l'accent sur des exemples d'application issus du monde industriel (données physiques quantitatives) plutôt que des applications (données qualitatives) de type sondage,  marketing ou fouille de textes... Comme écrit plus haut, l'introduction à d'autres méthodes et d'autres exemples d'application sont à rechercher dans les ressources des autres niveaux (2 et 4) d'approfondissement.


### 5.1 Documents de base à consulter en autonomie

- [Introduction](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsIntro.pdf): De la statistique à la *Science des Données* en passant par la fouille de données (*Data Mining*).
- [Exploration ](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsExplo.pdf) en grande dimension avec l'analyse en composantes Principales (ACP), l'analyse factorielle discriminante (AFD); classification non supervisée (*clustering*) avec *k-means*.

### 5.2 Tutoriels à approfondir lors du présenciel
Profiter du présenciel pour exécuter les calepins (*jupyer notebooks*) et **surtout poser les questions** relatives au cours et aux traitements présentés dans les différents tutoriels.

[**Télécharger**](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/archive/master.zip) l'ensemble de l'archive du dépôt ou *cloner* le dépôt si vous avez déjà un compte GitHub pour exécuter les tutoriels.

1. [Intro-ACP-AFD](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Intro-ACP-AFD-Python.ipynb)
2. [Adaptation statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Pic-Ozone-Python.ipynb) et prévision de la concentration en ozone. Traiter la première partie: *Exploration*.
3. [Reconnaissance d'activité](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-ML4IoT-Har-Python.ipynb) à partir des enregistrements d'un smartphone. Traiter la première partie: *Exploration*.
4. [Segmentation d'image](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Cluster-Mars-Python.ipynb) et cartographie de la surface de Mars.

D'autres exemples sont disponibles dans le dépôt [`github - wikistat - Exploration`](https://github.com/wikistat/Exploration).



## 6 Principes de l'Apprentissage Statistique
### 6.1 Document de base à consulter en autonomie

- [Principes de l'Apprentissage Statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Documents/csdmsApprent.pdf) 

### 6.2 Tutoriels à approfondir lors du présenciel

- [Classification supervisée](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Intro-Apprent-Python.ipynb) de données synthétiques dans **R**²
- [Adaptation statistique](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-Pic-Ozone-Python.ipynb) et prévision de la concentration en ozone. Deuxième partie: *Apprentissage et Prévision*.
- [Reconnaissance d'activité](https://github.com/Certificat-sciences-des-donnees-bigdata/Module-sensibilisation/blob/master/Calepins/CSdD-ML4IoT-Har-Python.ipynb) à partir des enregistrements d'un smartphone. Deuxième partie: *Apprentissage et Reconnaissance*.

D'autres exemples sont disponibles dans le dépôt [`github - wikistat - Apprentissage`](https://github.com/wikistat/Apprentissage).

