#!/bin/bash
set -euo pipefail

ROOT="$HOME/LDLS_Project1"
BENCH="$ROOT/llama.cpp/build/bin/llama-bench"
OUT="$ROOT/results/reproduction/threads"

mkdir -p "$OUT"

for MODEL in 1B 3B; do
    MODEL_PATH="$ROOT/models/Llama-3.2-${MODEL}-Instruct-Q4_K_M.gguf"

    for THREADS in 1 2 4 6 8 10; do
        echo "Running $MODEL with $THREADS threads"

        "$BENCH" \
            -m "$MODEL_PATH" \
            -p 0 -n 128 -d 1024 \
            -t "$THREADS" -ngl 0 -r 3 \
            --repack 0 \
            > "$OUT/${MODEL}_threads_${THREADS}.log" 2>&1
    done
done

echo "Thread scaling complete."
