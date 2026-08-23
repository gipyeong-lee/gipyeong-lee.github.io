---
layout: post
title: "[SPARC] Bitwise Operations"
description: "Problem Definition: Implement operations for a set storing numbers from 0 to 63. Sets are defined in the static area as set1, set2, and set3. Each bit of set1, set2, and set3 represents 63, 62, ..., 2, 1, 0, where the bit is 1 if the number belongs to the set and 0 otherwise."
date: 2015-08-27 01:47:27 +0900
section: blog
category: engineering
lang: en
ref: 2015-08-27-legacy-103-engineering-sparc
tags:
  - "sparc"
  - "bit-processing"
  - "mapinc"
  - "SPARC"
  - "engineering"
translation_source_hash: d3447d251f648c7d2141af13fb3bc9630ff3ea46abb1460309d0341414a93e6f
---

<p>
<b>
<span>
Problem Definition
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
Bitwise Operations
</span>
</p>
</div>
</div>
<div class="layoutArea">
<div class="column">
<p>
<span>
We aim to implement operations for a set that stores numbers from
</span>
<span>
0
</span>
<span>
to
</span>
<span>
63.
</span>
<span>
The sets are defined in the static area with the names
</span>
<span>
set1, set2, and set3.
</span>
<span>
Each bit of set1, set2, and set3 represents
</span>
<span>
63, 62,
</span>
<span>
...
</span>
<span>
, 2, 1, 0,
</span>
<span>
and the bit is set to
</span>
<span>
1
</span>
<span>
if the corresponding number belongs to the set, otherwise it is set to
</span>
<span>
0.
</span>
<span>
Initially, you just need to define the sets you want to test.
</span>
</p>
<ul>
<li>
<p>
<span>
 member(j, set): Returns
</span>
<span>
1
</span>
<span>
if j is an element of set.
</span>
</p>
</li>
<li>
<p>
<span>
 union: Union operation. set3 = set1 ∪ set2
</span>
</p>
</li>
<li>
<p>
<span>
 intersection: Intersection operation. set3 = set1 ∩ set2
</span>
</p>
</li>
<li>
<p>
<span>
 subtract: Set difference operation. set3 = set1 - set2
</span>
</p>
</li>
<li>
<p>
<span>
 add(j, set): Adds element j to the set set.
</span>
</p>
</li>
<li>
<p>
<span>
 mapinc(set, d): A set where d is added to each element of set. For example,
</span>
<span>
set({1, 13, 17}, 1) = {2, 14, 18}.
</span>
</p>
<p>
<span>
Submission
</span>
</p>
</li>
<li>
<p>
<span>
 Submit a file containing only the definitions of the above 3 functions. Do not submit the file containing main and the definitions of sets set1 and set2. Use them separately for your own testing and execution.
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
Design
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
1. Sets are defined in the static area as set1, set2, and set3.
</span>
</font>
</div>
<div>
<font>
<span>
2. Each bit of set1, set2, and set3 represents 63, 62, 61, ..., 2, 1, 0.
</span>
</font>
</div>
<div>
<font>
<span>
3. If the corresponding number is in the set, the bit is set to 1; otherwise, it is 0.
</span>
</font>
</div>
<div>
<font>
<span>
4. Define the initial sets to be tested.
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
&lt; Mediocre source code.. &gt;
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
1. member(j, set) function > Result 0 or 1
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
*To run the source code, please uncomment the
<span>
<b>
bold comments
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
!    st %l2,[%sp +
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
!    st %l3,[%sp +
<span>
32
</span>
]
</b>
</p>
<p>
<b>
!    mov
<span>
16
</span>
,%o0
</b>
</p>
<p>
<b>
!    call member
</b>
</p>
<p>
<b>
!    mov %l2,%o1
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
loop:   sll %l0,
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
ld [%o1],%l1    ! load [%fp
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
cmp %i0,%l1     ! x== [%fp
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
be isexist    ! if equal then goto isexist
</p>
<p>
cmp %l0,N      ! %l0 < N
</p>
<p>
bl,a indexup   ! if true goto indexup
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
2. add(j, set) function > { 1,3,4, j }
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
*To run the source code, please uncomment the
<span>
<b>
bold comments
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
!    mov
<span>
44
</span>
,%o1
</b>
</p>
<p>
<b>
!    call add
</b>
</p>
<p>
<b>
!    mov %l2,%o0
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
add :   save %sp,
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
addend:     ret
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
3. mapinc(set, d) function > {1,3,4}, d= 1 > {2,4,5}
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
*To run the source code, please uncomment the
<span>
<b>
bold comments
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
!    st %l2,[%sp +
<span>
16
</span>
]
</b>
</p>
<p>
<b>
!    mov
<span>
1
</span>
,%o1
</b>
</p>
<p>
<b>
!    call mapinc
</b>
</p>
<p>
<b>
!   mov %l2,%o0
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
mapinc :    save %sp,
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
indexup :   inc %l0 ! increase index ++
</p>
<p>
loop:       sll %l0,
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
ld [%o1],%l1    ! load [%fp
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
add %l1,%i1,%l1 ! add  %l1 = %l1 + %i1
</p>
<p>
st %l1,[%o1]    ! store %l1 to [%fp
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
cmp %l0,N       ! compare %l0 < N
</p>
<p>
bl,a indexup    ! if true goto indexup
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
The mediocre source codes are all finished...
</div>
<div>
What I felt while doing this assignment was that if you use bit processing when accessing array addresses, you don't need to calculate addresses using a separate multiplication. It's very convenient.
</div>
<div>
Of course, the source code is not optimized. Because I'm a complete beginner..
</div>
<div>
<br>
</div>
<div>
It took roughly 6 hours of struggling to write the source code. I debugged it and checked what was in the memory one by one.
</div>
<div>
<br>
</div>
<div>
Oh, as for the commands used for debugging..
</div>
<div>
<br>
</div>
<div>
<b>
- gcc -g main.c -o main    ::  Compiles the main.c file so that the global labels can be referenced, and spits out an executable file named 'main'.
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- gdb main  :: Debugs 'main'.
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- p $i0    ::  Prints the value of the %i0 register.
</b>
</div>
<div>
<b>
- p set1 @docs/superpowers/specs/2026-08-23-mac-release-dmg-design.md   ::  Checks up to the n-th value of the static variable set1.
</b>
</div>
<div>
<b>
ex) -p set1 @docs/superpowers/specs/2026-08-23-mac-release-dmg-design.md    >> {1 , 4 , 5 }
</b>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
My understanding may be very wrong in many places. If you correct me, I will revise it.
</div>
<div>
Thank you.
</div>
<div>
<br>
</div>
</div>
</div>
</div>
</div>
</div>