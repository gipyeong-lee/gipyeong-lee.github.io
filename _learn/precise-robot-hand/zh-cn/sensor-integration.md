---
layout: learn-module
title: 传感器集成与反馈控制
course_slug: precise-robot-hand
course_data_key: precise-robot-hand.zh-cn
course_locale: zh-cn
lang: zh-cn
ref: learn:precise-robot-hand:sensor-integration
translations:
- lang: ko
  url: /learn/precise-robot-hand/sensor-integration/
- lang: en
  url: /learn/en/precise-robot-hand/sensor-integration/
- lang: ja
  url: /learn/ja/precise-robot-hand/sensor-integration/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/sensor-integration/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/sensor-integration/
module_id: M8
permalink: /learn/zh-cn/precise-robot-hand/sensor-integration/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: e8f8435646734ebd8e061d010c356c2d
id: M8
slug: sensor-integration
phase_id: P3
estimated_hours: 10.0
prerequisites:
- M7
objectives:
- 理解使用 FSR 402 传感器和 10 kΩ 电阻构建分压电路的原理
- 熟悉 OpenCR 控制器的 ADC 功能及输入范围（0-3.3 V）限制条件
- 掌握传感器数据的滤波和校准技术
- 实现基于反馈的抓取控制算法，并进行机械手接触力控制实验
worked_examples:
- '示例 1: 计算 FSR 输出。当 $R_{FSR}$ 为 5 kΩ，$R_{fixed}$ 为 10 kΩ，输入 3.3 V 时，$V_{out} = 3.3
  \times (5 / (5 + 10)) = 1.1 V。该值正常位于 ADC 输入范围（0-3.3 V）内。'
- '示例 2: 抓取力校准。如果传感器值因噪声而波动，应用简单移动平均滤波器可以减少传感器值的剧烈变动，从而稳定地保持抓取力。'
lab:
  title: 指尖 FSR 传感器电路构建与校准
  steps:
  - 将 OpenCR 的 3.3 V 传感器轨和 GND 连接到面包板。
  - 将 FSR 402 与 10 kΩ 电阻串联，构建分压电路 [B4, B5]。
  - 将分压节点连接到 OpenCR 的 ADC 引脚 [B2]。
  - 连接 PC 与 OpenCR，运行读取传感器值的测试代码。
  - 记录无负载状态和施加目标力时的 ADC 值，并编制校准表。
  safety:
  - 通电前，务必使用万用表检查 3.3 V 轨与 12 V 执行器轨是否短路 [B2]。
  - 必须始终佩戴护目镜，通电期间请勿将手放入机械手的活动范围内。
  - 若检测到异常发热、异味或烟雾，请勿靠近。从危险区域外使用指定的楼宇配电盘断路器或经认证的上游主断路器切断 3 个适配器的电源后再撤离。如果没有可在危险区域外操作的上游断路手段，则禁止为系统通电。解除力矩并不能替代断电。维护和靠近操作仅限在计划停机、物理分离并确认无源测量后方可进行。
  - 修理或靠近传感器前，请物理分离 3 个绝缘电源适配器，并测量确认所有分支电压低于 1 V。
  deliverables:
  - ADC 传感器读取测试结果数据
  - 传感器校准表（ADC 值 vs 物理力）
  - 传感器数据滤波实现代码
assignment:
  title: 抓取力反馈控制算法实现
  deliverables:
  - 反馈控制代码（传感器读取、目标比较、电机力矩调整）
  - 抓取测试结果图（时间 vs 力）
  - 最终报告（控制逻辑说明及抓取稳定性分析）
  rubric:
  - ADC 数据是否在 0-3.3 V 范围内稳定测量？
  - 当传感器值达到目标值时，电机是否能适当地解除或保持力矩？
  - 紧急情况下，力矩解除是否能通过软件正常运作？
  - 报告中是否记录了断电确认流程？
quiz:
- question: 将 FSR 分压信号输入 OpenCR 控制器的 ADC 引脚时，必须遵守的事项是什么？
  choices:
  - 使用 12 V 执行器电源轨。
  - 仅使用 3.3 V 传感器电源轨。
  - 使用 5 V 电源轨。
  - 由外部另外供电。
  answer_index: 1
  explanation: OpenCR 的 ADC 输入范围为 0-3.3 V，为防止施加超出此范围的电压，必须仅使用 3.3 V 传感器电源轨。
- question: FSR 传感器的电阻值变化与物理力之间的关系是什么？
  choices:
  - 压力增加，电阻值增加。
  - 压力增加，电阻值减小。
  - 压力变化与电阻值无关。
  - 压力增加，电阻值按固定比例放大。
  answer_index: 1
  explanation: FSR 是一种压敏电阻，其特性是在施加压力时传感器电阻值会减小。
- question: 在机械手原型工作中，为维护或靠近而断电后，必须确认的安全状态是什么？
  choices:
  - 确认已通过软件解除力矩。
  - 用万用表测量保险丝是否熔断。
  - 物理分离 3 个电源适配器，并用直流电压档测量各分支电压是否低于 1 V。
  - 关闭电源开关后，用电阻档测量导线状态。
  answer_index: 2
  explanation: 断电是指物理分离 3 个电源，为了安全，必须使用万用表的直流电压档直接确认所有分支电压低于 1 V。
completion_criteria:
- 通过 ADC 读取 FSR 值的练习
- 抓取力反馈控制代码达到目标值的 90% 以上
- 证明遵守所有安全守则（物理断电及电压测量）
- 提交最终结果报告
source_ids:
- S3
- S12
- S26
---

## 传感器集成与接触力反馈

机械手的精密抓取控制始于准确测量作用于指尖的力。FSR 402 传感器是一种力敏电阻，其电阻值随施加压力的增加而减小 [S12]。为了将其转换为微控制器可读取的电压信号，需要分压电路。

### 1. 分压电路
将 FSR 传感器与 10 kΩ 分压电阻串联，并提供 3.3 V 传感器电源 [B4, B5, B2]。ADC 引脚连接在传感器和电阻的交点处，输出电压 $V_{out}$ 计算如下：
10 kΩ 下拉分压器使用 $V_{out}=V_{ref}\frac{R_{fixed}}{R_{FSR}+R_{fixed}}$

- OpenCR 控制器的 ADC 具有 12 位分辨率，输入范围限制在 0~3.3 V [B2]。超过此范围的输入可能会损坏电路元件，因此必须仅使用指定的传感器电源轨（3.3 V） [B2]。

### 2. 控制环路与反馈
测得的力数据用作 PID 控制算法或自适应控制策略的输入值 [S3]。当机械手抓取物体时，肌腱驱动电机 (DYNAMIXEL XM430-W350-T) 参考传感器值微调力矩，直至达到设定的目标接触力 [B1, B4]。
