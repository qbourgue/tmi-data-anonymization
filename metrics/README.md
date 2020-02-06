# Metrics to evaluate the anonymization

## Documentation

* Technical Privacy Metrics: A Systematic Survey
Isabel Wagner, David Eckhoff (2018)
https://doi.org/10.1145/3168389

## I) INTRODUCTION
   Privacy-enhancing technologies (PETs)

## II) CONDITIONS FOR PRIVACY METRICS

## III) PRIVACY DOMAINS
### 3.2) Databases

## IV) CHARACTERISTICS OF PRIVACY METRICS
#### 4.1) Adversary Goals
   quantify the level of privacy in a system (database) provided by a PET
#### 4.2) Adversary Capabilities
   - local/global
   - activite/passive
   - internal/external
   - static/adaptive
   - prior knowlegde
   - resources
#### 4.3) Data sources
   - Published Data
   - Observable Data
   - Repurposed Data
   - All Other Data
#### 4.4) Inputs for Computation of Metrics
   - Adversary's Estimate
   - Adversary's Resources
   - True Outcome
   - Prior Knowledge
   - Parameters
#### 4.5) Output Measures

   - Uncertainty
     high uncertainty in the adversary's estimate correlates with high privacy. 

   - Information Gain or Loss
     metrics that measure information gain or loss quantify the amount of information gained by the adversary or the amount of privacy lost by users due to disclosure of information

   - Data Similarity
     data similarity metrics measure similarity either within a dataset (forming equivalence classes, or  between two sets of data

   - Indistinguishability
     metrics analyze whether the adversary is able to distinguish bewteen two outcomes of a privacy mechanism (privacy)

   ====> SCHEMA
   - Adversary's Success Probability
     metrics using the adversary's success probability to quantify privacy indicate how likely it is for the adversary to succeed in any one attempt, or how often he or she would succeed in a large number of attempts

   - Error
     error-based metrics measure how correct the adversary's estimate is (the distance between the true outcome and the estimate)

   - Time
     time-based metrics measure either the time until the adversary's success or the time until the adversary's confusion

   - Accuracy or Precision
     metrics quantify how precise the adversary's estimate without considering the estimate's correctness

#### Metric's signifiance for the use case 1:

```
_by Quentin_
+---+---+---+---+---+---+---+---+
| 3 | 4 | 1 | 2 | 6 | 8 | 7 | 5 |
+---+---+---+---+---+---+---+---+

_by PH_
+---+---+---+---+---+---+---+---+
| 4 | 2 | 3 | 6 | 8 | 5 | 1 | 7 |
+---+---+---+---+---+---+---+---+

_by compromise_
+---+---+---+---+---+---+---+---+
| 4 | 3 | 2 | 1 | 6 | 8 | 5 | 7 |
+---+---+---+---+---+---+---+---+
```

## V) PRIVACY METRICS

### Indistinguishability (5.4)

#### 5.4.1  Cryptographic Games/Semantic Security

Adversary select input for a protocol, and is given the output and two alternative outcome. Probability of the adversary to guess the correct outcome out of two possible.
If proba lower than 1/2 + epsilon, than 

#### 5.4.2  Differential Privacy.
In statistical databases, differential privacy guarantees that any disclosure is equally likely regardless of whether or not an item is in the database. For example, the result of a database query should be roughly the same regardless of whether the database contains an individual’s record or not. This guarantee is usually achieved by adding a small amount of random noise to the results of database queries.

Differential Privacy provides privacy only for certain type of querry, abd limited number of queries.

Use  Hamming distance.

=> Adding noise 


#### 5.4.3 Approximate Differential Privacy.

Lighter form of Differential Privacy. 

#### 5.4.4 Distributed Differential Privacy

Use when distributed entities contribute data to a central data aggregator.
For *Smart metering*.

#### 5.4.5 Distributional Privacy

Distributional privacy extends differential privacy to a setting inwhich the datasets themselves do not need to be protected, but the parameters governing thegeneration of data do

#### 5.4.6 Geo-Indistinguishability.

Introduction of a two dimensional noise.
Ex: Be able to know the city, but not the precise location.

#### 5.4.7  d-χ-Privacy

d-χ-Privacy is a generalization of differential privacy that uses distinguishability metrics dχ to characterize the distance between two datasets instead of the Hamming distance used in standard differential privacy. 

#### 5.4.8  Joint Differential Privacy

The idea of joint differential privacy is that an individual’s private data can be disclosed to the individual himself, but not to other individuals.

#### 5.4.9  Computational Differential Privacy

#### 5.4.10  Information Privacy

Information privacy captures the notion that the prior and posterior probabilities of inferring sensitive data x do not change significantly, given query outputs y.

#### 5.4.11  Observational Equivalence

Observational equivalence is a formal property that states that the adversary cannot distinguish between two situations.

### Data Similarity (5.3)

(Database domain, applied in the context of data sanitization and data publishing)

 - k-Anonymity
  ° identifying columns are removed from the dataset
  ° quasi-identifying columns grouped by equivalence class
  ° minimum of k rows for one equivalence class
  => studies have shown k-anonymity to be insufficient (high-dimensional cases, correlation with other datasets, disclosure)

 - (alpha, k)-Anonymity
  ° the frequency of sensistive value has to be less than alpha
  ° disclosure problem
  => no single sensitive attribute can be dominant in an equivalence class

 - l-Diversity
  ° each equivalence class must contain at least l-well represented sensitive values
  ° do not prevent *probabilistic inference attack*
  => stronger instantiations: in each equivalence class, sensitive attacks must have roughly the same frequence ~ integrity ?

 - m-Invariance
  ° allow multiple releases of the same dataset that may contain added, modified or deleted rows
  ° every equivalence class must have at least m rows
  ° the values for sensitive attributes must all be different
  ° the set of distinct sensitive values in each equivalence class must be the same in every release

 - t-Closeness
  ° prevent attribute disclosure by an adversary with knowledge about the global distribution of sensitive attributes
  ° the distribution of sensitive values must be close to their distribution in the overall table
  ° the distance must be smaller than a threshold t

 - Stochastic t-Closeness
  ° modification of the sensitive values
  ° if the distribution of the sensitive values satisfies (epsilon)-differential privacy, then the data table satisfies stochastic t-closness

 - (c, t)-Isolation
  ° extends k-anonymity to consider an adversary, it measures how well an adversary can isolate points in a database

 - (k, e)-Anonymity
  ° modify k-anonymity to apply to numerical instead of categorical attributes
  ° (???) requires tgat the range of sensitive attributes in any equivalence class must be greater than e

 - (epsilon, m)-Anonymity 
  ° extension of k-anonymity to numerical attributes
  ° bounding the probability of inferring the value of a sensitive attribute to at most 1/m

 - Multirelational k-Anonymity
  ° k-anonimity extended to multiple tables in a relational database 

 - (X, Y)-Privacy
  ° 

### Information Gain (5.2)

#### 5.2.2 **Relative Entropy** 

Also called Kullback-Leibler divergence (KL divergence). Measures the distance between two probability distributions.

#### 5.2.3 **Mutual Information** 

Mutual information quantifies how much information is shared between two random variables.

#### 5.2.4 Conditional Privacy Loss

Fraction of privacy which is lost by revealing one attribute

#### 5.2.5 Conditional Mutual Information

Mutual Information with a prior knowledge consideration.

#### 5.2.6 Loss of Anonymity

The metric computes the maximum mutual information, ie the max amount of info that can leak from the anonymity protocol, over all possible distribution. 

#### 5.2.7 Maximum Information Leakage

Modifies mutual information to consider only a single realization of a random variable.

It quantifies the maximum amount of information about private events or dataX that can be gained by an adversary observing a single output y, where the maximum is taken over all possible outputs. 

#### 5.2.8 System Anonymity Level

It describes the amount of additional information needed to reveal all sender-receiver relationships.

#### 5.2.9 Information Surprisal 
It measures self-information. It quantifies how much information is contained in a specific outcome x of a random variable X.

#### 5.2.10 Privacy Score

The privacy score in a social network indicates a useru’s potential privacyrisk. It increases with the sensitivity and visibility of information items.

#### 5.2.11  Positive Information Disclosure

Shannon’s criterion for perfect secrecy demands that the adversary’s prior probability for the secret x equals the posterior probability that takes into account a new observation y.

This metrics quantifies  how much the adversary’s posterior probability improves.

#### 5.2.12 Increase in Adversary’s Belief

The increase in adversary’s belief measures the differencebetween the adversary’s prior and posterior probabilities.

#### 5.2.14 Pearson’s Correlation Coefficient

It measuresthe degree of linear dependence between two random variables.

#### 5.2.15 Full/Partial Disclosure

For query auditing. (Full disclosure indicates whether a set of data-base queries uniquely determines a sensitive value)

### Uncertainity (5.1)

