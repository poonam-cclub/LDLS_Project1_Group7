import matplotlib.pyplot as plt
import numpy as np

labels = ["1B\n1K", "1B\n8K", "1B\n16K",
          "3B\n1K", "3B\n8K"]

predicted = [141.5, 110.5, 88.3, 55.4, 40.0]
measured = [81.89, 35.58, 13.38, 31.50, 5.44]

x = np.arange(len(labels))
width = 0.35

plt.figure(figsize=(9, 5.5))

plt.bar(x - width/2, predicted, width,
        label="Bandwidth-only upper bound")

plt.bar(x + width/2, measured, width,
        label="Measured throughput")

plt.xticks(x, labels)
plt.xlabel("Model and Context Length")
plt.ylabel("Decode Throughput (tokens/s)")
plt.title("Roofline Estimate vs Measured CPU Decoding")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("plots/roofline_comparison.png", dpi=300)
plt.savefig("plots/roofline_comparison.pdf")
plt.close()

print("Roofline comparison plots generated successfully.")
