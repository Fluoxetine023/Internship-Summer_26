import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Plotting parameters
# ============================================================

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 22,
    "axes.labelsize": 23,
    "axes.titlesize": 22,
    "xtick.labelsize": 15,
    "ytick.labelsize": 15,
    "axes.linewidth": 2,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.major.size": 5,
    "ytick.major.size": 5,
    "figure.dpi": 150,
    "savefig.dpi": 600,
})

# ============================================================
# SSH parameters
# ============================================================

params = [
    (1.0, 0.0),
    (0.6, 0.4),
    (0.5, 0.5),
    (0.4, 0.6),
    (0.0, 1.0),
]

k = np.linspace(-np.pi, np.pi, 1000)


# ============================================================
# Physics
# ============================================================

def ssh_dispersion(v, w, k):
    """Energy dispersion."""
    return np.sqrt(v**2 + w**2 + 2 * v * w * np.cos(k))


def winding_curve(v, w, k):
    """Return d_x(k), d_y(k)."""
    dx = v + w * np.cos(k)
    dy = w * np.sin(k)
    return dx, dy


# ============================================================
# Plotting helpers
# ============================================================

def draw_arrow(ax, x, y, target_angle=np.pi/4, step=8):
    """
    Draw an arrow showing increasing k.

    The arrow is placed near a chosen polar angle and follows the
    local tangent direction.
    """

    cx = np.mean(x)
    cy = np.mean(y)

    theta = np.arctan2(y - cy, x - cx)

    idx = np.argmin(np.abs(np.angle(np.exp(1j * (theta - target_angle)))))

    i1 = max(idx - step, 0)
    i2 = min(idx + step, len(x) - 1)

    ax.annotate(
        "",
        xy=(x[i2], y[i2]),
        xytext=(x[i1], y[i1]),
        arrowprops=dict(
            arrowstyle="-|>",
            lw=1.8,
            color="black",
            mutation_scale=16,
            shrinkA=0,
            shrinkB=0,
        ),
    )


def plot_band(ax, v, w):
    """Plot SSH dispersion."""

    E = ssh_dispersion(v, w, k)

    ax.plot(k, E, color="blue", lw=2)
    ax.plot(k, -E, color="blue", lw=2)

    ax.set_xlim(-np.pi, np.pi)
    ax.set_ylim(-1.5, 1.5)

    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])

    ax.set_yticks([-1, 0, 1])

    ax.grid(alpha=0.25)

    ax.set_title(rf"$v={v:.1f},\; w={w:.1f}$")


def plot_winding(ax, v, w):
    """Plot winding trajectory."""

    dx, dy = winding_curve(v, w, k)

    ax.plot(dx, dy, color="blue", lw=2)

    draw_arrow(ax, dx, dy)

    # origin
    ax.scatter(
        0,
        0,
        s=22,
        color="black",
        zorder=5,
    )

    # reference axes
    ax.axhline(0, color="0.75", lw=0.8)
    ax.axvline(0, color="0.75", lw=0.8)

    ax.set_aspect("equal")

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    ax.set_xticks([-1.5, 0, 1.5])
    ax.set_yticks([-1.5, 0, 1.5])

    ax.grid(alpha=0.20)


# ============================================================
# Figure
# ============================================================

fig, axes = plt.subplots(
    2,
    5,
    figsize=(20, 8),
    sharey="row",
    constrained_layout=True,
)

for i, (v, w) in enumerate(params):

    plot_band(axes[0, i], v, w)
    plot_winding(axes[1, i], v, w)

    axes[0, i].set_xlabel(r"$k$")
    axes[1, i].set_xlabel(r"$d_x$")

axes[0, 0].set_ylabel(r"$E(k)$")
axes[1, 0].set_ylabel(r"$d_y$")

# ============================================================
# Saving
# ============================================================

plt.savefig("ssh_bands_winding.pdf", bbox_inches="tight")
plt.savefig("ssh_bands_winding.png", dpi=600, bbox_inches="tight")

plt.show()