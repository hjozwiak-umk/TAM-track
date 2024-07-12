import numpy as np
from tam_track import predict_TAM

# Define your parameters here
file_path = 'TAM_max.dat' # Reference TAM(E) datapoints based on preliminary calculations
min_energy_for_fitting = 60 # Power-law will be fitted for E > 60 cm-1
energy_offset = 221.9215 # The internal energy of CO in j = 8 and N2 in j=6.
output_file = 'TAM_prediction.txt' # Output file.
enable_plotting = True

# Define a kinetic energy grid
energy_grid = np.concatenate([
    np.arange(1, 51, 1),
    np.arange(50, 101, 2),
    np.arange(100, 301, 5),
    np.arange(300, 501, 10),
    np.arange(500, 1001, 100),
    np.array([1500, 2000])
])

# Run the analysis
predict_TAM(
    file_path=file_path,
    min_energy_for_fitting=min_energy_for_fitting,
    energy_offset=energy_offset,
    energy_grid=energy_grid,
    output_file=output_file,
    enable_plotting=enable_plotting
)

