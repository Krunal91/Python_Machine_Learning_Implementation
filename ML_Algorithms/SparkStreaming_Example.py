from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(master='local[2]', appName='Krunal Test')

ssc = StreamingContext(sc, batchDuration=1)

wordstream = ssc.socketTextStream('localhost', port=99)

words = wordstream.flatMap(lambda line: line.split(" "))
wordcount = words.map(lambda word: (word, 1))
reduce = wordcount.reduceByKey(lambda x, y: x + y)
reduce.pprint()

ssc.start()
ssc.awaitTermination()
