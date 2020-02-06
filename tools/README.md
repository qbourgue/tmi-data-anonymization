## ARX Anonymization Tool

### Installation

On linux:

> chmod u+x ARX-3.7.1-linux-x64-installer.run
> ./ARX-3.7.1-linux-x64-installer.run

> ./ARX-launcher.run

### Open a project

```
File -> Open a project...
Select the example project:
s5-data_anonymization/tools/arx/example.deid
```

### Create a new project

```
File -> New project...
File -> Import data...
```

### Basic anonymization process

```
Configure transformation
--> Data Transformation
 > select the type, the transformation, ...
--> Attribute medata
 > select which data to anonymize

Edit -> Anonymize
```

### See the anonymization's results

```
Analyze/enhance utility --> Output data
```

## Amnesia

### Installation

On linux:

```
Download the zip file for 64-bit Linux:
https://amnesia.openaire.eu/installation.html
```

> unzip amnesia_lin64bit.zip
> chmod u+x Amnesia.jar
> java -jar Amnesia.jar
~ problème à cette étape : Noe java alive ~~

Pros:
* get a score of your anonymization and allows the user to delete some data to improve the score.

Cons:
* k-anonymity only
* not customizable

## µ-ARGUS

It seems to be better to install the Windows release.

Cons:
* Doesn't work with a .csv file


## sdcMicro



## Anonimatron

### Installation

On linux:

```
Follow the Quick Start from https://github.com/realrolfje/anonimatron
```

Cons:
* CLI, few customizable options
