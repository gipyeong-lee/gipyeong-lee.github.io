---
layout: post
title: "[アルゴリズム] 選択ソート、挿入ソート"
description: "GiPyeong Lee selection_sort.c // studentID : A889056 // selection_sort.c // Algorithm_Hongik // // Created by GiPyeong Lee on 2015. 3. 3.. // Copyright (c) 2..."
date: 2015-03-04 02:43:17 +0900
section: blog
category: engineering
lang: ja
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
// コンテナ
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
/* ファイルとテストケース数の正確な実行のためにargcは2であるべき */
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
"引数を正しく入力してください (例. selection_sort hw1_input.txt 1000)\n"
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
// 正しい引数
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
// ファイルポインタを開く
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
// ファイルObjを行ごとに読み取るための数値コンテナ
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
// 行チェック用
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
// 整列されていない配列をintでセット
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
// ファイルポインタを閉じる
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
// 現在のインデックスを設定
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
// ここにコードを挿入...
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
// 時間変数宣言
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
// 終了時間
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
"実行時間 = %.1f ms\n"
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
// コンテナ
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
/* ファイルとテストケース数の正確な実行のためにargcは2であるべき */
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
"引数を正しく入力してください (例. selection_sort hw1_input.txt 1000)\n"
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
// 正しい引数 > タスク実行 :)
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
// ファイルポインタを開く
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
// ファイルObjを行ごとに読み取るための数値コンテナ
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
// 行チェック用
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
// 整列されていない配列をintでセット
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
// ファイルポインタを閉じる
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
// ここにコードを挿入...
</span>
</p>

<p>
<span>
clock_t start_time,
  end_time;
</span>
<span>
// 時間変数宣言
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
// 終了時間
</span>
</p>

<p>
<span>
printf(
</span>
<span>
"実行時間 = %.1f ms\n"
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
「選択ソート」と「挿入ソート」という2つのソートアルゴリズムをテストした結果、未整列の数値が10,000個を超えると、挿入ソートの方が選択ソートよりも高速でした。ほぼ半分の時間で処理できました。
</span>
</p>

<p>
<span>
しかし、挿入ソートを使って降順の数値を昇順に並べ替える場合は、選択ソートを使ってソートする場合と実行時間が同じになる可能性があります。
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
以下は、当該課題に対する教授からの指摘事項です。
</span>
</p>

<p>
<b>
<span>
- main関数以外の関数内で1,000,000個（4MB）のローカル変数を割り当てるのは非常に良くない方式・習慣である
</span>
<br>
<span>
- ローカル変数はオペレーティングシステムのスタックに入るが、スタックにはサイズ制限がある
</span>
<br>
<span>
- その関数が複数回呼び出されるとプログラムがクラッシュする
</span>
<br>
<span>
- そのように大きなものはグローバル変数にするか、mainに入れるか、さもなくばmalloc/freeを使用すること。
</span>
</b>
</p>
<p>
コード修正後にさらに詳しく調べてみた。
</p>

<p>
<b>
<span>
コード修正
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

int tempArray[1000001]={0,}; // コンテナ
void selection_sort(int argc, const char * argv[]){

    if ( argc &lt;= 2 ) /* ファイルとテストケース数の正確な実行のためにargcは2であるべき */
    {
        printf("引数を正しく入力してください (例. selection_sort hw1_input.txt 1000)\n");
        return;
    }

        // 正しい引数
        int i,j;
        int min,temp;
        FILE *file = fopen( argv[1], "r" ); // ファイルポインタを開く
        char number[11]; // ファイルObjを行ごとに読み取るための数値コンテナ
        int lineCounter=0; // 行チェック用
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // 整列されていない配列をintでセット
            lineCounter++;
        }
        fclose(file); // ファイルポインタを閉じる

        for (i=0; i&lt;maxCount; i++) {
            min = i; // 現在のインデックスを設定
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
    // ここにコードを挿入...
    clock_t start_time, end_time; // 時間変数宣言
    start_time = clock(); // 開始時間
    selection_sort(argc,argv);
    end_time = clock(); // 終了時間
    printf("実行時間 = %.1f ms\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC * 1000);

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
int tempArray[1000001]={0,}; // コンテナ
void insertion_sort(int argc, const char * argv[]){
    if ( argc &lt;= 2 ) /* ファイルとテストケース数の正確な実行のためにargcは2であるべき */
    {
        printf("引数を正しく入力してください (例. selection_sort hw1_input.txt 1000)\n");
        return;
    }

        // 正しい引数 > タスク実行 :)
        int i,j;
        int temp;
        FILE *file = fopen( argv[1], "r" ); // ファイルポインタを開く
        char number[11]; // ファイルObjを行ごとに読み取るための数値コンテナ
        int lineCounter=0; // 行チェック用
        int maxCount = atoi(argv[2]);
        while(fgets(number, sizeof(number), file)){
            if(lineCounter==maxCount){
                break;
            }
            tempArray[lineCounter] = atoi(number); // 整列されていない配列をintでセット
            lineCounter++;
        }
        fclose(file); // ファイルポインタを閉じる
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
    // ここにコードを挿入...
    clock_t start_time, end_time; // 時間変数宣言
    start_time = clock(); // 開始時間
    insertion_sort(argc,argv);
    end_time = clock(); // 終了時間
    printf("実行時間 = %.1f ms\n", ((double)(end_time-start_time)) / CLOCKS_PER_SEC * 1000);

    return 0;
}
</pre>



<p>
<font>
<b>
<span>
メモリ領域
</span>
</b>
</font>
</p>





<p>
<span>
私たちが特定の言語でコードを書いてコンパイルおよび実行すると、上記のようなメモリ構造に変数および関数が格納される。
</span>
</p>


<p class="바탕글">
<span>
<b>
<span>
データ領域 (Data Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
データ領域は、グローバル変数とstatic変数が割り当てられる領域である。この領域に割り当てられる変数は一般的にプログラムの開始と同時に割り当てられ、プログラムが終了して初めてメモリから消滅する。つまり、データ領域に割り当てられた変数はプログラムが終了するまで存在し続けるという特徴を持つ。グローバル変数とstatic変数の特徴と一致する部分である。
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
スタック領域 (Stack Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
スタック領域は、関数呼び出し時に生成されるローカル変数とパラメータが格納される領域である。この領域に割り当てられた変数は、関数呼び出しが完了すると消えるという特徴を持つ。これは他のメモリ領域とは明確に比較される特徴である。遅く割り当てられた変数のメモリが先に解除されるため、スタックの特徴と一致する。
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
ヒープ領域 (Heap Area)
</span>
</b>
</span>
</p>
<p class="바탕글">
<span>
ヒープ領域は、プログラマーが管理するメモリ領域である。つまり、プログラマーの必要に応じてメモリ空間が割り当ておよび消滅する領域である。動的割り当てによって生成されるメモリ領域である。
</span>
</p>

<p class="바탕글">
<span>
※ 静的に割り当てられる変数のメモリは、変数の特性によってデータまたはスタック領域に生成される。静的割り当てはコンパイル段階 (Compile-time) で全て行われる。ただし、コンパイル段階ではメモリのサイズを確保するだけで、変数の値は保存されない。このため、配列のサイズは定数でしか指定できないのである。変数値の保存はランタイム (Run-time) で行われ、ランタイム段階でメモリを生成しようとする際に使うのが動的割り当てである。
</span>
</p>

<p>
そうなると、ここで疑問が湧く...
</p>
<p>
ヒープとスタックがいっぱいになったらどうなるのだろうか？
</p>