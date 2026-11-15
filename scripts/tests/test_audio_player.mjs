// Audio player contract: no mp3 request until the reader presses play.
//
// With `new Audio(src)` at page load the browser downloaded the whole mp3 on
// every view of a post with narration, played or not (Chrome, 2026-11-15:
// 1,334,469 B for a 1,334,169 B file, initiator "audio"). That made the
// jsDelivr traffic for audio/ track page views instead of listens: 4,963
// hits / 3.39 GB in 30 days, for a use jsDelivr's Terms of Use section 6
// already discourage. If "opening a post fetches no audio" fails, every
// audio-post view costs readers ~1.3 MB again and the host sees it.
//
// Run: node --test scripts/tests/test_audio_player.mjs
import assert from "node:assert/strict";
import test from "node:test";
import { readFileSync } from "node:fs";
import { runInNewContext } from "node:vm";

const SOURCE = readFileSync(new URL("../../js/audio-player.js", import.meta.url), "utf8");
const MP3 = "https://cdn.jsdelivr.net/gh/gipyeong-lee/gipyeong-lee.github.io@main/audio/post.mp3";
const REF = "2026-11-15-post";
const flush = () => new Promise((resolve) => setImmediate(resolve));

class FakeElement {
  constructor() {
    this.listeners = {};
    this.attrs = {};
    this.children = {};
    this.style = {};
    this.textContent = "";
    this.className = "";
    const classes = new Set();
    this.classList = {
      add: (name) => classes.add(name),
      remove: (name) => classes.delete(name),
      contains: (name) => classes.has(name),
    };
  }
  getAttribute(name) {
    return name in this.attrs ? this.attrs[name] : null;
  }
  querySelector(selector) {
    return this.children[selector] || null;
  }
  addEventListener(type, listener) {
    (this.listeners[type] ||= []).push(listener);
  }
  click(event = {}) {
    for (const listener of this.listeners.click || []) listener(event);
  }
  getBoundingClientRect() {
    return { left: 0, width: 100 };
  }
}

// Mirrors the HTMLMediaElement behaviour the player depends on.
class FakeAudio {
  static instances = [];
  static failNextPlay = false;
  static nextPlay = null;

  constructor(src) {
    FakeAudio.instances.push(this);
    this.listeners = {};
    this.srcSets = [];
    this._src = "";
    this._time = 0;
    this.preload = "auto";
    this.paused = true;
    this.duration = NaN;
    this.playbackRate = 1;
    this.defaultPlaybackRate = 1;
    this.playCalls = 0;
    if (src !== undefined) this.src = src;
  }
  get src() {
    return this._src;
  }
  // Assigning src runs the media element load algorithm: position and
  // duration reset, and playbackRate goes back to defaultPlaybackRate.
  set src(value) {
    this._src = value;
    this.srcSets.push(value);
    this._time = 0;
    this.duration = NaN;
    this.playbackRate = this.defaultPlaybackRate;
  }
  get currentTime() {
    return this._time;
  }
  set currentTime(value) {
    // Browsers throw on NaN, e.g. a seek computed from an unknown duration.
    if (!Number.isFinite(value)) throw new TypeError("The provided double value is non-finite.");
    this._time = value;
  }
  // play() flips paused to false at once; a resource that fails to load (a
  // 404) rejects the promise later and leaves paused false.
  play() {
    this.playCalls += 1;
    this.paused = false;
    if (FakeAudio.failNextPlay) {
      FakeAudio.failNextPlay = false;
      return Promise.reject(new Error("NotSupportedError"));
    }
    const pending = FakeAudio.nextPlay || Promise.resolve();
    FakeAudio.nextPlay = null;
    return pending;
  }
  pause() {
    this.paused = true;
  }
  addEventListener(type, listener) {
    (this.listeners[type] ||= []).push(listener);
  }
  emit(type) {
    for (const listener of this.listeners[type] || []) listener({ type });
  }
}

function mount({ saved } = {}) {
  FakeAudio.instances = [];
  FakeAudio.failNextPlay = false;
  FakeAudio.nextPlay = null;
  const store = new Map(saved === undefined ? [] : [[`audio-pos-${REF}`, String(saved)]]);
  const icon = new FakeElement();
  icon.className = "ion ion-ios-play";
  const btn = new FakeElement();
  btn.children.i = icon;
  const parts = {
    btn,
    fill: new FakeElement(),
    progress: new FakeElement(),
    speed: new FakeElement(),
    time: new FakeElement(),
    close: new FakeElement(),
  };
  const bar = new FakeElement();
  bar.attrs = { "data-src": MP3, "data-ref": REF };
  bar.children = {
    ".audio-player__btn": parts.btn,
    ".audio-player__progress-fill": parts.fill,
    ".audio-player__progress": parts.progress,
    ".audio-player__speed": parts.speed,
    ".audio-player__time": parts.time,
    ".audio-player__close": parts.close,
  };
  const body = new FakeElement();
  runInNewContext(SOURCE, {
    document: { querySelector: (selector) => (selector === ".audio-player" ? bar : null), body },
    localStorage: {
      getItem: (key) => (store.has(key) ? store.get(key) : null),
      setItem: (key, value) => store.set(key, String(value)),
      removeItem: (key) => store.delete(key),
    },
    Audio: FakeAudio,
  });
  assert.equal(FakeAudio.instances.length, 1, "the player creates one Audio element");
  return { ...parts, bar, body, icon, store, audio: FakeAudio.instances[0] };
}

test("opening a post fetches no audio", () => {
  const player = mount();
  assert.deepEqual(player.audio.srcSets, [], "no src before the first play");
  assert.equal(player.audio.preload, "none");
  assert.ok(player.bar.classList.contains("is-visible"), "the bar still shows");
});

test("the first play loads the mp3 once and plays it", () => {
  const player = mount();
  player.btn.click();
  assert.deepEqual(player.audio.srcSets, [MP3]);
  assert.equal(player.audio.playCalls, 1);
  assert.equal(player.icon.className, "ion ion-ios-pause");

  player.btn.click();
  assert.equal(player.audio.paused, true);
  assert.equal(player.icon.className, "ion ion-ios-play");

  player.btn.click();
  assert.deepEqual(player.audio.srcSets, [MP3], "resuming must not reload the file");
  assert.equal(player.audio.playCalls, 2);
});

test("a saved position is restored once metadata arrives", () => {
  const player = mount({ saved: 42.5 });
  player.btn.click();
  player.audio.duration = 100;
  player.audio.emit("loadedmetadata");
  assert.equal(player.audio.currentTime, 42.5);
});

test("a saved position past the end is ignored", () => {
  const player = mount({ saved: 500 });
  player.btn.click();
  player.audio.duration = 100;
  player.audio.emit("loadedmetadata");
  assert.equal(player.audio.currentTime, 0);
});

test("loading does not overwrite the saved position before restoring it", () => {
  const player = mount({ saved: 42.5 });
  player.btn.click();
  player.audio.emit("timeupdate"); // still at 0: metadata not loaded yet
  assert.equal(player.store.get(`audio-pos-${REF}`), "42.5");
});

test("a speed picked before the first play survives loading", () => {
  const player = mount();
  player.speed.click();
  player.btn.click();
  assert.equal(player.audio.playbackRate, 1.5);
  assert.equal(player.speed.textContent, "1.5x");
});

test("a failed play puts the play button back and lets the next click retry", async () => {
  const player = mount();
  FakeAudio.failNextPlay = true;
  player.btn.click();
  await flush();
  assert.equal(player.icon.className, "ion ion-ios-play");
  assert.equal(player.audio.paused, true, "next click must call play, not pause");
});

test("a stale play rejection does not stop a newer play", async () => {
  const player = mount();
  let rejectFirst;
  FakeAudio.nextPlay = new Promise((resolve, reject) => {
    rejectFirst = reject;
  });
  player.btn.click(); // play, still pending
  player.btn.click(); // pause: the browser rejects the pending play with AbortError
  player.btn.click(); // play again
  rejectFirst(new Error("AbortError"));
  await flush();
  assert.equal(player.audio.paused, false);
  assert.equal(player.icon.className, "ion ion-ios-pause");
});

test("seeking before anything is loaded does nothing", () => {
  const player = mount();
  assert.doesNotThrow(() => player.progress.click({ clientX: 50 }));
  assert.equal(player.audio.currentTime, 0);
  assert.deepEqual(player.audio.srcSets, [], "a seek click must not start a download");
});
