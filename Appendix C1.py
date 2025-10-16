
import numpy as np
import pandas as pd

def azimuth_to_unit_vector(az_deg):
    az_rad = np.deg2rad(az_deg)
    return np.cos(az_rad), np.sin(az_rad)

def compute_s_value(az_structure, az_star):
    x_p, y_p = azimuth_to_unit_vector(az_structure)
    x_s, y_s = azimuth_to_unit_vector(az_star)
    return np.sqrt((x_p - x_s)**2 + (y_p - y_s)**2)

data = [
    {"Structure": "Khufu", "Azimuth": 90.9},
    {"Structure": "Khafre Valley Temple", "Azimuth": 90.6},
    {"Structure": "Menkaure", "Azimuth": 91.1},
    {"Structure": "Sphinx", "Azimuth": 90.2},
    {"Structure": "Osiris Shaft", "Azimuth": 91.8},
    {"Structure": "Khentkawes Complex", "Azimuth": 91.6},
    {"Structure": "Unfinished Pyramid", "Azimuth": 91.5},
]

alnitak_az_2500 = 89.3
alnitak_az_4400 = 90.9

results = []
for entry in data:
    name = entry["Structure"]
    az = entry["Azimuth"]
    delta_az_2500 = abs(az - alnitak_az_2500)
    delta_az_4400 = abs(az - alnitak_az_4400)
    s_2500 = compute_s_value(az, alnitak_az_2500)
    s_4400 = compute_s_value(az, alnitak_az_4400)
    results.append({
        "Structure": name,
        "Structure Azimuth (°)": az,
        "Azimuth (2500 BCE)": alnitak_az_2500,
        "ΔAz (2500 BCE)": delta_az_2500,
        "S (2500 BCE)": s_2500,
        "Azimuth (4400 BCE)": alnitak_az_4400,
        "ΔAz (4400 BCE)": delta_az_4400,
        "S (4400 BCE)": s_4400
    })

df = pd.DataFrame(results)
print(df.to_string(index=False, float_format="%.5f"))
