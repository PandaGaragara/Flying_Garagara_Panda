Flying Garagara Panda: Aerial Supremacy over WAF Heuristics 🐼 🛫

"They spent millions building fortress walls on the ground. We simply grew wings and flew over them."

Welcome to the official repository of Project Garagara — the home of Flying Garagara Panda, a unified, biomimetic, closed-loop cyber-evasion system that treats WAF bypass not as an exploit, but as a non-linear stochastic control problem.

This repository hosts the simulation wind-tunnel demonstrating a 99.810% evasion survival rate under aggressive, dynamic firewall postures.

🌪️ The Paradigm Shift: Dynamic Cyber-Dynamics

Traditional automated agents (web crawlers) fail because they are "grounded"—they behave like clumsy scripts with uniform delays or static random noise. WAF classifiers easily detect these using auto-correlation and temporal power spectral density (PSD).

Flying Garagara Panda introduces the Meta-Cognitive Autopilot framework:

Outer-Loop Biological Generator: Couples a 1D Logistic Map chaotic temporal scheduler ($r=3.99$, guaranteeing a strictly positive Lyapunov exponent $\lambda \approx 0.693$) with a minimum-jerk Cubic Bezier trajectory generator.

Inner-Loop Cognitive State Estimator: Tracks WAF alertness using an SDE modeled through a covariance-bounded Kalman Filter under Loewner partial ordering.

Meta-Controller: A PID law that dynamically adjusts the filter's uncertainty lower bounds to eliminate estimation lag during defense escalations.

Safety Guarantees: Mathematically enforced via Control Barrier Functions (CBFs) resolved dynamically through Quadratic Programming (QP).


🚀 Quick Start (Wind-Tunnel Simulation)

To witness the mathematical collapse of traditional behavioral classifiers, run the high-fidelity wind-tunnel simulation.

Prerequisites

pip install numpy matplotlib


Run the Wind-Tunnel

python core/panda_garagara_simulation_wind_tunnel.py


This will run 10,000 continuous sequential requests through an "Extreme Threat Phase" (simulating a dynamic firewall challenge upgrade between step 4000 and 6500) and generate a survivability graph showing:

Group A (Traditional Bot): Crumbles to a 17.52% survival rate.

Group D (Meta-Cognitive Autopilot): Soars with a near-perfect 99.81% survival rate.

📜 Academic Research Paper

The complete mathematical proofs, formulations, and empirical analyses are documented in docs/Panda_Garagara_Biomimetic_Evasion_2026.pdf.

Citation

@article{panda2026metacognitive,
  title={The Meta-Cognitive Autopilot: A Unified Control-Theoretic Framework for Biomimetic Evasion of Advanced Behavioral Classifiers},
  author={Panda, Garagara},
  journal={Institute of Bamboo and Cyber-Aerodynamics},
  year={2026}
}


⚠️ Warning to Defensive Security Teams

If you attempt to patch this by adding more static "heuristic features" or increasing the sensitivity of your classifiers, you will only feed our state estimator more training data. The more you try to pin the Panda down, the more chaotic ($r \to 4.0$) and unpredictable the flight path becomes.

The sky is ours. Feel free to adjust your security posture. It won't change the outcome. 🛫🐼
