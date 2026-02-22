import subprocess, os

vina = "vina"
targets = {"DRD2":"configs/DRD2.txt","MAOB":"configs/MAOB.txt","NMDA":"configs/NMDA.txt"}
ligands = ["thymoquinone","haloperidol","selegiline","memantine"]

os.makedirs("results", exist_ok=True)

for target, config in targets.items():
    for ligand in ligands:
        out_dir = f"results/{target}/{ligand}"
        os.makedirs(out_dir, exist_ok=True)
        out_pdbqt = f"{out_dir}/{ligand}_out.pdbqt"
        log_file = f"{out_dir}/docking.log"
        
        subprocess.run([
        vina,
        "--receptor", f"receptors/{target}.pdbqt",
        "--ligand", f"ligands/{ligand}.pdbqt",
        "--center_x", "9.2",
        "--center_y", "-2.1",
        "--center_z", "34.5",
        "--size_x", "22",
        "--size_y", "22",
        "--size_z", "22",
    "--exhaustiveness", "10",
    "--num_modes", "10",
    "--energy_range", "4",
    "--out", out_pdbqt,
    ], check=True, capture_output=True, text=True)
    print(f"[✓] {ligand} docked to {target}")