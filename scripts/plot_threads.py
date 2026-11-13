import matplotlib.pyplot as plt

threads = [1, 2, 3, 4]

data = {
    "1B Prefill": [126.61, 226.89, 308.25, 377.99],
    "1B Decode": [48.93, 82.82, 94.49, 94.89],
    "3B Prefill": [43.54, 73.20, 97.91, 105.52],
    "3B Decode": [18.22, 29.77, 35.26, 31.34],
}

plt.figure(figsize=(9, 5.5))

for label, values in data.items():
    plt.plot(threads, values, marker="o", linewidth=2, label=label)

plt.xlabel("Number of CPU Threads")
plt.ylabel("Throughput (tokens/s)")
plt.title("CPU Thread Scaling: Llama-3.2-1B vs 3B")
plt.xticks(threads)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("plots/thread_scaling.png", dpi=300)
plt.savefig("plots/thread_scaling.pdf")
plt.close()

print("Thread scaling plots generated successfully.")
