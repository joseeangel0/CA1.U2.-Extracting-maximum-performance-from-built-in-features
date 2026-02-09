# 🚀 High Performance Computing: Benchmarking & Profiling Lab Guide

👋 **Hi there!** This kit contains pre-made scripts to save you time. Follow this guide to finish your assignment in **10 minutes** without getting stuck!

---

## 🛠️ Prerequisites

Open your terminal (**PowerShell** on Windows, **Terminal** on macOS) in this folder and install the required tools:

```bash
pip install pytest pytest-benchmark line_profiler memory_profiler psutil matplotlib snakeviz
```

---

## 📸 Step-by-Step Guide

### a) 📝 Write Tests and Benchmarks

**Goal:** Show the code structure.

**Action:**
Open **simul.py** and **test_simul.py** in your code editor.

> 📸 **Evidence A:** Take a screenshot showing both files open side-by-side.

---

### b) ⏱️ Time Benchmark

**Goal:** Measure total execution time.

**Windows (PowerShell):**

```powershell
Measure-Command { python simul.py }
```

**macOS (Terminal):**

```bash
time python simul.py
```

> 📸 **Evidence B:** Screenshot the output showing **TotalSeconds** (Windows) or the **real** time (macOS).

---

### c) ⚡ Benchmark using timeit

**Goal:** Measure accurate execution time using Python's module.

**Command to Run:**

```bash
python -m timeit -s "from simul import benchmark" "benchmark()"
```

> 📸 **Evidence C:** Screenshot the result (e.g., "**10 loops, best of 3...**").

---

### d) 📊 Pytest Benchmark

**Goal:** Run statistical benchmarking on the **evolve** function.

**Command to Run:**

```bash
pytest test_simul.py
```

> 📸 **Evidence D:** Screenshot the green "**Passed**" table showing **Min/Max/Mean** times.

---

### e) 🐢 Find Bottlenecks with cProfile

**Goal:** Identify the slowest function.

**Windows (PowerShell):**

```powershell
python -m cProfile -s tottime simul.py | select -first 20
```

**macOS (Terminal):**

```bash
python -m cProfile -s tottime simul.py | head -n 20
```

> 📸 **Evidence E:** Screenshot the table. Look for **evolve** at the very top (highest tottime).

---

### f) 📉 Visualize Profiling Data (SnakeViz)

**Goal:** Visualize the call stack of the Taylor series example.

**Command 1 (Generate Data):**

```bash
python -m cProfile -o prof.out taylor.py
```

**Command 2 (Visualize):**

```bash
snakeviz prof.out
```

_(This will open your web browser)_

> 📸 **Evidence F:** Screenshot the colorful chart in your web browser.

---

### g) 🔍 Line Profiler

**Goal:** Find exactly which lines of code are slow.

⚠️ **WARNING:** DO NOT edit **simul_line.py**. The `@profile` decorator is already included in this file. Just run the command below. It will take **1-3 minutes** to run.

**Command to Run:**

```bash
kernprof -l -v simul_line.py
```

> 📸 **Evidence G:** Screenshot the table showing **% Time**. Note which math lines are taking the most percentage.

---

### h) 🚀 Optimize the Code

**Goal:** Prove the optimization is faster.

ℹ️ **Note:** No editing needed. We are comparing two different files: **simul.py** (slow) vs **simul_opt.py** (fast).

**Windows (PowerShell):**

```powershell
# Command 1 (Original - SLOW)
Measure-Command { python simul.py }

# Command 2 (Optimized - FAST)
Measure-Command { python simul_opt.py }
```

**macOS (Terminal):**

```bash
# Command 1 (Original - SLOW)
time python simul.py

# Command 2 (Optimized - FAST)
time python simul_opt.py
```

> 📸 **Evidence H:** Screenshot both results showing the Optimized version is faster.

---

### j) 💾 Memory Profiling

**Goal:** Compare memory usage before and after optimization.

#### Part 1: Baseline

Run the command on **simul_mem.py** exactly as is.

**Command to Run:**

```bash
python -m memory_profiler simul_mem.py
```

> 📸 **Evidence J1:** Screenshot the table. Note the "**Increment**" (approx **23 MiB**).

---

> 🛑 **STOP & EDIT:**
> Now open **simul_mem.py**, find the `Particle` class at the top, and uncomment or add the line `__slots__ = ('x', 'y', 'v')`.
>
> **Example:**
>
> ```python
> class Particle:
>     __slots__ = ('x', 'y', 'v')  # <--- Make sure this line is active!
>     def __init__(self, x, y, v):
>         ...
> ```
>
> **Save the file.**

---

#### Part 2: Optimized

Now run the command again to see the memory usage drop.

**Command to Run:**

```bash
python -m memory_profiler simul_mem.py
```

> 📸 **Evidence J2:** Screenshot the table. The "**Increment**" should be lower (approx **10-15 MiB**).

---

### 💡 One Final Tip for You Jose Angel only.

Before you zip the files, make sure your **simul_mem.py** does **not** have the `__slots__` line in it yet! Your classmate needs to add it themselves for the "Optimization" step.
