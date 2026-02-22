import pandas as pd
from scipy.stats import kruskal, mannwhitneyu

df = pd.read_csv("results/affinity_le.csv")
targets = df["Target"].unique()

for target in targets:
    subset = df[df["Target"]==target]
    groups = {lig: subset[subset["Ligand"]==lig]["Affinity"] for lig in subset["Ligand"].unique()}
    H,p = kruskal(*groups.values())
    print(f"[{target}] Kruskal-Wallis H={H:.2f}, p={p:.3f}")
    
    # Pairwise: TQ vs controls
    tq = groups["thymoquinone"]
    for ctrl in ["haloperidol","selegiline","memantine"]:
        U, pval = mannwhitneyu(tq, groups[ctrl], alternative="two-sided")
        print(f"{target} TQ vs {ctrl}: U={U}, p={pval:.3f}")