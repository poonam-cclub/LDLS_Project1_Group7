import matplotlib.pyplot as plt

# Measured decoding throughput (tokens/second)
context_1b = [1024, 8192, 16384]
speed_1b = [81.886, 35.581, 13.378]

context_3b = [1024, 8192]
speed_3b = [31.502, 5.444]

plt.figure(figsize=(8, 5))

plt.plot(context_1b, speed_1b, "o-", linewidth=2,
         label="Llama-3.2-1B Q4_K_M")

plt.plot(context_3b, speed_3b, "s-", linewidth=2,
         label="Llama-3.2-3B Q4_K_M")

plt.xlabel("Context Length (tokens)")
plt.ylabel("Decode Throughput (tokens/s)")
plt.title("CPU Decoding Throughput vs Context Length")

plt.xticks([1024, 8192, 16384], ["1K", "8K", "16K"])
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig("plots/decode_vs_context.png", dpi=300)
plt.savefig("plots/decode_vs_context.pdf")
plt.close()

print("Saved plots/decode_vs_context.png")
print("Saved plots/decode_vs_context.pdf")
