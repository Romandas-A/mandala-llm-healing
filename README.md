# 🧠 Mandala-Healing: Self-Evolving Knowledge Refinement for Language Models

> Post-training self-healing method for large language models based on Mandala symmetry analysis and autonomous knowledge refinement.

> **Field:** Artificial Intelligence · Machine Learning · LLM Post-Training · Self-Healing Models

---

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/Romandas-A/mandala-llm-healing">
    <img src="https://img.shields.io/badge/Built%20with-%F0%9F%A7%A0%20Mandala%20Healing-brightgreen" alt="Built with Mandala LLM Healing">
  </a>
</p>

---
<p align="center">
  <img src="mandala_preview.png" alt="Mandala-LLM-Healing Visualization" width="600">
</p>

## ✨ Overview

Traditional large language models (LLMs) are trained once on massive datasets,  
then often remain static — even if they have internal contradictions, missing facts, or logical inconsistencies.

There is **no natural way for models to repair themselves** once training is finished.  
Until now.

**Mandala-Healing** introduces a **new post-training phase**:

- Analyze the model’s **internal knowledge geometry**,
- Detect **weak or fragile branches** where knowledge is broken or missing,
- Trigger **self-healing cycles** — where the model generates sub-questions and internal simulations to fill gaps,
- **Test** if the healing improves answers,
- **Permanently inject** safe, minimal corrections into model weights.

This repository provides a working **proof-of-concept** system for Mandala-Healing,  
fully **open-source**, **transparent**, and **extendable**.

---

## 🧩 Mandala-Healing Principles

**Mandala-Healing** treats a trained language model like a living, evolving system.

- A model’s internal knowledge is structured as a **Mandala** —  
  a complex geometric map of facts, concepts, and logical relationships.

- **Healthy knowledge** appears as **symmetrical, well-organized branches**.

- **Broken knowledge** (missing facts, hallucinations, contradictions) manifests as **asymmetries, distortions, or fragile branches**.

By detecting and healing these weak areas,  
the model can **self-perfect** over time — without requiring external data or human retraining.

---

## ⚙️ Relation to Traditional Training

Mandala-Healing is designed as a **post-training evolution** phase —  
**not a replacement** for traditional pretraining or fine-tuning.

- **Traditional pretraining** (on large datasets) remains essential to give the model its basic world knowledge.
- **Fine-tuning** remains useful to specialize a model for specific domains.

**Mandala-Healing begins only after traditional training is finished:**

- It does not rely on new external datasets.
- It does not require expensive re-training cycles.
- It focuses on **detecting and repairing internal weaknesses** that were left behind during training.

In some cases, Mandala-Healing may even **generate new knowledge**:

- By identifying missing logical connections,
- By completing incomplete knowledge structures,
- By repairing fragile branches based on internal Mandala symmetry.

Thus, Mandala-Healing enables models to **grow beyond** their original training datasets —  
self-improving autonomously through internal geometric healing.

---

## 🛠️ The Core Healing Cycle

1. **Visualize Knowledge** — Project hidden-state activations into a 2D Mandala using UMAP or t-SNE.
2. **Detect Fragility** — Identify asymmetric, weak, or broken knowledge branches.
3. **Self-Ask and Simulate** — The model generates internal sub-questions to explore gaps.
4. **Self-Heal** — Propose small weight edits (e.g., tiny bias vector updates) based on internal simulations.
5. **Self-Test** — Healing is accepted only if testing shows improved answers.
6. **Permanent Repair** — Successful healing edits are injected directly into model weights.

---

## 🔥 What Makes Mandala-Healing Different

- **Self-generated healing.**  
  Healing comes entirely from within the model — no new external data is needed.

- **Minimal invasive edits.**  
  Healing uses small, safe internal corrections instead of costly full retraining.

- **Geometry becomes intelligence.**  
  Symmetry and balance of the Mandala become measurable indicators of knowledge health.

- **True self-evolution.**  
  The model can refine itself repeatedly, repairing errors and growing smarter over time.

- **Healing across multiple projections.**  
  Healing is not based on a single 2D view — Mandala-Healing explores many angles, layers, and projections to ensure robust evolution.

---

> 🧠 **Mandala-Healing is not fine-tuning.  
> It is not prompt engineering.  
> It is the next evolutionary step: models that can grow, heal, and evolve on their own.**

---

## 🌱 How the Idea Emerged

Mandala-Healing is an open idea —  
it was born while walking in a park and having deep conversations with ChatGPT,  
thinking about how models could heal and grow autonomously after their traditional training.

This repository is a **prototype and exploration**:

- It is **not yet validated** by large-scale experiments,
- It is **freely offered** to the community — to test, challenge, improve, or extend.

If you find it inspiring, useful, or if you want to build upon it —  
you are warmly invited to do so.

❤️

---

## 🛠️ Repository Contents

| File/Folder | Description |
|:------------|:------------|
| `README.md` | This page. Overview and quickstart instructions. |
| `whitepaper.md` | Full method description and procedures (honest, no fake experiments). |
| `requirements.txt` | Python dependencies list. |
| `mandala_projection.py` | Project internal activations into 2D Mandalas. |
| `gui_mandala_heal.py` | Clickable GUI to manually explore and heal knowledge branches. |
| `test_suite.py` | Simple exact and fuzzy answer evaluation tools. |
| `permanent_inject.py` | Script to permanently apply healing deltas into model weights. |
| `autonomous_loop.py` | Prototype self-healing cycle: detect weakness ➔ self-ask ➔ heal. |
| `examples/` | Example Jupyter notebooks to explore projections and self-healing.

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/Romandas-A/mandala-llm-healing.git
cd mandala-llm-healing

# Install Python dependencies
pip install -r requirements.txt

# Play with the Healing GUI
python gui_mandala_heal.py
