## Welcome!
Welcome! In this lesson, you'll learn how to use TensorFlow for building deep learning models. TensorFlow is an open source machine learning library developed by Google and has been making a pretty big impact in the deep learning community and is being adopted by teams everywhere in industry and academia. In my experience, it's the absolute best framework for learning deep learning and it is just a delight to work with in general. By the end of this lesson, you'll have trained your own deep learning model that can classify images of cats and dogs.

You will start by getting a basic introduction to TensorFlow, where you will learn about __tensors__ - the main data structure of TensorFlow. You will learn how to create tensors and use them to create neural networks.

Next, you will learn how to use TensorFlow and Keras to build and train neural networks, and how to test your models using test sets and validation sets.

Finally, you will learn how to use pre-trained networks to improve the performance of your models, a technique known as __transfer learning__.

Follow along with the videos and work through the exercises in your own notebooks. If you get stuck, check out my solution videos and notebooks.

## Get the notebooks
All the notebooks for this lesson are available from on the [GitHub repo](https://github.com/udacity/intro-to-ml-tensorflow).

Follow along in your notebooks to complete the exercises. I'll also be providing solutions to the exercises, both in videos and in the notebooks marked `(Solution)`.

## Dependencies
These notebooks require TensorFlow 2.0 or newer, TensorFlow Datasets, and TensorFlow Hub. The easiest way to install TensorFlow 2.0, TensorFlow Datasets, and TensorFlow Hub is via `pip`.

You'll also need to install NumPy and Jupyter notebooks, the newest versions of these should work fine. Using the conda package manager is generally best for this,

`conda install numpy jupyter notebook`

If you haven't used conda before, [please read the documentation](https://conda.io/en/latest/) to learn how to create environments and install packages. You can also install Miniconda instead of the whole Anaconda distribution. The normal package manager `pip` also works well in conda. If you have a preference, go with that.

The final part of the series has a soft requirement of a GPU used to accelerate network computations. Even if you don't have a GPU available, you'll still be able to run the code and finish the exercises. If you can't use a local GPU, you can use cloud platforms such as [Google Cloud GPUs](https://cloud.google.com/gpu/) to train your networks on a GPU. You can also check out Google's Colaboratory. Google's [Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb) is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud. With Google's Colaboratory you have the option to run your code with a GPU for free!

Our Nanodegree programs also provide GPU workspaces in the classroom.

## Feedback
If you have problems with the notebooks, please contact support or create an issue on the repo. We're also happy to incorporate your improvements through pull requests.