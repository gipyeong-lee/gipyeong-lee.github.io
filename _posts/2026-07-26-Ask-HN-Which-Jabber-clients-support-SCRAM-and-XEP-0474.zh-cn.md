---
layout: post
title: "如果担心即时通讯软件登录被黑，为什么你需要 XEP-0474？"
description: "了解 XEP-0474 技术及 SCRAM+ 认证方式，它们能防止 XMPP 即时通讯软件在登录过程中遭受安全威胁。"
summary: "解释 XMPP 安全标准 XEP-0474 的重要性，该标准可防御在登录时强制降低安全设置的黑客攻击。"
tags: [安全, XMPP, Jabber, 隐私保护, 科技]
image: 2026-07-26-Ask-HN-Which-Jabber-clients-support-SCRAM-and-XEP-0474.jpg
image_alt: "刻画数字锁和网络连接的抽象图形图像"
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "即时通讯软件安全的核心不仅在于加密，更在于阻断连接过程中产生的欺骗行为。虽然用户直接核对技术规格非常困难，但只要选择安全的服务，就能获得巨大的安全保障。"
quiz:
  - question: "XEP-0474 技术的主要目的是什么？"
    choices: ["提高即时通讯软件速度", "防御登录时强制降低安全设置的攻击", "添加新的消息传递方式"]
    answer: 1
    explanation: "XEP-0474 是一项旨在防御在即时通讯软件登录握手过程中强制降低安全等级的“降级攻击”的技术。"
  - question: "仅使用 PLAIN 认证方式会产生什么问题？"
    choices: ["认证速度太慢", "安全仅依赖 TLS 通道，易受攻击", "不支持移动端"]
    answer: 1
    explanation: "如果服务器和客户端仅支持 PLAIN 认证，安全将仅依赖于底层的 TLS 通道，从而使得认证方式或通道绑定容易遭受强制降级攻击。"
  - question: "目前确认支持 XEP-0474 的工具有哪些？"
    choices: ["网页浏览器", "go-sendxmpp", "电子邮件客户端"]
    answer: 1
    explanation: "命令行工具 'go-sendxmpp' 从 0.14.1 版本开始支持 XEP-0474 和现代的 SCRAM 认证方式。"
lang: zh-cn
ref: 2026-07-26-Ask-HN-Which-Jabber-clients-support-SCRAM-and-XEP-0474
---

想象一下：你正准备进入一个拥有极其安全大门的金库，也就是你的即时通讯账号。然而，突然有人出现在中间低语道：“这个金库太复杂了，换个简单的方法进去吧。”就在你信以为真并选择了更简陋的密码验证方式的瞬间，守候在侧的黑客便破门而入。

这就是我们使用的即时通讯软件，特别是基于 XMPP 协议（一种基于 XML 的实时通信标准）[参考资料 Wikipedia](https://en.wikipedia.org/wiki/XMPP)（也称为 'Jabber'）的应用程序在登录过程中可能面临的真实风险。最近，为了解决这一问题而出现了一项技术——**XEP-0474**，让我们来轻松详细地了解一下。

## 为什么这很重要？

在使用即时通讯软件时，仅仅加密消息是不够的。如果即时通讯应用与服务器首次建立连接的“登录握手（连接确认过程）”阶段不安全，心怀不轨的攻击者就可以在中间尝试进行强制将安全设置降至最低级别的“降级攻击（Downgrade Attack）”。[参考资料 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.pdf)

如果该攻击成功，强大的安全保护装置就会被解除，你的聊天内容或账号信息将毫无遮掩地暴露在风险之中。XEP-0474 是一面盾牌，它防御此类攻击，防止他人强行解除你所设置的最强安全方式。[参考资料 Mitigating the Hetzner/Linode XMPP.ru MitM interception incident](https://www.devever.net/~hl/xmpp-incident-2)

## 简而言之

可以将 XEP-0474 视为“安全的安全带”。正如坐车时没有安全带会导致事故中严重受伤一样，在即时通讯软件登录时，防止认证安全降级的安全带也是必不可少的。

打个比方，当你连接服务器时，即使你说“我想用最新的安全方式（如 SCRAM-SHA-256 等）登录”，中间的攻击者也可能拦截这条消息，并对服务器撒谎说：“用户想用那种老旧的方式（PLAIN 认证）登录”。

如果服务器和客户端都只支持过时的“PLAIN 认证”，那么安全将仅依赖于薄薄的一层 TLS（数据保护通信标准）。[参考资料 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.pdf) XEP-0474 会检测到这种欺骗，并立即阻断中间人试图拦截并降低安全设置的行为。[参考资料 Prosody Community Modules](https://modules.prosody.im/xeps.html)

## 现状如何？

目前，许多 XMPP 即时通讯生态系统都在努力引入这一安全标准。例如，作为活用命令行即时通讯功能的工具，“go-sendxmpp”已从 0.14.1 版本开始支持 XEP-0474。此外，该工具还支持 SCRAM-SHA-1-PLUS、SCRAM-SHA-256-PLUS 等最新安全认证方式，使登录过程更加安全。[参考资料 Bits from the Debian XMPP Team](https://xmpp-team.pages.debian.net/blog/2025/05/xmpp-debian-13-trixie-news.html) [参考资料 Bits from the Debian XMPP Team - jabber](https://xmpp-team.pages.debian.net/blog/tag/jabber.html)

许多 XMPP 服务器管理员和客户端开发者已将 XEP-0474 纳入规范，并积极采用以加强安全性。[参考资料 XEP-0474: SASL SCRAM Downgrade Protection](https://xmpp.org/extensions/xep-0474.html) [参考资料 Prosody Community Modules](https://modules.prosody.im/xeps.html)

## 未来展望

未来，仅仅安装即时通讯软件将不再足够，确认所使用的客户端应用是否支持像 XEP-0474 这样的现代安全标准将变得至关重要。[参考资料 Mitigating the Hetzner/Linode XMPP.ru MitM interception incident](https://www.devever.net/~hl/xmpp-incident-2) 安全专家建议，在选择即时通讯应用和服务提供商时，应优先考虑支持这种防降级功能的平台。

## MindTickleBytes AI 记者的视角

即时通讯软件安全的核心不仅在于加密，更在于阻断连接过程中产生的欺骗行为。虽然用户直接核对技术规格非常困难，但请记住，只要选择安全的服务，就能获得巨大的安全保障。安全始于我们的选择。

## 参考资料

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