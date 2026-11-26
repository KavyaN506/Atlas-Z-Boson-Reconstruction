::: {align="center"}
# ATLAS Z Boson Reconstruction

### Reproducible Dimuon Resonance Analysis with ATLAS Open Data

```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Physics-Particle%20Physics-5e60ce?style=for-the-badge" alt="Particle Physics">`{=html}
`<img src="https://img.shields.io/badge/Data-ATLAS%20Open%20Data-6930c3?style=for-the-badge" alt="ATLAS Open Data">`{=html}
`<img src="https://img.shields.io/badge/Python-Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/Notebook-Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Google Colab">`{=html}
```{=html}
</p>
```
**A hands-on particle-physics data analysis project:** selecting muons,
reconstructing the dimuon invariant mass, fitting the Z-boson resonance,
and validating the fit.
:::

------------------------------------------------------------------------

## 🔭 Project at a glance

This project uses the educational ATLAS 2-lepton Open Data sample to
reconstruct the dimuon mass spectrum associated with the process

\[ Z `\rightarrow `{=tex}`\mu`{=tex}\^+ `\mu`{=tex}\^-. \]

The workflow covers ROOT data inspection, event and muon selection,
opposite-charge pair construction, four-momentum reconstruction,
resonance fitting, fit diagnostics, and selection robustness checks.

> **Scope:** This is an educational, reproducible analysis of an ATLAS
> Open Data sample. It is not a precision measurement or a scientific
> publication.

## 📊 Final invariant-mass spectrum

```{=html}
<!-- Upload the final plot to this repository under figures/atlas_z_dimuon_mass_spectrum.png -->
```
```{=html}
<p align="center">
```
`<img src="figures/atlas_z_dimuon_mass_spectrum.png" alt="ATLAS dimuon invariant mass spectrum with Gaussian plus quadratic background fit" width="850">`{=html}
```{=html}
</p>
```
## 🧪 Fit diagnostics

```{=html}
<p align="center">
```
`<img src="figures/atlas_z_fit_residuals_pulls.png" alt="Residual and pull diagnostics for the final nominal fit" width="850">`{=html}
```{=html}
</p>
```
## ✨ Key result

  Quantity                               Nominal result
  ------------------------------------ ----------------
  Muon transverse-momentum threshold             25 GeV
  Opposite-charge pair entries                  226,483
  Fitted peak                            **90.828 GeV**
  Fit covariance uncertainty                  0.011 GeV
  Gaussian width                              1.933 GeV
  Reduced chi-square                              1.004

The reported fit uncertainty is the covariance uncertainty from the fit.
It does **not** include a complete systematic uncertainty evaluation.

## 🧭 Analysis workflow

1.  **Inspect the ROOT data** --- identify the `mini` tree and relevant
    muon branches.
2.  **Select muons** --- apply identification, trigger,
    transverse-momentum, and pseudorapidity requirements.
3.  **Build dimuon candidates** --- combine selected muons and retain
    opposite-charge pairs.
4.  **Reconstruct invariant mass** --- calculate the mass from the
    pair's four-momentum.
5.  **Fit the resonance** --- fit a Gaussian signal plus a quadratic
    background in the 85--97 GeV region.
6.  **Validate** --- inspect residuals and pulls, compare fit windows,
    and vary the pT threshold.

## 📐 Reconstruction and fit model

For two muons, the invariant mass is calculated from their combined
four-momentum:

\[ m\_{`\mu`{=tex}`\mu`{=tex}}\^{2} = (E_1+E_2)\^2 -
`\left`{=tex}\|`\vec{p}`{=tex}\_1+`\vec{p}`{=tex}\_2`\right`{=tex}\|\^2.
\]

The fitted model is a Gaussian signal with a quadratic background:

\[
f(m)=A`\exp`{=tex}`\left[-\frac{(m-\mu)^2}{2\sigma^2}\right]`{=tex}+a(m-91)\^2+b(m-91)+c.
\]

The final displayed histogram uses 80 bins over 70--110 GeV. The fit is
performed in 85--97 GeV using the same histogram binning as the
displayed spectrum.

## 🛠️ Tools and libraries

-   Python
-   Uproot
-   Awkward Array
-   NumPy
-   Pandas
-   Matplotlib
-   SciPy
-   Jupyter / Google Colab

## 📁 Repository structure

``` text
atlas-z-boson-reconstruction/
├── README.md
├── notebooks/
│   └── atlas_z_dimuon_analysis.ipynb
└── figures/
    ├── atlas_z_dimuon_mass_spectrum.png
    └── atlas_z_fit_residuals_pulls.png
```

## ▶️ Reproduce the analysis

1.  Download the ROOT dataset from the [CERN Open Data
    record](https://opendata.cern.ch/record/15003).
2.  Open the notebook in Google Colab or Jupyter.
3.  Install the required packages if they are not already available.
4.  Update the ROOT file path in the notebook.
5.  Run the notebook cells in order.

The large ROOT data file is not included in this repository; retrieve it
from the official Open Data record.

## 📚 Dataset and citation

-   **Experiment:** ATLAS
-   **Collision energy:** 13 TeV
-   **Open Data record:** [15003 --- ATLAS 2-lepton educational
    sample](https://opendata.cern.ch/record/15003)
-   **DOI:** `10.7483/OPENDATA.ATLAS.GQ1W.I9VI`
-   **ROOT tree:** `mini`
-   **Input file used:** `data_A.2lep.root`

Please consult the official record for the dataset's scope,
documentation, and educational-use conditions.

## 🔎 Validation and robustness

The pT threshold was varied from 25 to 30 GeV. The fitted peak remained
stable across the tested selections, with a total shift of approximately
41 MeV.

    pT threshold   Pair entries   Fitted peak (GeV)   Reduced χ²
  -------------- -------------- ------------------- ------------
          25 GeV        226,483              90.829        1.127
          27 GeV        211,512              90.842        1.110
          30 GeV        186,627              90.870        0.992

These robustness-table values use the 85--97 GeV fit with 80 bins. They
are reported separately from the final displayed-spectrum fit.

## ⚠️ Limitations and next steps

-   The dataset is an educational ATLAS Open Data sample.
-   The analysis is not intended as a precision Z-mass measurement.
-   The fit covariance uncertainty is not a total uncertainty;
    systematic effects were not fully evaluated.
-   A matched Monte Carlo comparison was not completed because the large
    educational MC file could not be reliably accessed during this
    workflow.
-   Future extensions could include data--simulation comparison,
    detector calibration studies, and systematic uncertainty evaluation.

## 👩‍💻 Author

**Kavya Nair**\
MCA Student · MANIT Bhopal

Created as a learning and portfolio project in particle-physics data
analysis.

------------------------------------------------------------------------

::: {align="center"}
*Learning to extract physics from data, one event at a time.*
:::
