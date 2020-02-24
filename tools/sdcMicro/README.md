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

## Anonymization methods

### Rank swapping

> K0:
The algorithm keeps the change in the means of the variables before and after rank swapping within a range based on the subset-mean preservation factor K_0. The absolute difference between the variable mean before and swapping (abs(X_1 - X_2), where X_1 is the (subset) sample mean before swapping and X_2 is the (subset) sample mean after swapping) is kept smaller than or equal to 2 * K_0 * X_1 / sqrt(N_S), where N_S is the sample size of the subset under consideration. Therefore, larger values of K_0 allow larger deviations.

## Parse results

Vim replace all characters up to first comma
:%s/^[^,]*,//g
:%s/"//g
