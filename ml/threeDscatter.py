import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. Create a realistic agricultural dataset
# -------------------------------------------------
data = {
    'Nitrogen_kg_per_ha': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Rainfall_mm': [300, 320, 340, 360, 380, 400, 420, 440, 460, 480],
    'Temp_C': [22, 22.5, 23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5],
    # Yield (tonnes per hectare) – realistic response
    'Yield_t_per_ha': [5.2, 5.5, 5.8, 6.0, 6.3, 6.5, 6.6, 6.7, 6.5, 6.2]
}

df = pd.DataFrame(data)

# -------------------------------------------------
# 2. 3D Scatter Plot: Nitrogen vs Rainfall vs Yield
# -------------------------------------------------
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Colour points by temperature (continuous colour map)
sc = ax.scatter(df['Nitrogen_kg_per_ha'],
                df['Rainfall_mm'],
                df['Yield_t_per_ha'],
                c=df['Temp_C'], cmap='viridis', s=50, alpha=0.8)

# Labels
ax.set_xlabel('Nitrogen (kg/ha)', fontsize=12)
ax.set_ylabel('Rainfall (mm)', fontsize=12)
ax.set_zlabel('Yield (tonnes/ha)', fontsize=12)
ax.set_title('Effect of Nitrogen & Rainfall on Crop Yield\n(coloured by Temperature)', fontsize=14)

# Add colour bar for temperature
cbar = fig.colorbar(sc, ax=ax, shrink=0.5, aspect=10)
cbar.set_label('Temperature (°C)', fontsize=11)

plt.tight_layout()
plt.show()

# -------------------------------------------------
# 3. Optional: Interactive version with Plotly
# -------------------------------------------------
import plotly.express as px

fig_int = px.scatter_3d(df, x='Nitrogen_kg_per_ha', y='Rainfall_mm', z='Yield_t_per_ha',
                        color='Temp_C', size='Yield_t_per_ha',
                        title='Interactive 3D Scatter – Agricultural Data',
                        labels={'Nitrogen_kg_per_ha':'Nitrogen (kg/ha)',
                                'Rainfall_mm':'Rainfall (mm)',
                                'Yield_t_per_ha':'Yield (t/ha)'})
fig_int.show()