import matplotlib.pyplot as plt

prompt_1b = [512, 4096, 16384]
speed_1b = [408.79, 238.07, 128.33]

prompt_3b = [512, 4096, 8192]
speed_3b = [138.67, 91.67, 56.15]

plt.figure(figsize=(8, 5))

plt.plot(prompt_1b, speed_1b, "o-", linewidth=2,
         label="Llama-3.2-1B Q4_K_M")

plt.plot(prompt_3b, speed_3b, "s-", linewidth=2,
         label="Llama-3.2-3B Q4_K_M")

plt.xlabel("Prompt Length (tokens)")
plt.ylabel("Prefill Throughput (tokens/s)")
plt.title("CPU Prefill Throughput vs Prompt Length")

plt.xticks(
    [512, 4096, 8192, 16384],
    ["512", "4K", "8K", "16K"]
)

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("plots/prefill_vs_prompt.png", dpi=300)
plt.savefig("plots/prefill_vs_prompt.pdf")
plt.close()

print("Prefill plots generated successfully.")
