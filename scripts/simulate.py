import pandas as pd
import numpy as np

df = pd.read_csv("results/affinity_le.csv")

def binding_to_power_change(aff, receptor):
    if receptor=="DRD2": return np.tanh(-aff)*10   # beta/theta
    if receptor=="NMDA": return np.tanh(-aff)*15  # gamma
    if receptor=="MAOB": return np.tanh(-aff)*8   # alpha

for target in ["DRD2","NMDA","MAOB"]:
    for ligand in ["thymoquinone","haloperidol","selegiline","memantine"]:
        aff = df[(df["Target"]==target)&(df["Ligand"]==ligand)]["Affinity"].values[0]
        delta = binding_to_power_change(aff, target)
        print(f"{ligand} → {target} EEG ΔPower: {delta:.2f}%")