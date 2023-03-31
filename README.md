# Josephjiao7-Wavelet-transform-fusion-for-spatial-data
This is the code for wavelet transform fusion.
Please check that the file has the same number of rows and columns using the resampling method before fusing.
The method consists of the following steps:
1.Read the input raster files and get the geographic coordinate information.

2.Read raster datasets and preprocess the data by replacing any NoData values with zero.

3.Perform wavelet decomposition on the preprocessed data using the Haar wavelet transform.

4.Fuse the approximation and detail coefficients obtained from the wavelet decomposition by computing theweighted average of the corresponding coefficients.

5.Perform wavelet reconstruction using the fused coefficients to obtain the final fused image.Write the output image to a GeoTIFF file.

If you use this code for your research, please cite the following paper:
Tile: Introducing big data to measure the spatial heterogeneity of human activities for optimizing the ecological security pattern: A case study from Guangzhou City, China.
Journal: Ecological Indicators
