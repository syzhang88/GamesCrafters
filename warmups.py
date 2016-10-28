from pyspark import SparkContext
from random  import uniform

conf = SparkConf().setAppName("warmups").setMaster("local")
sc = SparkContext(conf=conf)

euler1 =  sc.parallelize(range(1,1000)). \
            filter(lambda x: (x % 5 == 0) or (x % 3 == 0)). \
            reduce(lambda a, b: a + b)

print(euler1)

ratioPi =  sc.parallelize([[random.uniform(-1,1), random.uniform(-1,1)] for x in range(1,10000)]). \
            filter(lambda tuple: ((tuple[0] ** 2) + (tuple [1] ** 2)) ** 0.5 <= 1). \
            count()
approxPi = 4 * ratioPi

print(approxPi)
