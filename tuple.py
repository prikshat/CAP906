def cmp(a,b):
  return (a>b)-(a<b)

tuple1, tuple2 = (1003, 'xyz'), (556, 'abc')
print cmp(tuple1, tuple2)   
print cmp(tuple2, tuple1)  

