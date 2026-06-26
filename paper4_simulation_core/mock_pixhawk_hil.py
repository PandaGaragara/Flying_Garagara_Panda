# -*- coding: utf-8 -*-
"""
================================================================================
          PANDA GMC-AUTOPILOT: MOCK PIXHAWK HIL SIMULATION HARNESS
================================================================================
License: GNU Affero GPL v3.0 (AGPL-3.0)
Description:
    Emulates a 50Hz virtual Pixhawk flight control processor. Communicates
    directly with the middleware over UDP loopback to exchange physical
    telemetry and simulated motor response characteristics.
================================================================================
"""

import asyncio
import struct
import socket
import numpy as np

class MockPixhawkHIL:
    def __init__(self, target_ip="127.0.0.1", target_port=14540):
        self.target_ip = target_ip
        self.target_port = target_port
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)
        self.sock.bind(("127.0.0.1", 0))  # Bind to a random free local port
        
        self.step = 0
        self.running = True

    def generate_simulated_aerodynamics(self):
        """Generates standard textbook UAV dynamics under crosswind turbulence."""
        pitch_bias = 250.0 + np.random.normal(0, 15.0)
        roll_bias = -180.0 + np.random.normal(0, 12.0)
        yaw_bias = 95.0 + np.random.normal(0, 5.0)
        
        # Emulates transient physical drag response
        motor_1 = 1500.0 + pitch_bias - roll_bias
        motor_2 = 1500.0 - pitch_bias + roll_bias
        motor_3 = 1500.0 + pitch_bias + roll_bias
        motor_4 = 1500.0 - pitch_bias - roll_bias
        
        return [motor_1, motor_2, motor_3, motor_4]

    async def run_loop(self):
        print(f"[Mock HIL] Initializing virtual Pixhawk core...")
        print(f"[Mock HIL] Broadcasting simulated avionics to middleware at {self.target_ip}:{self.target_port}...")
        
        loop = asyncio.get_running_loop()
        queue = asyncio.Queue()
        
        def on_data_received():
            try:
                data, addr = self.sock.recvfrom(1024)
                queue.put_nowait(data)
            except Exception:
                pass
                
        loop.add_reader(self.sock.fileno(), on_data_received)
        
        try:
            while self.running and self.step < 50:
                try:
                    # Formulate physical feedback
                    motors = self.generate_simulated_aerodynamics()
                    
                    # Pack payload: [Step, Motor1, Motor2, Motor3, Motor4]
                    payload = struct.pack(
                        "!ddddd", 
                        float(self.step), 
                        float(motors[0]), 
                        float(motors[1]), 
                        float(motors[2]), 
                        float(motors[3])
                    )
                    
                    # Send feedback payload to middleware
                    self.sock.sendto(payload, (self.target_ip, self.target_port))
                    
                    # Wait for middleware flow control rates (15ms timeout window)
                    try:
                        recv_data = await asyncio.wait_for(queue.get(), timeout=0.015)
                        if len(recv_data) >= 40:
                            telemetry = struct.unpack("!ddddd", recv_data)
                            curr_rate = telemetry[1]
                            curr_state = telemetry[2]
                            print(f"HIL Step {self.step:02d} | Rx Rate: {curr_rate:.2f} r/s | Est Congestion: {curr_state:.4f}")
                    except asyncio.TimeoutError:
                        print(f"HIL Step {self.step:02d} | [INFO] Middleware tracking window closed. Normal operation.")
                except Exception as e:
                    print(f"HIL Simulation Loop Error: {e}")
                    
                self.step += 1
                await asyncio.sleep(0.02)  # Maintain stable 50Hz scheduling
        finally:
            loop.remove_reader(self.sock.fileno())
            self.sock.close()
            print("[Mock HIL] Simulation harness safely shutdown.")

if __name__ == "__main__":
    hil = MockPixhawkHIL()
    asyncio.run(hil.run_loop())
