# Etat de l'art - Exploration Autonome

## Robot deja existant et Algorithme Possible

Le [SMOB](https://blog.savoirfairelinux.com/fr-ca/2018/creation-dun-robot-autonome-pour-lexploration-et-la-mesure-de-surfaces/) se sert de l'algorithme de Mohamed Amine Yakoubi et Mohamed Tayeb Laskri, [Path Planning](https://www.sciencedirect.com/science/article/pii/S2352664516300050?via%3Dihub) cette algorithme est un [Genectic Algorithm](http://www.scholarpedia.org/article/Genetic_algorithms)

[Hector](https://ekvv.uni-bielefeld.de/blog/uninews/entry/first_steps_for_hector_the)

## Capteur

On pourrait mettre des capteurs comme un Lidar 3d ou autres qui nous permettrait d'eviter une chute sur un sol instable. Après avoir vu la simulation on sait que l'hexabot evolura sur un sol plat. Un simple lidar suffira à l'exploration autonome.


## Conclusion

Utiliser le modele du SMOB est une bonne idée (exploration complète d'un environnment inconnu), on pourait utiliser plus ou moins le meme algorithme de Path Planning avec un Lidar.
