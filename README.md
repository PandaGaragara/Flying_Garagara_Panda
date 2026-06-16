# 🐼 Flying-Garagara-Panda: Closed-Loop Actuation and Forward Invariance in Denied Networks

> **Garagara Aeronautics Laboratory (GAL) — Theoretical Release Mechanics**[cite: 11]
> _An inquiry into the control-theoretic limitations of empirical, window-based behavioral classifiers under optimal closed-loop actuation._

---

## 🔬 Theoretical Context: The Control Loop Deficit
Contemporary cybersecurity paradigms rely heavily on the assumption that automated agents operate strictly as open-loop systems. Consequently, commercial network defenses widely deploy stateful, machine learning-based classifiers to evaluate telemetry over non-stationary sliding windows. While commercially popular, these empirical architectures operate under an intrinsic vulnerability: they assume the adversary's state trajectories will remain passive, allowing simple sensitivity adjustments to enforce boundary conditions.

This project demonstrates that such an assumption is theoretically incomplete. By reframing multi-node network traversal as an aerospace flight control problem within a denied physical environment, we show that stateful threshold engines can be reduced to deterministic linear operators. 

Our framework does not attempt to "evade" detection through heuristic obfuscation. Instead, it computes real-time mathematical constraints via Control Barrier Functions (CBF), rendering the detector's memory state forward-invariant within a pre-defined safe operating set. In a system governed by rigorous boundary control, blocking actuation becomes an algebraic impossibility.

---

## 📂 Repository Architecture
This repository contains the complete mathematical proofs and local numerical simulation suites developed by the **Institute of Bamboo and Cyber-Aerodynamics**[cite: 11]. The underlying theoretical frameworks are partitioned into two core publisher-ready assets:

* 📄 **Paper I (Temporal & Kinematic Tuning)**: [`docs/paper1_biomimetic_evasion.md`](docs/paper1_biomimetic_evasion.md)  
  _Investigates the decoupling of temporal power spectral density (PSD) using ergodic chaotic scheduling ($r=4.0$) and minimum-jerk Cubic Bézier trajectories to eliminate tracking parameters in ML-based classifiers._[cite: 9]
* 📄 **Paper II (Topological Optimization)**: [`docs/paper2_stateful_ratelimiters.md`](docs/paper2_stateful_ratelimiters.md)  
  _Addresses multi-proxy network traversal as an NP-Hard Adversarial Time-Varying Traveling Salesperson Problem (ATV-TSP) resolved via Monte Carlo Tree Search (MCTS) and microsecond-level 1D Quadratic Programming (QP) convex filters._

---

## 🛠️ Cyber-Aerodynamic Core Components

The **Garagara-Panda** architecture bypasses the non-deterministic overhead of traditional machine learning approaches by enforcing strict control laws across two synchronized loops[cite: 9]:

### 1. Outer-Loop Ergodic Scheduler & Meta-Tracking (Paper I)
* **Chaotic Delay Generation**: Modulates request intervals via a 1D Logistic Map operating at $r=4.0$[cite: 9]. The strictly positive Lyapunov Exponent ($\lambda \approx 0.693$) mathematically guarantees the complete neutralizing of auto-correlation estimators[cite: 9].
* **Lag-Free State Tracking**: Models firewall alertness as a stochastic differential equation (SDE)[cite: 9]. A Proportional-Integral-Derivative (PID) meta-controller dynamically self-optimizes the eigenvalues of a Loewner-bounded Kalman Filter, bypassing the phase lag that typically plagues static trackers during defense upgrades[cite: 9].

### 2. Inner-Loop Convex Safety Filtration (Paper II)
* **Combinatorial Path Pruning**: Leverages an MCTS pathfinder governed by UCB1 selection policies to optimize proxy hop sequences under time-varying risk matrices[cite: 10].
* **Analytical QP Actuator**: Executes a microsecond-level 1D convex solver[cite: 10]. By mapping the safety margin directly into a discrete-time Control Barrier constraint ($A_{\text{cbf}} \cdot u(k) \le b_{\text{cbf}}$), the framework dynamically throttles input velocity strictly below the critical block boundary ($x_{\text{max}} = 1.5$)[cite: 10].

---

## 📊 Wind-Tunnel Simulation Telemetry

The unified framework was subjected to a 10,000 sequential request horizon within our dynamic threat wind-tunnel[cite: 9, 10]. To evaluate systemic resilience against non-stationary defensive updates, a sudden $250\%$ escalation in detector sensitivity ($\psi$ scales from $1.0$ to $2.5$) was systematically injected between steps 4,000 and 6,500[cite: 10].

### Table 1: System Performance under Non-Stationary Stringency Constraints
| Architectural Paradigm | Total Inputs | Cumulative WAF Blocks | Evasion Survival Rate | Mathematical Status |
| :--- | :---: | :---: | :---: | :--- |
| **Group A (Open-Loop Baseline)** | 10,000 | 4,999 | 50.010% | Deterministic Boundary Violation[cite: 10] |
| **Group B (Unconstrained MCTS)** | 10,000 | 1,583 | 84.170% | Transient Manifold Leakage[cite: 10] |
| **Group C/D (GMC Constrained Autopilot)** | 10,000 | **0** | **100.000%** | **Provable Forward Invariance**[cite: 10] |

### Telemetry Analysis
The empirical data exposes a profound **control loop deficit** inherent in static, data-driven defense models[cite: 10]. 

* **The Open-Loop Vulnerability**: Lacking real-time feedback parameters, Group A experiences a mathematically predictable block cycle every $\sim 3$ requests during standard phases[cite: 10]. Upon encountering the sensitivity step-shocks at step 4,000, its trajectory suffers immediate, continuous absorption into the blocking threshold on every subsequent input, yielding exactly 4,999 blocks[cite: 10].
* **The Closed-Loop Invariance**: At the exact onset of the $250\%$ stringency upgrade (step 4,000), the inner-loop Control Barrier Function detects the immediate contraction of the safe manifold[cite: 10]. The analytical QP solver instantly scales down the nominal command, maintaining the threat state safely below the $1.5$ critical threshold[cite: 10]. Once the non-stationary perturbation subsides, the Control Lyapunov Function dynamically restores transmission velocity to peak operational efficiency, achieving a flawless $100.000\%$ survival profile with zero blocks[cite: 10].

---

## 🛡️ Academic Disclaimer & Safe Harbor
* **Simulation Boundaries**: This repository contains no active network exploits, session hijackers, or platform-specific bypass payloads[cite: 11]. The core wind-tunnel executes strictly within an isolated numerical environment using synthesized data[cite: 11].
* **Defensive Objective**: This framework is compiled exclusively for academic evaluation under the paradigm of Adversarial Machine Learning. By mathematically mapping the control-theoretic deficit of sliding-window heuristics, this research provides defensive security engineering teams with the necessary analytical insights required to structurally reform contemporary anomaly detection engines[cite: 11].
