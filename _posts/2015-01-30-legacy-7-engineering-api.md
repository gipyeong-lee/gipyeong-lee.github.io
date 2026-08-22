---
layout: post
title: "크롬 확장 API 리스트 정리"
description: "크롬 확장 API 리스트 정리입니다. 리스트 추출은 Python 을 이용하였습니다. 관련 타이틀을 클릭하시면 해당 샘플 소스를 받을수 있습니다. 소스를 풀으셔서 크롬 확장 프로그램에 넣으시면 샘플이 동작합니다. My Bookmarks Page Redder Print this pag..."
date: 2015-01-30 11:59:53 +0900
section: blog
category: engineering
lang: ko
ref: 2015-01-30-legacy-7-engineering-api
tags:
  - "크롬"
  - "Chrome"
  - "API"
  - "Chrome Extension"
  - "engineering"
---

<p>
<b>
크롬 확장 API 리스트 정리입니다.
</b>
</p>




<p>
리스트 추출은 Python 을 이용하였습니다.
</p>
<p>
관련 타이틀을 클릭하시면 해당 샘플 소스를 받을수 있습니다.
</p>
<p>
소스를 풀으셔서 크롬 확장 프로그램에 넣으시면 샘플이 동작합니다.
</p>


<h2>
<a href="examples/api/bookmarks/basic.zip">
My Bookmarks
</a>
</h2>
<h2>
<a href="examples/api/browserAction/make_page_red.zip">
Page Redder
</a>
</h2>
<h2>
<a href="examples/api/browserAction/print.zip">
Print this page
</a>
</h2>
<h2>
<a href="examples/api/browserAction/set_icon_path.zip">
A browser action which changes its icon when clicked
</a>
</h2>
<h2>
<a href="examples/api/browserAction/set_page_color.zip">
A browser action with a popup that changes the page color
</a>
</h2>
<h2>
<a href="examples/api/browsingData/basic.zip">
BrowsingData API: Basics
</a>
</h2>
<h2>
<a href="examples/api/commands.zip">
Sample Extension Commands extension
</a>
</h2>
<h2>
<a href="examples/api/contentSettings.zip">
Content settings
</a>
</h2>
<h2>
<a href="examples/api/contextMenus/basic.zip">
Context Menus Sample
</a>
</h2>
<h2>
<a href="examples/api/contextMenus/event_page.zip">
Context Menus Sample (with Event Page)
</a>
</h2>
<h2>
<a href="examples/api/cookies.zip">
Cookie API Test Extension
</a>
</h2>
<h2>
<a href="examples/api/debugger/live-headers.zip">
Live HTTP headers
</a>
</h2>
<h2>
<a href="examples/api/debugger/pause-resume.zip">
JavaScript pause/resume
</a>
</h2>
<h2>
<a href="examples/api/desktopCapture.zip">
Desktop Capture Example
</a>
</h2>
<h2>
<a href="examples/api/deviceInfo/basic.zip">
My Devices
</a>
</h2>
<h2>
<a href="examples/api/devtools/audits/broken-links.zip">
Broken Links
</a>
</h2>
<h2>
<a href="examples/api/devtools/inspectedWindow/chrome-preprocessor.zip">
Chrome Preprocessor Example
</a>
</h2>
<h2>
<a href="examples/api/devtools/network/chrome-firephp.zip">
FirePHP for Chrome
</a>
</h2>
<h2>
<a href="examples/api/devtools/panels/chrome-query.zip">
Chrome Query
</a>
</h2>
<h2>
<a href="examples/api/document_scan.zip">
Document Scanning API Sample
</a>
</h2>
<h2>
<a href="examples/api/downloads/download_filename_controller.zip">
Download Filename Controller
</a>
</h2>
<h2>
<a href="examples/api/downloads/download_links.zip">
Download Selected Links
</a>
</h2>
<h2>
<a href="examples/api/downloads/download_manager.zip">
Download Manager Button
</a>
</h2>
<h2>
<a href="examples/api/downloads/download_open.zip">
Download and Open Button
</a>
</h2>
<h2>
<a href="examples/api/downloads/downloads_overwrite.zip">
Downloads Overwrite Existing Files
</a>
</h2>
<h2>
<a href="examples/api/eventPage/basic.zip">
Event Page Example
</a>
</h2>
<h2>
<a href="examples/api/extension/isAllowedAccess.zip">
`extension.isAllowedFileSchemeAccess` and `extension.isAllowedIncognitoAccess` Example
</a>
</h2>
<h2>
<a href="examples/api/fileSystemProvider/archive.zip">
Fake Archive Handler App
</a>
</h2>
<h2>
<a href="examples/api/fileSystemProvider/basic.zip">
File System Provider API Extension Example
</a>
</h2>
<h2>
<a href="examples/api/fontSettings.zip">
Advanced Font Settings
</a>
</h2>
<h2>
<a href="examples/api/history/showHistory.zip">
Typed URL History
</a>
</h2>
<h2>
<a href="examples/api/i18n/cld.zip">
CLD
</a>
</h2>
<h2>
<a href="examples/api/i18n/getMessage.zip">
AcceptLanguage
</a>
</h2>
<h2>
<a href="examples/api/i18n/localizedHostedApp.zip">
Minimal Localized Hosted App
</a>
</h2>
<h2>
<a href="examples/api/idle/idle_simple.zip">
Idle - Simple Example
</a>
</h2>
<h2>
<a href="examples/api/infobars/sandwichbar.zip">
SandwichBar
</a>
</h2>
<h2>
<a href="examples/api/input.ime/basic.zip">
Test IME
</a>
</h2>
<h2>
<a href="examples/api/messaging/timer.zip">
Message Timer
</a>
</h2>
<h2>
<a href="examples/api/nativeMessaging/app.zip">
Native Messaging Example
</a>
</h2>
<h2>
<a href="examples/api/notifications.zip">
Notification Demo
</a>
</h2>
<h2>
<a href="examples/api/omnibox/simple-example.zip">
Omnibox Example
</a>
</h2>
<h2>
<a href="examples/api/override/blank_ntp.zip">
Blank new tab page
</a>
</h2>
<h2>
<a href="examples/api/override/override_igoogle.zip">
iGoogle new tab page
</a>
</h2>
<h2>
<a href="examples/api/pageAction/pageaction_by_content.zip">
Page action by content
</a>
</h2>
<h2>
<a href="examples/api/pageAction/pageaction_by_url.zip">
Page action by URL
</a>
</h2>
<h2>
<a href="examples/api/pageAction/set_icon.zip">
Animated Page Action
</a>
</h2>
<h2>
<a href="examples/api/permissions/extension-questions.zip">
Top Chrome Extension Questions
</a>
</h2>
<h2>
<a href="examples/api/power.zip">
Keep Awake
</a>
</h2>
<h2>
<a href="examples/api/preferences/allowThirdPartyCookies.zip">
Block/allow third-party cookies API example extension
</a>
</h2>
<h2>
<a href="examples/api/preferences/enableReferrer.zip">
Block/allow referrer API example extension
</a>
</h2>
<h2>
<a href="examples/api/processes/process_monitor.zip">
Process Monitor
</a>
</h2>
<h2>
<a href="examples/api/processes/show_tabs.zip">
Show Tabs in Process
</a>
</h2>
<h2>
<a href="examples/api/storage/stylizr.zip">
Stylizr
</a>
</h2>
<h2>
<a href="examples/api/tabs/inspector.zip">
Tab Inspector
</a>
</h2>
<h2>
<a href="examples/api/tabs/pin.zip">
Keyboard Pin
</a>
</h2>
<h2>
<a href="examples/api/tabs/screenshot.zip">
Test Screenshot Extension
</a>
</h2>
<h2>
<a href="examples/api/tabs/zoom.zip">
Tabs Zoom API Demo
</a>
</h2>
<h2>
<a href="examples/api/topsites/basic.zip">
Top Sites
</a>
</h2>
<h2>
<a href="examples/api/topsites/magic8ball.zip">
NTP prototyping extension
</a>
</h2>
<h2>
<a href="examples/api/ttsEngine/console_tts_engine.zip">
Console TTS Engine
</a>
</h2>
<h2>
<a href="examples/api/webNavigation/basic.zip">
WebNavigation Tech Demo
</a>
</h2>
<h2>
<a href="examples/api/windows/merge_windows.zip">
Merge Windows
</a>
</h2>
<h2>
<a href="examples/apps/background-simple.zip">
Simple Background App
</a>
</h2>
<h2>
<a href="examples/apps/calculator/app.zip">
Calculator
</a>
</h2>
<h2>
<a href="examples/extensions/app_launcher.zip">
App Launcher
</a>
</h2>
<h2>
<a href="examples/extensions/buildbot.zip">
Chromium Buildbot Monitor
</a>
</h2>
<h2>
<a href="examples/extensions/calendar.zip">
Google Calendar Checker (by Google)
</a>
</h2>
<h2>
<a href="examples/extensions/catblock.zip">
CatBlock
</a>
</h2>
<h2>
<a href="examples/extensions/catifier.zip">
Catifier
</a>
</h2>
<h2>
<a href="examples/extensions/chrome_search.zip">
Chromium Search
</a>
</h2>
<h2>
<a href="examples/extensions/email_this_page.zip">
Email this page (by Google)
</a>
</h2>
<h2>
<a href="examples/extensions/fx.zip">
Chrome Sounds
</a>
</h2>
<h2>
<a href="examples/extensions/gdocs.zip">
Google Document List Viewer
</a>
</h2>
<h2>
<a href="examples/extensions/gmail.zip">
Google Mail Checker
</a>
</h2>
<h2>
<a href="examples/extensions/imageinfo.zip">
Imageinfo
</a>
</h2>
<h2>
<a href="examples/extensions/irc/app.zip">
Chromium IRC App
</a>
</h2>
<h2>
<a href="examples/extensions/managed_bookmarks.zip">
Managed Bookmarks
</a>
</h2>
<h2>
<a href="examples/extensions/mappy.zip">
Mappy
</a>
</h2>
<h2>
<a href="examples/extensions/maps_app.zip">
Google Maps
</a>
</h2>
<h2>
<a href="examples/extensions/news.zip">
News Reader (by Google)
</a>
</h2>
<h2>
<a href="examples/extensions/news_a11y.zip">
News Reader
</a>
</h2>
<h2>
<a href="examples/extensions/news_i18n.zip">
News Reader
</a>
</h2>
<h2>
<a href="examples/extensions/oauth_contacts.zip">
Sample - OAuth Contacts
</a>
</h2>
<h2>
<a href="examples/extensions/plugin_settings.zip">
Per-plugin content settings
</a>
</h2>
<h2>
<a href="examples/extensions/proxy_configuration.zip">
Proxy Extension API Sample
</a>
</h2>
<h2>
<a href="examples/extensions/speak_selection.zip">
Speak Selection
</a>
</h2>
<h2>
<a href="examples/extensions/talking_alarm_clock.zip">
Talking Alarm Clock
</a>
</h2>
<h2>
<a href="examples/extensions/ttsdebug.zip">
TTS Debug
</a>
</h2>
<h2>
<a href="examples/extensions/ttsdemo.zip">
TTS Demo
</a>
</h2>
<h2>
<a href="examples/howto/sandbox.zip">
Sandboxed Frame
</a>
</h2>
<h2>
<a href="examples/howto/tab_shortcuts.zip">
Tab Shortcuts
</a>
</h2>
<h2>
<a href="examples/tutorials/analytics.zip">
Event Tracking with Google Analytics
</a>
</h2>
<h2>
<a href="examples/tutorials/getstarted.zip">
Getting started example
</a>
</h2>


<p>
추후 필요에 따라 하나하나의 샘플을 분석하도록 하겠습니다.
</p>
