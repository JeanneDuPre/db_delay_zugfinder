import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


def get_abfertigungszeiten_berliner_bahnhöfe_DB():
    # Load the dataset
    df = pd.read_csv("pivot_table_berlin.csv")

    # Create the plot
    fig, ax = plt.subplots(figsize=(15, 8), dpi=96)

    # Define color map
    colours = ["green", "#ec0016"]
    cmap = mpl.colors.LinearSegmentedColormap.from_list("colour_map", colours, N=256)
    norm = mpl.colors.Normalize(df["count_delay"].min(), df["count_delay"].max())

    # Customize x-axis ticks and labels
    custom_xticks = df["Ankunftsbhf."]
    custom_xtick_labels = df["Ankunftsbhf."]

    # Create bar chart
    bar1 = ax.bar(
        df["Ankunftsbhf."],
        df["count_delay"],
        width=0.6,
        color=cmap(norm(df["count_delay"])),
    )

    # Add horizontal line at y = 0
    ax.axhline(0, color="gray", linewidth=1.0, linestyle="-")

    # Add vertical line at x = 8.5
    ax.axvline(x=8.5, color="gray", linewidth=1.0, linestyle="-")

    # Create horizontal grid lines
    ax.grid(which="major", axis="y", color="#DAD8D7", alpha=0.5, zorder=1)

    # Set custom x-axis tick positions and labels with rotation
    ax.set_xticks(custom_xticks)
    ax.set_xticklabels(custom_xtick_labels, rotation=60, ha="right", fontsize=12)

    # Add labels on top of each bar
    ax.bar_label(
        bar1,
        labels=[f"{e:,.1f}" for e in df["count_delay"]],
        padding=3,
        color="black",
        fontsize=9,
    )

    # Remove spines
    ax.spines[["top", "left", "bottom"]].set_visible(False)

    # Make the right spine thicker
    ax.spines["right"].set_linewidth(1.1)

    # Remove vertical tick marks on the x-axis
    ax.tick_params(axis="x", which="both", bottom=False)

    # Remove the y-axis
    ax.set_yticks([])

    # Add red line and rectangle on top
    ax.plot(
        [0.12, 0.9],
        [0.98, 0.98],
        transform=fig.transFigure,
        clip_on=False,
        color="#ec0016",
        linewidth=0.6,
    )
    ax.add_patch(
        plt.Rectangle(
            (0.12, 0.98),
            0.04,
            -0.02,
            facecolor="#ec0016",
            transform=fig.transFigure,
            clip_on=False,
            linewidth=0,
        )
    )

    # Add title and subtitle
    ax.text(
        x=0.12,
        y=0.92,
        s="Abfertigungszeiten an Berliner Bahnhöfen der DB",
        transform=fig.transFigure,
        ha="left",
        fontsize=14,
        weight="bold",
        alpha=0.8,
    )
    ax.text(
        x=0.12,
        y=0.83,
        s="In einer vergleichenden Analyse der Ankunfts- und Abfahrtszeiten von Zügen an den Berliner Bahnhöfen konnte festgestellt werden, dass\ninsbesondere an drei Bahnhöfen (Spandau, Berliner Hbf. [oben], Ostkreuz) erhebliche Verzögerungen bei der Zugabfertigung am jeweiligen\nBahnhof auftreten. Hingegen weist die Nord-Süd-Achse geringere Verzögerungen auf.",
        transform=fig.transFigure,
        ha="left",
        fontsize=12,
        alpha=0.8,
        linespacing=1.5,
    )

    # Set source text
    ax.text(
        x=0.6,
        y=0.001,
        s="Graphik: Janine Wiesemann | Daten: www.zugfinder.net, 25.09.2023",
        transform=fig.transFigure,
        fontsize=9,
        alpha=0.7,
    )

    # Adjust the margins around the plot area
    plt.subplots_adjust(
        left=None, bottom=0.2, right=None, top=0.8, wspace=None, hspace=None
    )

    # Set a white background
    fig.patch.set_facecolor("white")

    return fig
