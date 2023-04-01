# Author: Joseph Jiao @josephjiao233@gmail.com
# Date: 2023-03-31
# -*- coding: utf-8 -*-
import gdal
import pywt
import numpy as np

'''
The code is implemented in Python and uses the GDAL and PyWavelets libraries.
Please check that the file has the same number of rows and columns using the resampling method before fusing.

The method consists of the following steps:
1.Read the input raster files and get the geographic coordinate information.

2.Read raster datasets and preprocess the data by replacing any NoData values with zero.

3.Perform wavelet decomposition on the preprocessed data using the Haar wavelet transform.

4.Fuse the approximation and detail coefficients obtained from the wavelet decomposition by computing the
weighted average of the corresponding coefficients.

5.Perform wavelet reconstruction using the fused coefficients to obtain the final fused image.
Write the output image to a GeoTIFF file.

If you use this code for your research, please cite the following paper:
Tile: Introducing big data to measure the spatial heterogeneity of human activities for optimizing 
the ecological security pattern: A case study from Guangzhou City, China.
Journal: Ecological Indicators
'''
# Read the input raster file and get the geographic coordinate information
input_file1 = 'input1.tif'
input_file2 = 'input2.tif'
ds1 = gdal.Open(input_file1)
ds2 = gdal.Open(input_file2)
geotransform = ds1.GetGeoTransform()

# read raster datasets
band1 = ds1.GetRasterBand(1)
band2 = ds2.GetRasterBand(1)
data1 = np.array(band1.ReadAsArray())
data1 = np.where(data1 != band1.GetNoDataValue(), data1, 0)
data2 = np.array(band2.ReadAsArray())
data2 = np.where(data2 != band1.GetNoDataValue(), data2, 0)
# fusion
coeffs1 = pywt.dwt2(data1, 'haar')
coeffs2 = pywt.dwt2(data2, 'haar')
print(coeffs1[1])

# Fusing approximation and detail coefficients
cA = (coeffs1[0] + coeffs2[0]) / 2  # Fusing approximation factor
cH = (coeffs1[1][0] + coeffs2[1][0]) / 2  # Fusion level detail factor
cV = (coeffs1[1][1] + coeffs2[1][1]) / 2  # Fusion vertical detail factor
cD = (coeffs1[1][2] + coeffs2[1][2]) / 2  # Fusion diagonal detail factor

# Combine the fused coefficients into a list
fusion_coeffs = [cA, (cH, cV, cD)]

# Inverter
fusion_data = pywt.idwt2(fusion_coeffs, 'haar')

# output the result
driver = gdal.GetDriverByName('GTiff')
out_file = 'output.tif'
out_ds = driver.Create(out_file, ds1.RasterXSize, ds1.RasterYSize, 1, band1.DataType)
out_ds.SetProjection(ds1.GetProjection())
out_ds.SetGeoTransform(geotransform)
out_band = out_ds.GetRasterBand(1)
out_band.WriteArray(fusion_data)
out_band.FlushCache()
out_ds = None

# close output file
ds1 = None
ds2 = None
