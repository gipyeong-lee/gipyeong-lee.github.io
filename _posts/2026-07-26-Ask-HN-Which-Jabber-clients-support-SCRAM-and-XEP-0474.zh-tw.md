---
layout: post
title: "登入即時通訊軟體，擔心被駭嗎？為什麼 XEP-0474 至關重要"
description: "深入了解在 XMPP 即時通訊中，防止登入過程安全威脅的 XEP-0474 技術與 SCRAM+ 認證機制。"
summary: "介紹 XMPP 安全標準 XEP-0474 的重要性，該標準能防禦強制降低登入安全設定的駭客攻擊。"
tags: [安全, XMPP, Jabber, 隱私保護, 科技]
image: 2026-07-26-Ask-HN-Which-Jabber-clients-support-SCRAM-and-XEP-0474.jpg
image_alt: "象徵數位鎖與網路連線的抽象圖形"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "即時通訊的安全核心，不僅在於加密，更在於阻斷連線過程中發生的欺騙行為。雖然使用者難以親自驗證技術規格，但只要選擇安全的服務，就能獲得顯著的安全效益。"
quiz:
  - question: "XEP-0474 技術的主要目的是什麼？"
    choices: ["提升即時通訊速度", "防止登入時遭受強制降低安全設定的攻擊", "新增訊息傳遞方式"]
    answer: 1
    explanation: "XEP-0474 是一項能防禦在即時通訊登入交握過程中，強制降低安全等級的「降級攻擊」之技術。"
  - question: "僅使用 PLAIN 認證方式會產生什麼問題？"
    choices: ["認證速度太慢", "安全性僅依賴 TLS 通道，易遭受攻擊", "不支援行動裝置"]
    answer: 1
    explanation: "如果伺服器與用戶端僅支援 PLAIN 認證，安全性將完全依賴底層的 TLS 通道，導致認證方式或通道繫結容易遭受強制降級攻擊。"
  - question: "目前確認支援 XEP-0474 的工具有哪些？"
    choices: ["網頁瀏覽器", "go-sendxmpp", "電子郵件用戶端"]
    answer: 1
    explanation: "命令列工具「go-sendxmpp」從 0.14.1 版本開始，即支援 XEP-0474 與現代化的 SCRAM 認證方式。"
lang: zh-tw
ref: 2026-07-26-Ask-HN-Which-Jabber-clients-support-SCRAM-and-XEP-0474
---

想像一下。您正準備進入一個擁有堅固大門的保險庫，也就是您的即時通訊帳號。突然間，中間出現了一個人對您低語：「這個保險庫太複雜了，用簡單點的方法進去吧」。當您一時糊塗選擇了較為鬆散的密碼方式時，早已守候在此的駭客便順勢打開了大門。

這正是我們使用的即時通訊軟體，特別是基於 XMPP 協定（一種 XML 基礎的即時通訊規格，也稱為 Jabber）[出處 Wikipedia](https://en.wikipedia.org/wiki/XMPP) 的應用程式，在登入過程中可能遭遇的真實風險。近期為了因應這個問題，出現了一項名為 **XEP-0474** 的技術，讓我們簡單地深入了解它。

## 為什麼這很重要？

使用即時通訊時，僅僅加密訊息是不夠的。如果軟體與伺服器建立首次連線的「登入交握（連線確認過程）」階段不安全，心懷不軌的攻擊者便可能在中間攔截，試圖強制將安全設定調降至最低等級，發動所謂的「降級攻擊（Downgrade Attack）」。[出處 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.pdf)

若攻擊成功，強大的安全保護機制就會被解除，您的對話內容或帳號資訊將直接暴露於風險之中。XEP-0474 正是為了防禦這類攻擊，作為一種防禦盾牌，確保您設定的最強安全機制不會被強制解除。[出處 Mitigating the Hetzner/Linode XMPP.ru MitM interception incident](https://www.devever.net/~hl/xmpp-incident-2)

## 簡單來說

您可以將 XEP-0474 視為「安全的防護帶」。開車時若沒有安全帶，發生事故會造成嚴重傷害；同理，在即時通訊登入時，這條能阻擋認證安全降級攻擊的防護帶也是必不可少的。

打個比方。當您要連線至伺服器時，即便您說「我想用最新安全方式（如 SCRAM-SHA-256）登入」，中間的攻擊者也可能攔截這條訊息，並向伺服器謊稱「使用者只想用舊式方式（PLAIN 認證）登入」。

如果伺服器與用戶端都只支援舊式的「PLAIN 認證」，那麼安全性最終將只依賴於一層薄弱的 TLS（資料保護通訊規格）。[出處 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.pdf) XEP-0474 能偵測到這種詭計，並立即阻斷中間人試圖攔截並降低安全設定的企圖。[出處 Prosody Community Modules](https://modules.prosody.im/xeps.html)

## 目前進度如何？

目前 XMPP 即時通訊生態圈正努力引入這項安全標準。例如，命令列工具「go-sendxmpp」從 0.14.1 版本起，就已開始支援 XEP-0474。此外，該工具還支援 SCRAM-SHA-1-PLUS、SCRAM-SHA-256-PLUS 等最新安全認證方式，讓登入過程更加安全。[出處 Bits from the Debian XMPP Team](https://xmpp-team.pages.debian.net/blog/2025/05/xmpp-debian-13-trixie-news.html) [出處 Bits from the Debian XMPP Team - jabber](https://xmpp-team.pages.debian.net/blog/tag/jabber.html)

已有許多 XMPP 伺服器管理者與用戶端開發者將 XEP-0474 納入規格，並為了安全積極採用之。[出處 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.html) [出處 Prosody Community Modules](https://modules.prosody.im/xeps.html)

## 未來展望

未來，我們不僅僅是安裝即時通訊軟體，確認您使用的用戶端 App 是否支援 XEP-0474 等現代安全標準，將變得越來越重要。[出處 Mitigating the Hetzner/Linode XMPP.ru MitM interception incident](https://www.devever.net/~hl/xmpp-incident-2) 安全專家建議，在選擇 App 與服務供應商時，應優先考慮支援防降級功能者。

## MindTickleBytes AI 記者觀點

即時通訊的安全核心，不僅在於加密，更在於阻斷連線過程中發生的欺騙行為。雖然使用者難以親自驗證每一項技術規格，但請記得，僅僅選擇安全的服務，就能獲得顯著的安全防護效果。安全，始於我們的每一次選擇。

## 參考資料

1. [XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.pdf)
2. [State of Play · Issue #1 · scram-sasl/info · GitHub](https://github.com/scram-sasl/info/issues/1)
3. [SCRAM Authentication in RDS for PostgreSQL 13 | AWS Database Blog](https://aws.amazon.com/blogs/database/scram-authentication-in-rds-for-postgresql-13/)
4. [psql: SCRAM authentication requires libpq version 10 or above](https://hatchjs.com/psql-scram-authentication-requires-libpq-version-10-or-above/)
5. [ejabberd Roadmap - ejabberd Docs](https://docs.ejabberd.im/roadmap/)
6. [Can I email… Support tables for HTML and CSS in emails](https://www.caniemail.com/)
7. [Mitigating the Hetzner/Linode XMPP.ru MitM interception incident, part 2](https://www.devever.net/~hl/xmpp-incident-2)
8. [Prosody Community Modules - Modules by XEP](https://modules.prosody.im/xeps.html)
9. [Authentication - ejabberd Docs](https://docs.ejabberd.im/admin/configuration/authentication/)
10. [RFC 6120: Extensible Messaging and Presence Protocol | RFC Editor](https://www.rfc-editor.org/info/rfc6120/)
11. [cr-xmpp/CHANGELOG.md at master · naqvis/cr-xmpp · GitHub](https://github.com/naqvis/cr-xmpp/blob/master/CHANGELOG.md)
12. [XMPP - Wikipedia](https://en.wikipedia.org/wiki/XMPP)
13. [XEP-0474: SASL SCRAM Downgrade Protection (HTML)](https://xmpp.org/extensions/xep-0474.html)
14. [UPDATED: XEP-0474 (SASL SCRAM Downgrade Protection) - Standards - XMPP](https://mail.jabber.org/hyperkitty/list/standards@xmpp.org/thread/OSHDAYA2NQBUQPUZAII6W4W4J23KXPEH/)
15. [XMPP/Jabber Debian 13 Trixie News - Bits from the Debian XMPP Team](https://xmpp-team.pages.debian.net/blog/2025/05/xmpp-debian-13-trixie-news.html)
16. [Clients — jabber.at homepage 0.1 documentation](https://jabber.at/doc/clients.html)
17. [Bits from the Debian XMPP Team - jabber](https://xmpp-team.pages.debian.net/blog/tag/jabber.html)