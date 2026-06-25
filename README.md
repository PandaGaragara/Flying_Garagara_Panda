GMC-Autopilot: Control-Theoretic Invariance for Stochastic Impulsive Hybrid Systems

📌 1. System Philosophy & Control-Theoretic Paradigm

Modern behavioral classification and rate-limiting frameworks rely heavily on high-capacity empirical function approximators (e.g., non-convex loss-driven deep neural networks) to predict state boundaries. However, under non-stationary parameters and sudden boundary step-shocks, these heuristic and probabilistic approximation methods suffer from inherent feedback latency and state boundary violations.

GMC-Autopilot presents a deterministic control-theoretic alternative. We establish that under closed-loop actuation, any unmodeled, non-linear classification boundary can be reduced to a set of trivial linear operators. Safety invariance is a topological property of state space trajectories to be mathematically guaranteed, not a probabilistic gamble on gradient descent.

This repository hosts the academic verification engines and numerical sandboxes for Project Garagara (Phase I & II).

🛰️ 2. Dual-Loop Architecture & System Topology

We formalize multi-node network trajectory scheduling as a constrained Adversarial Time-Varying Traveling Salesperson Problem (ATV-TSP). To resolve real-time control rates while eliminating algebraic loops within a single computational epoch, the framework deploys a dual-loop hierarchical output-feedback control architecture.

    [ Outer Loop: Macro-Temporal Decision Layer ]
    ┌──────────────────────────────────────────────┐
    │              MCTS-TSP Planner                │
    │  Resolves ATV-TSP over Proxy Networks        │
    └──────────────────────┬───────────────────────┘
                           │
                           │ Feedforward Command: u_nominal
                           ▼
    [ Inner Loop: Micro-Temporal Safety Filtering ]
    ┌──────────────────────────────────────────────┐
    │ 1. Asymmetric Temporal Decoupling Sequence   │
    │    Prevents algebraic loops & feedback lag   │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ 2. Statistical CUSUM & Supermartingale Cushion│
    │    Pre-allocates safety buffer margins       │
    └──────────────────────┬───────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────┐
    │ 3. 1D CLF-CBF-QP Analytical Convex Actuator  │
    │    Enforces microsecond-level safety locks   │
    └──────────────────────┬───────────────────────┘
                           │
                           │ Closed-Loop Safe Actuation: u*
                           ▼
    ┌──────────────────────────────────────────────┐
    │   Stochastic Impulsive Hybrid System (SIHS)  │
    └──────────────────────────────────────────────┘


2.1 Asymmetric Temporal Decoupling

To prevent algebraic loops and computational lag at edge nodes, we decouple macro-temporal routing from micro-temporal safety filtration via a lower-triangular causal interface:

$$u_{nominal,k} \leftarrow \arg\max_{v} \mathcal{U}_{\text{MCTS}}(s_{k|k-1})$$

$$u_{k}^* \leftarrow \arg\min_{u_k} \left( \frac{1}{2}\|u_k - u_{nominal,k}\|^2 + q_u \|u_k - u_{k-1}^*\|^2 \right) \quad \text{s.t.} \quad A_{cbf}u_k \le b_{cbf} - \mathcal{D}_{delay}$$

$$s_{k+1|k} \leftarrow \mathcal{F}_{\text{hybrid}}(s_{k|k}, u_{k}^*)$$

Separating feedforward assignment and feedback registration by an asymmetric one-step temporal operator guarantees the existence, uniqueness, and immediate convergence of the control solution without computational bottlenecks.

2.2 Supermartingale Robust Cushion & CUSUM Observer

To protect the continuous safe flow-set against high-amplitude sudden impulse shocks, the inner-loop Control Barrier Function (CBF) incorporates a statistical drift observer:

Latency Absorption: During a sudden non-stationary parameter transition, the Cumulative Sum (CUSUM) drift observer experiences an inherent statistical accumulation lag of up to $\tau_{max} = 3$ steps.

Supermartingale Cushion: To prevent boundary penetration during this blind spot, we inject a pre-allocated Supermartingale Robust Cushion:

$$\mathcal{D}_{delay} = \sum_{j=1}^{\tau_{max}} \Delta t (\eta \cdot \psi_{max} \cdot u_{max})$$

This mathematical margin strictly dominates the real-world state drift acting upon the unobserved transition window, forcing the state evolution to behave as a discrete-time supermartingale process that asymptotically tracks a conservative invariant sub-set underneath the critical boundary.

📐 3. Hybrid System Capacity Limits & Zeno Exclusion

When facing active, memory-driven non-cooperative classifiers that employ cross-layer fingerprint correlation tracking, we model the active parameter resets as a Stochastic Impulsive Hybrid System (SIHS).

3.1 Ultimate Admissible Resilience Infimum ($m_{max}$)

Unlike empirical strategies that falsely assume state boundaries can be preserved under infinite parameter adjustments, we derive the exact analytical ceiling of the systemic capacity limit:

$$m_{max} = \left\lfloor \log_{\gamma_{punish}} \left( \frac{x_{trigger}}{\delta_{0} x_{max}} \right) \right\rfloor$$

Beyond this collapse boundary, the geometric intersection of the Control Barrier manifold and physical actuator limits degrades into a null set. To prevent flow-set vacuum deadlocks ($\mathcal{C}_{flow} = \emptyset$), the controller preemptively activates a Zero-Flow Active Safe Hold ($u^*_k = 0.0$), preserving strict hybrid forward invariance.

3.2 Topological Zeno Behavioral Exclusion

In physical actuators, pathologically high-frequency sliding limit cycles (Zeno anomalies) lead to actuator fatigue and system chattering. We prove that our hybrid system exhibits a strictly positive parametric minimum dwell-time $\tau_D(m)$ between consecutive discrete transitions:

$$\tau_D(m) \ge \frac{x_{trigger} - \delta_{evasion}(m)x_{max}}{\Delta t (\eta \psi_{max} u_{max} - d)} > 0, \quad \forall m \le m_{max}$$

This proof mathematically guarantees that infinite discrete jumps within a compact time interval are impossible, ensuring exceptional system stability compared to empirical, heuristic trial-and-error strategies.

🛠️ 4. Microsecond-Level Analytical Convex Solver

The low-level filter bypasses the need for computationally heavy commercial convex solvers by exploiting the $1\text{-D}$ nature of the CLF-CBF-QP formulation:

$$\min_{u} \frac{1}{2} \|u - u_{nominal}\|^2 \quad \text{s.t.} \quad A_{cbf} \cdot u \le b_{cbf}$$

This optimization problem admits an exact, microsecond-level analytical solution of $\mathcal{O}(1)$ complexity:

$$u^*(k) = \max\left(u_{min}, \min\left(u_{max}, u_{unbounded}\right)\right)$$

where $u_{unbounded} = b_{cbf}/A_{cbf}$ if $A_{cbf}\cdot u_{nominal} > b_{cbf}$, and $u_{nominal}$ otherwise.

This mathematical simplification allows the complete safety-critical control loop to run on resource-constrained embedded hardware, such as Pixhawk running NuttX RTOS, without introducing computational latency jitter.

📊 5. Telemetry & Numerical Verification

To validate our control-theoretic assertions, we executed a 10,000-step sequential stress test within a dynamic, non-stationary simulation wind-tunnel. Between steps $4,000 \le k \le 6,500$, the environment injected an "Extreme Threat Phase" where classifier sensitivity scaled by 250%.

5.1 Invariant Evasion Telemetry (10,000 Steps)

Experimental Group

Total Steps

Boundary Violations

Forward Invariance Rate (Survival Rate)

Heuristic Open-Loop Policy (Group A)

10,000

4,999

50.010%

Unconstrained MCTS Planner (Group B)

10,000

1,583

84.170%

GMC Autopilot (Group C - Proposed)

10,000

0

100.000% (Absolute Invariance)

5.2 Environment and Execution Decoupling Note

Please note that the open-source code disclosed in this repository provides isolated simulation environments for verification:

Phase I Academic Flight Data Engine simulates the Observer state estimation dynamics.

Phase II Dynamic Threat Wind-Tunnel Simulator validates the Controller trajectory optimization and analytical $1\text{-D}$ safety-locking.

To fully replicate a unified web-protection loop against cross-layer delays, the state estimator from Phase I and the actuator filter from Phase II must be cross-coupled and unified.

🔐 6. Source Disclosure & Intellectual Property Protection

To balance academic transparency with the strict preservation of structural intellectual property, our codebase roadmap is partitioned as follows:

Foundational Framework (Papers 1, 2, and 3): The complete, runnable Python scripts corresponding to these initial mathematical developments are fully open-sourced under the MIT license in this repository. These files include the runtime anti-analysis guards (AAG) and active timing-drift benchmarks (enforce_integrity_shields()).

Production Core (Paper 4 - Proprietary): The high-performance, enterprise-grade execution engine containing the real-time unified Stochastic MCTS-TSP trajectory planner, the cross-layer dynamic CUSUM state observer, and the hardware-in-the-loop (HIL) optimized analytical QP solver is strictly kept proprietary. There are no plans to release this production-grade core to the public domain.
