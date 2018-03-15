# RMRC_Motion_Detection
Detection module for RMRC

## Project aim
This project aims at reaching the motion detection challenge requirements of RMRC. The final go is to create a module that can detect and track some kind of specific object that is designated by the host of RMRC

## Package used
As this is a CV project, the following packages are used:
1. Opencv3.3 for python
2. numpy

## Current status of progress
Currently, I have implemented the tracking module for the project, i.e. a module that can keep track of a moving object and draw a bounding box around it.
What is left to be done is the module that can detect and give an initial bounding box around the challenge designated object to replace the existing manually drawing initial bounding box method.

## Brief introduction to the algorithm
1. Algorithm used for tracking:
1.1 Overall
The algorithm overall is a combination of two tracking method: a KCF tracker, and a LK OpticalFlow tracker. The tracking relies largely on KCF tracker, which is able to give give both the position and the size of the bounding box.
When the KCF tracker is disabled due to bad image condition, the OpticalFlow tracker would take charge to assist the tracking until KCF is back online

1.2 KCF tracker:
This is a existing tracker incoporated in Opencv, which does a good job in dealing with occlusions. And due to its nature of an online adaptive tracking agorithm, it has a quite high reliablity and as time goes on, it would become more robust to noise.
The only problem would be that it sometimes lose track of the object if the object is moving too fast or becoming too small, and once it lose track, it is very hard to get the object back without a strong detection module. That is why optical flow comes in handy.

1.3 LK OpticalFlow:
This algorithm is a quite universal feature tracker. It does not have the capability to draw bounding around the object, and it cannot understand what exactly it is tracking. However, what it can do is that it can keep track of feature points in the image anywhere you want.
In this project, by limiting the ROI to be around the tracker object, opticalflow can effectively keep track of the features on the tracked object despite their moving speed or size. 
The displacment of these feature points can be a rough indicator of which way the object is going, thus can assist or even replace the KCF tracker if the object has hight quality feature points.
