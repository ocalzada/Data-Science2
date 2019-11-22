# Data-Science

Our machine learning algorithm takes in a URL corresponding to a JPEG image. It processes that URL image and converts it into an array of vectors (e.g. numbers). At this point, we employed transfer learning to use a pre-trained convolutional neural network (NN) 50 layers deep called, ResNet-50. This NN, which has been trained using over 1 million images, then classifies new input images into up to 1000 objects. Specifically, our model returns the top 3 predictions for what our NN believes is in the image and its confidence in that prediction.
