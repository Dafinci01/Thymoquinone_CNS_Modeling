# Thymoquinone_CNS_Modeling

Computational neuropharmacology pipeline integrating **multi-target CNS docking**, **control-ligand benchmarking**, and **neural/behavioral interpretation** aligned with NeuroData training goals.

---

## Project Rationale
Natural compounds are frequently labeled “neuroprotective” without mechanistic specificity.  
This project evaluates **thymoquinone** against established CNS drug targets and maps molecular effects to **EEG signatures** and **reinforcement learning (RL) parameters**.

---

## CNS Targets & Controls

### Target Receptors
- Dopamine D2 receptor (reward learning, motivation)
- MAO-B (dopamine metabolism, neurodegeneration)
- NMDA receptor (plasticity, cortical oscillations)

### Control Ligands
- **Haloperidol** — D2 antagonist  
- **Selegiline** — MAO-B inhibitor  
- **Memantine** — NMDA antagonist  

Controls provide pharmacological grounding and prevent over-interpretation of docking scores.

---

## Methods Overview

### Molecular Docking
- Engine: **AutoDock Vina**
- Identical grid parameters per receptor
- Best binding pose extracted per ligand
- Results logged and exported to CSV

### Comparative Analysis
- Thymoquinone vs control ligands
- Rank-order binding affinity comparison
- Ligand efficiency normalization
- Statistical comparison across poses

---

## Neural & Behavioral Mapping

### Receptor → EEG Hypotheses
| Receptor | Expected EEG Effect |
|--------|--------------------|
| D2 | Beta-band modulation (13–30 Hz) |
| MAO-B | Theta–beta coupling |
| NMDA | Gamma-band power (30–80 Hz) |

### EEG → Reinforcement Learning Parameters
| Neural Effect | RL Parameter |
|-------------|--------------|
| Dopamine tone | Learning rate (α) |
| D2 signaling | Reward sensitivity |
| NMDA plasticity | Value update stability |
| Oscillatory balance | Exploration–exploitation tradeoff |

---

## Repository Structure
