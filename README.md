# Wavelet-transform-fusion-for-spatial-data

The source code of Wavelet transform fusion method in the paper "Introducing big data to measure the spatial heterogeneity of human activities for optimizing the ecological security pattern: A case study from Guangzhou City, China.". DOI: 10.1016/j.ecolind.2023.110203  Authors: Zhenzhi Jiao, Zhuo Wu, Baojing Wei, Yifan Luo, Yongquan Lin, Yongtai Xue, Shaoying Li, Feng Gao. Journal: Ecological Indicators. Year: 2023.

If you use this code for your research, please cite this paper.

This is the code for wavelet transform fusion. 

Python==3.9, gdal==3.3.2, pywt==1.4.1.

Please check that the file has the same number of rows and columns using the resampling method before fusing.

The method consists of the following steps:

1.Read the input raster files and get the geographic coordinate information.

2.Read raster datasets and preprocess the data by replacing any NoData values with zero.

3.Perform wavelet decomposition on the preprocessed data using the Haar wavelet transform.

4.Fuse the approximation and detail coefficients obtained from the wavelet decomposition by computing theweighted average of the corresponding coefficients.

5.Perform wavelet reconstruction using the fused coefficients to obtain the final fused image.Write the output image to a GeoTIFF file.

For Chinese readers, you can see the introduction at WeChat, https://mp.weixin.qq.com/s?__biz=MzIzMjU3MjYyNQ==&mid=2247500268&idx=1&sn=789ad17dcf2ce099825676b85509069d&chksm=e8905252dfe7db44fec08790bd817188d2451a6fba4b1286952255ee9986fc3cbe4ece0552f2&scene=126&sessionid=1699722609#rd
