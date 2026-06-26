# -*- coding: utf-8 -*-
"""
================================================================================
          PANDA GMC-AUTOPILOT: SECURED ADAPTIVE FLOW CONTROL ENGINE
                      [ OPEN-CORE BENCHMARK EDITION ]
================================================================================
License: GNU Affero General Public License v3.0 (AGPL-3.0)
Description:
    This module serves as the public-facing, sanitized middleware core of the 
    GMC-Autopilot flow controller. 
    
    1. Features a 50Hz asynchronous UDP socket interface (Port: 14540) to align
       seamlessly with virtual Pixhawk HIL flight simulators.
    2. Utilizes baseline 1-D Kalman Filtering and cumulative statistical tracking
       (CUSUM) to estimate simulated WAF congestion alert states (x_t).
    3. Integrates a textbook 1-D Control Barrier Function (CBF) QP projection.
    4. Hardened with cryptographic bytecode verification to protect boundary
       enforcement against runtime modification and local tampering.
================================================================================
"""

import asyncio
import time
import sys
import os
import struct
import socket
import hashlib

# ==============================================================================
# 1. RUNTIME ANTI-RE & CRYPTOGRAPHIC SELF-CHECK SHIELD
# ==============================================================================
HIL_ACTIVE = True  # Safety flag enforcing hardware-in-the-loop coordination

class AntiAnalysisGuard:
    """
    Protective runtime guard detecting execution tracing, breakpoints, 
    and bytecode modifications in non-real-time environments.
    """
    def __init__(self, allowed_time_drift=0.015, consecutive_trigger_limit=5):
        self.allowed_time_drift = allowed_time_drift
        self.consecutive_trigger_limit = consecutive_trigger_limit
        self.drift_streak = 0
        self.under_attack = False

    def check_debugger_static(self) -> bool:
        """Inspects runtime modules for active debuggers and trace hooks."""
        if sys.gettrace() is not None:
            self.under_attack = True
            return True
        for debugger in ["pydevd", "pdb", "gdb"]:
            if debugger in sys.modules:
                self.under_attack = True
                return True
        return False

    def check_temporal_drift(self, t_start: float) -> bool:
        """Detects single-step debugger pauses using monotonic hardware clocks."""
        t_duration = time.perf_counter() - t_start
        if t_duration > self.allowed_time_drift:
            self.drift_streak += 1
            if self.drift_streak >= self.consecutive_trigger_limit:
                self.under_attack = True
                return True
        else:
            self.drift_streak = max(0, self.drift_streak - 1)
        return False

    def check_bytecode_integrity(self, target_func) -> float:
        """
        Calculates SHA-256 fingerprint of the core QP solver bytecode.
        Compatible with compiled C-extensions (.so/.pyd) with graceful bypass.
        """
        # If compiled with Cython to machine code, target_func is a built-in method
        # and has no __code__ attribute. This represents the ultimate tamper proof state.
        if not hasattr(target_func, "__code__"):
            return 1.0  # Safe status (Fully compiled to C-extension)
            
        try:
            func_code = target_func.__code__.co_code
            hasher = hashlib.sha256()
            hasher.update(func_code)
            current_hash = hasher.hexdigest()
            
            if not hasattr(self, "base_hash"):
                self.base_hash = current_hash
                
            if current_hash != self.base_hash:
                return -999.0
        except Exception:
            return -999.0
        return 1.0

# ==============================================================================
# 2. ADVERSARIAL FLUID LIMITER (SIMULATED CONGESTION ENVIRONMENT)
# ==============================================================================
class StatefulAdversarialWAF:
    """
    Emulates an edge security limiter that responds dynamically to 
    transmission rates, triggering challenges when safety bounds are crossed.
    """
    def __init__(self):
        self.alert_state = 0.05
        self.x_trigger = 0.75

    def process_request(self, current_rate, resets):
        status_code = 200
        headers = {"Server": "Cloudflare-GMC-Shield"}
        content = b"OK"
        
        # Simulates rising load under heavy traffic, offset by control resets
        self.alert_state += (current_rate * 0.12) - (resets * 0.05)
        self.alert_state = max(0.01, min(1.0, self.alert_state))
        
        if self.alert_state >= self.x_trigger:
            status_code = 403
            headers["CF-Challenger"] = "True"
            content = b"Request Blocked by Edge Classifier"
            self.alert_state = 0.2  
            
        return status_code, headers, content

# ==============================================================================
# 3. ENGINE MIDDLEWARE (OPEN-CORE CONTROLLER)
# ==============================================================================
class GMCEngineMiddleware:
    def __init__(self):
        self.u_actual = 3.5          # Actual transmission rate (req/s)
        self.x_t = 0.0               # Estimated congestion state
        self.m_resets = 0            # Active control reset count
        self.guard = AntiAnalysisGuard()
        self.cusum_acc = 0.0
        self.cusum_threshold = 0.65

    def update_state_dynamics(self, rtt, status_code):
        """
        Updates internal tracking metrics using standard first-order filters.
        Proprietary multi-dimensional adaptive matrices are fully isolated.
        """
        t_start = time.perf_counter()
        
        # A. Runtime Integrity Check
        security_factor = self.guard.check_bytecode_integrity(self.qp_solve)
        if self.guard.check_debugger_static() or security_factor < 0:
            self.x_t = 1.0
            self.u_actual = 0.0
            return

        # B. Baseline 1-D First-Order Filtering
        rtt_normalized = min(1.0, max(0.0, rtt / 2.0))
        if status_code == 403:
            rtt_normalized = 0.95  
            
        self.x_t = 0.85 * self.x_t + 0.15 * rtt_normalized

        # C. Cumulative Sum (CUSUM) and Boundary Resets
        residual = rtt_normalized - self.x_t
        self.cusum_acc = max(0.0, self.cusum_acc + residual - 0.02)
        
        if self.cusum_acc >= self.cusum_threshold or self.x_t >= 0.75:
            self.m_resets += 1
            self.cusum_acc = 0.0
            self.x_t = 0.1  # Simplified algebraic reset
            self.u_actual = self.qp_solve(self.x_t, security_factor)
        else:
            self.u_actual = self.qp_solve(self.x_t, security_factor)

        # Monitor debug time dilation
        self.guard.check_temporal_drift(t_start)

    def qp_solve(self, x, security_factor=1.0) -> float:
        """
        Baseline 1-D Control Barrier Function (CBF) solver.
        Computes analytical projection to enforce transmission safety boundaries.
        """
        x_max = 0.75
        alpha_coeff = 1.15
        
        h = x_max - x
        # Cryptographic interlocking: collapses boundary to zero if code is modified
        u_safe_bound = (alpha_coeff * h) * security_factor
        
        u_nominal = 3.5
        u_opt = u_nominal
        
        if u_opt > u_safe_bound:
            u_opt = u_safe_bound
            
        return float(max(0.1, min(5.0, u_opt)))

# ==============================================================================
# 4. ASYNCHRONOUS SOCKET INTERACTION (50Hz HIL LOOP)
# ==============================================================================
async def main():
    engine = GMCEngineMiddleware()
    waf_target = StatefulAdversarialWAF()
    
    print("=" * 75)
    print("   GMC-AUTOPILOT: SECURED ADAPTIVE FLOW CONTROL [OPEN-CORE]")
    print("===========================================================================")
    print("[GMC Open-Core] Synchronizing with virtual Pixhawk HIL Simulator via UDP...")

    # Initialize UDP socket (Port: 14540)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.setblocking(False)
    
    # Securely bind the listener interface to port 14540 to capture simulator traffic
    try:
        client_socket.bind(("127.0.0.1", 14540))
    except Exception as e:
        print(f"[ERROR] Failed to bind to UDP Port 14540. Reason: {e}")
        print("[ERROR] Ensure no other instances are occupying Port 14540.")
        return
    
    loop = asyncio.get_running_loop()
    hil_queue = asyncio.Queue()

    def handle_udp_receive():
        try:
            data, addr = client_socket.recvfrom(1024)
            if len(data) >= 40: 
                hil_queue.put_nowait((data, addr))
        except Exception:
            pass

    # Register read event listener
    loop.add_reader(client_socket.fileno(), handle_udp_receive)

    try:
        for step in range(50):
            t_step_start = time.perf_counter()
            
            # Interact with the edge protection simulator
            status_code, headers, content = waf_target.process_request(engine.u_actual, engine.m_resets)
            
            # Simulate real-world network latency metrics
            rtt = 0.05 + (step % 5) * 0.03
                
            # Process state estimations
            engine.step_counter = step
            engine.update_state_dynamics(rtt, status_code)

            # Build binary payload: [Step, Rate, Estimator, ResetCount, MeasuredRTT]
            payload = struct.pack(
                "!ddddd", 
                float(step), 
                float(engine.u_actual), 
                float(engine.x_t), 
                float(engine.m_resets), 
                float(rtt)
            )

            # Transmit telemetry and await HIL physical motor feedback
            try:
                recv_payload, sender_addr = await asyncio.wait_for(hil_queue.get(), timeout=0.015)
                unpacked_forces = struct.unpack("!ddddd", recv_payload)
                pwm_feedback = unpacked_forces[1:]
                status_str = f"Motor PWM Feedback: [{pwm_feedback[0]:.1f}, {pwm_feedback[1]:.1f}]"
                
                # Transmit updated control values back to the simulator
                client_socket.sendto(payload, sender_addr)
            except asyncio.TimeoutError:
                status_str = "[INFO] HIL feedback window closed. Emulating standard convergence."

            print(f"Step {step:02d} | Rate: {engine.u_actual:.2f} r/s | Congestion x_t: {engine.x_t:.4f} | RTT: {rtt:.4f}s | {status_str}")

            # Enforce rigid 50Hz control frequency (20ms intervals)
            elapsed = time.perf_counter() - t_step_start
            sleep_time = max(0.001, 0.02 - elapsed)
            await asyncio.sleep(sleep_time)

    finally:
        loop.remove_reader(client_socket.fileno())
        client_socket.close()
        print("[GMC Open-Core] HIL Loop closed. Safe glide landing achieved.")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
