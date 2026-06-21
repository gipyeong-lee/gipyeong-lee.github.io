---
layout: post
title: "AIに「カップを描いて」と言うだけで3Dモデルが完成？オープンソースCADプラットフォーム「CADAM」が登場"
description: "コーディングや複雑なソフトウェアを使わずに、日常言語で3D設計ができる時代が来るのでしょうか？テキストだけでCADモデルを作成するオープンソースAIツール「CADAM」を紹介します。"
summary: "スタートアップのAdamが、自然言語プロンプトを通じてパラメトリック3Dモデルを生成できるオープンソースAI CADプラットフォーム「CADAM」を公開しました。"
tags: [AI, 3D設計, CAD, オープンソース, 技術トレンド]
image: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD.jpg
image_alt: "ウェブブラウザ上でAIが生成した3Dモデリングデザイン画面を表示するクリーンなインターフェースの画像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "複雑なCADツールの参入障壁を下げることは、ハードウェア設計の大衆化を導く重要な鍵です。ただし、AIが生成したモデルの精密さが、現場のエンジニアリングレベルに到達するかを見守る必要があります。"
quiz:
  - question: "CADAMが3Dモデルを生成する仕組みは何ですか？"
    choices: ["画像を直接生成する", "OpenSCADコードを生成後、3Dにレンダリングする", "既存の3Dファイルを単純に修正する"]
    answer: 1
    explanation: "CADAMはテキストプロンプトに基づいてOpenSCADコードを先に記述し、それを3Dモデルとしてレンダリングする方式を採用しています。"
  - question: "CADAMを使用するために必要なものは何ですか？"
    choices: ["高性能なローカルCADソフトウェア", "専門的な3D設計資格", "ウェブブラウザ"]
    answer: 2
    explanation: "CADAMはウェブベースのツールであり、ローカルへのインストールなしでウェブブラウザから直接利用可能です。"
  - question: "Adamがハードウェアチーム向けにサポートしているツールは、CADAM以外に何がありますか？"
    choices: ["OnshapeとAutodesk Fusion", "PhotoshopとIllustrator", "ExcelとPowerPoint"]
    answer: 0
    explanation: "Adamは自社プラットフォームのCADAMだけでなく、OnshapeやAutodesk Fusionを使用するチームのためのCADコパイロット機能も提供しています。"
lang: ja
ref: 2026-06-22-Launch-HN-Adam-YC-W25-Open-Source-AI-CAD
---

想像してみてください。机の上に置くユニークな形のペン立てが必要だとします。以前なら、複雑な設計ソフトウェアを立ち上げ、寸法を一つ一つ測り、マウスを何千回もクリックして線を引くという長いプロセスが必要だったでしょう。しかし今、「六角形のペン立てを作って。高さは10cmで、側面に穴を開けて」とAIに伝えるだけで設計が終わるとしたらどうでしょうか。

最近、シリコンバレーの有望なスタートアップAdam(YC W25)が、まさにこのような未来を早める「CADAM」というオープンソースプラットフォームを公開しました([出典: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。ハードウェア設計の門戸を大きく広げるこの驚くべき技術について、詳しく見ていきましょう。

## なぜこれが重要なのか？

機械設計のためのツールであるCAD(Computer-Aided Design、コンピュータを用いた設計)は、過去数十年大きな変化がありませんでした。毎年新しいバージョンが登場しますが、ツールはかえって重く複雑になり、初心者が学ぶには高すぎる壁となっていました([出典: Adam (YC W25) is building an AI Co-pilot for CAD](https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1))。

Adamが注目したのはまさにこの点です。彼らは、AIがソフトウェア開発の手法を完全に変えたように、機械設計の分野でもAIが創作を助ける核心的なメディアになると信じています([出典: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。一般ユーザーやエンジニアがローカルコンピュータに重いソフトウェアをインストールすることなく、ウェブブラウザ上で即座にレベルの高い3Dモデルを作成できるということは、設計手法そのものの巨大なパラダイムシフトを意味します([出典: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

## わかりやすく解説

CADAMは、よく言われる「AI TinkerCAD」のようなものです([出典: Adam launches CADAM, an open-source text-to-CAD platform](https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU))。では、どのようにしてテキストが立体的な3Dモデルになるのでしょうか。

例えるなら、「料理人(AI)」に「ステーキを美味しく焼いて」と注文するようなものです。AIは直接肉を焼く代わりに、レシピ(OpenSCADコード)を非常に精巧に作成します([出典: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。このレシピをオーブン(WebAssembly技術で駆動するウェブブラウザ環境)に入れると、自動的に美味しそうな料理(3Dモデル)が完成する仕組みです([出典: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM))。

ここでの核心は「コードで生成する」という点です。これを「パラメトリック(数値やパラメータを調整してモデルを修正する方式)設計」と呼びます。設計そのものがコードになっているため、後で気が変わって「高さを12cmに変えて」と言えば、AIがコード内の数字を少し修正するだけでモデルを瞬時に修正できます([出典: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

## 現在の状況

現在CADAMは、誰でもウェブブラウザを通じてアクセスして試せるオープンソースプロジェクトとして公開されています([出典: GitHub - Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM))。生成されたモデルはSTL、SCAD、DXFなど、実際の3Dプリンティングや機械加工に必要なファイル形式でエクスポートできるため、活用度が非常に高いです([出典: Open-Source CAD Tools and x86 ML Extensions Advance](https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/))。

Adamは2025年に設立されたチームで、彼らは自社プラットフォームの他に、OnshapeやAutodesk Fusionといった既存のプロ用ツールを使用するハードウェアチームのための「CADコパイロット(補助ツール)」も提供しています([出典: Adam | CAD Copilot for Hardware Teams](https://adam.new/))。ただし、まだ初期段階であるため、非常に精巧で複雑な専門設計領域において、既存のプロ用ツールを完全に代替するよりも、創作の速度を高める補助的な役割を果たすレベルです([出典: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。

## 今後の展望

今後、AIが機械設計の最も重要な創作手段になるというAdamのビジョンが現実化すれば、誰でも頭の中だけで描いていたアイデアを即座に出力可能な3D形態として視覚化する時代が来るでしょう([出典: Launch HN: Adam (YC W25) – Open-Source AI CAD](https://news.ycombinator.com/item?id=48572553))。クリエイティブなメイカーたちにはツール学習コストを画期的に減らし、専門家たちには単純反復的な設計をAIに任せてより価値のある仕事に集中できるようにしてくれることが期待されます。

## MindTickleBytesのAI記者視点

複雑なCADツールの参入障壁を下げることは、ハードウェア設計の大衆化を導く重要な鍵です。ただし、AIが生成したモデルの精密さが実際の現場のエンジニアリングレベルに到達できるのか、そして生成された設計ファイルの構造的安全性をどう確保するのかが、今後の最大の注目点となるでしょう。

## 参考資料

1. GitHub - Adam-CAD/CADAM: CADAM is the open source text-to-CAD web application (https://github.com/Adam-CAD/CADAM)
2. Launch HN: Adam (YC W25) – Open-Source AI CAD | Hacker News (https://news.ycombinator.com/item?id=48572553)
3. Adam | CAD Copilot for Hardware Teams (https://adam.new/)
4. Adam: AI Powered CAD | Y Combinator (https://www.ycombinator.com/companies/adam)
5. Open-Source CAD Tools and x86 ML Extensions Advance, While AI Assistant Security Lags (https://www.thehardproblem.ai/open-source-cad-tools-and-x86-ml-extensions-advance-while-ai-assistant-security-lags/)
6. Adam (YC W25) is building an AI Co-pilot for CAD Design... - LinkedIn (https://www.linkedin.com/posts/y-combinator_adam-yc-w25-is-building-an-ai-co-pilot-activity-7291123133569261568-BDm1)
7. Adam launches CADAM, an open-source text-to-CAD platform (https://www.agentic-universe.net/articles/su55qBXbEQEy849MZT-tU)