---
layout: post
title: "[SPARC] Floating Point Parameter Passing"
description: "Attached is my result based on the file... I'm just submitting it as is due to time constraints. Haven't optimized it yet. A parade of nops and repeated labels..."
date: 2015-08-27 01:46:14 +0900
section: blog
category: engineering
lang: en
ref: 2015-08-27-legacy-102-engineering-sparc
tags:
  - "parameter"
  - "floating point"
  - "sparc"
  - "SPARC"
  - "engineering"
translation_source_hash: 5debb101be0a34ac873da0cd935c7ab19ea46677050cae358920850feeb21e48
---

<div class="page" title="Page 1">
<div class="layoutArea">
<div class="column">

<div class="page" title="Page 1">
<div class="layoutArea">
<div class="column">
<p>
Here is my result based on the attachment.
</p>
<p>
I'm just submitting it as is due to time constraints. I haven't optimized it yet. A parade of nops and repeated labels.
</p>


<div>
<hr>
</div>


<p>

.section

<span>
".data"
</span>
</p>
<p>
N:.word
<span>
0
</span>
</p>
<p>
x1:.single
<span>
0
</span>
</p>
<p>
x2:.single
<span>
0
</span>
</p>
<p>
x3:.single
<span>
0
</span>
</p>
<p>
x4:.single
<span>
0
</span>
</p>
<p>
s:.single
<span>
0
</span>
</p>

<p>

.section

<span>
".text"
</span>
</p>
<p>
fmt0: .asciz
<span>
"input N = "
</span>
</p>
<p>
<span>
fmt1: .asciz
</span>
"input double Value x%d = "
</p>
<p>
fmt2: .asciz
<span>
"%d"
</span>
</p>
<p>
fmt3: .asciz
<span>
"%f"
</span>
</p>
<p>
<span>
fmt4: .asciz
</span>
"fsumdiff == output : %.1f == \n"
</p>
<p>
<span>
fmt5: .asciz
</span>
"fsumdiffpt == output : %.1f == \n"
</p>
<p>

.align

<span>
4
</span>
</p>
<p>
<span>
.global
</span>
main,scanf,printf
</p>
<p>
main: save %sp,
<span>
-192
</span>
,%sp !i, o , l register size
</p>
<p>
set fmt0,%o0
</p>
<p>
call printf ! printf(
<span>
"input N="
</span>
)
</p>
<p>
nop
</p>
<p>
set fmt2,%o0 ! scanf(
<span>
"%d"
</span>
,&amp;n)
</p>
<p>
set N,%o1
</p>
<p>
call scanf
</p>
<p>
nop
</p>
<p>
set fmt1,%o0
</p>
<p>
mov
<span>
1
</span>
,%o1
</p>
<p>
call printf !printf (
<span>
" input double Value x1 ="
</span>
)
</p>
<p>
nop
</p>
<p>
set fmt3,%o0 ! scanf (
<span>
"%f"
</span>
,&amp;x)
</p>
<p>
set x1,%o1
</p>
<p>
call scanf
</p>
<p>
nop
</p>
<p>
set fmt1,%o0
</p>
<p>
mov
<span>
2
</span>
,%o1
</p>
<p>
call printf !printf (
<span>
" input double Value x2 ="
</span>
)
</p>
<p>
nop
</p>
<p>
set fmt3,%o0 ! scanf (
<span>
"%f"
</span>
,&amp;x)
</p>
<p>
set x2,%o1
</p>
<p>
call scanf
</p>
<p>
nop
</p>
<p>
set fmt1,%o0
</p>
<p>
mov
<span>
3
</span>
,%o1
</p>
<p>
call printf !printf (
<span>
" input double Value x3 ="
</span>
)
</p>
<p>
nop
</p>
<p>
set fmt3,%o0 ! scanf (
<span>
"%f"
</span>
,&amp;x)
</p>
<p>
set x3,%o1
</p>
<p>
call scanf
</p>
<p>
nop
</p>
<p>
set fmt1,%o0
</p>
<p>
mov
<span>
4
</span>
,%o1
</p>
<p>
call printf !printf (
<span>
" input double Value x4 ="
</span>
)
</p>
<p>
nop
</p>
<p>
set fmt3,%o0 ! scanf (
<span>
"%f"
</span>
,&amp;x)
</p>
<p>
set x4,%o1
</p>
<p>
call scanf
</p>
<p>
nop
</p>
<p>
set N,%l0
</p>
<p>
set x1,%l1
</p>
<p>
set x2,%l2
</p>
<p>
set x3,%l3
</p>
<p>
set x4,%l4
</p>
<p>
set s,%l5
</p>
<p>
ld [%l0],%o0
</p>
<p>
ld [%l1],%o1
</p>
<p>
ld [%l2],%o2
</p>
<p>
ld [%l3],%o3
</p>
<p>
ld [%l4],%o4
</p>
<p>
ld [%l5],%o5
</p>
<p>
call fsumdiff
</p>
<p>
nop
</p>
<p>
st %o0,[%fp
<span>
-20
</span>
]
</p>
<p>
ld [%fp
<span>
-20
</span>
],%f0
</p>
<p>
fstod %f0,%f0
</p>
<p>
std %f0,[%fp
<span>
-16
</span>
]
</p>
<p>
ldd [%fp -
<span>
16
</span>
],%o4
</p>
<p>
mov %o4,%o1
</p>
<p>
set fmt4,%o0
</p>
<p>
call printf
</p>
<p>
nop
</p>
<p>
set N,%l0
</p>
<p>
ld [%l0],%o0
</p>
<p>
set x1,%o1
</p>
<p>
set x2,%o2
</p>
<p>
set x3,%o3
</p>
<p>
set x4,%o4
</p>
<p>
set s,%o5
</p>
<p>
call fsumdiffpt
</p>
<p>
nop
</p>
<p>
st %o0,[%fp
<span>
-20
</span>
]
</p>
<p>
ld [%fp
<span>
-20
</span>
],%f0
</p>
<p>
fstod %f0,%f0
</p>
<p>
std %f0,[%fp
<span>
-16
</span>
]
</p>
<p>
ldd [%fp -
<span>
16
</span>
],%o4
</p>
<p>
mov %o4,%o1
</p>
<p>
set fmt5,%o0
</p>
<p>
call printf
</p>
<p>
nop
</p>

<p>
test: ret
</p>
<p>
restore
</p>
<p>
fsumdiff: save %sp,
<span>
-128
</span>
,%sp
</p>
<p>
st %i0, [%fp
<span>
-4
</span>
] ! N
</p>
<p>
ld [%fp
<span>
-4
</span>
],%l0
</p>
<p>
st %i1, [%fp
<span>
-4
</span>
] ! x1
</p>
<p>
ld [%fp
<span>
-4
</span>
],%f0
</p>
<p>
st %i2, [%fp
<span>
-4
</span>
] ! x2
</p>
<p>
ld [%fp
<span>
-4
</span>
],%f1
</p>
<p>
st %i3, [%fp
<span>
-4
</span>
] ! x3
</p>
<p>
ld [%fp
<span>
-4
</span>
],%f2
</p>
<p>
st %i4, [%fp
<span>
-4
</span>
] ! x4
</p>
<p>
ld [%fp
<span>
-4
</span>
],%f3
</p>
<p>
st %i5, [%fp
<span>
-4
</span>
] ! *s
</p>
<p>
ld [%fp
<span>
-4
</span>
],%f4
</p>
<p>
cmp %l0,
<span>
0
</span>
! if N ?
<span>
0
</span>
</p>
<p>
ble allminus
</p>
<p>
cmp %l0,
<span>
1
</span>
</p>
<p>
be addFirst
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
2
</span>
</p>
<p>
be addSecond
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
3
</span>
</p>
<p>
be addThird
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
4
</span>
</p>
<p>
ble addFourth
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
<p>
allminus: fsubs %f4,%f0,%f4
</p>
<p>
fsubs %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addFirst: fadds %f4,%f0,%f4
</p>
<p>
fsubs %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addSecond:fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addThird: fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fadds %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addFourth:fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fadds %f4,%f2,%f4
</p>
<p>
fadds %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
fsumdiffpt: save %sp,
<span>
-128
</span>
,%sp
</p>
<p>
st %i0, [%fp
<span>
-4
</span>
] ! N
</p>
<p>
ld [%fp
<span>
-4
</span>
],%l0
</p>
<p>
ld [%i1],%f0
</p>
<p>
ld [%i2],%f1
</p>
<p>
ld [%i3],%f2
</p>
<p>
ld [%i4],%f3
</p>
<p>
ld [%i5],%f4
</p>
<p>
cmp %l0,
<span>
0
</span>
! if N ?
<span>
0
</span>
</p>
<p>
ble allminuspt
</p>
<p>
cmp %l0,
<span>
1
</span>
</p>
<p>
be addFirstpt
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
2
</span>
</p>
<p>
be addSecondpt
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
3
</span>
</p>
<p>
be addThirdpt
</p>
<p>
nop
</p>
<p>
cmp %l0,
<span>
4
</span>
</p>
<p>
ble addFourthpt
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
<p>
allminuspt: fsubs %f4,%f0,%f4
</p>
<p>
fsubs %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addFirstpt: fadds %f4,%f0,%f4
</p>
<p>
fsubs %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addSecondpt:fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fsubs %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addThirdpt: fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fadds %f4,%f2,%f4
</p>
<p>
fsubs %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
</p>
<p>
ret
</p>
<p>
restore
</p>
<p>
addFourthpt:fadds %f4,%f0,%f4
</p>
<p>
fadds %f4,%f1,%f4
</p>
<p>
fadds %f4,%f2,%f4
</p>
<p>
fadds %f4,%f3,%f4
</p>
<p>
st %f4,[%fp
<span>
-4
</span>
]
</p>
<p>
ld [%fp
<span>
-4
</span>
],%i0
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
</div>

</div>
</div>
</div>

</div>