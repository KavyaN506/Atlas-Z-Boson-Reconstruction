from pathlib import Path
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ATLAS Z Boson Reconstruction",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
FIGURES = ROOT / "figures"

st.markdown(
    """
    <div style="text-align:center; padding: 0.3rem 0 0.8rem 0;">
      <h1>⚛️ ATLAS Z Boson Reconstruction</h1>
      <h3>Dimuon Resonance Analysis with ATLAS Open Data</h3>
      <p>Educational particle-physics analysis · 13 TeV · ATLAS 2-lepton sample</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Analysis navigator")
section = st.sidebar.radio(
    "Explore",
    ["Overview", "Mass spectrum", "Fit validation", "Selection robustness", "Methodology & sources"],
)
st.sidebar.markdown("---")
st.sidebar.caption("Built with Python and Streamlit")
st.sidebar.link_button("View GitHub repository", "https://github.com/KavyaN506/Atlas-Z-Boson-Reconstruction")
st.sidebar.link_button("Open CERN Open Data record", "https://opendata.cern.ch/record/15003")

if section == "Overview":
    st.subheader("Project overview")
    st.write(
        "This dashboard presents the results of a reproducible educational analysis "
        "of the ATLAS Open Data dimuon sample. Selected opposite-charge muons are "
        "combined to reconstruct the invariant-mass spectrum, then the Z-boson "
        "resonance region is modelled with a Gaussian signal and quadratic background."
    )

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Selected pair entries", "226,483")
    m2.metric("Fitted peak", "90.828 GeV")
    m3.metric("Fit covariance error", "± 0.011 GeV")
    m4.metric("Reduced χ²", "1.004")

    st.info(
        "Scope: this is an educational ATLAS Open Data analysis, not a precision "
        "measurement or an official ATLAS result. The fit covariance uncertainty "
        "does not include a complete systematic uncertainty evaluation."
    )

    st.subheader("Analysis at a glance")
    st.markdown(
        """
        - Inspect the ROOT `mini` tree with Uproot and Awkward Array
        - Apply trigger, muon identification, pT and pseudorapidity selections
        - Construct opposite-charge dimuon candidates
        - Reconstruct invariant mass from four-momentum
        - Fit the resonance and inspect residuals and pulls
        - Test robustness against the muon pT threshold
        """
    )
    st.success("The notebook and figures are available in the linked GitHub repository.")

elif section == "Mass spectrum":
    st.subheader("Final dimuon invariant-mass spectrum")
    image_path = FIGURES / "atlas_z_dimuon_mass_spectrum.png"
    if image_path.exists():
        st.image(str(image_path), use_container_width=True,
                 caption="Final displayed spectrum and Gaussian-plus-quadratic fit")
    else:
        st.warning("Figure not found. Confirm the PNG is committed in the repository's figures/ folder.")
    st.markdown(
        "The final displayed histogram uses 80 bins over 70–110 GeV. "
        "The fit is performed in the 85–97 GeV interval with matching histogram binning."
    )

elif section == "Fit validation":
    st.subheader("Residuals and pull diagnostics")
    image_path = FIGURES / "atlas_z_fit_residuals_pulls.png"
    if image_path.exists():
        st.image(str(image_path), use_container_width=True,
                 caption="Residual and pull diagnostics for the final nominal fit")
    else:
        st.warning("Figure not found. Confirm the PNG is committed in the repository's figures/ folder.")
    st.markdown(
        """
        **Nominal fit summary**

        | Parameter | Result |
        |---|---:|
        | Peak, μ | 90.828248 GeV |
        | Covariance uncertainty | 0.011227 GeV |
        | Gaussian width, σ | 1.933044 GeV |
        | Reduced χ² | 1.004412 |
        | Mean pull | 0.004350 |
        | Pull standard deviation | 0.867923 |
        | Maximum absolute pull | 1.794683 |
        """
    )
    st.caption("Reported covariance error is fit-local; systematic uncertainties were not fully evaluated.")

elif section == "Selection robustness":
    st.subheader("Muon pT threshold robustness")
    data = pd.DataFrame(
        {
            "pT threshold (GeV)": [25, 27, 30],
            "Pair entries": [226483, 211512, 186627],
            "Fitted peak (GeV)": [90.829451, 90.841565, 90.870210],
            "Reduced chi-square": [1.126847, 1.110442, 0.992469],
        }
    )
    st.dataframe(data, hide_index=True, use_container_width=True)
    st.line_chart(data.set_index("pT threshold (GeV)")["Fitted peak (GeV)"])
    st.write(
        "Across these selections the fitted peak shifts by about 41 MeV, "
        "while selected pair entries decrease as the pT requirement becomes stricter."
    )
    st.caption(
        "These robustness values use an 85–97 GeV fit with 80 bins. "
        "They are distinct from the final displayed-spectrum fit configuration."
    )

else:
    st.subheader("Methodology")
    st.markdown(
        r"""
        **Dimuon invariant mass**

        $$m_{\mu\mu}^2 = (E_1 + E_2)^2 - |\vec{p}_1 + \vec{p}_2|^2$$

        **Fit model**

        $$f(m)=A\exp\left[-\frac{(m-\mu)^2}{2\sigma^2}\right]
        +a(m-91)^2+b(m-91)+c$$
        """
    )
    st.markdown("**Tools:** Python · Uproot · Awkward Array · NumPy · Pandas · Matplotlib · SciPy · Jupyter/Colab")
    st.markdown("**Dataset:** ATLAS 2-lepton educational Open Data, 13 TeV, 10 fb⁻¹")
    st.markdown(
        """
        - [CERN Open Data record 15003](https://opendata.cern.ch/record/15003)
        - DOI: `10.7483/OPENDATA.ATLAS.GQ1W.I9VI`
        - ROOT tree: `mini`
        - Input sample: `data_A.2lep.root`
        """
    )
    st.warning(
        "Limitations: educational sample; no precision-mass claim; full systematic "
        "uncertainty evaluation and matched Monte Carlo comparison are not included."
    )

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;">
      <p><b>Kavya Nair</b> · MCA Student, MANIT Bhopal</p>
      <p>Learning to extract physics from data, one event at a time.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
