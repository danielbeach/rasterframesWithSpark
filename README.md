# rasterframesWithSpark
Installing and running rasterframes on Spark for geospatial processing.


Full blog instructions https://www.confessionsofadataguy.com/geospatial-with-apache-spark-intro-to-rasterframes/


1. You need a Spark Cluster... if you don't have one read this...https://www.confessionsofadataguy.com/create-your-very-own-apache-spark-hadoop-cluster-then-do-something-with-it/

2. Install GDAL
- sudo apt-get install python3.6-dev
- sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
- sudo apt-get update
- sudo apt-get install gdal-bin
- sudo apt-get install libgdal-dev
- export CPLUS_INCLUDE_PATH=/usr/include/gdal
- export C_INCLUDE_PATH=/usr/include/gdal
- pip3 install GDAL==2.4.2

3. Install rasterframes
- python3 -m pip install pyrasterframes

4. cd /usr/local/spark/bin/

5. pyspark --master local[*] --py-files pyrasterframes_2.11-0.9.0-python.zip --packages org.locationtech.rasterframes:rasterframes_2.11:0.9.0,org.locationtech.rasterframes:pyrasterframes_2.11:0.9.0,org.locationtech.rasterframes:rasterframes-datasource_2.11:0.9.0 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.kryo.registrator=org.locationtech.rasterframes.util.RFKryoRegistrator --conf spark.kryoserializer.buffer.max=500m

6. import pyrasterframes
spark = spark.withRasterFrames()
df = spark.read.raster('https://landsat-pds.s3.amazonaws.com/c1/L8/158/072/LC08_L1TP_158072_20180515_20180604_01_T1/LC08_L1TP_158072_20180515_20180604_01_T1_B5.TIF')
print(df.head())
