import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

sns.set_style("whitegrid")
def load_and_clean():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    low = df["value"].quantile(0.025)
    up = df["value"].quantile(0.975)
    df = df[(df["value"] >= low) & (df["value"] <= up)].copy()
    return df

def draw_line_plot():
    df = load_and_clean().copy()
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.tight_layout()
    return fig

def draw_bar_plot():
    df = load_and_clean().copy()
    data = df.copy()
    data["year"] = data.index.year
    data["month"] = data.index.month
    group = data.groupby(["year", "month"])["value"].mean().unstack()
    month = [calendar.month_name[m] for m in group.columns]
    group.columns = month
    fig = group.plot(kind="bar", figsize=(15, 10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.tight_layout()
    return fig

def draw_box_plot():
    df = load_and_clean().copy()
    data = df.reset_index()
    data["year"] = data["date"].dt.year
    data["month_num"] = data["date"].dt.month
    data["month"] = data["date"].dt.strftime("%b")
    data = data.sort_values("month_num")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x="year", y="value", data=data, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    month_or = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    sns.boxplot(x="month", y="value", data=data, order=month_or, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    fig.tight_layout()
    return fig

if __name__ == "__main__":
    line = draw_line_plot()
    line.savefig("line_plot.png")
    bar = draw_bar_plot()
    bar.savefig("bar_plot.png")
    box = draw_box_plot()
    box.savefig("box_plot.png")
