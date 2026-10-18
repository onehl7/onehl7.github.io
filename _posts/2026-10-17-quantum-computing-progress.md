---
layout: post
title: "Quantum Computing: Current Status and Milestones"
date: 2026-10-17
last_reviewed: 2026-10-17
categories: [quantum]
excerpt: "A source-linked snapshot of quantum computing progress and selected milestones from 2020 onward."
---

## Current state of quantum technology

<section class="qtrl-status" aria-labelledby="qtrl-status-heading">
  <p class="eyebrow">Field snapshot</p>
  <h2 id="qtrl-status-heading">Progress is real, but practical fault tolerance is still a goal</h2>
  <p class="qtrl-reviewed">Last reviewed: <time datetime="{{ page.last_reviewed | date: '%Y-%m-%d' }}">{{ page.last_reviewed | date: "%-d %B %Y" }}</time></p>
  <p>Quantum computing has moved beyond proof-of-principle experiments: multiple platforms offer programmable processors, and researchers have demonstrated increasingly capable error-correction techniques. These remain platform-specific research results, however, and do not yet amount to a broadly useful, general-purpose fault-tolerant quantum computer.</p>
  <p>There is no universally adopted QTRL score for the whole field. A physical-qubit count, a logical-qubit experiment, and a deployed system measure different things, so this page tracks selected milestones rather than assigning one number to every technology.</p>
</section>

## A year-by-year journey

The timeline highlights selected milestones in quantum computing. It is not exhaustive, and progress in one platform does not represent every quantum technology.

<ol class="qtrl-timeline">
  <li>
    <time datetime="2026">2026</time>
    <div>
      <h3>Current view: progress is platform-specific</h3>
      <p>Research advances in logical qubits and error correction are promising, but one field-wide QTRL number would hide important differences between hardware approaches and between laboratory demonstrations and operational systems. This assessment was last reviewed on {{ page.last_reviewed | date: "%-d %B %Y" }}.</p>
    </div>
  </li>
  <li>
    <time datetime="2025">2025</time>
    <div>
      <h3>Roadmaps continue toward error-corrected systems</h3>
      <p>Industry roadmaps describe goals for scaling and integrating quantum hardware. Those targets are plans, not achieved readiness levels; performance must be judged against demonstrated results.</p>
      <a href="https://www.ibm.com/quantum/hardware" target="_blank" rel="noopener noreferrer">IBM Quantum hardware and system overview</a>
    </div>
  </li>
  <li>
    <time datetime="2024">2024</time>
    <div>
      <h3>Below-threshold error correction is demonstrated</h3>
      <p>Google reported that its Willow processor reduced logical errors as the surface-code array grew. This is a research milestone toward scalable logical qubits, not evidence that general-purpose fault-tolerant computing is already available.</p>
      <a href="https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/" target="_blank" rel="noopener noreferrer">Google: Willow and quantum error correction</a>
    </div>
  </li>
  <li>
    <time datetime="2023">2023</time>
    <div>
      <h3>Qubit count alone remains an incomplete measure</h3>
      <p>Progress was judged not only by physical qubit totals, but also by processor quality, error rates, and the ability to run useful circuits. Results across different hardware approaches were not directly interchangeable.</p>
    </div>
  </li>
  <li>
    <time datetime="2022">2022</time>
    <div>
      <h3>Error correction begins to show scaling benefits</h3>
      <p>Google reported a surface-code logical-qubit experiment where increasing code size reduced the logical error rate, an important step toward error-corrected systems.</p>
      <a href="https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/" target="_blank" rel="noopener noreferrer">Google Research: scaling a surface-code logical qubit</a>
    </div>
  </li>
  <li>
    <time datetime="2021">2021</time>
    <div>
      <h3>Physical processors pass 100 qubits</h3>
      <p>IBM introduced its 127-qubit Eagle processor. The milestone showed progress in physical scale, while useful computation still depended on improving quality, control, and error rates—not qubit count alone.</p>
      <a href="https://www.ibm.com/quantum/blog/127-qubit-quantum-processor-eagle" target="_blank" rel="noopener noreferrer">IBM: Eagle processor</a>
    </div>
  </li>
  <li>
    <time datetime="2020">2020</time>
    <div>
      <h3>Roadmaps focus on scaling systems</h3>
      <p>IBM published a development roadmap that paired larger processors with improvements to the quality and engineering of the full system. Its 65-qubit Hummingbird processor was part of that year's work.</p>
      <a href="https://www.ibm.com/quantum/blog/ibm-quantum-roadmap" target="_blank" rel="noopener noreferrer">IBM: quantum development roadmap</a>
    </div>
  </li>
</ol>

<p class="qtrl-note"><strong>How to read this:</strong> “Last reviewed” is the date this editorial snapshot was checked, not a claim that every milestone occurred or was independently re-evaluated on that date. Follow the linked sources for each organization's reported results.</p>
