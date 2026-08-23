---
layout: post
title: "[SPARC] 位元處理運算"
description: "問題定義 位元處理運算 嘗試實作對儲存 0 到 63 之間數值的集合進行運算。集合在靜態區定義為 set1、set2、set3。set1、set2、set3 的每個位元分別代表 63、62、...、2、1、0，若對應數值屬於該集合，則位元設為 1，否則為 0。初期只需定義要測試的集合。"
date: 2015-08-27 01:47:27 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-08-27-legacy-103-engineering-sparc
tags:
  - "sparc"
  - "位元處理"
  - "mapinc"
  - "SPARC"
  - "engineering"
translation_source_hash: d3447d251f648c7d2141af13fb3bc9630ff3ea46abb1460309d0341414a93e6f
---

<p>
<b>
<span>
問題定義
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
位元處理運算
</span>
</p>
</div>
</div>
<div class="layoutArea">
<div class="column">
<p>
<span>
嘗試實作對儲存 0 到 63 之間數值的集合進行運算。
</span>
<span>
集合在靜態區定義為
</span>
<span>
set1,
set2, set3
</span>
<span>
。
</span>
<span>
set1, set2, set3
</span>
<span>
的每個位元分別代表
</span>
<span>
63, 62,
</span>
<span>
...
</span>
<span>
,2, 1, 0
</span>
<span>
，
</span>
<span>
若對應數值屬於該集合，則位元設為
</span>
<span>
1
</span>
<span>
，否則為
</span>
<span>
0
</span>
<span>
。
</span>
<span>
初期只需定義要測試的集合。
</span>
</p>
<ul>
<li>
<p>
<span>

</span>
<span>
member(j, set): 若 j 為 set 的元素，回傳 1
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
聯集
</span>
<span>
。 set3 = set1
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
交集
</span>
<span>
。 set3 = set1
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
差集
</span>
<span>
。 set3 = set1 - set2
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
在集合 set 中加入元素 j
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
集合中每個元素加上 d。
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
提交僅定義上述 3 個函式的檔案。
</span>
<span>
不提交定義 main 與集合 set1、set2 的檔案。
</span>
<span>
自行製作並連結以進行各別測試。
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
設計
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
1. 集合在靜態區定義為 set1, set2, set3。
</span>
</font>
</div>
<div>
<font>
<span>
2. set1, set2, set3 的每個位元代表 63, 62, 61...., 2, 1, 0。
</span>
</font>
</div>
<div>
<font>
<span>
3. 若對應數值屬於集合，則位元設為 1，否則設為 0。
</span>
</font>
</div>
<div>
<font>
<span>
4. 定義要測試的初始集合。
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
&lt; 沒什麼特別的原始碼.. &gt;
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
1. member(j,set) 函式 &gt; 結果為 0 或 1
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
*若要執行此原始碼，請解除
<span>
<b>
粗體註解
</b>
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
2. add(j,set) 函式 &gt;  { 1,3,4, j }
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
*若要執行此原始碼，請解除
<span>
<b>
粗體註解
</b>
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
3. mapinc(set,d) 函式 &gt;  {1,3,4} , d= 1 &gt; {2,4,5}
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
*若要執行此原始碼，請解除
<span>
<b>
粗體註解
</b>
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
沒什麼特別的原始碼都結束了...
</div>
<div>
這次做作業時感覺到，存取陣列位址時若使用位元處理，就不需要另外使用 mul 來進行位址計算。非常方便。
</div>
<div>
當然，原始碼並沒有最佳化。因為我還是超級新手..
</div>
<div>
<br>
</div>
<div>
大概花了 6 小時在搞這些原始碼。我進行了除錯並逐一確認記憶體中的內容。
</div>
<div>
<br>
</div>
<div>
啊，除錯時使用的指令有..
</div>
<div>
<br>
</div>
<div>
<b>
- gcc -g main.c -o main     ::  將 main.c 編譯並使 global 標籤可被參考，並輸出名為 main 的執行檔。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- gdb main   :: 對 main 進行除錯。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- p $i0    ::  輸出 %i0 暫存器的值。
</b>
</div>
<div>
<b>
- p set1   ::  確認靜態變數 set1 到第 n 個的值。
</b>
</div>
<div>
<b>
ex) -p set1    >> {1 , 4 , 5 }
</b>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
我所理解的內容可能有許多錯誤。若能協助指正，我會進行修正。
</div>
<div>
謝謝。
</div>
<div>
<br>
</div>
</div>
</div>
</div>
</div>
</div>