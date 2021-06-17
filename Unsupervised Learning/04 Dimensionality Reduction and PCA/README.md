## What is PCA?

Here you saw that PCA (or principal component analysis) is the first of the techniques you will see aimed at dimensionality reduction. This technique is about taking your full dataset and reducing it to only the parts that hold the most information.

## How Well Will You Understand PCA After This Lesson?
The goal is for everyone to leave this lesson with an understanding of:

1. How PCA is used in the world.
2. How to perform PCA in python.
3. A conceptual understanding of how the algorithm works.
4. How to interpret the results of PCA.

If you want to dive deeper into the mathematics, there will be additional links provided, but it will not be a main focus of this lesson.

## PCA Lesson Topics
There is a lot to cover with Principal Component Analysis (or PCA). However, you will gain a solid understanding of PCA by the end of this lesson, by applying this technique in a couple of scenarios using scikit-learn, and practicing interpreting the results.

We will also cover conceptually how the algorithm works, and I will provide links to explore what is happening mathematically in case you want to dive in deeper! Here is an outline of what you can expect in this lesson.

### 1. Dimensionality Reduction through Feature Selection and Feature Extraction
With large datasets we often suffer with what is known as the "curse of dimensionality," and need to reduce the number of features to effectively develop a model. Feature Selection and Feature Extraction are two general approaches for reducing dimensionality.

### 2. Feature Extraction using PCA
Principal Component Analysis is a common method for extracting new "latent features" from our dataset, based on existing features.

### 3. Fitting PCA
In this part of the lesson, you will use PCA in scikit-learn to reduce the dimensionality of images of handwritten digits.

### 4. Interpreting Results
Once you are able to use PCA on a dataset, it is essential that you know how to interpret the results you get back. There are two main parts to interpreting your results - the principal components themselves and the variability of the original data captured by those components. You will get familiar with both.

### 5. Mini-project
Finally, you will put your skills to work on a new dataset.

### 6. Quick Recap
We will do a quick recap, and you will be ready to use PCA for your own applications, as well as the project!

## Dimensionality Reduction and PCA - Lesson Topics
Phew! That was a ton of information - here is a quick recap!

### 1. Two Methods for Dimensionality Reduction
You learned that Feature Selection and Feature Extraction are two general approaches for reducing the number of features in your data. Feature Selection processes result in a subset of the most significant original features in the data, while Feature Extraction methods like PCA construct new latent features that well represent the original data.

### 2. Dimensionality Reduction and Principal Components
You learned that Principal Component Analysis (PCA) is a technique that is used to reduce the dimensionality of your dataset. The reduced features are called __principal components__, or __latent features__. These __principal components__ are simply a linear combination of the original features in your dataset.

You learned that these components have two major properties:

1. They aim to capture the most amount of variability in the original dataset.
2. They are orthogonal to (independent of) one another.

### 3. Fitting PCA
Once you got the gist of what PCA was doing, we used it on handwritten digits within scikit-learn.

We did this all within a function called `do_pca`, which returned the PCA model, as well as the reduced feature matrix. You simply passed in the number of features you wanted back, as well as the original dataset.

### 4. Interpreting Results
You then saw there are two major parts to interpreting the PCA results:

1. The __variance explained__ by each component. You were able to visualize this with scree plots to understand how many components you might keep based on how much information was being retained.
2. The __principal components__ themselves, which gave us an idea of which original features were most related to why a component was able to explain certain aspects about the original datasets.

### 5. Mini-project
Finally, you applied PCA to a dataset on vehicle information. You gained valuable experience using scikit-learn, as well as interpreting the results of PCA.

With mastery of these skills, you are now ready to use PCA for any task in which you feel it may be useful. If you have a large amount of data, and are feeling afflicted by the curse of dimensionality, you want to reduce your data to a smaller number of latent features, and you know just the way to do it!

### 6. Do you think you understand PCA well enough yet to explain it in a way that would make sense to your grandmother?
Here is an interesting StackExchange post that does just that, and with animated graphics! https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues
