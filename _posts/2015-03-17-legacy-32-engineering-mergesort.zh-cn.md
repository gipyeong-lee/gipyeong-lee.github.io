---
layout: post
title: "[数据结构] MergeSort (归并排序)"
description: "合并排序算法实现特点 1. 稳定的排序。 2. 因为需要额外的空间，所以不是in-place算法。 ** 所谓的in-place算法是指使用少量额外空间进行处理的算法。 (In-place is an algorit..."
date: 2015-03-17 01:39:12 +0900
section: blog
category: engineering
lang: zh-cn
ref: 2015-03-17-legacy-32-engineering-mergesort
tags:
  - "DataStructure"
  - "engineering"
translation_source_hash: a613ce6fc9191278d287a753b787b0502d82782d0bda2dbc7059131d382f85e8
---

<p>
<b>
<span>
合并排序算法实现
</span>
</b>
</p>

<p>
<b>
<span>
特点
</span>
</b>
</p>
<p>
<b>
1. 稳定的排序。
</b>
</p>
<p>
<b>
2. 因为需要额外的空间，所以不是in-place算法。
</b>
</p>
<p>
** 所谓的in-place算法是指使用少量额外空间进行处理的算法。
</p>
<p>
(In-place is an algorithm which transforms input using a data structure with a small, constant amount of extra storage space.)
</p>
<p>
来源：维基百科
</p>


<p>
<b>
<span>
实现关键点
</span>
</b>
</p>

<p>
1. 分割（直到无法再分割为止，通过“/2”索引不断分割） lgN
</p>
<p>
2. 合并（将分割后的值重新聚合。在聚合的同时比较值进行排序） N
</p>
<p>
速度 : N * lgN
</p>

<p>
以下是实现的源码。
</p>


<pre class="brush: c;toolbar:false">
/**
 * Algorithm Course
 *
 * Homework Assignement #3
 * - find number of inversions in an arr (from input file with integers)
 *
 * @student ID: A889056
 * @name      : GiPyeongLee
 * @.agents/skills/caveman-compress/scripts/validate.py      : 2015.03.16
 **/

#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
#include "errno.h"
#include "sys/time.h"

#define MAX_NUM 1000000
unsigned long cnt = 0;

void seperate(int *arr,int left,int right);
void merge(int *arr,int left,int mid,int right);
void count_inversion (int *data, int left, int right) {
    seperate(data,left,right); // seperate and merge
}
void seperate(int *arr,int left,int right){
    if(left &lt; right){
        int mid;
        mid=(left+right)/2;
        seperate(arr,left,mid);
        seperate(arr,mid+1,right);
        merge(arr,left,mid,right);
    }
}
void merge(int *arr,int left,int mid,int right){
    int tempArr[right-left+1];
    int pos=0,lpos = left,rpos = mid + 1;
    while(lpos &lt;= mid &amp;&amp; rpos &lt;= right)
    {
        if(arr[lpos] &lt; arr[rpos])
        {
            tempArr[pos++] = arr[lpos++];
        }
        else
        {
            cnt+=(mid-lpos+1);
            tempArr[pos++] = arr[rpos++];

        }
    }
    while(lpos &lt;= mid)  tempArr[pos++] = arr[lpos++];
    while(rpos &lt;= right)tempArr[pos++] = arr[rpos++];
    int iter;
    // iterator to pos , tempArr to arr.
    for(iter = 0;iter &lt; pos; iter++)
    {
        arr[iter+left] = tempArr[iter];
    }
    return;
}

int main(int argc, char *argv[]) {
    char *filename;
    FILE *fp;
    char str[10];
    int number;
    unsigned int N;
    int data[MAX_NUM] = {};
    clock_t start_time,end_time;


    if (argc &gt; 1) {
        filename = argv[1];
    } else {
        printf("no input file argument\n");
        return -1;
    }

    if ((fp = fopen(filename, "r")) == NULL) {
        printf("Error opening input file\n");
        return -1;
    }

    while (fgets(str, 10, fp) != NULL) {
        if (N &gt;= MAX_NUM) {
            printf("too many data\n");
            break;
        }
        number = strtol(str, NULL, 10);
        if (errno == EINVAL)
            break;
        data[N] = number;
        N++;
    }
    start_time=clock();
    printf("INPUT : Number of data     N = %d\n", N);

    count_inversion(data, 0, N - 1);

    printf("OUTPUT: Number of inversions = %lu\n", cnt);

    end_time = clock();

    printf("running time = %f seconds\n",((double)(end_time-start_time))/CLOCKS_PER_SEC);

    return 0;
}
</pre>


<p>
通过上面的合并排序完成了作业，该作业的目的是计算逆序对的总数。
</p>

<p>
使用上面的源码，可以得到以下结果。
</p>


<span class="txt_fold">
查看更多
</span>
<div class="moreless_content">

<pre>
<br class="Apple-interchange-newline">
<span>
$ ./count_inversions hw3_input_10k.txt
INPUT : Number of data     N = 10000
OUTPUT: Number of inversions = 23948130
running time = 0.002207 seconds
$
$ ./count_inversions hw3_input.txt
INPUT : Number of data N = 100000
OUTPUT: Number of inversions = 2407905288
running time = 0.019184 seconds
$
$ ./count_inversions hw3_input_1000k.txt
INPUT : Number of data     N = 1000000
OUTPUT: Number of inversions = 249953281796
running time = 0.227101 seconds
</span>
</pre>


</div>