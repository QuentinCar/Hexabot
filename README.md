# Hexabot

Ceci est un template de dépôt Git pour le cours d'ingénierie système et modélisation robotique de l'UV 5.8 à l'ENSTA Bretagne en 2020.


## Lancer la simulation

### Dépendences

package hector_slam


### Démarrer la simulation
```bash
roslaunch phantomx_gazebo phatomx_gazebo.launch
roslaunch phantomx_description diplay.launch
rosrun phantomx_marker markerdisplay_marker
rosrun phantomx_gazebo follow_wal
```


## Groupe
	AQADAC

### Membres

Alexandre Argento
Axel Porlan
Aurelien Lebrun
Cyril Cotsaftis
David Brellmann
Quentin Cardinal

### Gestion de projet

Lien vers notre [Taiga](https://tree.taiga.io/project/quentincar-hexabot/backlog).



## Structure du dépôt

### Workspace ROS

Le dossier `workspaceRos` est la racine du workspace `catkin` pour les packages ROS. Ces derniers doivent être placés sous `workspaceRos/src`.    
Consulter le [README](workspaceRos/README.md) du workspace pour plus d'informations.


### Documents

Le dossier `docs` contient tous les documents utiles au projet:
- Des [instructions pour utiliser Git](docs/GitWorkflow.md)
- Un [Mémo pour ROS et Gazebo](docs/MemoROS.pdf)


### Rapports

Le dossier `reports` doit être rempli avec les rapports d'[objectifs](reports/GoalsTemplate.md) et de [rétrospectives](reports/DebriefTemplate.md) en suivant les deux templates mis à disposition. Ces deux rapports doivent être rédigés respectivement au début et à la fin de chaque sprint.
