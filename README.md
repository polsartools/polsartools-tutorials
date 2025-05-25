# `polsartools` Example Notebooks

Welcome to the **`polsartools` Example Notebooks** repository! This repo contains a collection of Jupyter notebooks showcasing various features and usage of the [polsartools](https://github.com/Narayana-Rao/polsartools) package.

These notebooks serve as hands-on tutorials and demonstrate how to use the core functionalities of Polsartools with various SAR sensors.

## Overview

This repository includes a set of example notebooks that you can run to explore and learn how to use **`polsartools`**. These notebooks cover a variety of use cases and will help you get up to speed with the package quickly.

## How to Use the Notebooks

To run the notebooks in this repository, follow these steps:

### 1. Install **`polsartools`** Package

Before running the notebooks, you'll need to install the core **Polsartools** package. 

You can install it using `pip`:

```bash
pip install polsartools
```

If you encounter an error like "function not found" or need the latest version, you can install the updated version directly from GitHub:

```bash
pip install git+https://github.com/Narayana-Rao/polsartools.git#egg=polsartools
```

## Troubleshooting

### Error due to GDAL installation:
If you face issues related to GDAL (e.g., "GDAL not found" or installation errors), try installing GDAL using `conda`:

```bash
conda install -c conda-forge gdal