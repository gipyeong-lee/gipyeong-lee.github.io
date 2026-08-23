---
layout: post
title: "[PHP] 所有 PHP 框架都糟透了！！！"
description: "PHP Frameworks Day 是去年十月在烏克蘭基輔舉辦的活動。這是一個關於各種不同框架的演講活動。我直到現在才得知這件事，這要歸功於..."
date: 2015-08-06 15:27:11 +0900
section: blog
category: engineering
lang: zh-tw
ref: 2015-08-06-legacy-69-engineering-php-all-php-framework-suck
tags:
  - "php"
  - "框架"
  - "Rasmus"
  - "Scrap"
  - "工程"
noindex: true
translation_source_hash: 17bb24f3c1785a8c12e29d3e9b7b2df0a9aeb21863e0beb66b15f9f4526064ab
---

<h2>
PHP Frameworks Day
</h2>
<p>
<a href="http://frameworksdays.com/" rel="nofollow">
PHP Frameworks day
</a>
是去年十月在烏克蘭基輔舉辦的活動。這是一個關於各種不同框架的演講活動。
</p>
<p>
我直到現在才得知這件事，這要歸功於由 PHPDeveloper.org 的 Chris Cornutt（又名 enygma）所整理的 <a href="https://twitter.com/phpquickfix" rel="nofollow">PHP Quick Fix</a> 新聞串。謝謝你，Chris。
</p>
<h2>
<span>
<img src="http://files.phpclasses.org/files/blog/file/Rasmus-Lerdorf.jpg" alt="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" title="Rasmus Lerdorf http://en.wikipedia.org/wiki/File:Wikirl.jpg" width="120" height="114">
</span>
為什麼所有 PHP 框架都糟透了
</h2>
<p>
PHP 的創始人 Rasmus Lerdorf 受邀在 PHP Frameworks Day 大會上發表演講。他主要談論了 PHP 的最新發展，但對我來說，最有趣的部分是問答環節。
</p>
<p>
除了其他問題外，有人問 Rasmus 對 PHP 框架的看法。這是一個直接詢問他意見的問題，所以 Rasmus 給出了直截了當的回答（約在 31 分 47 秒處）：「它們（PHP 框架）全都很糟！」
</p>
<p>
<span class="media-container">
<iframe width="560" height="315" src="http://www.youtube.com/embed/anr7DQnMMs0" frameborder="0" allowfullscreen="">
</iframe>
</span>
</p>
<p>
一位受邀演講者到 PHP 框架會議上說他們全都很糟，這看起來可能有點奇怪。然而，觀眾似乎很喜歡這個答案。總之，Rasmus 詳細說明了他的意思。
</p>
<h3>
1. 框架反覆執行相同的代碼且毫無必要
</h3>
<p>
Rasmus 澄清說，所有通用的框架都沒有針對每個人的需求進行優化。
</p>
<p>
一個更具體的抱怨是，框架提供的解決方案導致在每個 HTTP 請求中反覆執行不必要的 PHP 代碼。Rasmus 舉的例子是，框架在每個請求中都會檢查應用程式正在使用的資料庫類型，以載入對應的資料庫存取類別。由於應用程式部署後，資料庫類型不會改變，他認為這是一種浪費。
</p>
<p>
雖然我同意 Rasmus 的觀點，但我認為這個例子說服力不足，因為檢查設定檔來決定載入哪個資料庫存取類別所花的時間極短，特別是與執行資料庫查詢相比，後者通常需要許多毫秒，有時甚至需要幾秒鐘才能完成。
</p>
<p>
這個問題的一個更好的例子是當框架需要讀取設定檔來載入實際的設定值時。
</p>
<p>
框架通常從 INI 檔案讀取設定。PHP 內建了讀取和解析 INI 檔案的函數。儘管你可以用一個函數完成所有工作，但讀取並解析 INI 檔案所花的時間通常遠遠超過檢查已解析的設定值。
</p>
<p>
如果你的框架讀取並解析 PHP 沒有內建支援的其他格式（例如 YAML 或 XML）的設定檔，情況會更糟，因為框架必須用純 PHP 代碼進行解析。這比用 C 代碼編寫的 PHP 引擎解析 INI 檔案要慢得多。
</p>
<p>
一個更好的替代方案是將設定值定義在 PHP 指令碼檔案中。只需將設定值放在將值賦予變數的 PHP 指令碼中即可。
</p>
<p>
當你使用 PHP 快取擴充功能時，PHP 指令碼只會被編譯一次。在第二次執行時，編譯成操作碼（opcode）的 PHP 指令碼會直接從 RAM 中載入。這比從檔案載入設定要快得多。
</p>
<h3>
2. 框架需要太多相互依賴的類別
</h3>
<p>
Rasmus 提到的另一點是，有時你只需要框架的特定部分，但由於框架類別之間有太多依賴關係，即使你只使用框架的簡單功能，也需要載入太多類別。
</p>
<p>
雖然在一定程度上確實如此，但我已經看到一些框架開發人員致力於減少不同元件之間的依賴關係。不過，許多框架類別之間仍然經常存在依賴關係，有時對於有特定需求的應用程式而言，這些依賴並沒有增加任何價值。
</p>
<p>
為了這個問題，一些開發人員需要修改框架，剔除那些增加開銷的不必要部分。這會導致維護上的噩夢，因為每次他們想升級到他們已經開始適應需求的框架的新版本時，都需要再次進行修改。
</p>
<p>
Rasmus 建議使用針對特定用途進行優化的框架來避免這個問題。例如，如果你只是想發佈部落格，他建議使用 WordPress 或 Drupal。
</p>
<p>
或者，Rasmus 建議框架應該提供一種方法，讓開發人員只需將每個應用程式中所需的一小部分元件部署到生產環境中。
</p>
<p>
這個解決方案太籠統了。Rasmus 並沒有深入探討某些框架實現事物的方式，因此他沒有評論為什麼某些框架需要這麼多元件。
</p>
<p>
例如，許多框架依賴執行時期（runtime）的 ORM（物件關聯映射）。這些元件讓開發人員能夠定義如何查詢資料庫，將資訊視為物件而非記錄表。
</p>
<p>
物件導向對於抽象問題和將解決方案封裝成物件類別是很好的，但某些 ORM 的運作方式增加了太多不必要的開銷。
</p>
<p>
開發人員必須編寫代碼來動態指定類別變數（資料表欄位）、條件子句、物件關係（資料表關聯）等，以在執行時期組成實際的查詢。這增加了很多開銷，因為除了可能變化的參數值外，每次請求執行的查詢都是相同的。
</p>
<p>
有一個更好的解決方案可以避免這種開銷。與其在執行時期動態組成查詢，不如使用一個獨立的工具為 ORM 類別產生 PHP 代碼。產生的類別已經編譯好了 SQL 查詢，在執行時期無需進一步開銷即可執行。
</p>
<p>
自 2002 年我開發了一個名為 <a href="http://www.meta-language.net/metastorage.html" rel="nofollow">Metastorage</a> 的 ORM 工具以來，我就一直使用這種方法。它完全做到了我上面描述的事情。我在專案檔案中定義我需要應用於物件的物件、變數、關係和函數。
</p>
<p>
Metastorage 會處理我的物件定義，並產生 ORM 類別，這些類別僅透過呼叫類別函數即可在執行時期執行必要的查詢。執行時期不會進行任何查詢組裝。
</p>
<h3>
3. 不必要地複雜的解決方案
</h3>
<p>
Rasmus 沒有直接提到的一點是框架往往傾向於推動複雜的解決方案。
</p>
<p>
例如應用程式版本遷移的情況就是如此。一些框架複製了 Ruby on Rails 的遷移概念。這意味著你必須編寫代碼來在不同應用程式版本之間變更資料庫架構。
</p>
<p>
這是 Metastorage 以更有效率且對開發人員更少痛苦的方式解決的另一件事。Metastorage 將資料庫資料表架構定義與我的物件定義分開在不同的檔案中。它會產生一個安裝類別，在第一次執行時安裝資料庫資料表。
</p>
<p>
如果我變更了物件定義，安裝類別也可以使用較新的定義升級架構，而不會破壞資料庫資料表中已插入的任何資料。
</p>
<p>
這當然使開發變得快得多，且應用程式升級更不容易出錯，因為工具總是能產生正確的代碼來升級資料庫架構。當你手寫遷移代碼時，可能會犯錯，導致你花費更多時間和精力去修復。
</p>
<h3>
4. 重複網頁伺服器的功能
</h3>
<p>
Rasmus 沒有直接提到的另一個面向，與框架有時要求 PHP 代碼重做網頁伺服器已經完成的工作有關。
</p>
<p>
例如，路由是將某些代碼（控制器）分配給處理具有不同 URL 模式的請求的過程。許多框架推動應用程式使用 <a href="http://en.wikipedia.org/wiki/Front_Controller_pattern" rel="nofollow">前端控制器模式（Front Controller pattern）</a>。前端控制器會分析請求 URL 並載入特定的控制器來實際處理該請求。
</p>
<p>
問題在於，網頁伺服器已經做了這件事。它可以根據設定（例如 mod_rewrite 或類似的設定）比對請求 URL 並執行適當的 PHP 指令碼。
</p>
<p>
當你讓 PHP 處理路由過程時，你正在增加不必要的開銷來執行一項對於具有相同 URL 模式的每個請求都相同的任務。這屬於 Rasmus 對框架反覆執行相同代碼以達到相同結果的抱怨。
</p>
<p>
這似乎又是 PHP 框架從 Ruby on Rails 和 Java 獲得的另一個壞影響。在那些語言中，網頁伺服器會將請求轉發給應用程式伺服器。
</p>
<p>
PHP 不需要以這種方式工作，因為它總是與網頁伺服器整合執行，因此沒有必要以一種更慢且增加更多開銷的方式重複網頁伺服器功能。
</p>
<h2>
其他問題
</h2>
<p>
在同一個會議中，Rasmus 也回答了其他我覺得值得評論的有趣問題。
</p>
<h3>
放棄 APC 以支持 Zend Opcode Cache
</h3>
<p>
這是我們在 <a href="http://www.phpclasses.org/blog/category/podcast/">Lately in PHP podcast</a> 中討論過多次的話題。Rasmus 解釋說，PHP 需要採用一個能跟隨最新 PHP 發展且每個新版本都適用的操作碼快取。
</p>
<p>
有幾個操作碼快取。Rasmus 決定放棄 APC 而轉向 Zend 的解決方案，因為它更成熟、速度更快。這需要 Zend 將他們的解決方案開源。
</p>
<p>
有趣的是，現在官方 PHP 操作碼快取的維護者是 Dmitry Stogov。他曾是 Turck MMCache 的原始開發者，幾年前被 Zend 聘請開發他們自己的快取擴充功能。
</p>
<p>
結果好，一切都好。可惜 PHP 花了這麼長時間才擁有一個官方快取擴充功能。缺乏官方擴充功能讓 PHP 在過去許多對其他語言有利的基準測試中看起來很差。
</p>
<h3>
將 PHP 編譯成二進位代碼
</h3>
<p>
有人問 PHP 是否會有透過將代碼編譯成某種形式的二進位檔案來保護代碼的解決方案。
</p>
<p>
Rasmus 表示 PHP 永遠不會內建那種解決方案。他辯稱 Zend（和其他公司）提供了這類解決方案，但它們很容易被破解。所以他寧願不參與那個遊戲。
</p>
<p>
雖然這話沒錯，但 Rasmus 只是在考慮那些僅將 PHP 編譯成操作碼並加密結果的解決方案。這對駭客來說確實不是那麼難破解。
</p>
<p>
然而，有更好的解決方案，即將產生的代碼編譯成原生組合語言機器碼。雖然總是有可能反編譯機器碼，但將其逆向工程還原成對那些想要竊取工作或以某種有用方式更改它的人來說足夠有用的 PHP 代碼是非常困難的。
</p>
<p>
許多尋找 PHP 代碼防複製解決方案的開發人員擔心的是，任何有權存取安裝了代碼的伺服器的人都可以輕易地更改代碼。
</p>
<p>
我多次見過為客戶工作的開發人員，那些客戶在開發人員不知情的情況下直接更改了代碼。這造成了維護上的頭痛。有時客戶抱怨代碼無法正常運作，因為事實上他們更改了代碼。所以，一個讓查看或更改已安裝代碼變得更困難的解決方案將有所幫助。
</p>
<p>
對於這些情況，如今開發人員可以透過建立 <a href="http://www.php.net/phar" rel="nofollow">PHAR</a> 封存檔來最大程度地減少該問題。這些是包含一個或多個 PHP 指令碼的二進位封存檔。雖然 PHAR 封存檔並非真正的防複製解決方案，但至少它們會讓那些想查看開發人員代碼的客戶變得更困難。
</p>
<h3>
PHP 變數中的 $ 符號
</h3>
<p>
當被問及為什麼變數以 $ 符號開頭時，他解釋說這是為了能夠在字串字面值中插入變數，因此需要使用一個標記來區分什麼是變數以及字串的其餘部分。
</p>
<p>
由於他希望變數在字串內外看起來都一樣，他選擇了 $ 符號來作為變數開頭，這靈感來自 Perl 也採用的解決方案。
</p>
<h3>
Node.js 與非阻塞 I/O
</h3>
<p>
當被問及 PHP 是否會支援非阻塞 I/O 程式設計時，Rasmus 解釋說你已經可以用 <a href="http://pecl.php.net/package/libevent" rel="nofollow">libevent</a> 擴充功能做到這一點。但對於那種程式設計，Rasmus 寧願使用 <a href="http://golang.org/" rel="nofollow">Go 語言</a> 編寫代碼。
</p>
<p>
總之，不幸的是，使用例如 Node.js 完成的非同步（非阻塞 I/O）程式設計並不是那麼令人愉快，因為它需要透過巢狀回呼（nested callbacks）處理所有事情。
</p>
<p>
回呼中的巢狀代碼會導致非常令人沮喪的問題，例如當你在回呼函數中時無法中斷 while 迴圈。這是我們在 <a href="http://www.jsclasses.org/blog/post/44-Faster-JavaScript-with-asmjs--Lately-in-JavaScript-podcast-episode-28.html">Lately in JavaScript podcast</a> 中多次討論的話題。
</p>
<h3>
PHP 7 中的 Unicode 和 JIT
</h3>
<p>
當被問及未來 PHP 版本的計畫時，Rasmus 評論說他從 PHP 6 Unicode 支援失敗的經驗中學到這是一個太過雄心勃勃的目標。因此他期望 PHP 能以更小的跳躍進化。
</p>
<p>
他認為有兩個目標太過雄心勃勃但最終可能會在 PHP 7 中實現：基於比 ICU 更簡單方法的 Unicode 原生支援，以及可能基於 Google V8 或 Facebook HHVM 的 JIT 編譯引擎。
</p>
<h2>
結論
</h2>
<p>
Rasmus 的採訪非常有趣，因為它讓我們反思我們在 PHP 中做事的方式，這些方式可能並不理想，特別是當你使用通用框架時。
</p>
<p>
無論你同意還是不同意這些觀點，請在此發表評論，告訴我們你對這些話題的看法。
</p>
<div>
<br>
</div>
<div>
<br>
</div>
<div>
參考資料 :
<a href="http://www.phpclasses.org/blog/post/226-4-Reasons-Why-All-PHP-Frameworks-Suck.html" target="_blank" class="tx-link">
4 Reasons Why All PHP Frameworks Suck
</a>
</div>