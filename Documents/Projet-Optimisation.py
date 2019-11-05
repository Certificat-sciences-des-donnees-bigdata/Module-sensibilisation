# librairies requises
import numpy as np
from scipy import sparse

# Environnement Spark
from pyspark import SparkContext, SparkConf

# Version locale de python (python3)
import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python'

conf = SparkConf()
#conf.setMaster("local[*]")
conf.setAppName("Matrix Factorization")

sc = SparkContext(conf = conf)

import time

start_time = time.time()

###################

def parseRating(line):
    fields = line.split('::')
    return int(fields[0]), int(fields[1]), float(fields[2])

# Chemin vers le fichier de données
movieLensHomeDir="hdfs://master:54310/input/"

# ratings : RDD du type (userID, movieID, rating)
ratingsRDD = sc.textFile(movieLensHomeDir + "ratings.dat").map(parseRating).setName("ratings").cache()

numRatings = ratingsRDD.count()
numUsers = ratingsRDD.map(lambda r: r[0]).distinct().count()
numMovies = ratingsRDD.map(lambda r: r[1]).distinct().count()
print("We have %d ratings from %d users on %d movies.\n" % (numRatings, numUsers, numMovies))

M = ratingsRDD.map(lambda r: r[0]).max()
N = ratingsRDD.map(lambda r: r[1]).max()
matrixSparsity = float(numRatings)/float(M*N)
print("We have %d users, %d movies and the rating matrix has %f percent of non-zero value.\n" % (M, N, 100*matrixSparsity))

################@

# Séparation du jeu de données en un jeu d'apprentissage et un jeu de test
# Taille du jeu d'apprentissage (en %)
learningWeight = 0.7
# TO DO
# Création des RDD "apprentissage" et "test" depuis la fonction randomsplit

# Calcul du rating prédit
def predictedRating(x, P, Q):
    """ 
    This function computes predicted rating
    Args:
        x: tuple (UserID, MovieID, Rating)
        P: user's features matrix (M by K)
        Q: item's features matrix (N by K)
    Returns:
        predicted rating: l 
    """
    #### TO DO

# Calcul de l'erreur MSE
def computeMSE(rdd, P, Q):
    """ 
    This function computes Mean Square Error (MSE)
    Args:
        rdd: RDD(UserID, MovieID, Rating)
        P: user's features matrix (M by K)
        Q: item's features matrix (N by K)
    Returns:
        mse: mean square error 
    """ 
    ##### TO DO

    
################    

# Tailles des jeux de données d'apprentissage et de tests
print("Size of the training dataset:", trainRDD.count())
print("Size of the testing dataset:", testRDD.count())

# Création de matrices aléatoires de dimension (M,K) et (N,K)
K = 20
# TO DO

# Calcul et affichage de l'erreur MSE pour ces matrices aléatoires
#### TO DO


# Affichage de quelques ratings prédits depuis ces matrices
#### TO DO

##################

# Algorithem de descente de gradient pour la factorisation de matrices
def GD(trainRDD, K=10, MAXITER=50, GAMMA=0.001, LAMBDA=0.05):
    # create the rating matrix R (sparse)
    row=[]
    col=[]
    data=[]
    for part in trainRDD.collect():
        row.append(part[0]-1)
        col.append(part[1]-1)
        data.append(part[2])
    R=sparse.csr_matrix((data, (row, col)))
    
    # Initialisation aléatoire des matrices P et Q
    M,N = R.shape
    P = np.random.rand(M,K)
    Q = np.random.rand(N,K)
    
    # Calcul de l'erreur MSE initiale
    mse=[]
    mse_tmp = computeMSE(trainRDD, P, Q)
    mse.append([0, mse_tmp])
    print("epoch: ", str(0), " - MSE: ", str(mse_tmp))
    
    nonzero = R.nonzero()
    nbNonZero = R.nonzero()[0].size
    I,J = nonzero[0], nonzero[1]
    for epoch in range(MAXITER):
        for i,j in zip(I,J):
        # Mise à jour de P[i,:] et Q[j,:] par descente de gradient à pas fixe
        #### TO DO
        
        # Calcul de l'erreur MSE courante, et sauvegarde dans le tableau mse
        #### TO DO
        
    return P, Q, mse
    
    
######################
# Calcul de P, Q et de la mse
P,Q,mse = GD(trainRDD, K=10, MAXITER=5, GAMMA=0.001, LAMBDA=0.05)
######################

#####################
# Prédiction des ratings
ratingsTrueAndPred = testRDD.map(lambda x: (x[0], x[1], x[2], predictedRating(x, P, Q)))
print("\n(userID, movieID, rating, predicted SGD)")
ratingsTrueAndPred.takeSample(False, 5)

end_time = time.time()

print("==================================");
print("Execution time : %s seconds" % (end_time - start_time))
print("==================================");
