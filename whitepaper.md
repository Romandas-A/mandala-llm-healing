# 🧠 Mandala-Healing: Self-Evolving Knowledge Refinement for Language Models

---

## 1. Introduction

Large Language Models (LLMs) achieve remarkable fluency and broad knowledge coverage through pre-training and fine-tuning.  
However, even very large models contain:

- Inconsistencies,
- Hallucinations,
- Gaps in factual knowledge,
- Logical asymmetries.

Traditional retraining is costly, slow, and depends on new external data.

**Mandala-Healing** proposes a new idea:

> **Post-training internal healing**, where the model analyzes its own knowledge geometry, detects weak branches, self-generates missing information, tests it, and heals itself — without new external datasets.

This repository provides an open prototype for this idea.

---

## 2. Core Ideas

### 2.1 Mandala Projection

- We **project internal activations** (hidden states) into 2D/3D using UMAP or t-SNE.
- These projections form **mandala-like structures**.
- Symmetric clusters suggest healthy, coherent knowledge.
- Asymmetric or fragmented regions suggest missing or broken knowledge branches.

### 2.2 Healing Detection

- If answering a question activates a fragile branch, healing is triggered.
- Fragility detection uses simple metrics like:
  - Radial density imbalance,
  - Local curvature anomalies,
  - Asymmetrical clustering.

### 2.3 Self-Healing Cycle

The model itself:

1. **Generates sub-questions** to explore missing parts.
2. **Self-simulates** answers using its existing knowledge.
3. **Synthesizes corrections**.
4. **Proposes small, safe edits** to internal weights.

Healing is accepted only if automated testing shows improved answers without new errors.

### 2.4 Permanent Injection

- Edits are applied as **small bias vector changes** at selected layers.
- This method is simple and safe for initial prototypes.
- Future versions can extend to **low-rank updates** (e.g., LoRA, ROME).

---

## 3. Implementation Overview

This repository includes:

| Module | Description |
|:-------|:------------|
| `mandala_projection.py` | Project internal embeddings into low-dimensional space. |
| `gui_mandala_heal.py` | Visualize, click, and manually heal fragile branches. |
| `test_suite.py` | Simple QA evaluation using exact and fuzzy matching. |
| `permanent_inject.py` | Apply bias vector corrections to heal knowledge branches. |
| `autonomous_loop.py` | Prototype of self-question ➔ self-simulate ➔ self-test ➔ self-heal cycle. |
| `examples/` | Jupyter notebooks showing projections and healing examples. |

---

## 4. Procedures

### 4.1 Project Knowledge Mandala

- Pass sentences or questions through LLM.
- Collect hidden activations at specific layers.
- Apply UMAP/t-SNE to project into 2D.
- Identify asymmetric or broken clusters.

### 4.2 Detect Fragile Branches

- Calculate radial density variance.
- Optionally use simple clustering imbalance metrics.
- Highlight suspicious regions.

### 4.3 Healing Methods

- **Manual Healing** (via GUI):
  - Click on outlier points.
  - Suggest a correction manually.
- **Autonomous Healing**:
  - Model detects low-confidence or hallucinated answers.
  - Model generates sub-questions to explore.
  - Model proposes small weight corrections.
  - Healing accepted only after internal re-testing.

### 4.4 Permanent Correction

- Apply small bias-deltas to transformer MLP layers.
- Save healed model version.

---

## 5. Current Limitations

- Healing logic is early-stage — many improvements possible.
- Bias injection method is simple; better methods (e.g., LoRA) should be explored.
- Symmetry detection uses basic heuristics; topological metrics can improve detection.
- No full-scale evaluation experiments are published yet.

This repository focuses on the **concept** and **prototype code**,  
**not on publishing benchmark results**.

---

## 6. Future Directions

| Idea | Description |
|:-----|:------------|
| Multi-Projection Voting | Use multiple different projections to detect fragile regions more robustly. |
| Simulation-Based Research | Encourage model to simulate missing facts more realistically. |
| Fine-Grained Delta Injection | Switch to low-rank or adapter-based healing methods. |
| Scalable Healing | Run automated healing over thousands of questions in parallel. |
| Human Review Option | Allow human curators to approve/reject proposed healings. |
| Larger Model Testing | Try healing on larger LLMs (e.g., LLaMA, Falcon, GPT-J). |

---

## 7. How to Contribute

- Extend symmetry metrics.
- Improve the GUI.
- Build safer edit mechanisms.
- Expand self-questioning logic.
- Test healing on different domains.

Pull requests welcome!

---

## 8. License

MIT License — free for research, experimentation, and education.

---

## 9. Closing Note

Mandala-Healing is an open idea:  
**an invitation to rethink how LLMs can grow and repair themselves**  
after training — autonomously, geometrically, logically.

We hope it inspires further research and real-world applications.

❤️

*Created by Romandas-A (2025).*

---
