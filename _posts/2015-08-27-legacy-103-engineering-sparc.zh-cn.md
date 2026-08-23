---
layout: post
title: "[SPARC] 位处理运算"
description: "问题定义 位处理运算 想要实现对存储 0 到 63 的数字集合的运算。集合在静态区域中以 set1、set2、set3 的名称定义。set1、set2、set3 的每一位代表 63、62、...、2、1、0，如果对应的数字属于该集合，则该位指定为 1，否则为 0。起初只需定义用于测试的集合。"
date: 2015-08-27 01:47:27 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-08-27-legacy-103-engineering-sparc
tags:
  - "sparc"
  - "位处理"
  - "mapinc"
  - "SPARC"
  - "engineering"
translation_source_hash: d3447d251f648c7d2141af13fb3bc9630ff3ea46abb1460309d0341414a93e6f
---

<p>
<b>
<span>
问题定义
</span>
</b>
</p>
<p>
<b>
<br>
</b>
</p>

<div class="page" title="Page 1">


<div class="layoutArea">
<div class="column">
<p>
<span>
位处理运算
</span>
</p>
</div>
</div>
<div class="layoutArea">
<div class="column">
<p>
<span>
想要实现对存储
</span>
<span>
0
</span>
<span>
到
</span>
<span>
63
</span>
<span>
的数字集合的运算。集合在静态区域中以
</span>
<span>
set1、
</span>
<span>
set2、set3
</span>
<span>
的名称定义。
</span>
<span>
set1、set2、set3
</span>
<span>
的每一位代表
</span>
<span>
63、62、
</span>
<span>
...
</span>
<span>
、2、1、0，如果对应
</span>
<span>
的数字属于该集合，则该位指定为
</span>
<span>
1
</span>
<span>
，否则为
</span>
<span>
0
</span>
<span>
。
</span>
<span>
起初只需定义用于测试的集合。
</span>
</p>
<ul>
<li>
<p>
<span>

</span>
<span>
member(j, set): 
</span>
<span>
如果
</span>
<span>
j
</span>
<span>
是
</span>
<span>
set
</span>
<span>
的元素，则返回
</span>
<span>
1
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
union: 
</span>
<span>
并集。
</span>
<span>
set3 = set1
</span>
<span>
∪
</span>
<span>
set2
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
intersection: 
</span>
<span>
交集。
</span>
<span>
set3 = set1
</span>
<span>
∩
</span>
<span>
set2
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
subtract: 
</span>
<span>
差集。
</span>
<span>
set3 = set1 - set2
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
add(j, set): 
</span>
<span>
在集合
</span>
<span>
set
</span>
<span>
中添加元素
</span>
<span>
j
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
mapinc(set,d): 
</span>
<span>
集合
</span>
<span>
set
</span>
<span>
中每个元素加上
</span>
<span>
d
</span>
<span>
后的集合。
</span>
<span>
例如
</span>
<span>
set({1, 13, 17}, 1) = {2, 14, 18}
</span>
</p>
<p>
<span>
。
</span>
</p>
<p>
<span>
提交物
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
提交仅定义了上述
</span>
<span>
3
</span>
<span>
个函数的文件。
</span>
<span>
不提交定义了
</span>
<span>
main
</span>
<span>
和集合
</span>
<span>
set1、set2
</span>
<span>
的文件。
</span>
<span>
各自用于测试时，需单独创建并链接使用。
</span>
</p>
</li>
</ul>
<div>
<br>
</div>
<div>
<b>
<span>
设计
</span>
</b>
</div>
<div>
<b>
<span>
<br>
</span>
</b>
</div>
<div>
<font>
<span>
1. 集合在静态区域中以 set1、set2、set3 的名称定义。
</span>
</font>
</div>
<div>
<font>
<span>
2. set1、set2、set3 的每一位代表 63、62、61....、2、1、0。
</span>
</font>
</div>
<div>
<font>
<span>
3. 如果对应的数字属于该集合，则该位指定为 1，否则为 0。
</span>
</font>
</div>
<div>
<font>
<span>
4. 定义初始测试集合。
</span>
</font>
</div>
<div>
<font>
<span>
<br>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
&lt; 不起眼的源代码.. &gt;
</b>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
<span>
1. member(j,set) 函数 &gt; 结果 0 或 1
</span>
</b>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</font>
</div>
<div>
<span>
*如需运行相应源代码，请取消
<span>
<b>
粗体注释
</span>
<span>
。
</span>
</span>
</span>
</div>
<div>
<span>
<br>
</span>
</div>
<div>
<p>
<b>
!.section
<span>
".data"
</span>
</b>
</p>
<p>
<b>
!set1:.word
<span>
1
</span>
,
<span>
4
</span>
,
<span>
5
</span>
,
<span>
16
</span>
</b>
</p>
<p>
<b>
!set2:.word
<span>
1
</span>
,
<span>
4
</span>
,
<span>
7
</span>
,
<span>
23
</span>
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
!.section
<span>
".text"
</span>
</b>
</p>
<p>
<b>
!!local variables
</b>
</p>
<p>
<b>
!n =
<span>
-4
</span>
</b>
</p>
<p>
<b>
<br>
</b>
</p>
<p>
<b>
! index i in $l0
</b>
</p>
<p>
<b>
! max in $l1
</b>
</p>
<p>
<span class="Apple-tab-span">
<b>
</b>
</span>
</p>
<p>
<b>
!

.global main
</b>
</p>
<p>
<b>
!main :

save %sp,
<span>
-96
</span>
,%sp
</b>
</p>
<p>
<b>
!

set set1, %l2
</b>
</p>
<p>
<b>
!    st %l2,[%sp +
<span>
16
</span>
]
</b>
</p>
<p>
<b>
!

set set2, %l3
</b>
</p>
<p>
<b>
!    st %l3,[%sp +
<span>
32
</span>
]
</b>
</p>
<p>
<b>
!    mov
<span>
16
</span>
,%o0
</b>
</p>
<p>
<b>
!    call member
</b>
</p>
<p>
<b>
!    mov %l2,%o1
</b>
</p>
<p>
<b>
!test :

ret
</b>
</p>
<p>
<b>
!

restore
</b>
</p>
<p>
<b>
<br>
</b>
</p>
<p>
<b>
<span>
!N=
</span>
4
<span>
! ( if N =
</span>
4
<span>
, it
</span>
's only works in {a,b,c,d} just 4 objects)
</b>
</p>


<p>
<span>
.global
</span>
member
</p>
<p>
member : save %sp,
<span>
-96
</span>
,%sp
</p>
<p>
mov
<span>
1
</span>
,%l0 ! move
<span>
1
</span>
to l0
</p>
<p>
sll %l0,N,%l5 !
<span>
2
</span>
^N to l5 (this time
<span>
2
</span>
^
<span>
4
</span>
=
<span>
16
</span>
)
</p>
<p>
add %fp,%l5,%o3 ! address %fp
<span>
+16
</span>
</p>
<p>
ld [%o3],%o0 ! right value of [%fp
<span>
+16
</span>
]
</p>
<p>
cmp %i0,%o0 ! x == [%fp
<span>
+16
</span>
] ?
</p>
<p>
be,a isexist ! if yes goto isexist return
</p>
<p>
ba loop ! or not goto loop
</p>
<p>
indexup : inc %l0 ! increase index ++
</p>
<p>
loop:   sll %l0,
<span>
2
</span>
,%l2 ! address l2 = i*
<span>
4
</span>
</p>
<p>
add %o0,%l2,%o1 ! [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
ld [%o1],%l1    ! load [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
cmp %i0,%l1     ! x== [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
be isexist      ! if equal then goto isexist
</p>
<p>
cmp %l0,N       ! %l0 &lt; N
</p>
<p>
bl,a indexup    ! if true goto indexup
</p>
<p>
nop
</p>
<p>
nonexist: mov
<span>
0
</span>
,%i0 ! return value
<span>
0
</span>
- not exist
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
isexist: mov
<span>
1
</span>
,%i0 ! return value
<span>
1
</span>
- it
<span>
's exist
</span>
</p>
<p>
ret
</p>
<p>
restore
</p>
<div>
<br>
</div>
</div>
<div>
<font>
<span>
<br>
</span>
</font>
</div>
<div>
<div>
<font>
<span>
<b>
<span>
2. add(j,set) 函数 &gt;  { 1,3,4, j }
</span>
</b>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</font>
</div>
<div>
<span>
*如需运行相应源代码，请取消
<span>
<b>
粗体注释
</span>
<span>
。
</span>
</span>
</span>
</div>
<div>
<span>
<span>
<br>
</span>
</span>
</div>
<div>
<p>
<b>
!.section
<span>
".data"
</span>
</b>
</p>
<p>
<b>
!set1:.word
<span>
1
</span>
,
<span>
4
</span>
,
<span>
5
</span>
,
<span>
16
</span>
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
!.section
<span>
".text"
</span>
</b>
</p>
<p>
<b>
!local variables
</b>
</p>
<p>
<b>
!n =
<span>
-4
</span>
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
! index i in $l0
</b>
</p>
<p>
<b>
! max in $l1
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
!

.global main
</b>
</p>
<p>
<b>
!main :

save %sp,
<span>
-96
</span>
,%sp
</b>
</p>
<p>
<b>
!

set set1, %l2
</b>
</p>
<p>
<b>
!    mov
<span>
44
</span>
,%o1
</b>
</p>
<p>
<b>
!    call add
</b>
</p>
<p>
<b>
!    mov %l2,%o0
</b>
</p>
<p>
<b>
!test :

ret
</b>
</p>
<p>
<b>
!

restore
</b>
</p>

<p>
<span>
!N=
</span>
4
<span>
! ( if N =
</span>
4
<span>
, it
</span>
's only works in {a,b,c,d} just 4 objects)
</p>
<p>
<span>
.global
</span>
add
</p>
<p>
add :    save %sp,
<span>
-96
</span>
,%sp
</p>
<p>
mov
<span>
1
</span>
,%l0
</p>
<p>
mov %i0,%o0
<span>
;
</span>
</p>
<p>
sll %l0,N,%l5 !
<span>
2
</span>
^N to l5 (this time
<span>
2
</span>
^
<span>
4
</span>
=
<span>
16
</span>
)
</p>
<p>
add %i0,%l5,%i0
</p>
<p>
st %i1,[%i0]
</p>

<p>
addend:     ret
</p>
<p>
restore
</p>
</div>
</div>
<div>
<b>
<span>
<br>
</span>
</b>
</div>
<div>
<div>
<font>
<span>
<b>
<span>
3. mapinc(set,d) 函数 &gt;  {1,3,4} , d= 1 &gt; {2,4,5}
</span>
</b>
</span>
</font>
</div>
<div>
<font>
<span>
<b>
<span>
<br>
</span>
</b>
</span>
</font>
</div>
<div>
<span>
*如需运行相应源代码，请取消
<span>
<b>
粗体注释
</span>
<span>
。
</span>
</span>
</span>
</div>
<div>
<span>
<span>
<br>
</span>
</span>
</div>
<div>
<p>
<b>
!.section
<span>
".data"
</span>
</b>
</p>
<p>
<b>
!set1:.word
<span>
1
</span>
,
<span>
4
</span>
,
<span>
5
</span>
,
<span>
16
</span>
</b>
</p>
<p>
<b>
!set2:.word
<span>
1
</span>
,
<span>
4
</span>
,
<span>
7
</span>
,
<span>
23
</span>
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
!.section
<span>
".text"
</span>
</b>
</p>
<p>
<b>
!local variables
</b>
</p>
<p>
<b>
!n =
<span>
-4
</span>
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
! index i in $l0
</b>
</p>
<p>
<b>
! max in $l1
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
!

.global main
</b>
</p>
<p>
<b>
!main :

save %sp,
<span>
-96
</span>
,%sp
</b>
</p>
<p>
<b>
!

set set1, %l2
</b>
</p>
<p>
<b>
!    st %l2,[%sp +
<span>
16
</span>
]
</b>
</p>
<p>
<b>
!    mov
<span>
1
</span>
,%o1
</b>
</p>
<p>
<b>
!    call mapinc
</b>
</p>
<p>
<b>
!   mov %l2,%o0
</b>
</p>
<p>
<b>
!test :

ret
</b>
</p>
<p>
<b>
!

restore
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
<span>
!N=
</span>
4
<span>
! ( if N =
</span>
4
<span>
, it
</span>
's only works in {a,b,c,d} just 4 objects)
</b>
</p>

<p>
<span>
.global
</span>
mapinc
</p>
<p>
mapinc :    save %sp,
<span>
-96
</span>
,%sp
</p>
<p>
mov
<span>
1
</span>
,%l0
</p>
<p>
sll %l0,N,%l5 !
<span>
2
</span>
^N to l5 (this time
<span>
2
</span>
^
<span>
4
</span>
=
<span>
16
</span>
)
</p>
<p>
add %fp,%l5,%o3 ! address %fp
<span>
+16
</span>
</p>
<p>
ld [%o3],%o0 ! right value of [%fp
<span>
+16
</span>
]
</p>
<p>
ba loop ! or not goto loop
</p>
<p>
clr %l0
</p>
<p>
indexup :   inc %l0 ! increase index ++
</p>
<p>
loop:       sll %l0,
<span>
2
</span>
,%l2 ! address l2 = i*
<span>
4
</span>
</p>
<p>
add %o0,%l2,%o1 ! [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
ld [%o1],%l1    ! load [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
add %l1,%i1,%l1 ! add  %l1 = %l1 + %i1
</p>
<p>
st %l1,[%o1]    ! store %l1 to [%fp
<span>
+16
</span>
+i*
<span>
4
</span>
]
</p>
<p>
cmp %l0,N       ! compare %l0 &lt; N
</p>
<p>
bl,a indexup    ! if true goto indexup
</p>
<p>
nop
</p>
<p>
ret
</p>
<p>
restore
</p>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
不起眼的源代码已经全部结束了...
</div>
<div>
在做这次作业的过程中，我感觉到访问数组地址时如果使用位处理，就不需要另外使用 mul 来计算地址了。非常方便。
</div>
<div>
当然，代码并没有经过优化。因为我还是个超级菜鸟..
</div>
<div>
<br>
</div>
<div>
大概花了 6 个小时在捣鼓这些代码上。通过调试逐一确认了内存中存储的内容。
</div>
<div>
<br>
</div>
<div>
啊，调试时使用的命令是..
</div>
<div>
<br>
</div>
<div>
<b>
- gcc -g main.c -o main     ::  将 main.c 文件编译为 global 标签可引用的文件，并生成名为 main 的可执行文件。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- gdb main   :: 调试 main。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- p $i0    ::  输出 %i0，即 i0 寄存器的值。
</b>
</div>
<div>
<b>
- p set1   ::  查看静态变量 set1 到第 n 个值。
</b>
</div>
<div>
<b>
ex) -p set1    &gt;&gt; {1 , 4 , 5 }
</b>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
我对内容的理解可能有很多错误之处。如果能指正，我会进行修正。
</div>
<div>
谢谢。
</div>
<div>
<br>
</div>
</div>
</div>
</div>
</div>
</div>