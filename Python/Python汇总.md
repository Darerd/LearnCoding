# Python汇总

1. `Python`使用==缩进==来组织代码块，请务必遵守约定俗成的习惯，坚持使用==4个空格==的缩进。

2. `Python`程序是==大小写==敏感的，如果写错了==大小写==，==程序会报错==。

3. 计算机由于使用==二进制==，所以，有时候用==十六进制==表示整数比较方便，==十六进制==用`0x`前缀和``0-9，a-f``表示，例如：`0xff00`，`0xa5b4c3d2`，等等。

4. 在Python中，有两种除法，一种除法是`/`：

   ```
   >>> 10 / 3
   3.3333333333333335
   ```

   `/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：

   ```
   >>> 9 / 3
   3.0
   ```

   还有一种除法是`//`，称为==地板除==，两个整数的除法仍然是整数：

   ```
   >>> 10 // 3
   3
   ```

   你没有看错，整数的地板除`//`永远是整数，即使除不尽。要做精确的除法，使用`/`就可以。

   因为`//`除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：

   ```
   >>> 10 % 3
   1
   ```

   无论整数做`//`除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。
   
5. 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

   ```
   #!/usr/bin/env python3
   # -*- coding: utf-8 -*-
   ```

   第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

   第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

   申明了UTF-8编码并不意味着你的`.py`文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：

   ![set-encoding-in-notepad++](C:\Users\yuhui\Pictures\Saved Pictures\1008802356788736.png)

   如果`.py`文件本身使用UTF-8编码，并且也申明了`# -*- coding: utf-8 -*-`，打开命令提示符测试就可以正常显示中文：

   ![py-chinese-test-in-cmd](C:\Users\yuhui\Pictures\Saved Pictures\1008802515054144.png)

   6. 格式化

   最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似`'亲爱的xxx你好！你xx月的话费是xx，余额是xx'`之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。

   ![py-str-format](C:\Users\yuhui\Pictures\Saved Pictures\0.png)

   在Python中，采用的格式化方式和C语言是一致的，用`%`实现，举例如下：

   ```
   >>> 'Hello, %s' % 'world'
   'Hello, world'
   >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
   'Hi, Michael, you have $1000000.'
   ```

   你可能猜到了，`%`运算符就是用来格式化字符串的。在字符串内部，`%s`表示用字符串替换，`%d`表示用整数替换，有几个`%?`占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个`%?`，括号可以省略。

   常见的占位符有：

   | 占位符 | 替换内容     |
   | :----- | :----------- |
   | %d     | 整数         |
   | %f     | 浮点数       |
   | %s     | 字符串       |
   | %x     | 十六进制整数 |

如果你不太确定应该用什么，`%s`永远起作用，它会把任何数据类型转换为字符串：

```
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
```

有些时候，字符串里面的`%`是一个普通字符怎么办？这个时候就需要转义，用`%%`来表示一个`%`：

```
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
```

7. ### list

   Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

   比如，列出班里所有同学的名字，就可以用一个list表示：

   ```
   >>> classmates = ['Michael', 'Bob', 'Tracy']
   >>> classmates
   ['Michael', 'Bob', 'Tracy']
   ```

   变量`classmates`就是一个list。用`len()`函数可以获得list元素的个数：

   ```
   >>> len(classmates)
   3
   ```

   用索引来访问list中每一个位置的元素，记得索引是从`0`开始的：

   ```
   >>> classmates[0]
   'Michael'
   >>> classmates[1]
   'Bob'
   >>> classmates[2]
   'Tracy'
   >>> classmates[3]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range
   ```

   当索引超出了范围时，Python会报一个`IndexError`错误，所以，要确保索引不要越界，记得最后一个元素的索引是`len(classmates) - 1`。

   如果要取最后一个元素，除了计算索引位置外，还可以用`-1`做索引，直接获取最后一个元素：

   ```
   >>> classmates[-1]
   'Tracy'
   ```

   以此类推，可以获取倒数第2个、倒数第3个：

   ```
   >>> classmates[-2]
   'Bob'
   >>> classmates[-3]
   'Michael'
   >>> classmates[-4]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range
   ```

   当然，倒数第4个就越界了。

   list是一个可变的有序表，所以，可以往list中追加元素到末尾：

   ```
   >>> classmates.append('Adam')
   >>> classmates
   ['Michael', 'Bob', 'Tracy', 'Adam']
   ```

   也可以把元素插入到指定的位置，比如索引号为`1`的位置：

   ```
   >>> classmates.insert(1, 'Jack')
   >>> classmates
   ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
   ```

   要删除list末尾的元素，用`pop()`方法：

   ```
   >>> classmates.pop()
   'Adam'
   >>> classmates
   ['Michael', 'Jack', 'Bob', 'Tracy']
   ```

   要删除指定位置的元素，用`pop(i)`方法，其中`i`是索引位置：

   ```
   >>> classmates.pop(1)
   'Jack'
   >>> classmates
   ['Michael', 'Bob', 'Tracy']
   ```

   要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

   ```
   >>> classmates[1] = 'Sarah'
   >>> classmates
   ['Michael', 'Sarah', 'Tracy']
   ```

   list里面的元素的数据类型也可以不同，比如：

   ```
   >>> L = ['Apple', 123, True]
   ```

   list元素也可以是另一个list，比如：

   ```
   >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
   >>> len(s)
   4
   ```

   要注意`s`只有4个元素，其中`s[2]`又是一个list，如果拆开写就更容易理解了：

   ```
   >>> p = ['asp', 'php']
   >>> s = ['python', 'java', p, 'scheme']
   ```

   要拿到`'php'`可以写`p[1]`或者`s[2][1]`，因此`s`可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。

   如果一个list中一个元素也没有，就是一个空的list，它的长度为0：

   ```
   >>> L = []
   >>> len(L)
   0
   ```

8. ### dict

   Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

   举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：

   ```
   names = ['Michael', 'Bob', 'Tracy']
   scores = [95, 75, 85]
   ```

   给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

   如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：

   ```
   >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
   >>> d['Michael']
   95
   ```

   为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。

   第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。

   dict就是第二种实现方式，给定一个名字，比如`'Michael'`，dict在内部就可以直接计算出`Michael`对应的存放成绩的“页码”，也就是`95`这个数字存放的内存地址，直接取出来，所以速度非常快。

   你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

   把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

   ```
   >>> d['Adam'] = 67
   >>> d['Adam']
   67
   ```

   由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

   ```
   >>> d['Jack'] = 90
   >>> d['Jack']
   90
   >>> d['Jack'] = 88
   >>> d['Jack']
   88
   ```

   如果key不存在，dict就会报错：

   ```
   >>> d['Thomas']
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   KeyError: 'Thomas'
   ```

   要避免key不存在的错误，有两种办法，一是通过`in`判断key是否存在：

   ```
   >>> 'Thomas' in d
   False
   ```

   二是通过dict提供的`get()`方法，如果key不存在，可以返回`None`，或者自己指定的value：

   ```
   >>> d.get('Thomas')
   >>> d.get('Thomas', -1)
   -1
   ```

   注意：返回`None`的时候Python的交互环境不显示结果。

   要删除一个key，用`pop(key)`方法，对应的value也会从dict中删除：

   ```
   >>> d.pop('Bob')
   75
   >>> d
   {'Michael': 95, 'Tracy': 85}
   ```

   请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

   和list比较，dict有以下几个特点：

   1. 查找和插入的速度极快，不会随着key的增加而变慢；
   2. 需要占用大量的内存，内存浪费多。

   而list相反：

   1. 查找和插入的时间随着元素的增加而增加；
   2. 占用空间小，浪费内存很少。

   所以，dict是用空间来换取时间的一种方法。

   dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是**不可变对象**。

   这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

   要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

   ```
   >>> key = [1, 2, 3]
   >>> d[key] = 'a list'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: unhashable type: 'list'
   ```

   ### set

   set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

   要创建一个set，需要提供一个list作为输入集合：

   ```
   >>> s = set([1, 2, 3])
   >>> s
   {1, 2, 3}
   ```

   注意，传入的参数`[1, 2, 3]`是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

   重复元素在set中自动被过滤：

   ```
   >>> s = set([1, 1, 2, 2, 3, 3])
   >>> s
   {1, 2, 3}
   ```

   通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果：

   ```
   >>> s.add(4)
   >>> s
   {1, 2, 3, 4}
   >>> s.add(4)
   >>> s
   {1, 2, 3, 4}
   ```

   通过`remove(key)`方法可以删除元素：

   ```
   >>> s.remove(4)
   >>> s
   {1, 2, 3}
   ```

   set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

   ```
   >>> s1 = set([1, 2, 3])
   >>> s2 = set([2, 3, 4])
   >>> s1 & s2
   {2, 3}
   >>> s1 | s2
   {1, 2, 3, 4}
   ```

   set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

   ### 再议不可变对象

   上面我们讲了，str是不变对象，而list是可变对象。

   对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：

   ```
   >>> a = ['c', 'b', 'a']
   >>> a.sort()
   >>> a
   ['a', 'b', 'c']
   ```

   而对于不可变对象，比如str，对str进行操作呢：

   ```
   >>> a = 'abc'
   >>> a.replace('a', 'A')
   'Abc'
   >>> a
   'abc'
   ```

   虽然字符串有个`replace()`方法，也确实变出了`'Abc'`，但变量`a`最后仍是`'abc'`，应该怎么理解呢？

   我们先把代码改成下面这样：

   ```
   >>> a = 'abc'
   >>> b = a.replace('a', 'A')
   >>> b
   'Abc'
   >>> a
   'abc'
   ```

   要始终牢记的是，`a`是变量，而`'abc'`才是字符串对象！有些时候，我们经常说，对象`a`的内容是`'abc'`，但其实是指，`a`本身是一个变量，它指向的对象的内容才是`'abc'`：

   ```ascii
   ┌───┐                  ┌───────┐
   │ a │─────────────────>│ 'abc' │
   └───┘                  └───────┘
   ```

   当我们调用`a.replace('a', 'A')`时，实际上调用方法`replace`是作用在字符串对象`'abc'`上的，而这个方法虽然名字叫`replace`，但却没有改变字符串`'abc'`的内容。相反，`replace`方法创建了一个新字符串`'Abc'`并返回，如果我们用变量`b`指向该新字符串，就容易理解了，变量`a`仍指向原有的字符串`'abc'`，但变量`b`却指向新字符串`'Abc'`了：

   ```ascii
   ┌───┐                  ┌───────┐
   │ a │─────────────────>│ 'abc' │
   └───┘                  └───────┘
   ┌───┐                  ┌───────┐
   │ b │─────────────────>│ 'Abc' │
   └───┘                  └───────┘
   ```

   所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。