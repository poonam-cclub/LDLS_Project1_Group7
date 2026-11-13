#!/bin/bash
set -u

ROOT="$HOME/LDLS_Project1"
BENCH="$ROOT/llama.cpp/build/bin/llama-bench"
OUT="$ROOT/results/memory"
CSV="$OUT/memory_results.csv"

mkdir -p "$OUT"
echo "model,phase,tokens,peak_rss_bytes,peak_rss_gib,swaps" > "$CSV"

run_test() {
    local model="$1"
    local phase="$2"
    local tokens="$3"
    local model_path="$ROOT/models/Llama-3.2-${model}-Instruct-Q4_K_M.gguf"
    local log="$OUT/${model}_${phase}_${tokens}.log"

    echo "Running: $model $phase $tokens"

    if [[ "$phase" == "prefill" ]]; then
        /usr/bin/time -l "$BENCH" \
            -m "$model_path" -p "$tokens" \
            -t 4 -ngl 0 -r 3 > "$log" 2>&1
    else
        /usr/bin/time -l "$BENCH" \
            -m "$model_path" -p 0 -n 128 \
            -d "$tokens" \
            -t 4 -ngl 0 -r 3 > "$log" 2>&1
    fi

    local rss swaps rss_gib
    rss=$(awk '/maximum resident set size/ {print $1}' "$log" | tail -1)
    swaps=$(awk '/^[[:space:]]*[0-9]+[[:space:]]+swaps$/ {print $1}' "$log" | tail -1)

    if [[ -z "$rss" ]]; then
        echo "ERROR: RSS missing for $model $phase $tokens"
        return 1
    fi

    rss_gib=$(awk -v n="$rss" 'BEGIN {printf "%.3f", n/1073741824}')

    echo "$model,$phase,$tokens,$rss,$rss_gib,${swaps:-NA}" >> "$CSV"
    echo "Peak RSS: $rss_gib GiB"
}

run_test 1B prefill 4096
run_test 1B prefill 16384
run_test 3B prefill 4096
run_test 3B prefill 8192

run_test 1B decode 1024
run_test 1B decode 8192
run_test 1B decode 16384
run_test 3B decode 1024
run_test 3B decode 8192

echo "Finished. Results saved to $CSV"
