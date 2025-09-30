
#%%

# import time
# from nbclient import NotebookClient
# from nbformat import read, write

# notebooks = [
#     "ESAR_dual_pol_GTC.ipynb",
#     # other notebooks...
# ]

# for nb in notebooks:
#     print(f"Running {nb}...")
#     start_time = time.time()
#     try:
#         with open(nb) as f:
#             nb_obj = read(f, as_version=4)
#         client = NotebookClient(nb_obj, timeout=600, kernel_name="python3")
#         client.execute()
#         with open(nb, "w") as f:
#             write(nb_obj, f)
#         elapsed = time.time() - start_time
#         print(f"{nb} ran successfully in {elapsed:.2f} seconds.\n")
#     except Exception as e:
#         elapsed = time.time() - start_time
#         print(f"{nb} failed after {elapsed:.2f} seconds. Skipping.\n")
#         print("Error output:")
#         print(str(e))

#%%

import subprocess
import time
import os
os.environ["TQDM_NOTEBOOK"] = "1"

notebooks = [
    # "00_Polarimetric_signatures.ipynb",
    # "ALOS2_Dual_pol.ipynb",
    # "ALOS2_full_pol.ipynb",
    # "Chandrayaan_II_DFSAR_Full_pol.ipynb",
    "ESAR_dual_pol_GTC.ipynb",
    "ESAR_Full_pol_GTC.ipynb",
    # "ISRO_ASAR.ipynb",
    # "RADARSAT-2_FP.ipynb",
    # "RISAT_CP.ipynb",
    # "UAVSAR_GRD_pol_decompositions.ipynb",
    # "NISAR_GSLC_Full_pol.ipynb",
    # "NISAR_RSLC_Full_pol.ipynb",
    # "NISAR_GSLC_Dual_pol.ipynb",
    # "NISAR_RSLC_Dual_pol.ipynb",
]

for nb in notebooks:
    print(f"Running {nb}...")
    start_time = time.time()
    try:
        result = subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", nb],
            check=True,
            capture_output=True,
            text=True
        )
        elapsed = time.time() - start_time
        print(f"{nb} ran successfully in {elapsed:.2f} seconds.\n")
    except subprocess.CalledProcessError as e:
        elapsed = time.time() - start_time
        print(f"{nb} failed after {elapsed:.2f} seconds. Skipping.\n")
        print("Error output:")
        print(e.stderr)
#%%
# import os
# os.environ["TQDM_NOTEBOOK"] = "0"
# import papermill as pm
# import time

# notebooks = [
#     "ESAR_dual_pol_GTC.ipynb",
#     "ESAR_Full_pol_GTC.ipynb",
# ]

# for nb in notebooks:
#     print(f"Running {nb}...")
#     start_time = time.time()
#     try:
#         pm.execute_notebook(
#             nb,
#             nb.replace(".ipynb", "_executed.ipynb")
#         )
#         elapsed = time.time() - start_time
#         print(f"{nb} ran successfully in {elapsed:.2f} seconds.\n")
#     except Exception as e:
#         elapsed = time.time() - start_time
#         print(f"{nb} failed after {elapsed:.2f} seconds. Skipping.\n")
#         print("Error output:")
#         print(str(e))

#%%