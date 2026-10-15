---
layout: learn-module
title: 量子脅威と格子暗号
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
ref: learn:post-quantum-cryptography-migration-lab:quantum-threat-model
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/quantum-threat-model/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/quantum-threat-model/
module_id: m1
permalink: /learn/ja/post-quantum-cryptography-migration-lab/quantum-threat-model/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: e5164bbefc324eff94b7957c62695f66
translation_run_id: 180bcdae1f304308ae765fa770418d34
primary_category: ai-software
topics:
- post-quantum-cryptography
- cryptographic-inventory
- ml-kem
- ml-dsa
- crypto-agility
course_type: academic
published_at: '2026-10-16T00:55:40.127560+09:00'
id: m1
slug: quantum-threat-model
phase_id: p1
estimated_hours: 8.0
prerequisites: []
objectives:
- 量子コンピュータが現代暗号体系(RSA, ECC)に与える脅威モデルを理解する。
- 格子暗号(Lattice-based Cryptography)の数学的基礎と安定性の根拠を分析する。
- NISTが推奨する耐量子暗号標準(ML-KEM, ML-DSA)の設計原理を学習する。
- 格子ベースアルゴリズムの効率およびセキュリティ特性(worst-case hardness)を記述する。
worked_examples:
- '例 1: 量子コンピュータがRSAに与える影響分析 - RSAは大きな数の素因数分解の難易度に基づいている。ショアのアルゴリズムは、nビットの整数を素因数分解する複雑度を指数時間から多項式時間に短縮することで、暗号文を即座に解読する。'
- '例 2: 格子ベース難題(LWE)概念の理解 - 秘密ベクトルsと誤差eを加えた線形方程式系 A*s + e = t を考慮する。格子暗号は、行列Aと結果tからsを見つけ出すことが困難であるという「Learning
  With Errors」問題の難易度に基づいている。'
lab:
  title: 格子暗号基礎環境の構築および可視化
  steps:
  - 隔離されたLinux/Docker環境にてPython 3 仮想環境を作成
  - liboqsライブラリのインストールおよびコンパイル
  - 格子ベースLWE問題のパラメータ変化による鍵サイズおよび演算時間の収集スクリプト作成
  - データ分析および可視化ノートブックの実行
  safety:
  - すべての実験は隔離されたローカル仮想環境内で行うこと
  - 実際の運用証明書、秘密鍵、顧客データの使用を厳禁する
  - 研究用ライブラリを実際のサービスセキュリティ手段と見なさないこと
  deliverables:
  - 環境設定ログおよびコンパイル結果物
  - アルゴリズムパフォーマンス(鍵サイズ、時間)比較分析データ
  - 格子暗号特性レポート
assignment:
  title: 量子脅威分析レポートの作成
  deliverables:
  - 量子脅威モデルおよび格子暗号理論のまとめ文書
  - 主要PQCアルゴリズム(ML-KEM, ML-DSA)比較表
  rubric:
  - ショアのアルゴリズムの原理を正確に説明している
  - 格子暗号の最悪ケースの難題(worst-case hardness)概念を論理的に記述している
  - 提示されたソース [S3, S4] に基づき、現代暗号が直面する課題を記述している
quiz:
- question: ショアのアルゴリズム(Shor's algorithm)が既存のPKIに与える脅威は何か？
  choices:
  - すべての対称鍵暗号を無条件に解読する。
  - 素因数分解および離散対数問題を多項式時間内に解決する。
  - ハッシュ関数の衝突耐性を完全に排除する。
  - 量子コンピュータの処理速度を低下させる。
  answer_index: 1
  explanation: ショアのアルゴリズムは、RSAの基盤である素因数分解とECCの基盤である離散対数問題を多項式時間内に解決することで、既存の公開鍵暗号体系を脅かします。
- question: 格子暗号(Lattice-based Cryptography)が有望な理由は何か？
  choices:
  - 最悪ケースの難題を平均的なケースの難題に換算できるからである。
  - すべての対称鍵暗号よりはるかに高速であるからである。
  - 量子コンピュータでも絶対に解くことができないからである。
  - コンピュータメモリをまったく使用しないからである。
  answer_index: 0
  explanation: 格子暗号は、最悪ケースの難題(worst-case hardness)から平均的なケース(average-case)のセキュリティを保証する数学的利点を持っています
    [S4]。
completion_criteria:
- 理論学習完了および量子脅威レポート提出
- 実習環境にてliboqsを用いた基礎アルゴリズムの実行に成功
- クイズ項目ごとに 80% 以上の正解率を達成
source_ids:
- S3
- S4
---

## 量子脅威モデル
現代の公開鍵暗号(PKI)は主に、素因数分解(RSA)と離散対数問題(ECC)という困難な難題に依存している。ショアのアルゴリズム(Shor's algorithm)は、量子コンピュータを使用して多項式時間内にこれらの問題を解決できる。これは事実上、現在のすべての標準PKIを無力化することを意味する[S3]。

## 格子暗号 (Lattice-based Cryptography)
格子暗号は、高次元空間内において格子の基底ベクトルから特定の点を探索する問題(例: SVP, LWE)を難題として使用する。これらの問題は最悪のケース(worst-case)でも解くのが困難であることが証明されており、平均的なケース(average-case)でもセキュリティが保証される[S4]。

## 耐量子標準 (ML-KEM/ML-DSA)
- **ML-KEM (Module-Lattice-based Key-Encapsulation Mechanism):** 鍵カプセル化メカニズムであり、効率的な実装とともに格子ベースの難題を使用して耐量子性を提供する。
- **ML-DSA (Module-Lattice-based Digital Signature Algorithm):** 電子署名標準であり、格子ベースの数学的構造を使用して強力な署名の整合性を保証する。
格子ベースのシステムは、現在標準化の過程において強力なworst-case to average-caseの換算性と効率的なパフォーマンスを立証しており、PQC移行の中心となっている[S4]。
