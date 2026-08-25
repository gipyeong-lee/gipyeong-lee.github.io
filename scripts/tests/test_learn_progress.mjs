import assert from "node:assert/strict";
import test from "node:test";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const progress = require("../../js/learn-progress.js");

test("initial progress stores curriculum identity without payment data", () => {
  const state = progress.initialState("precision-robot-hand", "1.0.0");
  assert.deepEqual(state, {
    schemaVersion: 2,
    courseSlug: "precision-robot-hand",
    curriculumVersion: "1.0.0",
    completedModuleIds: [],
    assignmentChecks: {},
    quizScores: {},
    capstoneChecks: [],
    capstoneCompleted: false,
    sponsorshipDismissed: { start: false, complete: false },
  });
  assert.equal("payment" in state, false);
  assert.equal("sponsored" in state, false);
});

test("assignment checks stay local to course module", () => {
  const state = progress.initialState("course", "1");
  const checked = progress.setAssignmentCheck(state, "m01", 1, true);
  const unchecked = progress.setAssignmentCheck(checked, "m01", 1, false);
  assert.deepEqual(checked.assignmentChecks, { m01: [1] });
  assert.deepEqual(unchecked.assignmentChecks, { m01: [] });
  assert.deepEqual(state.assignmentChecks, {});
});

test("completing module is immutable and idempotent", () => {
  const state = progress.initialState("course", "1");
  const completed = progress.completeModule(state, "m01");
  const repeated = progress.completeModule(completed, "m01");
  assert.deepEqual(state.completedModuleIds, []);
  assert.deepEqual(completed.completedModuleIds, ["m01"]);
  assert.deepEqual(repeated.completedModuleIds, ["m01"]);
});

test("module completion requires every assignment and at least 80 quiz points", () => {
  let state = progress.initialState("course", "1");
  state = progress.setAssignmentCheck(state, "m01", 0, true);
  state = progress.setAssignmentCheck(state, "m01", 1, true);
  assert.equal(progress.canCompleteModule(state, "m01", 2), false);
  state = progress.setQuizScore(state, "m01", 79);
  assert.equal(progress.canCompleteModule(state, "m01", 2), false);
  state = progress.setQuizScore(state, "m01", 80);
  assert.equal(progress.canCompleteModule(state, "m01", 2), true);
});

test("capstone is a required final progress step", () => {
  let state = progress.initialState("course", "1");
  state = progress.completeModule(state, "m01");
  state = progress.setCapstoneCheck(state, 0, true);
  assert.equal(progress.progressPercent(state, ["m01"]), 50);
  assert.equal(progress.canCompleteCapstone(state, ["m01"], 2), false);
  state = progress.setCapstoneCheck(state, 1, true);
  assert.equal(progress.canCompleteCapstone(state, ["m01"], 2), true);
  state = progress.completeCapstone(state);
  assert.equal(progress.progressPercent(state, ["m01"]), 100);
});

test("import accepts matching valid state", () => {
  const raw = JSON.stringify({
    ...progress.initialState("course", "1"),
    completedModuleIds: ["m01"],
    quizScores: { m01: 80 },
  });
  const restored = progress.importState(raw, {
    courseSlug: "course",
    curriculumVersion: "1",
    moduleIds: ["m01", "m02"],
    capstoneCount: 1,
  });
  assert.deepEqual(restored.completedModuleIds, ["m01"]);
  assert.equal(restored.quizScores.m01, 80);
});

test("import rejects another curriculum, unknown modules, and invalid scores", () => {
  const base = progress.initialState("course", "1");
  const contract = { courseSlug: "course", curriculumVersion: "1", moduleIds: ["m01"] };
  assert.throws(() => progress.importState(JSON.stringify({ ...base, curriculumVersion: "2" }), contract), /curriculum/i);
  assert.throws(() => progress.importState(JSON.stringify({ ...base, completedModuleIds: ["m99"] }), contract), /module/i);
  assert.throws(() => progress.importState(JSON.stringify({ ...base, quizScores: { m01: 101 } }), contract), /score/i);
});

test("Stripe sponsorship URL adds moment-specific UTM parameters", () => {
  const start = new URL(progress.sponsorshipUrl("https://buy.stripe.com/example?locale=ko", "start"));
  assert.equal(start.searchParams.get("locale"), "ko");
  assert.equal(start.searchParams.get("utm_source"), "learn");
  assert.equal(start.searchParams.get("utm_medium"), "sponsorship");
  assert.equal(start.searchParams.get("utm_campaign"), "learn_start");
  const complete = new URL(progress.sponsorshipUrl("https://buy.stripe.com/example", "complete"));
  assert.equal(complete.searchParams.get("utm_campaign"), "learn_complete");
  assert.equal(progress.sponsorshipUrl("", "start"), "");
});
