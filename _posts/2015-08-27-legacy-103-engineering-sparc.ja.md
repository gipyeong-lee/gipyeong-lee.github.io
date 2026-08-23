---
layout: post
title: "[SPARC] ビット処理演算"
description: "問題定義 ビット処理演算 0 から 63 までの数を格納する集合に対する演算を実装しようとする。集合は静的領域に set1, set2, set3 という名前で定義する。set1, set2, set3 の各ビットは 63, 62, ... , 2, 1, 0 を表し、該当..."
date: 2015-08-27 01:47:27 +0900
section: blog
category: engineering
lang: ja
ref: 2015-08-27-legacy-103-engineering-sparc
tags:
  - "sparc"
  - "ビット処理"
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
ビット処理演算
</span>
</p>
</div>
</div>
<div class="layoutArea">
<div class="column">
<p>
<span>
0
</span>
<span>
から
</span>
<span>
63
</span>
<span>
までの数を格納する集合に対する演算を実装しようとする。
</span>
<span>
集合は静的領域に
</span>
<span>
set1,
set2, set3
</span>
<span>
という名前で定義する。set1, set2, set3
</span>
<span>
の各ビットは
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
を表し、該当
する数が集合に属していればそのビットが
</span>
<span>
1
</span>
<span>
、そうでなければ
</span>
<span>
0
</span>
<span>
に指定される。
</span>
<span>
初期にはテストしようとする集合を定義すればよい。
</span>
</p>
<ul>
<li>
<p>
<span>

</span>
<span>
member(j, set): j
</span>
<span>
が
</span>
<span>
set
</span>
<span>
の要素であれば
</span>
<span>
1
</span>
<span>
を返す。
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
和集合。set3 = set1 ∪ set2
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
積集合。set3 = set1 ∩ set2
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
差集合。set3 = set1 - set2
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
集合
</span>
<span>
set
</span>
<span>
に要素
</span>
<span>
j
</span>
<span>
を追加する。
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
mapinc(set,d): set
</span>
<span>
の各要素に
</span>
<span>
d
</span>
<span>
を足した集合。
</span>
<span>
例えば
</span>
<span>
set({1, 13, 17}, 1) = {2, 14, 18}
</span>
</p>
<p>
<span>
である。
</span>
</p>
<p>
<span>
提出物
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
上記
</span>
<span>
3
</span>
<span>
つの関数のみが定義されているファイルを提出する。main
</span>
<span>
と集合
</span>
<span>
set1, set2
</span>
<span>
が定義されるファイルは提出しない。
</span>
<span>
各自テストのために別途作成し、リンクして実行するのに使用する。
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
1. 集合は静的領域に set1, set2, set3 という名前で定義。
</span>
</font>
</div>
<div>
<font>
<span>
2. set1, set2, set3 の各ビットは 63, 62, 61...., 2, 1, 0 を表す。
</span>
</font>
</div>
<div>
<font>
<span>
3. 該当する数が集合に属していればそのビットが 1、そうでなければ 0 に指定される。
</span>
</font>
</div>
<div>
<font>
<span>
4. 初期テストしようとする集合を定義。
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
&lt; 取るに足らないソースコード.. &gt;
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
1. member(j,set) 関数 &gt; 結果値 0 or 1
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
*該当のソースコードを動かすには
<span>
<b>
太字のコメント
</b>
<span>
を解除してください。
</span>
.
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
<b>
!
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
.global main
</b>
</p>
<p>
<b>
!main :
</b>
</p>
<p>
<b>
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
</b>
</p>
<p>
<b>
set set1, %l2
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; st %l2,[%sp +
<span>
16
</span>
]
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
set set2, %l3
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; st %l3,[%sp +
<span>
32
</span>
]
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; mov
<span>
16
</span>
,%o0
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; call member
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; mov %l2,%o1
</b>
</p>
<p>
<b>
!test :
</b>
</p>
<p>
<b>
ret
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
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
loop: &nbsp; sll %l0,
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
ld [%o1],%l1&nbsp; &nbsp; ! load [%fp
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
cmp %i0,%l1 &nbsp; &nbsp; ! x== [%fp
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
be isexist&nbsp; &nbsp; &nbsp; ! if equal then goto isexist
</p>
<p>
cmp %l0,N &nbsp; &nbsp; &nbsp; ! %l0 &lt; N
</p>
<p>
bl,a indexup&nbsp; &nbsp; ! if true goto indexup
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
2. add(j,set) 関数 &gt; &nbsp;{ 1,3,4, j }
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
*該当のソースコードを動かすには
<span>
<b>
太字のコメント
</b>
<span>
を解除してください。
</span>
.
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
</b>
</p>
<p>
<b>
.global main
</b>
</p>
<p>
<b>
!main :
</b>
</p>
<p>
<b>
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
</b>
</p>
<p>
<b>
set set1, %l2
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; mov
<span>
44
</span>
,%o1
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; call add
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; mov %l2,%o0
</b>
</p>
<p>
<b>
!test :
</b>
</p>
<p>
<b>
ret
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
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
add :&nbsp; &nbsp; save %sp,
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
addend: &nbsp; &nbsp; ret
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
3. mapinc(set,d) 関数 &gt; &nbsp;{1,3,4} , d= 1 &gt; {2,4,5}
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
*該当のソースコードを動かすには
<span>
<b>
太字のコメント
</b>
<span>
を解除してください。
</span>
.
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
</b>
</p>
<p>
<b>
.global main
</b>
</p>
<p>
<b>
!main :
</b>
</p>
<p>
<b>
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
</b>
</p>
<p>
<b>
set set1, %l2
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; st %l2,[%sp +
<span>
16
</span>
]
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; mov
<span>
1
</span>
,%o1
</b>
</p>
<p>
<b>
!&nbsp; &nbsp; call mapinc
</b>
</p>
<p>
<b>
! &nbsp; mov %l2,%o0
</b>
</p>
<p>
<b>
!test :
</b>
</p>
<p>
<b>
ret
</b>
</p>
<p>
<b>
!
</b>
</p>
<p>
<b>
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
mapinc :&nbsp; &nbsp; save %sp,
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
indexup : &nbsp; inc %l0 ! increase index ++
</p>
<p>
loop: &nbsp; &nbsp; &nbsp; sll %l0,
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
ld [%o1],%l1&nbsp; &nbsp; ! load [%fp
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
add %l1,%i1,%l1 ! add &nbsp; %l1 = %l1 + %i1
</p>
<p>
st %l1,[%o1]&nbsp; &nbsp; ! store %l1 to [%fp
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
cmp %l0,N &nbsp; &nbsp; &nbsp; ! compare %l0 &lt; N
</p>
<p>
bl,a indexup&nbsp; &nbsp; ! if true goto indexup
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
取るに足らないソースコードがすべて終わりました...
</div>
<div>
今回の課題をしながら感じたのは、配列のアドレスにアクセスする際にビット処理を行うと、別途 mul を使用してアドレス計算をしなくてもよいということです。非常に便利です。
</div>
<div>
もちろん、ソースは最適化されていません。私は超初心者ですから..
</div>
<div>
<br>
</div>
<div>
だいたいソースを組むのに6時間の試行錯誤がかかりました。デバッグをしてメモリに何があるのか一つ一つ確認してみました。
</div>
<div>
<br>
</div>
<div>
あ、デバッグ時に使用するコマンドとしては..
</div>
<div>
<br>
</div>
<div>
<b>
- gcc -g main.c -o main &nbsp; &nbsp; :: &nbsp;main.c ファイルを global ラベルを参照可能にコンパイルし、main という名前の実行ファイルを出力する。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- gdb main &nbsp; :: main をデバッグする。
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- p $i0 &nbsp; &nbsp;:: &nbsp;%i0 &nbsp;、 i0 レジスタの値を表示する。
</b>
</div>
<div>
<b>
- p set1 &nbsp; :: &nbsp;静的変数 set1 の n 番目までの値を確認する
</b>
</div>
<div>
<b>
ex) -p set1 &nbsp; &nbsp;&gt;&gt; {1 , 4 , 5 }
</b>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
私が理解した内容が多く間違っている可能性があります。正していただければ修正するようにします。
</div>
<div>
ありがとうございます。
</div>
<div>
<br>
</div>
</div>
</div>
</div>
</div>
</div>