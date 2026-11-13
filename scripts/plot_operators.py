import matplotlib.pyplot as plt
import numpy as np

workloads = [
    "1B Prefill\n4K",
    "3B Prefill\n4K",
    "1B Decode\n8K",
    "3B Decode\n8K",
]

# Counts extracted from earlier macOS sample profiling.
# These are sampling indicators, NOT exclusive execution times.
data = {
    "Q4 GEMM": [14826, 21343, 0, 0],
    "Q6 GEMM": [3361, 4865, 0, 0],
    "Attention": [8920, 2477, 11515, 11687],
    "Q4 GEMV": [0, 0, 4063, 4970],
    "Q6 GEMV": [0, 0, 4100, 2590],
    "FP16 dot": [0, 0, 3834, 5121],
}

x = np.arange(len(workloads))
width = 0.12

plt.figure(figsize=(10, 5.5))

for i, (operation, counts) in enumerate(data.items()):
    plt.bar(
        x + (i - 2.5) * width,
        counts,
        width,
        label=operation
    )

plt.xticks(x, workloads)
plt.ylabel("Observed Stack Sample Counts")
plt.title("CPU Operator Profiling: Prefill vs Decoding")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("plots/operator_breakdown.png", dpi=300)
plt.savefig("plots/operator_breakdown.pdf")
plt.close()

print("Operator breakdown plots generated successfully.")
