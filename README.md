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
