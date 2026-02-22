import pandas as pd

df = pd.read_csv("results/affinity_le.csv")
alpha = 0.1
max_aff = df["Affinity"].min()  # strongest binding = most negative

def td_signal(aff, max_aff):
    return alpha*(aff/max_aff)

td_results = {}
for ligand in ["thymoquinone","haloperidol","selegiline","memantine"]:
    aff = df[(df["Target"]=="DRD2") & (df["Ligand"]==ligand)]["Affinity"].values[0]
    td_results[ligand] = td_signal(aff, max_aff)

print("Simulated TD RPE signals (DRD2):", td_results)