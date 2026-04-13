import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")

def draw_cat_plot():
    df = pd.read_csv("medical_examination.csv")
    hm= df["height"] / 100
    bmi = df["weight"] / (hm** 2)
    df["overweight"] = (bmi > 25).astype(int)
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)
    df_cat = pd.melt
    (
        df,
        id_vars=["cardio"],
        v_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
        var_n="variable",
        v_n="value",
    )

    df_cat = 
    (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    catplot = sns.catplot
    (
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        height=5,
        aspect=1,
        palette="pastel",
    )

    catplot.set_axis_labels("variable", "total")
    catplot.set_titles("cardio = {col_name}")
    for ax in catplot.axes.flat:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    fig = catplot.fig
    return fig
def draw_heat_map():
    df = pd.read_csv("medical_examination.csv")
    hm= df["height"] / 100
    bmi = df["weight"] / (hm** 2)
    df["overweight"] = (bmi > 25).astype(int)
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)
    df_heat = df
    [
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ].copy()

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap
    (
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax,
    )

    fig.tight_layout()
    return fig

if __name__ == "__main__":
    cat_fig = draw_cat_plot()
    cat_fig.savefig("catplot.png")
    heat_fig = draw_heat_map()
    heat_fig.savefig("heatmap.png")
