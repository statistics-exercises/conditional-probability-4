# Bayesian statistics 

In this next series of exercises, we are going to consider how to use Bayes theorem to analyse the results from experiments.  This material is slightly beyond what is covered in the exam.  These exercises are primarily there to show you that Bayes theorem is not simply a curiosity.  If you do not fully understand you do not need to worry too much I am just trying to give you a flavour of how we might actually use Bayes theorem.  Without further ado then let's consider the experiment:

_We have developed a cheap test for a disease and we want to determine how accurate it is.  Every time we encounter a patient with symptoms of this disease we run the older (more-expensive and more-reliable) test for the disease.  If this test confirms the patient has the disease we run the newer, cheaper test.  Our objective is to calculate the conditional probability that the test gives a positive result given that the person has the disease._

If we apply the method of moments or the maximum likelihood method to the Bernoulli random variable that is sampled in this experiment we see that the conditional probability we desire can be calculated by dividing the total number of individuals with a positive test result by the total number of tests performed.  Importantly, however, the value of the probability that we are estimating using these methods is a random variable.  What we will see here is that Bayes theorem allows us to extract the distribution that is sampled by this random variable directly.  If we suppose that the outcome of the first test was positive (T_1=1) we can then write the following:

![](https://render.githubusercontent.com/render/math?math=P(p=\theta|T_1=1)=\frac{P(T_1=1|p=\theta)P(p=\theta)}{P(T_1=1)} = \frac{P(T_1=1|p=\theta)P(p=\theta)}{\int_{0}^{1}P(T_1=1|p=\theta')P(p=\theta')\textrm{d}\theta'})

In this expression, p is the quantity we are interested in; namely, our estimate for the conditional probability of a positive test result given the patient definitely has the disease.  ![](https://render.githubusercontent.com/render/math?math=P(p=\theta|T_1=1)) is the conditional probability density for this quantity given that the first test (![](https://render.githubusercontent.com/render/math?math=T_1)) we did gave a positive result.  This quantity is known as the posterior probability.

If you look at the middle part of the equation above you see that we have written is just a statement of Bayes theorem.  The only difference from what we have seen previously is that ![](https://render.githubusercontent.com/render/math?math=P(T_1=1|p=\theta)) is a conditional probability density (the likelihood) and ![](https://render.githubusercontent.com/render/math?math=P(p=\theta)) is also probability density (the prior).  To calculate ![](https://render.githubusercontent.com/render/math?math=P(T_1=1)) we thus have to perform an integral over all the possible probability values that the parameter of the distribution might take using a continuous analogue of the partition theorem.

The likelihood part of this expression is simple.  We use a Bernoulli random variable to model the outcome of each test so this random variable can only be 0 or 1.  Furthermore:

![](https://render.githubusercontent.com/render/math?math=P(T_1=1|p=\theta)=\theta\qquad\P(T_1=0|p=\theta)=1-\theta)

The prior is more tricky.  We have to pick the initial probability density function for the parameter.  In this case, it is not unreasonable to assume that the test is more likely to give a positive result if the patient is sick.  We will thus assume that: 

![](https://render.githubusercontent.com/render/math?math=P(p=\theta)=2\theta\qquad\0<\theta<1)

We could (however) have also assumed that this probability was simply equal to 1.  If we had done so we would have been assuming a so-called uniform prior i.e. that every value for the parameter is equally likely. 

__With all that in mind, your task in this exercise is to use SymPy to determine the posterior probability density.__  To do this I would recommend you use `sy.integrate` to calculate the integral in the denominator of first expression above.  Use the expressions that I have given in the second two expressions on this page for the likelihood and the posterior and set the variable `denom` to the value output by this integration.  `denom` and the numerator of the above expression can then be inserted into an `sy.simplify` command to determine the posterior.  The variable `posterior` should be set equal to the function that is output by this `sy.simplify` command. The code I have written for you will then print out this function and draw a graph showing the distribution.
