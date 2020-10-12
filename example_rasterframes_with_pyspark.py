import pyrasterframes
spark = spark.withRasterFrames()
from pyspark.sql import SQLContext
sqlc = SQLContext(spark)

l8 = spark.read.format('aws-pds-l8-catalog').load()

sqlc.registerDataFrameAsTable(l8, "landsat_catalog")
df2 = sqlc.sql("""SELECT product_id, entity_id, acquisition_date, B4, B5, st_geometry(bounds_wgs84) as geom, bounds_wgs84
                FROM landsat_catalog
                WHERE acquisition_date > to_date('2020-08-01') AND acquisition_date < to_date('2020-08-31')
""")
df2.show()


df_field = spark.read.geojson('hdfs://master:9000/geo/input.json')
sqlc.registerDataFrameAsTable(df_field, "field")
field_imagery = sqlc.sql("""SELECT product_id, entity_id, acquisition_date, B4, B5, st_geometry(bounds_wgs84) as geom, (SELECT geometry FROM field) as field_geom
                            FROM landsat_catalog
                            WHERE acquisition_date > to_date('2020-08-01') AND acquisition_date < to_date('2020-08-31')
                            AND st_intersects(st_geometry(bounds_wgs84), (SELECT geometry FROM field))
                            ORDER BY acquisition_date ASC
                          """)
field_imagery.show()
