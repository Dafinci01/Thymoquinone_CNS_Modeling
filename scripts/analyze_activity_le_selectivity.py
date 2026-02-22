import pandas as pd, re, os

targets = ["DRD2","MAOB","NMDA"]
ligands = ["thymoquinone","haloperidol","selegiline","memantine"]
heavy_atoms = {"thymoquinone":15,"haloperidol":22,"selegiline":14,"memantine":11}
records = []

for target in targets:
    for ligand in ligands:
        log_path = f"results/{target}/{ligand}/docking.log"
        with open(log_path) as f:
            for line in f:
                match = re.match(r"\s*1\s+(-?\d+\.\d+)", line)
                if match:
                    affinity = float(match.group(1))
                    le = affinity / heavy_atoms[ligand]
                    records.append({"Target":target,"Ligand":ligand,"Affinity":affinity,"LE":le})

df = pd.DataFrame(records)
df.to_csv("results/affinity_le.csv",index=False)

# Selectivity
sel = []
for ligand in ligands:
    sub = df[df["Ligand"]==ligand].sort_values("Affinity")
    best = sub.iloc[0]
    second = sub.iloc[1]
    sel.append({"Ligand":ligand,"Preferred_Target":best["Target"],
                "Selectivity":second["Affinity"]-best["Affinity"]})
pd.DataFrame(sel).to_csv("results/selectivity.csv",index=False)
print("[✓] Affinity, LE, and selectivity analysis complete")