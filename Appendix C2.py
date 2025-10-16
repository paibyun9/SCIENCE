
import matplotlib.pyplot as plt
import numpy as np

# Monument identifiers (same order as Appendix C1.4)
structures = [
    'Khufu',
    'Khafre Valley Temple',
    'Menkaure',
    'Sphinx',
    'Osiris Shaft',
    'Khentkawes Complex',
    'Unfinished Pyramid'
]

# Azimuthal deviation from Alnitak’s rising point (°)
azimuth_dev_2500 = [1.60, 1.30, 1.80, 0.90, 2.50, 2.30, 2.20]
azimuth_dev_4400 = [0.00, 0.30, 0.20, 0.70, 0.90, 0.70, 0.60]

# Corresponding S-values (unit-circle Euclidean similarity)
s_value_2500 = [0.02792, 0.02269, 0.03141, 0.01571, 0.04363, 0.04014, 0.03839]
s_value_4400 = [0.00000, 0.00524, 0.00349, 0.01222, 0.01571, 0.01222, 0.01047]

# Plot configuration
x = np.arange(len(structures))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 7))
bars_2500 = ax.bar(x - width/2, azimuth_dev_2500, width, label='2500 BCE', color='salmon')
bars_4400 = ax.bar(x + width/2, azimuth_dev_4400, width, label='4400 BCE', color='royalblue')
ax.set_ylabel('Azimuth Deviation (°)', fontsize=12)
ax.set_title('Azimuthal Alignment of Giza Monuments with Alnitak’s Rising Point\n(Deviation and S-values at Two Epochs)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(structures, rotation=45, ha='right')
ax.legend()

# Annotate each bar with its ΔAz value
def annotate_bars(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

annotate_bars(bars_2500)
annotate_bars(bars_4400)
plt.tight_layout()
plt.show()
