# ⚙️ 32-bit RISC-V Simulator

A comprehensive **RISC-V Instruction Set Architecture (ISA)** simulator built in Python. This tool simulates the execution of 32-bit RISC-V assembly code with support for **pipelined and non-pipelined** execution modes, **L1 & L2 cache memory hierarchy**, **branch prediction**, **hazard detection**, and a **graphical user interface (GUI)** for visualizing execution.

---

##  Key Features

- Supports **29 RISC-V instructions** (arithmetic, logical, data transfer, control)
- **Pipelined and Non-Pipelined** execution modes
- Implements **branch prediction**, **hazard detection** (data/control/structural)
- **Memory hierarchy simulation** with L1 and L2 caches
-  Real-time GUI for visualizing instruction execution and pipeline stages
- Instruction-by-instruction and cycle-by-cycle trace

---

## 🛠️ Tech Stack

| Layer         | Tools/Libraries             |
|---------------|-----------------------------|
| Language       | Python 3.x                 |
| GUI            | Tkinter / PyQt (as used)   |
| Architecture   | Custom simulator engine    |
| ISA            | RISC-V (RV32I subset)      |

---

 Instructions Supported

- **Arithmetic & Logical**: `ADD`, `SUB`, `MUL`, `AND`, `OR`, `XOR`, `SLL`, `SRL`, etc.
- **Data Transfer**: `LW`, `SW`, `LUI`, `ADDI`
- **Control Flow**: `BEQ`, `BNE`, `JAL`, `JALR`

---

 How It Works

1. Parses RISC-V assembly code from input file.
2. Simulates instruction cycle-by-cycle using:
   - Fetch → Decode → Execute → Memory → Writeback (5-stage pipeline)
   - Hazard resolution and forwarding
   - Branch prediction handling
3. Memory system simulates:
   - L1 and L2 cache hits/misses
   - Main memory fallback

4. GUI visualizes:
   - Instruction progress across pipeline stages
   - Clock cycles
   - Register values and memory usage

---



