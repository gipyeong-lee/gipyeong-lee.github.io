---
layout: post
title: "我完成了生平第一个 Dapp。"
description: "大家好，我是 Slow Thinking。我进行了一个月左右的开发。如果没有 AI，我可能无法完成。这是我这个懒人选择的方法：在 Visual Studio Code 的左右面板中分别设置 Codex 和 Claude Code。当遇到 Token 限制时，就轮流使用。以下是这两个工具的对比表，供参考。"
date: 2025-10-18 20:57:34 +0900
section: blog
category: web3
lang: zh-cn
ref: 2025-10-18-legacy-391-web3-dapp
tags:
  - "Ai"
  - "Claude"
  - "Codex"
  - "DAPP"
  - "项目"
  - "项目集合"
translation_source_hash: 80e0e93d306232af16e6f6d408598d3b9b8be3d0a9bae18b179452ac9bae1aa4
---

<p>
大家好，我是 Slow Thinking。
</p>
<p>
我进行了一个月左右的开发。
</p>
<p>
如果没有 AI，我可能无法完成。
</p>
<p>
这是我这个懒人选择的方法：
</p>

<p>
在 Visual Studio Code 的左右面板中分别设置 Codex 和 Claude Code。
</p>
<p>
当遇到 Token 限制时，就轮流使用。以下是这两个工具的对比表，供参考。
</p>

<table>
<tbody>
<tr>
<td>
<b>
项目
</b>
</td>
<td>
<b>
Codex CLI (OpenAI)
</b>
</td>
<td>
<b>
Claude Code CLI (Anthropic)
</b>
</td>
</tr>
<tr>
<td>
<b>
计划名称
</b>
</td>
<td>
ChatGPT Plus (每月 $20) 内含 Codex CLI
</td>
<td>
Claude Pro (每月 $20)
</td>
</tr>
<tr>
<td>
<b>
会话限制方式
</b>
</td>
<td>
约
<b>
5小时滚动窗口
</b>
(每5小时重置使用量)
</td>
<td>
约
<b>
5小时滚动窗口
</b>
(每5小时重置)
</td>
</tr>
<tr>
<td>
<b>
会话限额 (粗略)
</b>
</td>
<td>
约 30 ~ 150 条本地消息或 5 ~ 40 个云端任务
</td>
<td>
约 45 条消息或 10 ~ 40 个提示级别
</td>
</tr>
<tr>
<td>
<b>
周累计限额
</b>
</td>
<td>
存在
<b>
共享周配额 (weekly quota)
</b>
(官方数据未公开)
</td>
<td>
存在约
<b>
7天为单位
</b>
重置的周限额
</td>
</tr>
<tr>
<td>
<b>
重置时间点 (会话)
</b>
</td>
<td>
首次请求后5小时自动重置
</td>
<td>
首次提示后5小时自动重置
</td>
</tr>
<tr>
<td>
<b>
重置时间点 (每周)
</b>
</td>
<td>
约
<b>
一周
</b>
周期重置 (确切时间未公开)
</td>
<td>
约
<b>
7天
</b>
后重置 (各账户时间不同)
</td>
</tr>
<tr>
<td>
<b>
Token 上下文窗口
</b>
</td>
<td>
约
<b>
192,000 Token
</b>
(推测为输入 + 输出 + 历史记录总和)
</td>
<td>
约
<b>
200,000 Token
</b>
(基于 Pro 版)，最高 500,000 (企业版)
</td>
</tr>
<tr>
<td>
<b>
基础模型
</b>
</td>
<td>
GPT-4 Turbo (代码解析模式)
</td>
<td>
Claude 3 Sonnet (编码模式)
</td>
</tr>
<tr>
<td>
<b>
超出时消息
</b>
</td>
<td>
“Usage limit reached. Try again in X hours.”
</td>
<td>
“You’ve hit your limit. Resets in ~X hours.”
</td>
</tr>
<tr>
<td>
<b>
重置方式
</b>
</td>
<td>
自动滚动重置 (不可手动初始化)
</td>
<td>
自动滚动重置 (5小时后刷新会话)
</td>
</tr>
<tr>
<td>
<b>
附加特征
</b>
</td>
<td>
- 区分本地与云端任务 - 包含代码执行功能
</td>
<td>
- 可通过 /clear、/compact 命令缩减上下文 - 支持以 Sonnet 4 为中心模型
</td>
</tr>
<tr>
<td>
<b>
官方来源示例
</b>
</td>
<td>
<a href="https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan">
help.openai.com
</a>
</td>
<td>
<a href="https://claudelog.com/faqs/claude-code-usage/">
claudelog.com
</a>
/
<a href="https://portkey.ai/blog/claude-code-limits/">
portkey.ai
</a>
</td>
</tr>
</tbody>
</table>

<p>
以下是关于本次 Project L 的信息：
</p>


<table>
<tbody>
<tr>
<td>
<b>
项目名称
</b>
</td>
<td>
Project L
</td>
</tr>
<tr>
<td>
<b>
开发语言
</b>
</td>
<td>
Rust (链上程序) + TypeScript (客户端 / 前端)
</td>
</tr>
<tr>
<td>
<b>
平台
</b>
</td>
<td>
Solana 区块链 (Anchor Framework)
</td>
</tr>
<tr>
<td>
<b>
开发周期
</b>
</td>
<td>
2025.09.29 ~ 2025.10.18 (总计 19 天，38 小时)
</td>
</tr>
<tr>
<td>
<b>
主要目标
</b>
</td>
<td>
在 Solana 网络上完成智能合约部署及客户端联动
</td>
</tr>
<tr>
<td>
<b>
依赖关系图 (Dependency Graph)
</b>
</td>
<td>
总计 2,130 个依赖 (包含软件包、模块、构建依赖)
</td>
</tr>
</tbody>
</table>

<p>
开发已完成，目前正在进行自测 (self QA)。
</p>
<p>
之后计划进行发布。
</p>

<hr>

<blockquote>
<s>
devnet QA - 已完成
</s>
<br>
testnet QA -
<b>
进行中
</b>
<br>
主网部署 (Deploy on mainnet) - 待办
</blockquote>