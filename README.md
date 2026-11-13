# LDLS Project 1 — CPU Inference Benchmarking

## Overview

This project evaluates CPU-only LLM inference performance using
llama.cpp on an Apple M5 MacBook Air.

Models:
- Llama 3.2 1B Instruct Q4_K_M
- Llama 3.2 3B Instruct Q4_K_M

Experiments include prefill throughput, decode throughput,
thread scaling, memory usage, operator profiling, roofline
analysis, and correctness/perplexity checks.

## Hardware

- System: Apple MacBook Air
- CPU: Apple M5 (ARM64)
- CPU cores: 10 (4 performance + 6 efficiency)
- Memory: 16 GiB
- GPU acceleration: Disabled

## Software

- llama.cpp commit: bbc2e4b65
- Backend: CPU / BLAS
- GGML_METAL: OFF
- Python plotting packages: NumPy, Matplotlib

## Build

Install Homebrew dependencies:

    brew install cmake git

Clone llama.cpp:

    git clone https://github.com/ggml-org/llama.cpp.git
    cd llama.cpp
    git checkout bbc2e4b65

Build without Metal:

    cmake -S . -B build -DGGML_METAL=OFF
    cmake --build build --config Release -j 4

## Models

Place these GGUF files in models/:

    Llama-3.2-1B-Instruct-Q4_K_M.gguf
    Llama-3.2-3B-Instruct-Q4_K_M.gguf

Models are not committed to Git because of their size.
Use appropriately licensed model downloads.

## Benchmarking

All commands below are run from the project root.

Prefill sweep:

    bash scripts/benchmark_prefill.sh

Decode sweep:

    bash scripts/benchmark_decode.sh

Thread scaling:

    bash scripts/benchmark_threads.sh

Memory measurement:

    bash scripts/measure_memory.sh

The three benchmark sweep scripts use:
- CPU-only execution: -ngl 0
- Three repetitions: -r 3
- Weight repacking disabled: --repack 0

The memory script was originally run with the default
repacking configuration. Its results should not be
interpreted as directly comparable to no-repack runs
without checking the settings.

Decode depth (-d) is a synthetic KV-cache depth benchmark,
not a real prefetched prompt of that length.

## Results

Benchmark results are stored in results/.

- CSV files: benchmark measurements
- correctness/: generation and perplexity checks
- profiling/: operator profiling outputs
- memory/: memory measurements
- raw/: additional raw benchmark logs
- reproduction/: logs from rerunning sweep scripts

Selected measurements:

- STREAM bandwidth: approximately 117.99 GB/s
- 3B prefill, 4096 tokens, repack disabled:
  147.95 ± 2.54 tokens/sec
- 1B decode, depth 8064:
  35.58 ± 1.12 tokens/sec

## Plotting

Install Python dependencies:

    python3 -m pip install -r requirements.txt

Plotting scripts:

    python3 scripts/plot_decode.py
    python3 scripts/plot_prefill.py
    python3 scripts/plot_threads.py
    python3 scripts/plot_operators.py
    python3 scripts/plot_roofline.py

Required plots are available in plots/:

1. Decode speed versus context length
2. Prefill speed versus prompt length
3. Thread scaling
4. Operator time breakdown
5. Predicted versus measured decode speed

## Shared PARAM Rudra Reference

A separate CPU reference benchmark was completed on
PARAM Rudra using Llama 3.2 1B Q4_K_M.

- CPU threads: 4
- Prompt tokens: 512
- Generation tokens: 128
- Combined throughput: 88.28 tokens/sec

This combined result is not directly comparable to
prefill-only or decode-only throughput.

## Reproducibility Notes

- Use the specified llama.cpp commit.
- Record the repacking configuration.
- Keep model, thread count, and benchmark parameters fixed.
- Preserve raw logs and CSV files.
- Compare measurements only when configurations match.
