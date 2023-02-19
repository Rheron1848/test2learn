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
number = 7
guess = 6
print("let us guess!（answer is 7)")
while guess != number:
  guess = int(input("input ur num plz:"))
  if guess == number:
    print("u r right!")
  elif guess < number:
    print("it is smaller")
  elif guess > number:
    print("it is bigger")
#if是条件控制，while是循环控制

print(" ")
n = 100
sum = 0
counter = 1
while counter <= n:
  sum = sum + counter
  counter += 1
print("1 到 %d 之和为 %d"%(n,sum))

print(" ")
#while```else:如果while后面的条件语句为fales，则执行else的语句块。
count = 0
while count < 5:
  print(count,"小于5")
  count = count + 1
else:
  print(count, "大于或等于5")

print(" ")
#while的简单语句组写法：
flag = 0
while(flag):print("hello!")
print("goodbye!")
#如果将flag改为1，实际执行的就是while flag==1：print（），这使得while的条件表达式永远不为false，达到无限循环的效果。

print("")
#for循环可以遍历任何可迭代对象，如一个列表或者一个字符串：常见格式如下：
#for <variable> in <sequence>:
# <statements>
#else:
# <statements>
sites = ["baidu","google","runoob","taobao"]
for site in sites:
  print(site)
