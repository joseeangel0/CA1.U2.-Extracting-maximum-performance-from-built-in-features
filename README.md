# HPC Assignment - Chapter 2 Profiling

This repository contains the scripts and instructions needed to reproduce the profiling case studies from Chapter 2 of the High Performance Computing course.

**Objective:** Generate three pieces of evidence (screenshots) demonstrating I/O and CPU profiling.

## 📋 Prerequisites

Before starting, install the required Python libraries by running this command in your terminal:

```bash
pip install snakeviz line_profiler requests
```

---

## 🚀 Part 1: I/O Profiling (Section 2.1)

In this part, we analyze network latency using `load.py`.

### Step 1: Run the Profiler

Run the following command. This will execute the script and save the profiling data to a text file named `profile.txt`.

```bash
# Note: This may take 1-2 minutes to run.
python -m cProfile -s cumulative load.py 01044099999 2021-2021 > profile.txt
```

### 📸 Evidence Checkpoint 1

1. Open the generated `profile.txt` file.
2. Look at the top 10-20 lines. You should see a total run time of approximately **129 seconds**.
3. **Action:** Take a screenshot of these top lines.
4. **Save using specific filename (if required) or add to your report.**

---

## 💻 Part 2: CPU Profiling (Section 2.2)

In this part, we analyze the CPU-intensive `distance_cache.py` script.

### Method A: Line Profiler (Detailed Table)

**Requirement:** Ensure the `@profile` decorator is present in `distance_cache.py` (it usually is by default).

### Step 2: Run Kernprof

Run the special line profiler command:

```bash
kernprof -l -v distance_cache.py
```

### 📸 Evidence Checkpoint 2

1. After the command finishes, a table will be printed in your terminal.
2. Look for the **% Time** column showing high usage on the mathematical operations within `get_distance`.
3. **Action:** Take a screenshot of this table in your terminal.

---

### Method B: SnakeViz (Visual Chart)

### ⚠️ CRITICAL WARNING: Before You Proceed

**You MUST open `distance_cache.py` and delete (or comment out) the `@profile` decorator.**

If you do not remove `@profile`, the next command will fail with a `NameError`.

```python
# distance_cache.py

# @profile  <-- DELETE THIS LINE OR ADD A #
def get_distance(p1, p2):
    ...
```

### Step 3: Run Standard Profiler

Once the decorator is removed, run:

```bash
python -m cProfile -o distance_cache.prof distance_cache.py
```

### Step 4: Launch SnakeViz

Visualize the results:

```bash
snakeviz distance_cache.prof
```

### 📸 Evidence Checkpoint 3

1. A browser window will open showing a colorful "Icicle" chart.
2. **Action:** Take a screenshot of this chart.

---

## ✅ Checklist

- [ ] Evidence 1: `profile.txt` screenshot (~129s).
- [ ] Evidence 2: `kernprof` terminal output.
- [ ] Evidence 3: SnakeViz chart (after removing `@profile`).
