# # ...existing code...
# import numpy as np
# import matplotlib.pyplot as plt


# sample_marks = [45, 48, 50, 51, 52, 53, 55, 56, 58, 59, 60, 61, 62, 63, 66, 67, 68, 70, 71, 72, 73, 74, 75, 76, 78, 80, 82, 85, 90]
# marks = np.array(sample_marks)

# # statistics
# mean_marks = marks.mean()
# median_marks = np.median(marks)
# values, counts = np.unique(marks, return_counts=True)
# mode_marks = values[counts.argmax()]
# std_dev_marks = marks.std()

# # plotting
# fig, ax = plt.subplots(figsize=(10, 6))
# bins = 10
# ax.hist(marks, bins=bins, edgecolor='black', alpha=0.6, density=True)

# # normal distribution curve (pdf)
# x = np.linspace(marks.min() - 5, marks.max() + 5, 300)
# pdf = (1 / (std_dev_marks * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_marks) / std_dev_marks) ** 2)
# ax.plot(x, pdf, color='red', lw=2, label='Normal PDF')

# # vertical lines for statistics
# ax.axvline(mean_marks, color='black', linestyle='--', lw=1.5, label=f'Mean: {mean_marks:.2f}')
# ax.axvline(median_marks, color='blue', linestyle='--', lw=1.5, label=f'Median: {median_marks:.2f}')
# ax.axvline(mode_marks, color='green', linestyle='--', lw=1.5, label=f'Mode: {mode_marks}')

# # labels, legend, grid
# ax.set_title('Distribution of Student Marks')
# ax.set_xlabel('Marks')
# ax.set_ylabel('Density')
# ax.legend(loc='upper right')
# ax.grid(axis='y', alpha=0.3)

# # annotations (optional)
# ax.text(mean_marks + 1, ax.get_ylim()[1] * 0.9, f'Mean: {mean_marks:.2f}')
# ax.text(median_marks + 1, ax.get_ylim()[1] * 0.8, f'Median: {median_marks:.2f}')
# ax.text(mode_marks + 1, ax.get_ylim()[1] * 0.7, f'Mode: {mode_marks}')

# plt.tight_layout()
# plt.show()


# Subplots to show the postive, negative and symmetric skew graph on  in single row three plots 
# ...existing code...
import numpy as np
import matplotlib.pyplot as plt

# Create sample data for different skewness distributions
np.random.seed(42)

# Positive skew (right skew)
positive_skew = np.concatenate([np.random.normal(50, 10, 500), np.random.normal(80, 15, 200)])

# Negative skew (left skew)
negative_skew = np.concatenate([np.random.normal(20, 15, 200), np.random.normal(50, 10, 500)])

# Symmetric (normal distribution)
symmetric = np.random.normal(50, 15, 700)

def kde_estimate(data, x_grid, bw=None):
    n = data.size
    if n <= 1:
        return np.zeros_like(x_grid)
    if bw is None:
        # Silverman's rule of thumb
        bw = 1.06 * data.std(ddof=1) * n ** (-1/5)
        if bw == 0:
            bw = 1.0
    kernels = np.exp(-0.5 * ((x_grid[:, None] - data[None, :]) / bw) ** 2) / (np.sqrt(2 * np.pi) * bw)
    return kernels.mean(axis=1)

# Create subplots in a single row
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot 1: Positive Skew
ax = axes[0]
ax.hist(positive_skew, bins=30, edgecolor='black', alpha=0.6, density=True, color='lightblue')
x_grid = np.linspace(positive_skew.min() - 5, positive_skew.max() + 5, 300)
kde_vals = kde_estimate(positive_skew, x_grid)
ax.plot(x_grid, kde_vals, color='red', lw=2, label='KDE')
ax.axvline(positive_skew.mean(), color='black', linestyle='--', linewidth=1.5, label=f'Mean: {positive_skew.mean():.2f}')
ax.axvline(np.median(positive_skew), color='green', linestyle='--', linewidth=1.5, label=f'Median: {np.median(positive_skew):.2f}')
ax.set_title('Positive Skew (Right Skew)', fontsize=12, fontweight='bold')
ax.set_xlabel('Values')
ax.set_ylabel('Density')
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Plot 2: Negative Skew
ax = axes[1]
ax.hist(negative_skew, bins=30, edgecolor='black', alpha=0.6, density=True, color='navajowhite')
x_grid = np.linspace(negative_skew.min() - 5, negative_skew.max() + 5, 300)
kde_vals = kde_estimate(negative_skew, x_grid)
ax.plot(x_grid, kde_vals, color='red', lw=2, label='KDE')
ax.axvline(negative_skew.mean(), color='black', linestyle='--', linewidth=1.5, label=f'Mean: {negative_skew.mean():.2f}')
ax.axvline(np.median(negative_skew), color='green', linestyle='--', linewidth=1.5, label=f'Median: {np.median(negative_skew):.2f}')
ax.set_title('Negative Skew (Left Skew)', fontsize=12, fontweight='bold')
ax.set_xlabel('Values')
ax.set_ylabel('Density')
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Plot 3: Symmetric (Normal Distribution)
ax = axes[2]
ax.hist(symmetric, bins=30, edgecolor='black', alpha=0.6, density=True, color='lightgreen')
x_grid = np.linspace(symmetric.min() - 5, symmetric.max() + 5, 300)
kde_vals = kde_estimate(symmetric, x_grid)
ax.plot(x_grid, kde_vals, color='red', lw=2, label='KDE')
# also plot normal pdf for comparison
mean_sym = symmetric.mean()
std_sym = symmetric.std(ddof=1)
pdf = (1 / (std_sym * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_grid - mean_sym) / std_sym) ** 2)
ax.plot(x_grid, pdf, color='blue', lw=1.5, linestyle='--', label='Normal PDF')
ax.axvline(mean_sym, color='black', linestyle='--', linewidth=1.5, label=f'Mean: {mean_sym:.2f}')
ax.axvline(np.median(symmetric), color='green', linestyle='--', linewidth=1.5, label=f'Median: {np.median(symmetric):.2f}')
ax.set_title('Symmetric (Normal Distribution)', fontsize=12, fontweight='bold')
ax.set_xlabel('Values')
ax.set_ylabel('Density')
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
# ...existing code...