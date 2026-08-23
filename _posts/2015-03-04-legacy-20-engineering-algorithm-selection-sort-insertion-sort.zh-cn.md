---
layout: post
title: "[算法] 选择排序 (Selection sort), 插入排序 (Insertion sort)"
description: "GiPyeong Lee selection_sort.c // studentID : A889056 // selection_sort.c // Algorithm_Hongik // // Created by GiPyeong Lee on 2015. 3. 3.. // Copyright (c) 2..."
date: 2015-03-04 02:43:17 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-03-04-legacy-20-engineering-algorithm-selection-sort-insertion-sort
tags:
  - "Algorithm"
  - "engineering"
translation_source_hash: b85db7355393cdae72d33173642cee8dac30c8e52c0348c4384b0218e00dca8d
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
年
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
年
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
结论 (conclusion)
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
在测试了名为“选择排序”和“插入排序”的两种排序算法后发现，当无序数据的数量超过 10000 时，插入排序比选择排序更快。运行时间几乎缩短了一半。
</span>
</p>

<p>
<span>
但是，如果我们使用插入排序将降序排列的数字转换为升序排列，那么运行时间可能与使用“选择排序”进行排序的时间相同。
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
以下是针对该作业教授的指点意见。
</span>
</p>

<p>
<b>
<span>
- 在 main 以外的其他函数内分配 1000000 大小的（4MB）局部变量是非常糟糕的方式/习惯。
</span>
<br>
<span>
- 局部变量会进入操作系统的栈（stack）中，而栈是有大小限制的。
</span>
<br>
<span>
- 如果该函数被多次调用，程序会崩溃。
</span>
<br>
<span>
- 对于这么大的变量，要么放在全局变量中，要么放在 main 中，或者使用 malloc/free 进行动态分配。
</span>
</b>
</p>
<p>
在修改代码后，我又进一步了解了一些内容。
</p>

<p>
<b>
<span>
代码修改
</span>
</b>
</p>


<pre class="brush: c">
//  studentID : A889056
//  selection_sort.c
//  Algorithm_Hongik
//
//  Created by GiPyeong Lee on 2015. 3. 3..
//  Copyright (c) 2015年 com.devsfolder.Hongik. All rights reserved.
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
//  Copyright (c) 2015年 com.devsfolder.Hongik. All rights reserved.
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
内存区域
</span>
</b>
</font>
</p>





<p>
<span>
当我们用某种语言编写代码、编译并运行程序时，变量和函数会存储在如下的内存结构中。
</span>
</p>


<p class="바탕글">
<span>
<b>
<span>
数据区 (Data Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
数据区是分配全局变量和静态 (static) 变量的区域。分配在该区域的变量通常在程序开始时分配，只有在程序结束时才从内存中消失。也就是说，分配在数据区的变量具有持续存在直到程序结束的特性。这部分与全局变量和静态变量的特性相吻合。
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
栈区 (Stack Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
栈区是存储函数调用时创建的局部变量和参数的区域。该区域分配的变量具有在函数调用完成后消失的特性。这与其他内存区域有明显的区别。由于后分配的变量内存先被释放，这与栈的特性相一致。
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
堆区 (Heap Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
堆区是程序员管理的内存区域。也就是说，这是根据程序员的需要进行内存空间分配和销毁的区域。它是通过动态分配创建的内存区域。
</span>
</p>

<p class="바탕글">
<span>
※ 静态分配的变量内存根据变量的特性生成在数据区或栈区。静态分配全部在编译阶段 (Compile-time) 完成。但是，编译阶段只是生成内存大小，并不存储变量的值。这就是为什么数组大小必须指定为常量的原因。变量值的存储在运行时 (Run-time) 进行，在运行时阶段想要创建内存时所使用的就是动态分配。
</span>
</p>

<p>
那么，这里产生了一个疑问……
</p>
<p>
如果堆 (Heap) 和栈 (Stack) 都满了会怎样？
</p>