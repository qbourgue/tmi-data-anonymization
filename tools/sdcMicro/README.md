# sdcMicro

## Installation

> Install R:

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/"
sudo apt update
sudo apt install r-base
```

> Open R-shell:
```
R
```

> Download and import R-library:
(in the R-shell)
```
install.packages('sdcMicro')

library(sdcMicro)
```

> Start the sdcMicro's GUI:
(in the R-shell)
```
sdcApp()
```

## Use

* import data
* set SDC problem
* select anonymizations techniques 
