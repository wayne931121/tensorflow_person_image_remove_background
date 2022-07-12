# tensorflow_person_image_remove_background

*   [Model weights url](https://drive.google.com/drive/folders/1wU1Np8thAQ5qBpwmUTCcIWpS9772Nror?usp=sharing)
*   Object Detection: SSD ResNet50 V1 FPN 640x640 (RetinaNet50)
*   Image Segmentation: Unet

## Target

*   Remove person images or videos background

## Using

*   Python
*   Tensorflow
*   Opencv
*   Numpy
*   and so on.

## What our code do?

1. Object Detection > Get boxes
2. Image Segmentation in each detected image boxes > Get mask
3. Remove background > Result

## References

*   [https://www.tensorflow.org/?hl=zh-tw](https://www.tensorflow.org/?hl=zh-tw)
*   [https://github.com/tensorflow/models](https://github.com/tensorflow/models)
*   [https://github.com/tensorflow/models/blob/master/research/object_detection/colab_tutorials/eager_few_shot_od_training_tf2_colab.ipynb](https://github.com/tensorflow/models/blob/master/research/object_detection/colab_tutorials/eager_few_shot_od_training_tf2_colab.ipynb)
