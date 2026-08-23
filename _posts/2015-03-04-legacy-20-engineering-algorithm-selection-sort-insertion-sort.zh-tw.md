---
layout: post
title: "[演算法] 選擇排序 (Selection sort)、插入排序 (Insertion sort)"
description: "GiPyeong Lee selection_sort.c // studentID : A889056 // selection_sort.c // Algorithm_Hongik // // Created by GiPyeong Lee on 2015. 3. 3.. // Copyright (c) 2..."
date: 2015-03-04 02:43:17 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-03-04-legacy-20-engineering-algorithm-selection-sort-insertion-sort
tags:
  - "演算法"
  - "工程"
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
// 容器
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
/* argc 應為 2，以便正確執行檔案並指定測試案例數量 */
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
// 正確的參數
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
// 開啟檔案指標
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
// 用於讀取檔案中逐行物件的數字容器
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
// 檢查行數
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
// 設定整數未排序陣列
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
// 關閉檔案指標
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
// 設定目前索引
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
// 在此插入程式碼...
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
// 宣告時間變數
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
// 開始時間
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
// 結束時間
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
// 容器
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
/* argc 應為 2，以便正確執行檔案並指定測試案例數量 */
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
// 正確的參數 > 執行任務 :)
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
// 開啟檔案指標
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
// 用於讀取檔案中逐行物件的數字容器
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
// 檢查行數
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
// 設定整數未排序陣列
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
// 關閉檔案指標
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
// 在此插入程式碼...
</span>
</p>

<p>
<span>
clock_t start_time,
  end_time;
</span>
<span>
// 宣告時間變數
</span>
</p>

<p>
<span>
start_time = clock();
</span>
<span>
// 開始時間
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
// 結束時間
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
圖表
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
對數圖
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
結論
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
在測試完「選擇排序」與「插入排序」兩種排序演算法後，當未排序數字的數量超過 10,000 個時，插入排序比選擇排序快。時間幾乎縮短了一半。
</span>
</p>

<p>
<span>
但如果我們使用插入排序將遞減數字改為遞增排序，那麼執行時間可能與選擇排序相同。
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
以下是教授針對此作業提出的指正事項：
</span>
</p>

<p>
<b>
<span>
- 在 main 以外的函式中配置 1,000,000 個（4MB）的區域變數是非常不好的方式/習慣。
</span>
<br>
<span>
- 區域變數會進入作業系統的堆疊（stack），而堆疊有大小限制。
</span>
<br>
<span>
- 若該函式被多次呼叫，程式將會崩潰。
</span>
<br>
<span>
- 像這樣的大型變數應設為全域變數、放在 main 中，或者使用 malloc/free 進行動態配置。
</span>
</b>
</p>
<p>
修正程式碼後，我又進一步了解了相關知識。
</p>

<p>
<b>
<span>
程式碼修正
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

int tempArray[1000001]={0,}; // 容器
void selection_sort(int argc, const char * argv[]){

    if ( argc &lt;= 2 ) /* argc 應為 2，以便正確執行檔案並指定測試案例數量 */
    {
        printf("Please Input Correctly Arguments (eg. selection_sort hw1_input.txt 1000\n");
        return;
    }

        // 正確的參數
        int i,j;
        int min,temp;
        FILE *file = fopen( argv[1], "r" ); // 開啟檔案指標
        char number[11]; // 用於讀取檔案中逐行物件的數字容器
        int lineCounter=0; // 檢查行數
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // 設定整數未排序陣列
            lineCounter++;
        }
        fclose(file); // 關閉檔案指標

        for (i=0; i&lt;maxCount; i++) {
            min = i; // 設定目前索引
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
    // 在此插入程式碼...
    clock_t start_time, end_time; // 宣告時間變數
    start_time = clock(); // 開始時間
    selection_sort(argc,argv);
    end_time = clock(); // 結束時間
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
int tempArray[1000001]={0,}; // 容器
void insertion_sort(int argc, const char * argv[]){
    if ( argc &lt;= 2 ) /* argc 應為 2，以便正確執行檔案並指定測試案例數量 */
    {
        printf("Please Input Correctly Arguments (eg. selection_sort hw1_input.txt 1000\n");
        return;
    }

        // 正確的參數 > 執行任務 :)
        int i,j;
        int temp;
        FILE *file = fopen( argv[1], "r" ); // 開啟檔案指標
        char number[11]; // 用於讀取檔案中逐行物件的數字容器
        int lineCounter=0; // 檢查行數
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // 設定整數未排序陣列
            lineCounter++;
        }
        fclose(file); // 關閉檔案指標
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
    // 在此插入程式碼...
    clock_t start_time, end_time; // 宣告時間變數
    start_time = clock(); // 開始時間
    insertion_sort(argc,argv);
    end_time = clock(); // 結束時間
    printf("Running time = %.1f ms\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC * 1000);

    return 0;
}
</pre>



<p>
<font>
<b>
<span>
記憶體區域
</span>
</b>
</font>
</p>





<p>
<span>
當我們使用特定語言編寫程式碼，經過編譯並執行時，變數與函式會儲存在如下的記憶體結構中。
</span>
</p>


<p class="바탕글">
<span>
<b>
<span>
資料區（Data Area）
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
資料區是分配全域變數與 static 變數的區域。在此區域分配的變數通常會在程式啟動時同步分配，並直到程式結束時才會從記憶體中清除。換句話說，資料區分配的變數具有會持續存在直到程式結束的特徵。這與全域變數與 static 變數的特性一致。
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
堆疊區（Stack Area）
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
堆疊區是儲存函式呼叫時所產生的區域變數與參數的區域。此區域分配的變數具有會在函式呼叫結束後消失的特性。這與其他記憶體區域有顯著的區別。後分配的變數記憶體會先被釋放，這與堆疊（Stack）的特性一致。
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
堆積區（Heap Area）
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
堆積區是由程式設計師管理的記憶體區域。也就是說，這是根據程式設計師的需求分配及銷毀記憶體空間的區域，是透過動態配置產生的記憶體區域。
</span>
</p>

<p class="바탕글">
<span>
※ 靜態分配變數的記憶體會根據變數的特性，在資料區或堆疊區中產生。靜態分配在編譯階段（Compile-time）即全部完成。然而，編譯階段只會產生記憶體大小，並不會儲存變數的值。這就是為什麼陣列大小必須指定為常數的原因。變數值的儲存是在執行階段（Run-time）完成的，而為了在執行階段產生記憶體所使用的技術即為動態配置。
</span>
</p>

<p>
這時產生了一個疑問...
</p>
<p>
如果 Heap 和 Stack 都滿了會發生什麼事呢？
</p>