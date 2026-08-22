---
layout: post
title: "[자료구조] MergeSort"
description: "합병정렬 알고리즘 구현 특징 1. Stable 한 정렬이다. 2. 추가적인 공간이 필요하므로 in-place algorithm 형식이 아니다. ** in-place algorithm 이란 적은 공간으로 처리하는 알고리즘을 의미한다고 한다. (In-place is an algorit..."
date: 2015-03-17 01:39:12 +0900
section: blog
category: engineering
lang: ko
ref: 2015-03-17-legacy-32-engineering-mergesort
tags:
  - "DataStructure"
  - "engineering"
---

<p>
<b>
<span>
합병정렬 알고리즘 구현
</span>
</b>
</p>

<p>
<b>
<span>
특징
</span>
</b>
</p>
<p>
<b>
1. Stable 한 정렬이다.
</b>
</p>
<p>
<b>
2. 추가적인 공간이 필요하므로 in-place algorithm 형식이 아니다.
</b>
</p>
<p>
** in-place algorithm 이란 적은 공간으로 처리하는 알고리즘을 의미한다고 한다.
</p>
<p>
(In-place is an algorithm which transforms input using a data structure with a small, constant amount of extra storage space.)
</p>
<p>
출처: 위키피디아
</p>


<p>
<b>
<span>
구현 KEY POINT
</span>
</b>
</p>

<p>
1. 분할을 한다 ( 더이상 쪼갤 수 없을 때까지 "/2" 로 인덱스를 나누어 계속 쪼갠다. ) lgN
</p>
<p>
2. 병합한다. ( 쪼개어진 값들을 다시 뭉친다. 뭉치면서 값을 비교하여 정렬한다. ) N
</p>
<p>
속도 : N * lgN
</p>

<p>
아래는 구현한 코드이다.
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
 * @date      : 2015.03.16
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
위의 합병정렬을 통해 과제가 나왔고 해당 과제는 Inversion 된 값들의 총 경우의 수들을 구하는 것이다.
</p>

<p>
위 소스를 이용하여 다음의 결과를 얻을 수 있었다.
</p>


<span class="txt_fold">
더보기
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
