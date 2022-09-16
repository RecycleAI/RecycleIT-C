Analyzing Different Types of ObjectMoments (7 different types)

Hu Moment invariants
We would like to calculate moments that are invariant to translation, scale, and rotation and they are called Hu Moments. 
Hu Moments (or rather Hu moment invariants) are a set of 7 numbers calculated using central moments that are invariant to image transformations. The first 6 moments have been proved to be invariant to translation, scale, rotation, and reflection. While the 7th moment’s sign changes for image reflection.

Develop ObjectMoments Class
•	Read in image as Grayscale
•	Binarize the image using thresholding
•	Calculate Hu Moments
•	Log Transform

Shape Matching using Hu Moments
If the distance is small, the shapes are close in appearance and if the distance is large, the shapes are farther apart in appearance. OpenCV provides an easy to use a utility function called matchShapes that takes in two images (or contours) and finds the distance between them using Hu Moments.