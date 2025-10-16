
import numpy as np
import pandas as pd

# Define constants
mass = 50000          # kg
width = 2.5           # m
height = 2.0          # m
g = 9.81              # m/s²
mu_static = 0.6       # Static friction coefficient

# Calculate tipping threshold
tipping_angle = np.degrees(np.arctan((width / 2) / height))  # ~38.7°

# Define incline angles from 5° to 35°
angles = np.arange(5, 36, 1)
results = []

# Perform force calculations for each incline
for theta in angles:
    theta_rad = np.radians(theta)
    gravity_force = mass * g * np.sin(theta_rad)
    friction_resistance = mu_static * mass * g * np.cos(theta_rad)
    slip = gravity_force > friction_resistance
    tip = theta >= tipping_angle

    # Classification logic
    if theta < 15:
        classification = "Stable"
    elif 15 <= theta < tipping_angle:
        classification = "Slip Likely" if slip else "Stable"
    else:
        classification = "Tipping Probable" if tip else "Slip Likely"

    results.append({
        "Incline (°)": theta,
        "Gravity Force (N)": round(gravity_force, 1),
        "Friction Resistance (N)": round(friction_resistance, 1),
        "Slip Risk": "Yes" if slip else "No",
        "Tipping Risk": "Yes" if tip else "No",
        "Classification": classification
    })

# Create and display dataframe
df = pd.DataFrame(results)
print(df)
