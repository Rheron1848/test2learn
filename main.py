print("hello, world!")
print(" ")

i = 0
while i <= 10:
  print("I am ", i)
  i += 1
print("end, bye！")
#end

print(" ")
a, b = 0, 1
while b < 10:
  print(b)
  a, b = b, a + b
#复合赋值 右边的表达式会在赋值变动之前计算完。右边表达式的顺序是从左往右的。也就是说，先计算，再复制。

print(" ")
a, b = 0, 1
while b < 1000:
  print(b, end=",")
  a, b = b, a + b

print(" ")
a, b = 0, 1
while b < 1000:
  print(b, end="")
  a, b = b, a + b

#end可以用于将输出的结果输出到同一行，或在输出的末尾添加不同的字符。

print(" ")
var1 = 100
if var1:
  print("1 - if 表达式为true")
  print(var1)

var2 = 0
if var2:
  print("2 - if表达式条件为true")
  print(var2)

var3 = 0
if var1:
  print("2 - if表达式条件为true")
  print(var3)
#if条件不满足时，又没有else和ifel约束，就会不执行。
print("goodbye!")

print(" ")
print("hello!hello! i m python!")