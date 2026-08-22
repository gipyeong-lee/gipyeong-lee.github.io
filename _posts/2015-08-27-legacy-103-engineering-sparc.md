---
layout: post
title: "[SPARC] 비트처리 연산"
description: "문제 정의 비트 처리 연산 0 부터 63 까지의 수를 저장하는 집합에 대한 연산을 구현하려 한다 . 집합은 정적 영역에 set1, set2, set3 이란 이름으로 정의한다 . set1, set2, set3 의 각 비트는 63, 62, ... ,2, 1, 0 를 나타내고 , 해당..."
date: 2015-08-27 01:47:27 +0900
section: blog
category: engineering
lang: ko
ref: 2015-08-27-legacy-103-engineering-sparc
tags:
  - "sparc"
  - "비트처리"
  - "mapinc"
  - "SPARC"
  - "engineering"
---

<p>
<b>
<span>
문제 정의
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
비트 처리 연산
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
부터
</span>
<span>
63
</span>
<span>
까지의 수를 저장하는 집합에 대한 연산을 구현하려 한다
</span>
<span>
.
</span>
<span>
집합은 정적 영역에
</span>
<span>
set1,
set2, set3
</span>
<span>
이란 이름으로 정의한다
</span>
<span>
. set1, set2, set3
</span>
<span>
의 각 비트는
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
를 나타내고
</span>
<span>
,
</span>
<span>
해당
하는 수가 집합에 속해 있으면 그 비트가
</span>
<span>
1
</span>
<span>
아니면
</span>
<span>
0
</span>
<span>
으로 지정된다
</span>
<span>
.
</span>
<span>
초기에는 테스트 하려고 하
는 집합을 정의하면 된다
</span>
<span>
.
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
가
</span>
<span>
set
</span>
<span>
의 원소이면
</span>
<span>
1
</span>
<span>
을 반환
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
합집합
</span>
<span>
. set3 = set1
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
교집합
</span>
<span>
. set3 = set1
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
차집합
</span>
<span>
. set3 = set1 - set2
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
집합
</span>
<span>
set
</span>
<span>
에 원소
</span>
<span>
j
</span>
<span>
를 추가
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
의 각 원소에
</span>
<span>
d
</span>
<span>
를 더한 집합
</span>
<span>
.
</span>
<span>
예를 들어
</span>
<span>
set({1, 13, 17}, 1) = {2, 14, 18}
</span>
</p>
<p>
<span>
이다
</span>
<span>
.
</span>
</p>
<p>
<span>
제출물
</span>
</p>
</li>
<li>
<p>
<span>

</span>
<span>
위
</span>
<span>
3
</span>
<span>
개의 함수만 정의되어 있는 파일을 제출한다
</span>
<span>
. main
</span>
<span>
과 집합
</span>
<span>
set1, set2
</span>
<span>
가 정의되는 파
일은 제출하지 않는다
</span>
<span>
.
</span>
<span>
각자 테스팅을 위해 별도로 만들어 연결하여 실행하는데 사용한
다
</span>
<span>
.
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
설계
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
1. 집합은 정적영역에 set1, set2, set3 이란 이름으로 정의.
</span>
</font>
</div>
<div>
<font>
<span>
2. set1, set2,set 3 의 각 비트는 63,62,61....,2,1,0 을 나타냄.
</span>
</font>
</div>
<div>
<font>
<span>
3. 해당 하는 수가 집합에 속해 있으면 그 비트가 1 아니면 0 으로 지정됨.
</span>
</font>
</div>
<div>
<font>
<span>
4. 초기 테스트 하려는 집합 정의.
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
&lt; 별볼일 없는 소스 코드.. &gt;
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
1. member(j,set) 함수 &gt; 결과값 0 or 1
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
*해당 소스코드를 돌리시려면
<span>
<b>
굵은 글씨 주석
</b>
<span>
을 풀어주세요
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
2. add(j,set) 함수 &gt;  { 1,3,4, j }
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
*해당 소스코드를 돌리시려면
<span>
<b>
굵은 글씨 주석
</b>
<span>
을 풀어주세요
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
3. mapinc(set,d) 함수 &gt;  {1,3,4} , d= 1 &gt; {2,4,5}
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
*해당 소스코드를 돌리시려면
<span>
<b>
굵은 글씨 주석
</b>
<span>
을 풀어주세요
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
별거 없는 소스코드들이 모두 끝났습니다...
</div>
<div>
이번 과제를 하면서 느낀건 배열의 주소를 접근할때 bit 처리를 하면 따로 mul 을 사용하여 주소 계산을 하지 않아도 된다는 것입니다. 매우 편리합니다.
</div>
<div>
물론, 소스가 최적화 되어 있지 않습니다. 저는 왕초보이니까요..
</div>
<div>
<br>
</div>
<div>
대략 소스 짜는데 6시간의 삽질이 걸렸습니다. 디버깅을 해서 메모리에 뭐가있는지 하나하나 확인해보았습니다.
</div>
<div>
<br>
</div>
<div>
아, 디버깅시 사용하는 명령어로는..
</div>
<div>
<br>
</div>
<div>
<b>
- gcc -g main.c -o main     ::  main.c 파일을 global 레이블 참조가능하게 컴파일하고, main 이라는 이름의 실행파일을 뱉어낸다.
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- gdb main   :: main 을 디버깅한다.
</b>
</div>
<div>
<b>
<br>
</b>
</div>
<div>
<b>
- p $i0    ::  %i0  ,  i0 레지스트의 값을 출력한다.
</b>
</div>
<div>
<b>
- p set1@n   ::  정적변수 set1 의 n 번째 값까지 확인한다
</b>
</div>
<div>
<b>
ex) -p set1@3    &gt;&gt; {1 , 4 , 5 }
</b>
</div>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
제가 이해한 내용들이 많이 틀렸을 수 있습니다. 바로 잡아주시면 수정하도록 하겠습니다.
</div>
<div>
감사합니다.
</div>
<div>
<br>
</div>
</div>
</div>
</div>
</div>
</div>
