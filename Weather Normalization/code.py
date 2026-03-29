import plotly.graph_objects as go
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# --- Parameters ---
f = 1e-4   # Coriolis parameter
Gx = -0.01
Gy = 0.00
Fx = -0.00035
Fy = -0.00058

# --- Time setup ---
t_max = 5 * 24 * 3600  
t_eval = np.linspace(0, t_max, 2000)
u0 = 3.0
v0 = 5.0
y0 = [u0, v0]

# --- ODE system ---
def ode_fun(t, state):
    u_, v_ = state
    du = f * v_ + Gx + Fx
    dv = -f * u_ + Gy + Fy
    return [du, dv]


sol = solve_ivp(ode_fun, [0, t_max], y0, t_eval=t_eval)
u = sol.y[0]
v = sol.y[1]
t_hours = sol.t / 3600  # convert time to hours

# --- Compute magnitude and direction ---
speed = np.sqrt(u**2 + v**2)
direction = np.degrees(np.arctan2(v, u))  # in degrees

# --- Create interactive 3D Plot ---
fig = go.Figure(data=[go.Scatter3d(
    x=u,
    y=v,
    z=t_hours,
    mode='lines',
    line=dict(color='magenta', width=4),
    name="Velocity Trajectory"
)])

fig.update_layout(
    scene=dict(
        xaxis_title="u (eastward velocity, m/s)",
        yaxis_title="v (northward velocity, m/s)",
        zaxis_title="Time (hours)"
    ),
    title="3D Interactive Trajectory of Wind Vector (u, v, t)",
    width=900,
    height=700
)

fig.show()

# --- Plot u(t) and v(t) ---
plt.figure(figsize=(10, 4))
plt.plot(t_hours, u, label='u (eastward)', color='blue')
plt.plot(t_hours, v, label='v (northward)', color='orange')
plt.xlabel("Time (hours)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity Components over Time")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t_hours, speed, label='Speed (m/s)', color='green')
plt.xlabel("Time (hours)")
plt.ylabel("Speed (m/s)")
plt.title("Velocity Magnitude over Time")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(t_hours, direction, label='Direction (degrees)', color='red')
plt.xlabel("Time (hours)")
plt.ylabel("Direction (° from East)")
plt.title("Velocity Direction over Time")
plt.legend()
plt.grid(True)
plt.show()
