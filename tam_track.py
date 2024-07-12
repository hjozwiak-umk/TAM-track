# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Enable LaTeX style font rendering in matplotlib
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=22)

def power_law(x, a, b):
    """Power law function."""
    return a * np.power(x, b)

def predict_TAM(file_path, min_energy_for_fitting, energy_offset, energy_grid, output_file="TAM_prediction.txt", enable_plotting=True):
    """
    This function analyzes the relationship between the maximum total angular momentum (TAM)
    required to converge quantum scattering calculations and the total energy. It serves the following purposes:

    1. Reads energy and TAM_max data from a specified file.
    2. Applies a power law fit to the data above a specified energy threshold.
    3. Predicts TAM_max values for a given energy grid using the fitted power law model.
    4. Optionally plots the original data, the power law fit, and the predicted values.
    5. Outputs the predictions to a specified file.

    Parameters:
        file_path (str): Path to the input data file containing energy and TAM_max values.
        min_energy_for_fitting (float): Minimum energy threshold for including data points in the fit.
        energy_offset (float): Offset added to each energy grid point for prediction, typically representing a physical shift in energy.
        energy_grid (numpy.array): Array of energy values for which TAM_max will be predicted.
        output_file (str): Path to the output file where predictions will be saved.
        enable_plotting (bool, optional): If True, plots the data, fit, and predictions; defaults to True.

    Returns:
        numpy.array: Parameters of the fitted power law model.
    """
    
    # Read data
    data = np.loadtxt(file_path, delimiter='\t')
    energy = data[:, 0]
    TAM_max = data[:, 1]

    # Filter data
    filtered_indices = energy > min_energy_for_fitting
    energy_filtered = energy[filtered_indices]
    TAM_max_filtered = TAM_max[filtered_indices]

    # Fit the power law
    params_power, _ = curve_fit(power_law, energy_filtered, TAM_max_filtered, p0=[1, 1])

    # Predictions for higher energies
    high_energy = energy_grid + energy_offset
    predicted_TAM_max_power = np.ceil(power_law(high_energy, *params_power)).astype(int)

    # Plotting
    if enable_plotting:
        plt.figure(figsize=(10, 8))
        plt.scatter(energy, TAM_max, color='blue', label='Data')
        plt.plot(energy, power_law(energy, *params_power), 'r-', label=f'$a E^b$, $a={params_power[0]:.2f}$, $b={params_power[1]:.2f}$')
        plt.scatter(high_energy, predicted_TAM_max_power, color='red', marker='o', facecolors='none', label='Predicted by $a E^b$')
        plt.xscale('log')
        plt.yscale('log')

        # Add vertical line at the energy offset
        if energy_offset > 0:
            plt.axvline(x=energy_offset, color='gray', linestyle='--', linewidth=1)
            # Add rotated text to indicate the energy offset
            # Adjust the vertical position through alpha (between 1 and 10)
            alpha = 3
            plt.text(energy_offset, plt.ylim()[0] * alpha, 'Energy offset', rotation=90, verticalalignment='bottom', color='gray')

        plt.xlabel(r'Energy (cm$^{-1}$)')
        plt.ylabel(r'$\mathrm{TAM}_{\mathrm{max}}$')
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

    # Save predictions
    np.savetxt(output_file, np.column_stack((energy_grid, predicted_TAM_max_power)), fmt=['%0.4f', '%d'], header='Energy TAM_max')

    return params_power
