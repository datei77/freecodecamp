import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10, color='blue')
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year_ex = np.arange(df['Year'].min(), 2051)
    line_all = res_all.intercept + res_all.slope *year_ex
    ax.plot(years_extended, line_all, color='red', label='Fit: all data')

    df_r= df[df['Year'] >= 2000]
    res_r = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    year_r_ex = np.arange(2000, 2051)
    line_r = res_r.intercept + res_r.slope * year_r_ex
    ax.plot(year_r_ex, line_r, color='green', label='Fit: 2000 onwards')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    fig.tight_layout()
  
    return fig

if __name__ == "__main__":
    fig = draw_plot()
    fig.savefig("sea_level_plot.png")
