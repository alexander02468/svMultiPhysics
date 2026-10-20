"""
Script to test the adaption of existing benchmark with svBenchmark



"""

from pathlib import Path
import svbenchmark

# load in the benchmark
benchmark = svbenchmark.load_benchmark("./benchmark.toml")

# run the preprocess
svbenchmark.run_preprocess(benchmark)

# define the local execution environment
SOLVER_PATH = Path("/Users/alexanderbaker/Documents/Code_Repository/svMultiPhysics/build/svMultiPhysics-build/bin/svmultiphysics")

local_solve_context = svbenchmark.SolveExecutionContext(
    solver_executable=SOLVER_PATH,
    mpi_ranks=4
)
svbenchmark.run_solver(benchmark, local_solve_context)
svbenchmark.run_postprocess(benchmark)
svbenchmark.run_evaluation(benchmark)
svbenchmark.run_cleanup(benchmark)
