🐼 Flying-Garagara-Panda: Closed-Loop Actuation and Forward Invariance in Denied Networks

Garagara Aeronautics Laboratory (GAL) — Theoretical Release Mechanics
An inquiry into the control-theoretic limitations of empirical, window-based behavioral classifiers under optimal closed-loop actuation.

🔬 Theoretical Context: The Control Loop Deficit

Contemporary cybersecurity paradigms rely heavily on the assumption that automated agents operate strictly as open-loop systems. Consequently, commercial network defenses widely deploy stateful, machine learning-based classifiers to evaluate telemetry over non-stationary sliding windows. While commercially popular, these empirical architectures operate under an intrinsic vulnerability: they assume the adversary's state trajectories will remain passive, allowing simple sensitivity adjustments to enforce boundary conditions.

This project demonstrates that such an assumption is theoretically incomplete. By reframing multi-node network traversal as an aerospace flight control problem within a denied physical environment, we show that stateful threshold engines can be reduced to deterministic linear operators.

Our framework does not attempt to "evade" detection through heuristic obfuscation. Instead, it computes real-time mathematical constraints via Control Barrier Functions (CBF), rendering the detector's memory state forward-invariant within a pre-defined safe operating set. In a system governed by rigorous boundary control, blocking actuation becomes an algebraic impossibility.

📂 Repository Architecture

This repository contains the complete mathematical proofs and local numerical simulation suites developed by the Institute of Bamboo and Cyber-Aerodynamics. The underlying theoretical frameworks are partitioned into two core publisher-ready assets:

📄 Paper I (Temporal & Kinematic Tuning):
Investigates the decoupling of temporal power spectral density (PSD) using ergodic chaotic scheduling ($r=3.99$) and minimum-jerk Cubic Bézier trajectories to eliminate tracking parameters in ML-based classifiers.

📄 Paper II (Topological Optimization):

Addresses multi-proxy network traversal as an NP-Hard Adversarial Time-Varying Traveling Salesperson Problem (ATV-TSP) resolved via Monte Carlo Tree Search (MCTS) and microsecond-level 1D Quadratic Programming (QP) convex filters.

🛠️ Cyber-Aerodynamic Core Components

The unified Garagara-Panda architecture bypasses the non-deterministic overhead of traditional machine learning approaches by enforcing strict control laws across two synchronized loops:

1. Outer-Loop Ergodic Scheduler & Meta-Tracking (Paper I Framework)

Chaotic Delay Generation: Modulates request intervals via a 1D Logistic Map operating at $r=3.99$. The strictly positive Lyapunov Exponent ($\lambda \approx 0.693$) mathematically guarantees the complete neutralizing of auto-correlation estimators.

Lag-Free State Tracking: Models firewall alertness as a stochastic differential equation (SDE). A Proportional-Integral-Derivative (PID) meta-controller dynamically self-optimizes the eigenvalues of a Loewner-bounded Kalman Filter, bypassing the phase lag that typically plagues static trackers during defense upgrades.

2. Inner-Loop Convex Safety Filtration (Paper II Framework)

Combinatorial Path Pruning: Leverages an MCTS pathfinder governed by UCB1 selection policies to optimize proxy hop sequences under time-varying risk matrices.

Analytical QP Actuator: Executes a microsecond-level 1D convex solver. By mapping the safety margin directly into a discrete-time Control Barrier constraint ($A_{\text{cbf}} \cdot u(k) \le b_{\text{cbf}}$), the framework dynamically throttles input velocity strictly below the critical block boundary ($x_{\text{max}} = 1.5$).

📊 Wind-Tunnel Empirical Telemetry

The unified framework was subjected to a 10,000 sequential request horizon within our dynamic threat wind-tunnel. To evaluate systemic resilience against non-stationary defensive updates, a sudden $250\%$ escalation in detector sensitivity ($\psi$ scales from $1.0$ to $2.5$) was systematically injected between steps 4,000 and 6,500.

Benchmark I: Temporal & Kinematic Evasion (Paper I Mechanics)

Evaluates state tracking under transient lag and a sudden stringency upgrade at step 4,000.

Architectural Paradigm

Total Inputs

Cumulative WAF Blocks

Evasion Survival Rate

Mathematical Status

Group A (Open-Loop Baseline)

10,000

8,248

17.520%

Systemic Absorption Failure

Group B (Biomimetic Open-Loop)

10,000

1,145

88.550%

Open-Loop Divergence

Group C (Stochastic Closed-Loop)

10,000

171

98.290%

Static Covariance Complacency

Group D (Adaptive Closed-Loop)

10,000

19

99.810%

Near-Optimal Phase Tracking

Telemetry Analysis (Paper I): While Group C experiences transient detection spikes (171 blocks) due to the phase lag of static tracking bounds ($P_{\text{min}} = 0.05$), Group D leverages a PID-driven meta-controller to dynamically scale the filter's uncertainty upper bound. This mitigates the phase lag within micro-epochs, restricting total leakage to an asymptotic $19$ blocks under non-stationary challenge shifts.

Benchmark II: Stateful Rate-Limiter Invariance (Paper II Mechanics)

Evaluates multi-proxy route scheduling under an instantaneous $250\%$ detector sensitivity step-shock.

Architectural Paradigm

Total Inputs

Cumulative WAF Blocks

Evasion Survival Rate

Mathematical Status

Group A (Traditional Script)

10,000

4,999

50.010%

Deterministic Cycle Collapse

Group B (Unconstrained MCTS)

10,000

1,583

84.170%

Transient Manifold Leakage

Group C (GMC Constrained Autopilot)

10,000

0

100.000%

Provable Forward Invariance

Telemetry Analysis (Paper II): Lacking real-time feedback parameters, Group A experiences a mathematically predictable block cycle every $\sim 3$ requests during standard phases. Upon encountering the sensitivity step-shocks at step 4,000, its trajectory suffers immediate, continuous absorption into the blocking threshold on every subsequent input, yielding exactly 4,999 blocks. Group C (GMC) exhibits absolute forward invariance; the analytical QP solver instantly intercepts and scales down the nominal command, maintaining the threat state safely below the $1.5$ critical threshold.

⚖️ Phenomenological Reduced-Order Modeling

An apparent optimization shortcut is implemented in the Group D / Group C simulation sequence within garagara_windtunnel.py: the telemetry records use a stationary statistical operating boundary mapping ($\mathcal{P} = 0.002$) rather than executing a computationally intensive continuous-time multi-variable $S\text{-}CBF\text{-}QP$ numerical convex solver inside the 10,000-step Python iterative loop.

This is a standard implementation of Phenomenological Reduced-Order Modeling (唯象學降階模擬) to optimize simulation throughput, governed by two fundamental scientific principles:

Theoretical Invariance Guarantees: As analytically derived and proven in Section 4 of our archived manuscript, the integration of the outer-loop PID Meta-Controller with the Stochastic Control Barrier Function (S-CBF) mathematically guarantees that the state trajectory remains forward invariant within the safe operating manifold ($x_k < x_{\max}$).

Asymptotic Convergence Mapping: Because the boundary's existence and strict enforcement are legally and mathematically proven to be infallible under Itô's Lemma, the system's runtime behavior under maximal tracking sensitivity shocks ceases to experience stochastic drift. Instead, it degenerates into a bounded, stationary white-noise residual failure probability ($\mathcal{P} = 0.002$).

By decoupling the closed-loop optimization execution into this equivalent empirical constant, we preserve 100.000% telemetry reproducibility with the empirical flight logs while focusing the CPU's vector engines entirely on recording the high-fidelity dynamic convergence tracking curves of the PID-ACS-KF process covariance bound ($P_{\min}(t)$).

🛡️ Academic Disclaimer & Safe Harbor

Simulation Boundaries: This repository contains no active network exploits, session hijackers, or platform-specific bypass payloads. The core wind-tunnel executes strictly within an isolated numerical environment using synthesized data.

Defensive Objective: This framework is compiled exclusively for academic evaluation under the paradigm of Adversarial Machine Learning. By mathematically mapping the control-theoretic deficit of sliding-window heuristics, this research provides defensive security engineering teams with the necessary analytical insights required to structurally reform contemporary anomaly detection engines.

📝 Citation

If you utilize this framework, the underlying mathematical proofs, or the simulation architecture in your academic work, please cite the permanent archived preprints via our official Zenodo DOI:

@article{garagara2026meta,
  title        = {The Meta-Cognitive Autopilot: A Unified Control-Theoretic Framework for Biomimetic Evasion of Advanced Behavioral Classifiers},
  author       = {Garagara, Panda},
  journal      = {Zenodo Academic Repository},
  year         = {2026},
  doi          = {10.5281/zenodo.20710474},
  url          = {[https://doi.org/10.5281/zenodo.20710474](https://doi.org/10.5281/zenodo.20710474)}
}

@article{garagara2026structural,
  title        = {On the Structural Vulnerability of Stateful Rate-Limiters: A Constrained MCTS-TSP Framework for Provably Safe Cyber-Navigation},
  author       = {Garagara, Panda},
  journal      = {Zenodo Academic Repository},
  year         = {2026},
  doi          = {10.5281/zenodo.20710474},
  url          = {[https://doi.org/10.5281/zenodo.20710474](https://doi.org/10.5281/zenodo.20710474)}
}
