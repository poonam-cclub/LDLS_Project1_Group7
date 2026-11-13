#!/bin/bash
set -euo pipefail

ROOT="$HOME/LDLS_Project1"
BENCH="$ROOT/llama.cpp/build/bin/llama-bench"
OUT="$ROOT/results/reproduction/decode"

mkdir -p "$OUT"

for MODEL in 1B 3B; do
    MODEL_PATH="$ROOT/models/Llama-3.2-${MODEL}-Instruct-Q4_K_M.gguf"

    for DEPTH in 1024 8192 16384; do
        echo "Running $MODEL decode at depth $DEPTH"

        "$BENCH" \
            -m "$MODEL_PATH" \
            -p 0 -n 128 -d "$DEPTH" \
            -t 4 -ngl 0 -r 3 \
            --repack 0 \
            > "$OUT/${MODEL}_decode_${DEPTH}.log" 2>&1
    done
done

echo "Decode sweep complete."
