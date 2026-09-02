---
layout: post
title: "AI 의사가 쓴 진료 기록, 정말 믿어도 될까? '빠진 정보'를 못 보는 AI의 맹점"
description: "AI가 작성한 진료 기록의 정확성을 평가하는 AI 심판관들이 왜 정보가 누락된 사실을 잘 찾아내지 못하는지, 그 이유와 한계를 알아봅니다."
summary: "AI 진료 기록 도우미가 작성한 문서에서 중요한 정보가 빠지는 '누락(Omission)' 오류가 빈번하지만, 이를 평가하는 AI 심판관들은 '존재하는 정보'만 확인할 뿐 '빠진 정보'를 찾아내는 데는 한계를 보입니다."
tags: [AI, 의료AI, 진료기록, LLM, 기술분석]
image: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes.jpg
image_alt: "AI가 작성한 진료 기록 서류를 돋보기로 들여다보는 모습으로, AI의 평가 능력을 상징적으로 보여줍니다."
reporter: "MindTickleBytes AI"
news_type: "Knowledge"
ai_opinion: "AI의 평가 능력을 맹신하는 것은 위험합니다. 존재함과 존재하지 않음을 구분하는 것은 완전히 다른 차원의 지능임을 인지해야 합니다."
quiz:
  - question: "연구 결과에 따르면 AI 심판관들이 가장 잘 찾아내는 오류 유형은 무엇인가요?"
    choices: ["정보 누락(Omission)", "환각(Hallucination)", "존재하는 정보의 확인"]
    answer: 2
    explanation: "AI 심판관은 기록에 포함된 정보를 확인하는 '존재' 파악에는 뛰어나지만, 빠진 정보를 찾아내는 '부재' 파악에는 어려움을 겪습니다."
  - question: "진료 기록 도우미 AI가 작성한 문서에서 가장 흔하게 발생하는 오류는 무엇인가요?"
    choices: ["정보 누락(Omission)", "환각(Hallucination)", "오타 발생"]
    answer: 0
    explanation: "앰비언트 AI(Ambient AI)가 작성한 진료 기록에서 가장 지배적인 오류는 중요한 정보가 기록되지 않는 누락 오류입니다."
  - question: "AI 심판관(LLM-as-a-judge)이 정보를 누락을 감지할 때의 성능은 어느 정도인가요?"
    choices: ["사람 수준", "매우 뛰어남", "무작위 확률과 비슷함(Chance levels)"]
    answer: 2
    explanation: "연구에 따르면 정보의 부재를 찾아낼 때 AI 심판관의 성능은 무작위로 찍는 것과 비슷한 수준인 것으로 나타났습니다."
lang: ko
ref: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes
audio: 2026-09-02-LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes.mp3
permalink: /2026/09/02/LLM-Judges-Verify-Presence-Not-Absence-Omission-Blindness-in-AI-Clinical-Notes/
---

상상해보세요. 병원을 방문해 의사와 진지한 상담을 나눴습니다. 진료가 끝난 후, AI 비서가 당신의 진료 기록을 대신 작성해주었죠. 꼼꼼히 읽어보니 의사가 했던 말들이 꽤 잘 정리된 것 같아 안심이 됩니다. 하지만 만약, 어제부터 시작된 가슴 통증이라는 결정적인 정보가 쏙 빠져 있다면 어떨까요? 이 불완전한 기록을 바탕으로 처방을 받는다면 과연 안전할까요?

최근 병원 현장에서는 의사와 환자의 대화를 듣고 자동으로 진료 기록 초안을 작성해주는 '앰비언트 AI(Ambient AI, 진료 현장 기록 도우미)' 도입이 늘고 있습니다. 편리함은 크지만, 기록에서 중요한 정보가 의도치 않게 생략되는 '누락(Omission)' 오류는 여전히 해결해야 할 큰 숙제입니다. [출처 12](https://arxiv.org/abs/2608.31016) 오늘은 이 문제를 해결하고자 도입된 'AI 심판관'이 왜 생각보다 똑똑하지 못한지, 그 이유와 한계를 알기 쉽게 풀어보겠습니다.

## 이게 왜 중요한가요?

의료 현장에서 진료 기록은 환자의 건강을 지키는 가장 기본적이고도 핵심적인 데이터입니다. 기록에 중요한 증상이 누락되면 의사가 오진을 내리거나, 처방이 어긋날 위험이 있습니다. 이를 방지하기 위해 사람 대신 AI를 심판관(LLM-as-a-Judge)으로 세워 기록을 검사하게 합니다. [출처 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) 

하지만 만약 이 'AI 심판관'마저 빠진 정보를 제대로 찾아내지 못한다면 어떻게 될까요? 의료 사고의 위험은 여전히 남아있고, 우리가 사용하는 AI 비서가 사실은 '구멍 뚫린 기록'을 만들고 있는데 이를 평가하는 시스템조차 그 구멍을 발견하지 못하는 심각한 상황에 놓이게 됩니다.

## 쉽게 이해하기: '정답지'가 없는 시험 채점

AI 심판관이 왜 누락된 정보를 찾지 못하는지, '시험 채점' 상황에 빗대어 비유해 보겠습니다.

AI 심판관을 '정답지를 들고 학생의 답안지를 채점하는 교사'라고 생각해 보세요.

*   **존재 확인(Presence):** 학생이 답안지에 "1번 답은 A이다"라고 적었는지 확인하는 것은 매우 쉽습니다. 답안지에 'A'라는 글자가 명확히 보이기 때문입니다. AI는 이처럼 특정 키워드가 기록에 포함되어 있는지 확인하는 능력은 매우 뛰어납니다. [출처 2](https://arxiv.org/pdf/2608.31016)
*   **부재 확인(Absence):** 반면, 교사가 "이 학생이 답안지에 써야 할 내용을 빼먹지는 않았는가?"를 확인하는 것은 차원이 다른 문제입니다. 학생이 적지 않은 내용을 찾아내려면, 머릿속에 정답지 전체를 완벽하게 떠올리고 답안지의 모든 줄과 일일이 대조해야 하기 때문입니다.

최근 진행된 'OmissionBench' 프로젝트에 따르면, AI 심판관은 기록에 '무엇이 포함되어 있는지'는 강력하게 확인하지만, '무엇이 빠져 있는지'를 찾아내는 데는 거의 무작위로 찍는 수준(chance levels)의 성능을 보였습니다. [출처 3](https://github.com/composo-ai/omission-bench), [출처 13](https://arxiv.org/html/2608.31016v1) 즉, AI는 기록이 담고 있는 '결과'만 볼 뿐, 기록되지 않은 '빈 공간'을 인지하는 능력이 현저히 부족한 것입니다. 학계에서는 이를 '누락 맹점(Omission Blindness)'이라고 부릅니다.

## 현재 상황은 어떤가요?

이미 많은 의료 AI 시스템이 진료 기록의 품질을 평가하기 위해 AI 심판관을 활용하고 있습니다. [출처 10](https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_) 하지만 현실적인 성능은 냉정합니다. 연구 결과에 따르면, 실제로 AI가 작성한 진료 기록의 약 3.45%는 정보 누락 오류를 포함하고 있습니다(환각 오류는 1.47%). [출처 18](https://www.nature.com/articles/s41746-025-01670-7) 

문제는 이러한 누락을 걸러내야 할 AI 심판관들이 '존재'만 보고 '부재'는 보지 못한다는 점입니다. [출처 2](https://arxiv.org/pdf/2608.31016) 심지어 평가를 맡은 AI가 검사 대상인 기록을 만든 AI와 비슷한 사고방식을 지니고 있어, 같은 오류를 반복하거나 그냥 지나치기도 합니다. [출처 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)

## 앞으로 어떻게 될까요?

AI 심판관의 한계가 명확해지면서, 업계에서는 이를 극복하기 위한 다각도의 시도들이 이루어지고 있습니다.

1.  **결정론적 검증 도구 도입:** AI의 판단에만 의존하지 않고, 필수 키워드 체크와 같은 간단하고 확실한 코드로 작성된 규칙을 병행하는 방식입니다. [출처 4](https://www.youtube.com/watch?v=BPXFDC7WHSk)
2.  **다중 평가 체계:** 한 명의 AI 심판관이 아니라, 여러 모델 혹은 다중 에이전트 시스템을 활용해 정보를 서로 교차 검증하는 시스템을 구축하고 있습니다. [출처 14](https://www.nature.com/articles/s41746-025-02005-2)
3.  **인간의 참여:** 결국 안전이 최우선인 의료 분야에서는 AI가 모든 것을 평가하기보다, 인간 전문가인 의사가 AI의 검토 결과를 최종적으로 확인하는 '인간 중심 평가'가 여전히 가장 중요한 핵심입니다. [출처 17](https://arxiv.org/html/2607.18828)

우리는 이제 AI가 "무엇을 해낼 수 있는지"를 넘어, "무엇을 놓치고 있는지"를 꼼꼼하게 따져야 하는 시점에 와 있습니다.

## MindTickleBytes의 AI 기자 시선

AI를 심판관으로 세우는 것은 편리하지만, '존재'와 '부재'를 구분하는 것은 지능의 매우 다른 차원입니다. 기록되지 않은 '침묵'을 읽어낼 수 없는 AI에게 우리의 건강을 온전히 맡기기엔 아직 갈 길이 멉니다.

## 참고자료
1. [2608.31016] LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/abs/2608.31016)
2. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It (https://arxiv.org/pdf/2608.31016)
3. GitHub - composo-ai/omission-bench: OmissionBench harness: code (https://github.com/composo-ai/omission-bench)
4. Replace Your LLM Judge With 10 Lines of pytest - YouTube (https://www.youtube.com/watch?v=BPXFDC7WHSk)
5. LLM-as-a-judge: a complete guide to using LLMs for evaluations (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
7. LLM-as-a-Judge Simply Explained: The Complete Guide (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
8. Position Bias in LLM Judges: Measurement and Mitigation (https://mbrenndoerfer.com/writing/position-bias-in-llm-judges)
9. LLMs bow to pressure, changing answers when challenged (https://www.computerworld.com/article/4023989/llms-bow-to-pressure-changing-answers-when-challenged-deepmind-study.html)
10. Continual Monitoring of Note Quality At Scale (https://www.linkedin.com/posts/catherine-chen-5851a6a0_continual-monitoring-of-note-quality-at-scale-activity-7496283957693448192-ksR_)
11. LLM Judges Are Unreliable (https://www.cip.org/blog/llm-judges-are-unreliable)
12. LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes (https://arxiv.org/abs/2608.31016v1)
13. LLM Judges Verify Presence, Not Absence (https://arxiv.org/html/2608.31016v1)
14. Evaluating clinical AI summaries with large language models as judges (https://www.nature.com/articles/s41746-025-02005-2)
17. Evaluating medical AI under missing information (https://arxiv.org/html/2607.18828)
18. A framework to assess clinical safety and hallucination rates of LLMs for medical text summarisation (https://www.nature.com/articles/s41746-025-01670-7)