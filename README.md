# TAM-Track: Total Angular Momentum Tracker

Welcome to TAM-Track, a sophisticated computational tool designed to optimize and predict the maximum total angular momentum (TAM) required to achieve convergence in quantum scattering calculations. This tool leverages the relationship between TAM and total energy, using a power law fitting model to facilitate efficient parallel computations in challenging molecular collision systems.

## Installation

Clone the repository using:

`git clone [repository-link]`

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

You can install the required packages using:

`pip install numpy matplotlib scipy`

## Usage

Adjust parameters in predict_total_angular_momentum.py and execute:

`python run.py`

## Data Format

The script expects input data in a two-column format:

- Energy (cm-1)
- TAM_max

Tab-separated values are provided in an example file "TAM_max.dat".

## Description

The script `predict_total_angular_momentum.py` is designed to:
1. Read energy and `TAM_max` data from a specified file.
2. Filter the data based on a minimum energy threshold.
3. Fit a power law model to the filtered data.
4. Predict `TAM_max` values for an extended range of energies using the fitted model.
5. Optionally, plot both the original data along with the fitting curve and predictions.
6. Save the predictions to a designated output file.

This analysis is crucial for prediciting the number of total angular momenta that are needed to converge quantum scattering calculations 
for different collision energies.

## Background
The dynamics of colliding molecules and/or atoms are described by coupled-channel equations-sets of differential equations derived from the time-independent Schrödinger equation by expanding the total wave function of the scattering system in a chosen basis. This basis typically involves the eigenstates of the colliding molecules and spherical harmonics that describe the relative motion of the colliding partners, known as partial waves.

The expansion of the scattering wave function in partial waves is theoretically infinite, which poses significant computational challenges. To make the problem computationally feasible, the expansion must be truncated once the contribution of additional terms falls below a certain threshold, ensuring a satisfactory convergence of the cross-sections.

To simplify the structure of the coupled-channel equations they are typically solved in the total angular momentum (TAM) representation. In this representation, the equations become block-diagonal with respect to TAM and parity, which allows for simultaneous solution of the coupled-channel equations through parallelization.

However, just as the expansion in partial waves is in principle infinite, so too is the expansion in terms of TAM. In practice, the expansion is truncated based on a convergence criterion that determines when additional TAM contributions are negligible—below a specified threshold—to the desired accuracy of the cross-sections. This approach is critical in scattering calculations performed using tools such as MOLSCAT, HIBRIDON, or BIGOS, which can automatically assess convergence with respect to TAM.

### Parallelization
For complex systems such as diatomic-diatomic collisions, optimizing computation through parallelization—solving for separate TAM blocks and summing the results—is crucial. The key question becomes: How many TAMs are needed to converge the cross-sections?

### TAM-Track's Solution
TAM-Track addresses this by identifying the relationship between the maximum TAM required for convergence and total energy, which tends to follow a power law at higher energies. This observation aligns with classical expectations where energy is proportional to the square of angular momentum (E ~ J^2).

**Workflow**
- Run initial calculations with a scattering code to establish a baseline for convergence at various energy levels using a minimal rotational basis (noting that TAM(E) should remain consistent despite changes in the rotational basis).
- Record the maximum TAM needed at each energy point.
- Fit these data points to a power law.
- Use this model to predict required TAM values over a new grid of desired collision energies, considering specific molecular states (e.g., CO in J=8 and N2 in J=6, with an energy offset of approximately 222 cm-1).

## Test case: CO-N2 scattering
As a practical application of TAM-Track, we explore the quantum scattering of carbon monoxide (CO) in the j=8 rotational state and nitrogen (N2) in the j=6 rotational state.

The initial TAM values were obtained from preliminary scattering calculations where both CO and N2 were in the J=0 state. The convergence criterion was established such that the calculations terminated once four consecutive TAM blocks modified the largest elastic and the largest inelastic cross-section by less than  10-3 A^2.

The objective is now to predict how many TAM blocks are needed to achieve the same level of convergence for a set kinetic energy grid with CO in j=8 and N2 in j=6. The internal energies of the two molecules define an energy offset (ECO+EN2=222cm-1).

The power law is fitted to data points with energies greater than 60 cm-1. Predicted TAM values for different energies are then saved to a new file.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your enhancements.

