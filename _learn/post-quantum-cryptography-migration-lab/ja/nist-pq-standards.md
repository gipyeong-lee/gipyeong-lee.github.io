---
layout: learn-module
title: ML-KEMおよびML-DSA標準の理解
course_slug: post-quantum-cryptography-migration-lab
course_data_key: post-quantum-cryptography-migration-lab-ja
course_locale: ja
lang: ja
ref: learn:post-quantum-cryptography-migration-lab:nist-pq-standards
translations:
- lang: ko
  url: /learn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: en
  url: /learn/en/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: ja
  url: /learn/ja/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-cn
  url: /learn/zh-cn/post-quantum-cryptography-migration-lab/nist-pq-standards/
- lang: zh-tw
  url: /learn/zh-tw/post-quantum-cryptography-migration-lab/nist-pq-standards/
module_id: m2
permalink: /learn/ja/post-quantum-cryptography-migration-lab/nist-pq-standards/
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
id: m2
slug: nist-pq-standards
phase_id: p1
estimated_hours: 8.0
prerequisites:
- m1
objectives:
- 格子暗号体系(Lattice-based cryptography)の数学的基礎と安定性の根拠を説明する。
- NIST標準ML-KEM(鍵カプセル化メカニズム)の動作原理を理解する。
- NIST標準ML-DSA(デジタル署名アルゴリズム)の構造的特性を把握する。
- 格子暗号が他の暗号方式(コードベース、ハッシュベース)と比較して実務的な利点を持つ理由を分析する。
worked_examples:
- '例 1: 格子ベースKEMのセキュリティ強度比較。ML-KEM-512, 768, 1024は、それぞれNISTセキュリティ強度 1, 3, 5 レベルに対応する。これは古典暗号のAES-128,
  192, 256と同様のセキュリティレベルを目標としている。'
- '例 2: モジュール格子(Module Lattice)概念の適用。ベクトルと行列を使用して演算を効率化することで、一般の格子よりパフォーマンスを最適化しつつセキュリティ強度を維持する。'
lab:
  title: ML-KEMおよびML-DSAアルゴリズム基礎実験
  steps:
  - liboqsをインストールし、環境変数を設定する。
  - サンプルPythonコードを使用してML-KEM鍵ペアの生成およびカプセル化プロセスを実行する。
  - ML-DSAを使用してメッセージに署名および検証を行うスクリプトを実行する。
  - 各演算に要する時間を測定して記録する。
  safety:
  - 実験用の仮想環境外のシステム証明書や実際の鍵ファイルにはアクセスしないこと。
  - liboqsライブラリは研究およびテスト用途でのみ使用し、運用環境のセキュリティソリューションと誤解しないこと。
  - 実験データはすべてローカル仮想環境内に保持し、外部ネットワークには送信しないこと。
  deliverables:
  - 演算時間測定データが含まれたCSVファイル
  - アルゴリズム実装体の実行結果キャプチャ
  - 実習プロセス要約ログ
assignment:
  title: 耐量子暗号標準分析レポート
  deliverables:
  - ML-KEMおよびML-DSAのアルゴリズム的特徴の要約表
  - 格子ベースシステムが実際の移行時に考慮すべきパフォーマンス上の制約(鍵サイズなど)の分析
  - 研究用ライブラリを活用したテストの限界点の記述
  rubric:
  - 標準アルゴリズムの数学的根拠を正確に記述しているか？
  - 格子ベースシステムの利点と限界を分析しているか？
  - セキュリティ脅威モデルに対する正しい理解を示しているか？
quiz:
- question: 格子ベースシステムが実務標準化を主導している主な理由として、次のうちどれが適切か？
  choices:
  - 最も短いセキュリティ履歴を持っているから
  - 最悪の事例から平均的な事例への換算が可能であり、効率的な実装が可能であるから
  - 量子アルゴリズムで容易に解くことができるから
  - コードベースの暗号のみを使用してセキュリティを極大化しているから
  answer_index: 1
  explanation: 格子ベースシステムは、強力な数学的換算根拠と効率的な実装可能性により、NIST標準化の中心にあります [S4]。
- question: ML-KEMが基盤としている数学的問題タイプは何か？
  choices:
  - 素因数分解問題
  - 楕円曲線離散対数問題
  - モジュール学習誤差問題(MLWE)
  - ハッシュ衝突問題
  answer_index: 2
  explanation: ML-KEMは、モジュール格子ベースの学習誤差(MLWE)問題を安全性の根拠としています。
completion_criteria:
- 理論学習確認用クイズに全問正解して合格すること
- 実験プロセスおよび測定データが含まれたレポートを提出すること
- 実習の安全指針を遵守し、隔離された環境でテストを実行したことを確認するチェックリストを提出すること
source_ids:
- S4
---

## ML-KEMおよびML-DSA標準の理解

### 1. 格子暗号の台頭
現在、実務的な標準化を主導しているのは格子ベース(Lattice-based)のシステムである。これには、最悪の事例(worst-case)から平均的な事例(average-case)への強力な数学的換算(reductions)が存在し、効率的な実装が可能であるためである [S4]。一方で、コードベース(Code-based)やハッシュベース(Hash-based)方式は保守的な錨(conservative anchors)の役割を果たし、より長いセキュリティ履歴や最小限の仮定のみを要求する特性を持つ [S4]。

### 2. ML-KEM (Module-Lattice Key Encapsulation Mechanism)
ML-KEMは、以前Kyberとして知られていたアルゴリズムに基づいている。モジュール格子問題(Module Learning With Errors, MLWE)に基づいており、次のような流れを持つ。
- **KeyGen:** モジュール格子内で公開鍵と秘密鍵を生成。
- **Encapsulation:** 公開鍵を使用して共有秘密値(Shared Secret)とカプセル化された鍵(Ciphertext)を生成。
- **Decapsulation:** 秘密鍵を使用してカプセル化された鍵から元の共有秘密値を復旧。

### 3. ML-DSA (Module-Lattice Digital Signature Algorithm)
ML-DSAはDilithiumに基づいており、「Fiat-Shamir with Aborts」技法を使用する。格子問題の困難さによって偽造耐性を提供し、署名サイズと公開鍵サイズのバランスを取った実用的な標準である。

### 4. セキュリティの仮定
格子ベースシステムの安全性は、最短ベクトル問題(Shortest Vector Problem, SVP)と密接に関連している。量子コンピュータの「ショアのアルゴリズム(Shor's Algorithm)」が既存のRSAやECCを効率的に破るのに対し、格子問題は量子アルゴリズムでも多項式時間内には解けないと仮定されている。
