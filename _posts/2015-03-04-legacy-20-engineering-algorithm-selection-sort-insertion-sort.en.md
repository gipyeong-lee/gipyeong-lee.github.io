---
layout: post
title: "[Algorithm] Selection sort, Insertion sort"
description: "GiPyeong Lee selection_sort.c // studentID : A889056 // selection_sort.c // Algorithm_Hongik // // Created by GiPyeong Lee on 2015. 3. 3.. // Copyright (c) 2..."
date: 2015-03-04 02:43:17 +0900
section: blog
category: engineering
lang: en
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
// Correct Arguments
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
// Correct Arguments &gt; Do Task :)
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
After testing both sorting algorithms called ‘selection sort’ and ‘insertion sort’, insertion is faster than selection sort when the amount of unsorted numbers is more than 10,000. Almost half the time was saved.
</span>
</p>

<p>
<span>
However, if we sort descending numbers into ascending order using insertion sort, the running time might be the same as using selection sort.
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
Below is the feedback from the professor regarding the assignment.
</span>
</p>

<p>
<b>
<span>
- Allocating a 1,000,000 (4MB) local variable in a function other than main is a very bad practice/habit.
</span>
<br>
<span>
- Local variables are placed on the operating system's stack, and the stack has a size limit.
</span>
<br>
<span>
- If that function is called multiple times, the program will crash.
</span>
<br>
<span>
- For such large data, use global variables, put them in main, or use malloc/free.
</span>
</b>
</p>
<p>
I looked into it further after modifying the code.
</p>

<p>
<b>
<span>
Code Modification
</span>
</b>
</p>

<pre class="brush: c">
//  studentID : A889056
//  selection_sort.c
//  Algorithm_Hongik
//
//  Created by GiPyeong Lee on 2015. 3. 3..
//  Copyright (c) 2015 com.devsfolder.Hongik. All rights reserved.
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

        // Correct Arguments
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
//  Copyright (c) 2015 com.devsfolder.Hongik. All rights reserved.
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

        // Correct Arguments &gt; Do Task :)
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
Memory Area
</span>
</b>
</font>
</p>

<p>
<span>
When we write code in a certain language and execute it after compilation, variables and functions are stored in the memory structure as shown above.
</span>
</p>

<p>
<span>
<b>
<span>
Data Area
</span>
</b>
</span>
</p>
<p>
<span>
The data area is where global variables and static variables are allocated. Variables allocated to this area are generally allocated when the program starts and are only removed from memory when the program terminates. In other words, variables allocated in the data area exist until the program terminates. This matches the characteristics of global and static variables.
</span>
</p>

<p>
<span>
<br>
</span>
</p>
<p>
<span>
<b>
<span>
Stack Area
</span>
</b>
</span>
</p>
<p>
<span>
The stack area is where local variables and parameters generated during function calls are stored. Variables allocated in this area have the characteristic of disappearing once the function call is completed. This is a characteristic that clearly differentiates it from other memory areas. Since the memory for variables allocated later is freed first, it aligns with the characteristics of a stack.
</span>
</p>

<p>
<span>
<br>
</span>
</p>
<p>
<span>
<b>
<span>
Heap Area
</span>
</b>
</span>
</p>
<p>
<span>
The heap area is a memory area managed by the programmer. In other words, it is an area where memory space is allocated and deallocated according to the programmer's needs. It is the memory area created through dynamic allocation.
</span>
</p>

<p>
<span>
※ The memory for statically allocated variables is created in either the data or stack area depending on the characteristics of the variable. Static allocation is done entirely at the compile-time stage. However, at the compile-time stage, only the size of the memory is generated, and the value of the variable is not stored. This is why the size of an array must be specified only as a constant. Storing the variable's value occurs at the run-time stage, and dynamic allocation is used when you want to create memory at the run-time stage.
</span>
</p>

<p>
This leads to a question...
</p>
<p>
What happens if the Heap and Stack become full?
</p>