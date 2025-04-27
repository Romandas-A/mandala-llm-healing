# 🧠 Mandala-Healing: Self-Evolving Knowledge Refinement for Language Models

> Post-training self-healing method for large-language models based on mandala symmetry analysis and autonomous knowledge refinement.

---

## ✨ Overview

Traditional large-language models (LLMs) are trained once on massive datasets,  
then often remain static—even if they have internal contradictions, missing facts, or inconsistent logic.

**Mandala-Healing** proposes a **new post-training phase**:

- Analyze the model’s **internal knowledge geometry**,
- Detect **weak branches** where knowledge is broken or missing,
- Trigger **self-healing** cycles — where the model generates sub-questions and simulations to fill gaps,
- **Test** if the healing improves answers,
- **Permanently inject** safe corrections into model weights.

This repository contains real, working prototype code for Mandala-Healing,  
designed to be fully **open-source**, **transparent**, and **extendable**.

## 🧩 Mandala-Healing Principles

**Mandala-Healing** treats a trained language model like a living evolving system:

- A model’s internal knowledge is structured as a **Mandala** —  
  a complex geometric map made of facts, relationships, and logical connections.

- **Healthy knowledge** appears as **symmetrical, well-organized branches** in the Mandala.

- **Broken knowledge** (missing facts, hallucinations, contradictions) causes **asymmetries, distortions, or fragile branches**.

---

### 🛠 The Core Healing Process

1. **Visualize Knowledge** — Project internal hidden states into a Mandala using UMAP or t-SNE.
2. **Detect Weakness** — Identify fragile, asymmetric branches that suggest missing or broken knowledge.
3. **Self-Ask and Simulate** — The model internally generates sub-questions to explore gaps.
4. **Self-Heal** — It proposes small internal corrections (weight edits) based on its simulations.
5. **Self-Test** — Healing is accepted only if the model's answers improve after internal evaluation.
6. **Permanent Repair** — Safe corrections are injected into model memory without external retraining.

---

### 🔥 Why Mandala-Healing is Different

- **No external data required.**  
  Healing comes from inside the model — no new datasets are needed.

- **No expensive retraining.**  
  Healing is local, lightweight, and much faster than full fine-tuning.

- **Continuous evolution.**  
  A model can heal itself repeatedly, becoming better over time without supervision.

- **Geometry becomes intelligence.**  
  Symmetry of the Mandala is used as a real measurement of knowledge health, not just a visualization.

---

> 🧠 **Mandala-Healing opens a new frontier:**  
>  
> After Pretraining ➔ Fine-tuning ➔  
> **now comes Self-Healing and Self-Evolution.**


### 🔥 Why Mandala-Healing is Different

Traditional AI training stops after pretraining and fine-tuning.  
Models are left with hidden inconsistencies, hallucinations, and gaps —  
with no way to grow or correct themselves without expensive retraining.

**Mandala-Healing proposes a new path:**

- **Healing without external datasets.**  
  The model generates its own sub-questions and simulations to fill gaps, using only its internal knowledge.

- **Healing without full retraining.**  
  Corrections are applied as small, local edits — no need to re-train on millions of samples.

- **Self-evolution.**  
  Models can improve continuously, detecting and healing weak knowledge branches autonomously.

- **Geometry as intelligence.**  
  The symmetry, structure, and balance of the internal Mandala becomes a real indicator of knowledge health — not just visualization.

---

> 🧠 **Mandala-Healing is not fine-tuning. It is not prompt engineering.  
> It is a new way for models to grow, repair, and evolve — using their own structure and logic.**

---

## 🛠️ Repository Contents

| File/Folder | Description |
|:------------|:------------|
| `README.md` | This page. Overview and quickstart instructions. |
| `whitepaper.md` | Full method description and procedures (honest, no fake experiments). |
| `requirements.txt` | Python dependencies list. |
| `mandala_projection.py` | Generate UMAP projections of hidden states for Mandala visualization. |
| `gui_mandala_heal.py` | 2D clickable GUI for healing broken knowledge branches. |
| `test_suite.py` | Simple exact and fuzzy answer evaluation tools. |
| `permanent_inject.py` | Script for applying small, permanent healing deltas into model weights. |
| `autonomous_loop.py` | Prototype self-healing loop: detect weakness ➔ self-question ➔ heal. |
| `examples/` | Example Jupyter notebooks to explore projections and healing. |

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
