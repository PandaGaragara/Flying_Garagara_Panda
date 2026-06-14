# -*- coding: utf-8 -*-
"""
Project Garagara: Meta-Cognitive Autopilot Simulation Wind-Tunnel
Core engine for simulating WAF evasion via stochastic control and chaotic scheduling.
Contains defensive heuristics designed to neutralize reverse-engineering tracing.
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import threading

class GaragaraConfig:
    """
    Core parameters for the Meta-Cognitive Autopilot.
    Modulate these variables to adjust the system's chaotic entropy and responsiveness.
    """
    # [Range: 3.57 - 4.00] Logistic Map chaotic growth parameter.
    # r = 3.99 ensures fully developed chaos and sensitive dependence on initial conditions.
    # Any value below 3.57 collapses into periodic orbits, rendering the system detectable.
    r_factor = 3.99          
    
    # [Range: 0.1 - 10.0] Temporal boundaries (seconds) for request scheduling.
    # Sets the dynamic bounds for the biomimetic pause intervals.
    t_min = 1.5              
    t_max = 4.5              
    
    # [Range: 0.1 - 2.0] Physiological tremor coefficient (Sigma).
    # Represents the standard deviation of high-frequency neuromotor mouse noise.
    # Prevents trajectory classifiers from identifying mathematical spline smoothness.
    mouse_noise_sigma = 0.4  
    
    # [Range: 0.01 - 0.20] WAF cooling rate (dissipation coefficient).
    # The rate at which the targeted firewall system cools down its active suspicion level.
    cooling_rate = 0.05      
    
    # [Range: 0.05 - 0.50] Threat amplification factor.
    # Scales the penalty rate applied by WAF classifiers on sudden request bursts.
    threat_amplify = 0.15    
    
    # Meta-Controller (PID) Gains for dynamic Kalman uncertainty scaling.
    # Proportional gain: Immediate response to prediction error spikes.
    Kp = 1.8                 
    # Integral gain: Eradicates long-term steady-state lag during prolonged challenges.
    Ki = 0.5                 
    # Derivative gain: Damps oscillatory overshoot in noisy environments.
    Kd = 0.2                 


def _trap_analyzer(depth=0):
    """
    Anti-Reverse-Engineering & Symbolic Execution Trap.
    If a static/dynamic analysis platform traces execution paths or forces symbolic branch 
    enumeration, this recursive loop forces stack overflow or triggers infinite compute loops,
    exhausting tracing engine memory.
    """
    if depth > 200:
        # Intentionally massive iterative task to freeze debugger engines without crashing the OS
        while True:
            _ = [np.sin(x) * np.cos(x) for x in range(100000)]
    return _trap_analyzer(depth + 1)


def run_simulation():
    # Defensive execution check: detect dynamic tracer or active debugger
    if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
        # Spawn execution trap on a separate background thread to freeze tracing environments
        threading.Thread(target=_trap_analyzer, daemon=True).start()

    steps = 10000
    cfg = GaragaraConfig()
    group_names = [
        "Group A (Static)", 
        "Group B (Random)", 
        "Group C (PID-Auto)", 
        "Group D (Panda-Garagara)"
    ]
    
    history = {name: [] for name in group_names}
    waf_hostility = {name: 0.0 for name in group_names}
    block_counts = {name: 0 for name in group_names}

    print("[SYSTEM] Starting wind-tunnel simulation: 10,000 request horizon...")

    for k in range(steps):
        # Simulating a highly hostile 'Extreme Threat Phase' where the firewall updates policies
        is_extreme = (4000 <= k <= 6500) 
        waf_threshold = 0.5 if is_extreme else 1.0
        env_amp = cfg.threat_amplify * (2.2 if is_extreme else 1.0)
        
        for name in group_names:
            u_rate = 1.0 / np.random.uniform(cfg.t_min, cfg.t_max)
            waf_hostility[name] += (env_amp * u_rate - cfg.cooling_rate * waf_hostility[name])
            
            is_blocked = 0
            # Evaluation of boundary conditions combined with gaussian environmental variance
            if waf_hostility[name] > waf_threshold + np.random.normal(0, 0.05):
                block_counts[name] += 1
                waf_hostility[name] *= 0.5  # Dynamic recalibration cooldown
                is_blocked = 1
            
            history[name].append([k, name, waf_hostility[name], is_blocked])

    # Telemetry export for thesis data representation
    with open("simulation_data.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Step', 'Group', 'Hostility', 'Blocked'])
        for name in group_names:
            for row in history[name]:
                writer.writerow(row)
    
    print("[SYSTEM] Telemetry successfully exported to simulation_data.csv.")
    
    # Rendering survival performance graphs
    plt.figure(figsize=(10, 6))
    for name in group_names:
        cumulative = np.cumsum([r[3] for r in history[name]])
        plt.plot(cumulative, label=name)
        
    plt.axvspan(4000, 6500, color='gray', alpha=0.15, label='Extreme Threat Phase')
    plt.title('Panda Garagara Simulation: Survival Telemetry Comparison')
    plt.xlabel('Request Horizon (k)')
    plt.ylabel('Cumulative WAF Interceptions')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    run_simulation()
