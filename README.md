# Thymoquinone_CNS_Modeling

Computational neuropharmacology pipeline integrating **multi-target CNS docking**, **control-ligand benchmarking**, and **neural / behavioral interpretation*.

---

## Project Rationale

Natural compounds are often described as *neuroprotective* without mechanistic grounding.  
This project evaluates **thymoquinone** against established CNS drug targets and maps molecular-level interactions to **EEG signatures** and **reinforcement learning (RL) parameters**.

---

## CNS Targets and Controls

### Target Receptors
- **Dopamine D2 receptor (DRD2)** — reward learning, motivation
- **MAO-B** — dopamine metabolism, neurodegeneration
- **NMDA receptor** — synaptic plasticity, cortical oscillations

### Control Ligands
- **Haloperidol** — D2 antagonist  
- **Selegiline** — MAO-B inhibitor  
- **Memantine** — NMDA antagonist  

Control ligands provide pharmacological baselines and prevent over-interpretation of docking scores.

---

## Methods Overview

### Molecular Docking
- Docking engine: **AutoDock Vina**
- Identical grid definitions per receptor
- Best binding pose extracted per ligand
- Docking logs parsed programmatically
- Results exported to CSV for analysis

### Comparative Analysis
- Thymoquinone vs control ligands
- Rank-order binding affinity comparison
- Ligand efficiency normalization
- Statistical comparison across poses

---

## Neural and Behavioral Mapping

### Receptor → EEG Hypotheses

| Receptor | Expected EEG Effect |
|--------|--------------------|
| DRD2 | Beta-band modulation (13–30 Hz) |
| MAO-B | Theta–beta coupling |
| NMDA | Gamma-band power (30–80 Hz) |

### EEG → Reinforcement Learning Parameters

| Neural Effect | RL Parameter |
|--------------|-------------|
| Dopamine tone | Learning rate (α) |
| D2 signaling | Reward sensitivity |
| NMDA plasticity | Value update stability |
| Oscillatory balance | Exploration–exploitation tradeoff |

---
##project structure

Thymoquinone_CNS_Modeling/
├── README.md
├── ligands/        # Thymoquinone + control ligands (PDBQT)
├── receptors/      # CNS receptor structures
├── configs/        # AutoDock Vina configuration files
├── scripts/        # Docking, parsing, statistics, modeling
└── results/        # Logs, CSVs, statistical outputs

---

## Reproducibility
- Fixed docking parameters
- Control ligands for benchmarking
- Analysis-ready outputs
- Modular and extensible design

---

## Project Status
Active development

Planned extensions:
- Automated multi-ligand docking
- Expanded statistical testing
- EEG and RL simulation modules

---
