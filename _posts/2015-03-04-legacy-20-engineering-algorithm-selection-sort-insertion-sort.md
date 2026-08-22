---
layout: post
title: "[Algorithm] Selection sort, Insertion sort"
description: "GiPyeong Lee selection_sort.c // studentID : A889056 // selection_sort.c // Algorithm_Hongik // // Created by GiPyeong Lee on 2015. 3. 3.. // Copyright (c) 2..."
date: 2015-03-04 02:43:17 +0900
section: blog
category: engineering
lang: ko
ref: 2015-03-04-legacy-20-engineering-algorithm-selection-sort-insertion-sort
tags:
  - "Algorithm"
  - "engineering"
---

<table class="MsoTableGrid" width="667">
<tbody>
<tr>
<td width="424">

<p>
<b>
<span>
GiPyeong Lee
</span>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">

<p>
<b>
<span>
selection_sort.c
</span>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">

<p>
<span>
//
  studentID : A889056
</span>
</p>

<p>
<span>
//
  selection_sort.c
</span>
</p>

<p>
<span>
//
  Algorithm_Hongik
</span>
</p>

<p>
<span>
//
</span>
</p>

<p>
<span>
//
  Created by GiPyeong Lee on 2015. 3. 3..
</span>
</p>

<p>
<span>
//
  Copyright (c) 2015
</span>
<span>
년
</span>
<span>
com.devsfolder.Hongik. All rights
  reserved.
</span>
</p>

<p>
<span>
//
</span>
</p>



<p>
<span>
#include
</span>
<span>
&lt;stdio.h&gt;
</span>
</p>

<p>
<span>
#include
</span>
<span>
&lt;time.h&gt;
</span>
</p>

<p>
<span>
#include
</span>
<span>
&lt;stdlib.h&gt;
</span>
</p>
<p>
<span>
int
</span>
<span>
tempArray[
</span>
<span>
1000001
</span>
<span>
]={
</span>
<span>
0
</span>
<span>
,};
</span>
<span>
// Container
</span>
</p>

<p>
<span>
void
</span>
<span>
selection_sort(
</span>
<span>
int
</span>
<span>
argc,
</span>
<span>
const
</span>

<span>
char
</span>
<span>
* argv[]){
</span>
</p>



<p>

<span>
if
</span>
<span>
( argc &lt;=
</span>
<span>
2
</span>
<span>
)
</span>
<span>
/* argc should be 2 for correct
  execution for file and how many testcase */
</span>
</p>

<p>
<span>
{
</span>
</p>

<p>

<span>
printf
</span>
<span>
(
</span>
<span>
"Please Input Correctly Arguments
  (eg. selection_sort hw1_input.txt 1000\n"
</span>
<span>
);
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>

<span>
else
</span>
<span>
{
</span>
</p>

<p>

<span>
// Correct Alguments
</span>
</p>



<p>

<span>
int
</span>
<span>
i,j;
</span>
</p>

<p>

<span>
int
</span>
<span>
min,temp;
</span>
</p>

<p>

<span>
FILE
</span>
<span>
*file =
</span>
<span>
fopen
</span>
<span>
( argv[
</span>
<span>
1
</span>
<span>
],
</span>
<span>
"r"
</span>
<span>
);
</span>
<span>
// open file pointer
</span>
</p>

<p>

<span>
char
</span>
<span>
number[
</span>
<span>
11
</span>
<span>
];
</span>
<span>
// number container for reading line
  by line in file Obj
</span>
</p>

<p>

<span>
int
</span>
<span>
lineCounter=
</span>
<span>
0
</span>
<span>
;
</span>
<span>
// this is check line
</span>
</p>

<p>

<span>
int
</span>
<span>
maxCount =
</span>
<span>
atoi
</span>
<span>
(argv[
</span>
<span>
2
</span>
<span>
]);
</span>
</p>

<p>

<span>
while
</span>
<span>
(
</span>
<span>
fgets
</span>
<span>
(number,
</span>
<span>
sizeof
</span>
<span>
(number), file)){
</span>
</p>

<p>

<span>
if
</span>
<span>
(lineCounter==maxCount){
</span>
</p>

<p>

<span>
break
</span>
<span>
;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
tempArray[lineCounter] =
</span>
<span>
atoi
</span>
<span>
(number);
</span>
<span>
// set int unordered array
</span>
</p>

<p>
<span>
lineCounter++;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>

<span>
fclose
</span>
<span>
(file);
</span>
<span>
// close file pointer
</span>
</p>



<p>

<span>
for
</span>
<span>
(i=
</span>
<span>
0
</span>
<span>
; i&lt;maxCount; i++) {
</span>
</p>

<p>
<span>
min = i;
</span>
<span>
// set current Index
</span>
</p>

<p>

<span>
for
</span>
<span>
(j=i+
</span>
<span>
1
</span>
<span>
; j&lt;maxCount; j++) {
</span>
</p>

<p>

<span>
if
</span>
<span>
(tempArray[min]&gt;tempArray[j]){
</span>
</p>

<p>
<span>
min =
  j;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
temp =
  tempArray[min];
</span>
</p>

<p>
<span>
tempArray[min]
  = tempArray[i];
</span>
</p>

<p>
<span>
tempArray[i]=temp;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>

<span>
for
</span>
<span>
(i=
</span>
<span>
0
</span>
<span>
;i&lt;maxCount;i++){
</span>
</p>

<p>

<span>
printf
</span>
<span>
(
</span>
<span>
"%d\n"
</span>
<span>
,tempArray[i]);
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
int
</span>
<span>
main(
</span>
<span>
int
</span>
<span>
argc,
</span>
<span>
const
</span>

<span>
char
</span>
<span>
* argv[]) {
</span>
</p>

<p>

<span>
// insert code here...
</span>
</p>

<p>

<span>
clock_t
</span>
<span>
start_time, end_time;
</span>
<span>
// Time Variable Declare
</span>
</p>

<p>
<span>
start_time =
</span>
<span>
clock
</span>
<span>
();
</span>
<span>
// Time to start
</span>
</p>

<p>

<span>
selection_sort
</span>
<span>
(argc,argv);
</span>
</p>

<p>
<span>
end_time =
</span>
<span>
clock
</span>
<span>
();
</span>
<span>
// Time to end
</span>
</p>

<p>

<span>
printf
</span>
<span>
(
</span>
<span>
"Running time = %.1f ms\n"
</span>
<span>
, ((
</span>
<span>
double
</span>
<span>
)(end_time-start_time)) /
</span>
<span>
CLOCKS_PER_SEC
</span>
<span>
*
</span>
<span>
1000
</span>
<span>
);
</span>
</p>



<p>

<span>
return
</span>

<span>
0
</span>
<span>
;
</span>
</p>

<p>
<span>
}
</span>
</p>



</td>
</tr>
<tr>
<td width="424">

<p>
<b>
<span>
Insertion_sort.c
</span>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">

<p>
<span>
//
  studentID : A889056
</span>
</p>

<p>
<span>
//
  insertion_sort.c
</span>
</p>

<p>
<span>
//
  Algorithm_Hongik
</span>
</p>

<p>
<span>
//
</span>
</p>

<p>
<span>
//
  Created by GiPyeong Lee on 2015. 3. 4..
</span>
</p>

<p>
<span>
//
  Copyright (c) 2015
</span>
<span>
년
</span>
<span>
com.devsfolder.Hongik. All rights
  reserved.
</span>
</p>

<p>
<span>
//
</span>
</p>



<p>
<span>
#include
</span>
<span>
&lt;stdio.h&gt;
</span>
</p>

<p>
<span>
#include
</span>
<span>
&lt;time.h&gt;
</span>
</p>

<p>
<span>
#include
</span>
<span>
&lt;stdlib.h&gt;
</span>
</p>
<p>
<span>
<br>
</span>
</p>
<p>
<span>
int
</span>
<span>
tempArray[
</span>
<span>
1000001
</span>
<span>
]={
</span>
<span>
0
</span>
<span>
,};
</span>
<span>
// Container
</span>
</p>

<p>
<span>
void
</span>
<span>
insertion_sort(
</span>
<span>
int
</span>
<span>
argc,
</span>
<span>
const
</span>

<span>
char
</span>
<span>
* argv[]){
</span>
</p>

<p>

<span>
if
</span>
<span>
( argc &lt;=
</span>
<span>
2
</span>
<span>
)
</span>
<span>
/* argc should be 2 for correct
  execution for file and how many testcase */
</span>
</p>

<p>
<span>
{
</span>
</p>

<p>
<span>
printf(
</span>
<span>
"Please Input Correctly Arguments
  (eg. selection_sort hw1_input.txt 1000\n"
</span>
<span>
);
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>

<span>
else
</span>
<span>
{
</span>
</p>

<p>

<span>
// Correct Alguments &gt; Do Task :)
</span>
</p>

<p>

<span>
int
</span>
<span>
i,j;
</span>
</p>

<p>

<span>
int
</span>
<span>
temp;
</span>
</p>

<p>
<span>
FILE *file =
  fopen( argv[
</span>
<span>
1
</span>
<span>
],
</span>
<span>
"r"
</span>
<span>
);
</span>
<span>
// open file pointer
</span>
</p>

<p>

<span>
char
</span>
<span>
number[
</span>
<span>
11
</span>
<span>
];
</span>
<span>
// number container for reading line
  by line in file Obj
</span>
</p>

<p>

<span>
int
</span>
<span>
lineCounter=
</span>
<span>
0
</span>
<span>
;
</span>
<span>
// this is check line
</span>
</p>

<p>

<span>
int
</span>
<span>
maxCount = atoi(argv[
</span>
<span>
2
</span>
<span>
]);
</span>
</p>

<p>

<span>
while
</span>
<span>
(fgets(number,
</span>
<span>
sizeof
</span>
<span>
(number), file)){
</span>
</p>

<p>

<span>
if
</span>
<span>
(lineCounter==maxCount){
</span>
</p>

<p>

<span>
break
</span>
<span>
;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
tempArray[lineCounter] = atoi(number);
</span>
<span>
// set int unordered array
</span>
</p>

<p>
<span>
lineCounter++;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
fclose(file);
</span>
<span>
// close file pointer
</span>
</p>

<p>

<span>
for
</span>
<span>
(i=
</span>
<span>
1
</span>
<span>
; i&lt;maxCount; i++) {
</span>
</p>

<p>
<span>
temp =
  tempArray[i];
</span>
</p>

<p>
<span>
j=i-
</span>
<span>
1
</span>
<span>
;
</span>
</p>

<p>

<span>
while
</span>
<span>
((temp&lt;tempArray[j])&amp;&amp;(j&gt;=
</span>
<span>
0
</span>
<span>
)){
</span>
</p>

<p>
<span>
tempArray[j+
</span>
<span>
1
</span>
<span>
]=tempArray[j];
</span>
</p>

<p>
<span>
j=j-
</span>
<span>
1
</span>
<span>
;
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
tempArray[j+
</span>
<span>
1
</span>
<span>
]=temp;
</span>
</p>

<p>
<span>
}
</span>
</p>



<p>

<span>
for
</span>
<span>
(i=
</span>
<span>
0
</span>
<span>
;i&lt;maxCount;i++){
</span>
</p>

<p>
<span>
printf(
</span>
<span>
"%d\n"
</span>
<span>
,tempArray[i]);
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
}
</span>
</p>

<p>
<span>
}
</span>
</p>



<p>
<span>
int
</span>
<span>
main(
</span>
<span>
int
</span>
<span>
argc,
</span>
<span>
const
</span>

<span>
char
</span>
<span>
* argv[]) {
</span>
</p>

<p>

<span>
// insert code here...
</span>
</p>

<p>
<span>
clock_t start_time,
  end_time;
</span>
<span>
// Time
  Variable Declare
</span>
</p>

<p>
<span>
start_time = clock();
</span>
<span>
// Time to start
</span>
</p>

<p>
<span>
insertion_sort(argc,argv);
</span>
</p>

<p>
<span>
end_time = clock();
</span>
<span>
// Time to end
</span>
</p>

<p>
<span>
printf(
</span>
<span>
"Running time = %.1f ms\n"
</span>
<span>
, ((
</span>
<span>
double
</span>
<span>
)(end_time-start_time)) / CLOCKS_PER_SEC
  *
</span>
<span>
1000
</span>
<span>
);
</span>
</p>



<p>

<span>
return
</span>

<span>
0
</span>
<span>
;
</span>
</p>

<p>
<span>
}
</span>
</p>

</td>
</tr>
<tr>
<td width="424">

<p>
<b>
<span>
Graph
</span>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">





</td>
</tr>
<tr>
<td width="424">

<p>
<b>
<span>
Log Graph
</span>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">





</td>
</tr>
<tr>
<td width="424">

<p>
<b>
<span>
conclusion
</span>
</b>
<b>
</b>
</p>

</td>
</tr>
<tr>
<td width="424">

<p>
<span>
After testing both sorting algorithms called
  ‘selection sort’ and ‘insertion sort’. insertion is more faster than
  selection sort when amount of numbers unsorted is more than 10000.  Almost half of time passed.
</span>
</p>

<p>
<span>
But If we make decendant numbers to
  ascendant ordering by using insertion sorting. Than maybe running time same by
  sorting using ‘selection sort’ .
</span>
</p>

</td>
</tr>
</tbody>
</table>


<p>
<span>
<br>
</span>
</p>
<p>
<span>
아래는 해당 과제에 따른 교수님의 지적사항이다.
</span>
</p>

<p>
<b>
<span>
- main이 아닌 다른 함수내에서 1000000짜리 (4MB짜리) 지역변수를 할당하는 건 매우 안 좋은 방식/습관임
</span>
<br>
<span>
- 지역변수는 운영체제의 stack에 들어가게 되는데, stack은 크기 한계가 있음
</span>
<br>
<span>
- 그 함수가 여러번 호출되면 프로그램 폭파
</span>
<br>
<span>
- 저렇게 큰건 전역변수로 두거나, main에 두거나, 아니면 malloc/free 할것.
</span>
</b>
</p>
<p>
코드 수정을 한 후에 좀 더 알아보았다.
</p>

<p>
<b>
<span>
코드 수정
</span>
</b>
</p>


<pre class="brush: c">
//  studentID : A889056
//  selection_sort.c
//  Algorithm_Hongik
//
//  Created by GiPyeong Lee on 2015. 3. 3..
//  Copyright (c) 2015년 com.devsfolder.Hongik. All rights reserved.
//

#include &lt;stdio.h&gt;
#include &lt;time.h&gt;
#include &lt;stdlib.h&gt;

int tempArray[1000001]={0,}; // Container
void selection_sort(int argc, const char * argv[]){

    if ( argc &lt;= 2 ) /* argc should be 2 for correct execution for file and how many testcase */
    {
        printf("Please Input Correctly Arguments (eg. selection_sort hw1_input.txt 1000\n");
        return;
    }

        // Correct Alguments
        int i,j;
        int min,temp;
        FILE *file = fopen( argv[1], "r" ); // open file pointer
        char number[11]; // number container for reading line by line in file Obj
        int lineCounter=0; // this is check line
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // set int unordered array
            lineCounter++;
        }
        fclose(file); // close file pointer

        for (i=0; i&lt;maxCount; i++) {
            min = i; // set current Index
            for (j=i+1; j&lt;maxCount; j++) {
                if(tempArray[min]&gt;tempArray[j]){
                    min = j;
                }
            }
            temp = tempArray[min];
            tempArray[min] = tempArray[i];
            tempArray[i]=temp;
        }
        for(i=0;i&lt;maxCount;i++){
            printf("%d\n",tempArray[i]);
        }

}

int main(int argc, const char * argv[]) {
    // insert code here...
    clock_t start_time, end_time; // Time Variable Declare
    start_time = clock(); // Time to start
    selection_sort(argc,argv);
    end_time = clock(); // Time to end
    printf("Running time = %.1f ms\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC * 1000);

    return 0;
}
</pre>



<pre class="brush: c">
//  studentID : A889056
//  insertion_sort.c
//  Algorithm_Hongik
//
//  Created by GiPyeong Lee on 2015. 3. 4..
//  Copyright (c) 2015년 com.devsfolder.Hongik. All rights reserved.
//

#include &lt;stdio.h&gt;
#include &lt;time.h&gt;
#include &lt;stdlib.h&gt;
int tempArray[1000001]={0,}; // Container
void insertion_sort(int argc, const char * argv[]){
    if ( argc &lt;= 2 ) /* argc should be 2 for correct execution for file and how many testcase */
    {
        printf("Please Input Correctly Arguments (eg. selection_sort hw1_input.txt 1000\n");
        return;
    }

        // Correct Alguments &gt; Do Task :)
        int i,j;
        int temp;
        FILE *file = fopen( argv[1], "r" ); // open file pointer
        char number[11]; // number container for reading line by line in file Obj
        int lineCounter=0; // this is check line
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // set int unordered array
            lineCounter++;
        }
        fclose(file); // close file pointer
        for (i=1; i&lt;maxCount; i++) {
            temp = tempArray[i];
            j=i-1;
            while((temp&lt;tempArray[j])&amp;&amp;(j&gt;=0)){
                tempArray[j+1]=tempArray[j];
                j=j-1;
            }
            tempArray[j+1]=temp;
        }

        for(i=0;i&lt;maxCount;i++){
            printf("%d\n",tempArray[i]);
        }

}

int main(int argc, const char * argv[]) {
    // insert code here...
    clock_t start_time, end_time; // Time Variable Declare
    start_time = clock(); // Time to start
    insertion_sort(argc,argv);
    end_time = clock(); // Time to end
    printf("Running time = %.1f ms\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC * 1000);

    return 0;
}
</pre>



<p>
<font>
<b>
<span>
메모리 영역
</span>
</b>
</font>
</p>





<p>
<span>
우리가 특정 언어로 코드를 짜서 컴파일 후 실행할 경우 위와 같은 메모리 구조에 변수 및 함수들이 저장된다.
</span>
</p>


<p class="바탕글">
<span>
<b>
<span>
데이터 영역(Data Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
데이터 영역은 전역 변수와 static 변수가 할당되는 영역이다. 이 영역에 할당되는 변수들은 일반적으로 프로그램의 시작과 동시에 할당되고, 프로그램이 종료되어야만 메모리에서 소멸된다. 즉, 데이터 영역에 할당된 변수는 프로그램이 종료될 때까지 계속 존재한다는 특징을 지닌다. 전역 변수와 static 변수의 특징과 일치하는 부분이다.
</span>
</p>

<p class="바탕글">
<span>
<br>
</span>
</p>
<p class="바탕글">
<span>
<b>
<span>
스택 영역(Stack Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
스택 영역은 함수 호출 시 생성되는 지역 변수와 매개 변수가 저장되는 영역이다. 이 영역에 할당된 변수는 함수 호출이 완료되면 사라진다는 특징을 지닌다. 이는 다른 메모리 영역과 확실히 비교되는 특징이다. 늦게 할당된 변수의 메모리가 먼저 해제되므로 스택의 특징과 일치한다.
</span>
</p>

<p class="바탕글">
<span>
<br>
</span>
</p>
<p class="바탕글">
<span>
<b>
<span>
힙 영역(Heap Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
힙 영역은 프로그래머가 관리하는 메모리 영역이다. 즉 프로그래머의 필요에 의해서 메모리 공간이 할당 및 소멸되는 영역이다. 동적 할당으로 생성되는 메모리 영역이다.
</span>
</p>

<p class="바탕글">
<span>
※ 정적 할당되는 변수의 메모리는 변수의 특성에 따라 데이터 또는 스택 영역에 생성된다. 정적 할당은 컴파일 단계(Compile-time)에서 모두 이루어진다. 하지만 컴파일 단계에서는 메모리의 크기만 생성 할 뿐 변수의 값은 저장 되지 않는다. 이 때문에 배열의 크기는 상수로만 지정해야 하는 것이다. 변수 값의 저장은 런타임(Run-time)에서 이루어지며, 런타임 단계에서 메모리를 생성하고자 할때 사용하는 것이 동적 할당이다.
</span>
</p>

<p>
그렇다면 여기서 궁금증이 생긴다..
</p>
<p>
Heap 과 Stack 이 가득차게 되면 어떻게 되는걸까?
</p>
