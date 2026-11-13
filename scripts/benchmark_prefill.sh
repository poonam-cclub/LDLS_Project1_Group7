#!/bin/bash
set -euo pipefail

ROOT="$HOME/LDLS_Project1"
BENCH="$ROOT/llama.cpp/build/bin/llama-bench"
OUT="$ROOT/results/reproduction/prefill"

mkdir -p "$OUT"

for MODEL in 1B 3B; do
    MODEL_PATH="$ROOT/models/Llama-3.2-${MODEL}-Instruct-Q4_K_M.gguf"

    for PROMPT in 512 1024 4096 8192; do
        echo "Running $MODEL prefill $PROMPT"

        "$BENCH" \
            -m "$MODEL_PATH" \
            -p "$PROMPT" -n 0 \
            -t 4 -ngl 0 -r 3 \
            --repack 0 \
            > "$OUT/${MODEL}_prefill_${PROMPT}.log" 2>&1
    done
done

echo "Prefill sweep complete."
