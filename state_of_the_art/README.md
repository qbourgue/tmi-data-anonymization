# Abstract of articles about the data anonymization

### Anonynimisation des données d'entreprise en lien avec le RGPD :
Le lien suivant donne une introduction aux problèmes d'anonymisation des données d'entreprise en lien avec le RGPD :

https://medium.com/meetech/lanonymisation-de-donn%C3%A9es-une-qu%C3%AAte-encore-difficile-au-lendemain-de-l-entr%C3%A9e-en-vigueur-du-rgpd-6d25522fd2d6

```
Introduction :
> utilisation des données personnelles à des fins de cliblage, ou d'étude marketing, de recherche ou pour des tests applicatifs.
> l'objectif est d'ôter leur caractère identifiant tout en préservant leur signifiancee et cohérence.

Anonymisation, enjeux, difficultés, et limites :
> distinction entre anonymisation / pseudonymisation / chiffrement
anonymisation et chiffrement -> réversible, données partiellement ou totalement illisibles -> nécessite la clé de déchiffrement ou une table de pivot
> anonymisation : appliquer une série de transformations irréversibles pour rendre l'identification d'un individu impossible - mais que les données restent exploitables (marketing, dev. logiciel)  
> risque de réidentification : difficulté majeure de l'anonymisation --> risque toujours existant, à mesurer.
> critères pour évaluer la qualité d'une anonymisation :
	* individualisation : est-il possible d'isoler un individu ?
	* corrélation : relier des données concernant un individu entre plusieurs ensembles distincts
	* inférence : est-il possible de déduire de l'information sur un individu à partir des données disponibles ?

Marché technologique en cours de maturation :
> data masking
> certification des solutions ?
```


### Besoins d'anonymisation des odnnées de production

Le lien suivant est plus ciblé sur les besoins d'anonymisation des données de production qui est le sujet de votre projet :

https://arcadsoftware.fr/infos-et-evenements/blog-fr/questions-frequentes-anonymisation-donnees/

```
Rôle de l'anonymisation des données :

Différence entre anonymisation et pseudonymisation :

Données personnelles & données sensibles :
> donnée personnelle : "toute information relative à une personne physique susceptible d'être identifiée, directement ou indirectement"
> donnée sensible : "toute information qui rév_le les origines raciales ou ethniques, les opinions politiques, philosophiques ou religieuses, l'appartenance syndicale, la santé ou la vie sexuelle d'une personne physique"
>> identifier les données à anonymiser

Impact de l'anonymisation sur l'informatique
> "on constate que seuls une vingtaine de pourcents des données nécessitent d'être anonymisées"

Comment identifier les données qui doivent être anonymisées ?
> anonymisation réalisée pour les environnements de tests : bonne connaissance du périmètre global de la bdd
> données indissociables
> droit à l'oubli (à prendre en compte ??)
```

### Pseudonymization, anonymization, chiffrement ... what is the difference ? 

https://teskalabs.com/blog/data-privacy-pseudonymization-anonymization-encryption

```
> ** Pseudonymisation ** : tranforme une donnée sensible en une pseudoaléatoire chaîne de caractères. Le string resultant est toujours le même pour le même input, tel que des corrélations analytiques sont toujours posibles.

Ce procédé est appelé ** "data tokenization" **.

>> Recommander d'utiliser les fonction de hash cryptographique au coeur de la pseudonymisation (ex: SHA-384, SHA-512).

> ** Anonymisation ** : altération irreversible d'information qui pourrait mener à l'identification d'un individu. Cas extrême : suppression de l'information.

> ** Généralisation ** : Remplace les données individuelles par des catégories plus larges. (ex:  55 ans --> 50-60 ans, 14510 -> Calvados, OL -> Equipes de foot dans la décadence) 

>> Encombinant la généralisation et la suppression, on peut atteindre la ** k-anonymity **. 

>> K-anonymity : une information concernant une personne ne peut pas être distinguées de k-1 individus. [wiki]<https://en.wikipedia.org/wiki/K-anonymity>


> ** Encryption ** : Transcrit les données en une autre forme, telle que seules les personnes posèdant la clé secrète d'chiffrement puisse lire les données.

>> Il existe différents type d'chiffrement: symétrique, asymétrique et hybride (mélange des deux)

>> Chiffrement Symétrique : Advanced Encryption Standard [AES]<https://en.wikipedia.org/wiki/Advanced_Encryption_Standard>. Faiblesse: la clée secrète est présente du coté de l'chiffrement. Ainsi n'importe qui ayant accés à la chaine d'chiffrement peut décoder les données.

>> Chiffrement Asymétrique : utilise deux clées: public et privé. Mais l'chiffrement est très lente. Rarement utilisé en data chiffrement.

> ** Chiffrement Homéomorphique **: le but est de permettre les calculs sur les données chiffrées. Les résultats de calcul sur les données chiffrés correspondent aux résultats de calcul sur les données originale, une fois déchiffré.

En pratique, deployement compliqué. 

```

### Top 5 Free Data Anonymization Tools

https://aircloak.com/top-5-free-data-anonymization-tools/

```
Overview:
> Wide range of data anonymization tools available
> The most important questions:
 * what programming environment are you using?
 * what anonymization methods do you need?
 * how accessible and easy to use should the solution be ?

Open Source Anonymization Software:
> ARX Data Anonymization Tool
https://arx.deidentifier.org/
Populare and cross-platform tool, it supports k-anonymity (and its variants) and has a GUI.
> Amnesia
https://amnesia.openaire.eu/
It support k-anonymity (and km-a), it allows the user to find the right balance between privacy and data utility.
> µ-ARGUS
http://neon.vb.cbs.nl/casc/mu.htm
Tool build to support statistical analyses.
Uses a wide range of different statistical anonymization methods such as global recording (grouping of categories), local suppression, randomisation, adding noise, microaggregation, top- and bottom coding.
Generates synthetic data
> sdcMicro
https://cran.r-project.org/package=sdcMicro
Generation of anonymized (micro)data.
Risk estimation methods are included.
Includes a GUI
> Anonimatron
https://realrolfje.github.io/anonimatron/
https://github.com/realrolfje/anonimatron
Tool that pseudonymizes datasets
Can be used to generate pseudonymized production data to find bug

Professional Data ANonymization Software:
Offer GDPR-compliant and interaction anonymization (very high level of data utility for precise analyses)
```

### Tool to anonymize database

https://github.com/DivanteLtd/anonymizer

(requirements) ruby, mysql
(supported frameworks) magento, pimcore, sylius

### Tool to anonymize data

https://github.com/sunitparekh/data-anonymization

### Inform about: Junade Ali

Junade Ali a combiné le k-anonymity avec du [hashing cryptographique]<https://en.wikipedia.org/wiki/Cryptographic_hash_function> pour créer un protocol de communication pour verifier anonymement si un mot de passe a été fuité sans révéler les password recherchés.
Ce même protocol a été utilisé dans l'API de Troy Hunt,  "Have I been Pwned ?"  
