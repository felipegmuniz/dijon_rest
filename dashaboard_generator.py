import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
file_path = 'C:\\Users\\norsk\\dijon_rest\\dijon_et_beaune.xlsx'
data = pd.read_excel(file_path)

# Filter data for cities and map categories
data['category'] = data['categoryName'].replace({
    r'.*restaurant.*': 'Restaurant',
    r'.*(EHPAD|retirement|senior|maison de retraite|school|college|lycée).*': 'EHPAD/École/Senior',
}, regex=True).fillna('Other')

# Separate data for Dijon and Beaune
dijon_data = data[data['city'].str.contains('Dijon', case=False, na=False)]
beaune_data = data[data['city'].str.contains('Beaune', case=False, na=False)]

# Count occurrences
dijon_counts = dijon_data['category'].value_counts().sort_values(ascending=True)
beaune_counts = beaune_data['category'].value_counts().sort_values(ascending=True)

# Setup figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), facecolor='#333333')
fig.subplots_adjust(wspace=0.5)

# Define color map
cmap = plt.get_cmap('cividis')

# Function to plot the data
def plot_data(ax, data_counts, title):
    norm = plt.Normalize(data_counts.min(), data_counts.max())
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    bars = ax.barh(data_counts.index, data_counts.values, color=sm.to_rgba(data_counts.values))

    ax.set_title(title, color='white', fontsize=14)
    ax.set_frame_on(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    ax.tick_params(axis='y', colors='white')

    # Color bar beside the chart
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', pad=0.05)
    cbar.set_label('Number of Establishments', color='white', rotation=270, labelpad=15)
    cbar.ax.yaxis.set_tick_params(color='white')
    cbar.outline.set_edgecolor('white')

    # Add value labels to bars
    for bar in bars:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{int(bar.get_width())}',
                va='center', ha='left', color='white', fontsize=10)

# Plot data for each city
plot_data(ax1, dijon_counts, 'Dijon Establishment Distribution')
plot_data(ax2, beaune_counts, 'Beaune Establishment Distribution')

plt.show()
