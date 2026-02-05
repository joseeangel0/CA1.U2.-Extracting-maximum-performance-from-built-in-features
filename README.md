# HPC Assignment: Code Optimization & Profiling (Chapter 2)

This guide provides step-by-step instructions to reproduce the profiling case studies from **Chapter 2 (Sections 2.1 & 2.2)** of the "High Performance Computing" course.

**Objective:** Profile Python code to identify I/O bottlenecks (Section 2.1) and CPU bottlenecks (Section 2.2).

## 📋 Prerequisites

Open your terminal or command prompt and install the required tools:

```bash
pip install snakeviz line_profiler requests
```

---

## Part 1: I/O Profiling (Section 2.1)

In this section, we will analyze `load.py` to identify excessive Input/Output operations.

### 1. Run the Profiler

Run the standard Python profiler (`cProfile`) on the data loading script. We will request data for a specific station over a year range.

```bash
# Syntax: python -m cProfile -o <output_file> load.py <stations> <year_range>
python -m cProfile -o load.prof load.py "ABC" 2022-2023
```

_(Note: Replace `"ABC"` with a valid station ID from `locations.csv` if needed)_

### 2. Visualize with SnakeViz

Launch the interactive visualizer to see where the time is being spent.

```bash
snakeviz load.prof
```

Look for large blocks in the visualization. You should see time dominated by network requests (e.g., `socket.read` or `recv`), clearly indicating an I/O bottleneck.

---

## Part 2: CPU Profiling (Section 2.2)

In this section, we will analyze `distance_cache.py`, which computes distances between coordinates.

### ⚠️ IMPORTANT: Before You Start

Open `distance_cache.py` and ensure the `@profile` decorator is **COMMENTED OUT** or **DELETED**.

```python
# distance_cache.py
# @profile  <-- MUST BE COMMENTED OUT for Step 1
def get_distance(p1, p2):
    ...
```

_If you leave `@profile` enabled, the standard profiler in Step 1 will crash!_

### Step 1: Broad Profiling with SnakeViz

First, we get a high-level view of the performance.

1.  **Run cProfile:**

    ```bash
    python -m cProfile -o distance_cache.prof distance_cache.py
    ```

2.  **Visualize:**
    ```bash
    snakeviz distance_cache.prof
    ```
    _Observation:_ You will likely see that the `get_distance` function consumes the majority of the execution time.

### Step 2: Line-by-Line Profiling

Now that we know `get_distance` is the culprit, we need to inspect it line-by-line using `line_profiler`.

1.  **Enable the Decorator:**
    Open `distance_cache.py` and **uncomment** (or add) the `@profile` decorator above the `get_distance` function.

    ```python
    @profile  # <-- UNCOMMENT THIS NOW
    def get_distance(p1, p2):
        ...
    ```

2.  **Run Line Profiler:**
    Use `kernprof` (part of the `line_profiler` package) to run the script.

    ```bash
    kernprof -l -v distance_cache.py
    ```

    _Result:_ The terminal will display a table showing exactly how much time each line of code took to execute, helping you pinpoint the inefficient mathematical operations.
