# svMultiPhysics 2D lid-driven-cavity benchmark

This benchmark is ported to `svbenchmark` from Dr. Sujal Dave's benchmark: [https://github.com/sujaldave/2DLidDrivenCavityBenchmark]

The original readme, which contains a description of the setup and the evaluation criteria can be found in [./README_original.md]

## Changes

In order to accommodate the `svbenchmark` harness, several changes were made:

1. Individual Reynolds number cases were moved into associated folder e.g. [Case_Re1000/]
2. In each folder two files were added:
    - `benchmark.toml` - defines the scripts to use, arguments to call, and the original comparison values from the original benchmark.
    - `local_run.py` - A python script that uses the `svbenchmark` harness to run the file locally. The `svmultiphysics` path is hardcoded, so it needs to be changed as needed.
3. Two scripts were added, [./scripts/extract_metric.py] and [./scripts/cleanup.py].
    - `extract_metric.py` - script to extract a single metric from the summary metrics already calculated by original benchmark.
    - `cleanup.py` - script that deletes any files created during the benchmark run.

## Running

Using `svbenchmark`, one can use Python to run the benchmark as defined by the `benchmark.toml` file. See the instructions in `svbenchmark` for instructions.
