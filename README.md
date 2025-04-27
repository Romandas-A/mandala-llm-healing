# 🧠 Mandala-Healing: Self-Evolving Knowledge Refinement for Language Models

> Post-training self-healing method for large language models based on Mandala symmetry analysis and autonomous knowledge refinement.

---

## ✨ Overview

Traditional large language models (LLMs) are trained once on massive datasets,  
then often remain static — even if they have internal contradictions, missing facts, or logical inconsistencies.

There is **no natural way for models to repair themselves** once training is finished.  
Until now.

**Mandala-Healing** introduces a **new post-training phase**:

- Analyze the model’s **internal knowledge geometry**,
- Detect **weak or fragile branches** where knowledge is broken or missing,
- Trigger **self-healing cycles** — where the model generates sub-questions and simulations to fill gaps,
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
the model can **self-perfect** over time — without human intervention.

---

### 🛠 The Core Healing Cycle

1. **Visualize Knowledge** — Project internal activations into a Mandala using UMAP/t-SNE.
2. **Detect Fragility** — Identify asymmetric or broken knowledge branches.
3. **Self-Ask and Simulate** — Model generates sub-questions and imagined answers internally.
4. **Self-Heal** — Propose small memory corrections (e.g., bias vector updates).
5. **Self-Test** — Healing is accepted only if internal testing shows real answer improvement.
6. **Permanent Repair** — Safe healing edits are injected directly into model weights.

---

## 🔥 What Makes Mandala-Healing Different

- **Self-generated healing.**  
  Healing comes from inside the model — no external datasets needed.

- **Minimal invasive edits.**  
  Small corrections (e.g., bias adjustments) instead of expensive full retraining.

- **Geometry becomes intelligence.**  
  Symmetry and balance of the Mandala reflect real knowledge health.

- **True self-evolution.**  
  The model can autonomously refine itself, repair errors, and grow smarter over time.

- **Healing across multiple projections.**  
  One view is not enough — Mandala-Healing explores different angles, layers, and projections to build a robust self-healing process.

---

> 🧠 **Mandala-Healing is not fine-tuning.  
> It is not prompt engineering.  
> It is the next evolutionary step: models that can grow, heal, and evolve on their own.**

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
| `permanent_inject.py` | Script to permanently apply healing deltas to model weights. |
| `autonomous_loop.py` | Prototype self-healing cycle: detect weakness ➔ self-ask ➔ heal. |
| `examples/` | Example Jupyter notebooks to explore projections and self-healing.

---

## 🚀 Quickstart

```bash
# Clone the repository
git clone https://github.com/YOUR_USER/mandala-healing.git
cd mandala-healing

# Install Python dependencies
pip install -r requirements.txt

# Play with the Healing GUI
python gui_mandala_heal.py
