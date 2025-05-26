# `polsartools` Example Notebooks

Welcome to the **`polsartools` Example Notebooks** repository! This repo contains a collection of Jupyter notebooks showcasing various features and usage of the [polsartools](https://github.com/Narayana-Rao/polsartools) package.

These notebooks serve as hands-on tutorials and demonstrate how to use the core functionalities of Polsartools with various SAR sensors.

## Overview

This repository includes a set of example notebooks that you can run to explore and learn how to use **`polsartools`**. These notebooks cover a variety of use cases and will help you get up to speed with the package quickly.

## How to Use the Notebooks

To run the notebooks in this repository, follow these steps:

### 1. Install **`gdal`** Package
Installing `gdal` via `pip` may fail. Therefore, we recommend using conda to install it:
```bash
conda install gdal -c conda-forge
```

### 2. Install **`polsartools`** Package

Before running the notebooks, you'll need to install the core **`polsartools`** package. 

**Option A:** Install from PyPI `pip` (stable release)

```bash
pip install polsartools
```

**Option B:**  Install the latest version from GitHub (if you need recent updates or fixes)

```bash
pip install git+https://github.com/Narayana-Rao/polsartools.git#egg=polsartools
```
> **Note:** If youIf you encounter a `"module not found"` error or require newer features, prefer the [GitHub installation](https://github.com/Narayana-Rao/polsartools).

### 3. Verify the Installation

After successfully installing `polsartools`, you can verify it by importing the package:

```bash
import polsartools as pst
```

If this runs without errors, you're ready to explore and run the notebooks.
