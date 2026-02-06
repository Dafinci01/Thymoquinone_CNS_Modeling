# Thymoquinone_CNS_Modeling
Alright. Here’s a **NeuroData-grade README.md** — tight, serious, zero fluff, and reviewer-proof. You can paste this directly.

---

# Thymoquinone_CNS_Modeling

## Overview

This repository implements an **in-silico neuropharmacology pipeline** to evaluate the CNS relevance of **thymoquinone** via multi-target molecular docking, control-ligand benchmarking, statistical comparison, and mechanistic mapping to **EEG dynamics and reinforcement learning (RL) parameters**.

The project is designed as a **computational neuroscience mini-proposal**, not a docking demo. It emphasizes interpretability, biological grounding, and reproducibility.

---

## Scientific Motivation

Natural compounds are frequently reported to exhibit “neuroprotective” or “cognitive” effects, yet mechanistic specificity is often unclear.
This project addresses that gap by asking:

> *Does thymoquinone show CNS-relevant binding profiles comparable to established neuroactive drugs, and what neural and behavioral signatures would such modulation imply?*

---

## Targets and Controls

### CNS Targets

Docking is performed against receptors with clear neural and behavioral relevance:

* **Dopamine D2 receptor** (reward learning, motivation, motor control)
* **MAO-B** (dopamine metabolism, neurodegeneration)
* **NMDA receptor** (synaptic plasticity, learning, cortical oscillations)

### Control Ligands

Established CNS drugs are used as benchmarks:

* **Haloperidol** — D2 antagonist (dopaminergic control)
* **Selegiline** — MAO-B inhibitor (dopamine preservation)
* **Memantine** — NMDA antagonist (excitatory modulation)

Controls anchor effect sizes and prevent over-interpretation of raw docking scores.

---

## Methods

### 1. Molecular Docking

* Docking performed using **AutoDock Vina**
* Identical grid definitions used across ligands per receptor
* Best binding affinity extracted from Vina log files
* Results stored in structured CSV format for analysis

### 2. Statistical Comparison

* Thymoquinone binding affinities compared against control ligands
* Effect sizes and rank-order comparisons emphasized over raw scores
* Statistical tests applied across poses where appropriate
* Focus on **relative selectivity**, not absolute potency

### 3. Ligand Efficiency

* Binding affinity normalized by molecular size
* Prevents bias toward larger ligands
* Enables fair comparison between natural compounds and synthetic drugs

---

## EEG and Neural Interpretation

Docking results are mapped to **expected neural signatures**, not treated as endpoints.

### Receptor → EEG Mapping

| Receptor         | Expected EEG Effect                                                  |
| ---------------- | -------------------------------------------------------------------- |
| D2 modulation    | Changes in **beta (13–30 Hz)** power and reward prediction signaling |
| MAO-B inhibition | Increased dopamine tone → **theta–beta coupling**                    |
| NMDA modulation  | Altered **gamma (30–80 Hz)** power and cortical synchronization      |

These mappings are grounded in established systems neuroscience literature.

---

## Reinforcement Learning Interpretation

Receptor-level effects are further translated into **computational behavioral parameters**:

| Neural Effect         | RL Parameter                     |
| --------------------- | -------------------------------- |
| Dopamine tone         | Learning rate (α)                |
| D2 signaling          | Reward sensitivity               |
| NMDA plasticity       | Value updating stability         |
| Cortical oscillations | Exploration–exploitation balance |

This allows hypotheses to be tested in **behavioral or EEG datasets**, even without wet-lab experiments.

---

## Project Structure

```
Thymoquinone_CNS_Modeling/
├── README.md
├── ligands/        # Thymoquinone + control ligands (PDBQT)
├── receptors/      # CNS receptor structures
├── configs/        # AutoDock Vina configuration files
├── scripts/        # Docking, parsing, statistics, modeling
└── results/        # Logs, CSVs, statistical outputs
```

---

## Reproducibility

* All docking parameters are explicit and version-controlled
* Control ligands ensure interpretability
* Output formats are analysis-ready (CSV, logs)
* Pipeline is modular and extensible

---

## Significance

This project demonstrates:

* Computational rigor beyond single-ligand docking
* Integration of **molecular**, **neural**, and **behavioral** levels
* Clear relevance to **neurodata analysis and modeling**

It is intentionally structured to align with **NeuroData / computational neuroscience training standards**.

---

## Status

Active development.
Next steps include:

* Automated multi-ligand docking
* Expanded statistical testing
* Parameterized EEG/RL simulation modules

---


