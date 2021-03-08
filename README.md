Road slope calculator

Algorithm description

This algorithm is used to calculate the longitudinal slope of forest paths and roads, based on a 2D line vector layer and a DEM (Digital Elevation Model). 
It should not be used on national road systems, such as highways, motorways, national and regional roads, which have engineering works designed to smooth the slope (bridges, excavations, landfills, etc.), unless the user has access to a high precision Digital Surface Model (DSM).

Input parameters: 

1 - Segment length: to calculate the slope, the initial vector layer will be segmented, and the value entered here determines the length of these segments. It is advisable that the length of the segments is equal or greater than 5 times the pixel size of the DEM. Slopes of segments whose lengths are less than 3 times the pixel size, should be considered with caution, or even discarded.

2 - Digital Elevation Model (DEM): any elevation raster, with elevation values in same units as road network vector layer lengths. 

3 - Road network vector layer: any 2D line layer; please note that this layer will be segmented, so it is recommended that the length of the features in this layer be much longer than the segment length. Make sure this vector layer is completely within the DEM data area; otherwise, slope values of segments outside the DEM data area will be meaningless.

Outputs: a new line vector layer, segmented, with two new fields:

"Length", with the current length of the segmentation (note that there will always be residual segments, of less than the chosen length); 

"Slope_%", with the longitudinal slope of each segment, in percentage.

Please start RSC plugin at Processing Toolbox:

![image](https://user-images.githubusercontent.com/37844852/110397321-8e2a7280-8069-11eb-95a3-356154fab8eb.png)
