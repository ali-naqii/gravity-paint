import tkinter as tk
import math
import random

# ── Config ─────────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 900, 700
NUM_PARTICLES = 80
GRAVITY = 3000
DAMPING = 0.995
TRAIL_LENGTH = 40
BG = "#0a0a1a"

# Beautiful color palette
COLORS = [
    "#ff6b6b", "#feca57", "#48dbfb", "#ff9ff3",
    "#54a0ff", "#5f27cd", "#01a3a4", "#f368e0",
    "#ff6348", "#7bed9f", "#70a1ff", "#ffa502",
]

# ── Particle ──────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, canvas, x=None, y=None):
        self.canvas = canvas
        self.x = x or random.uniform(50, WIDTH - 50)
        self.y = y or random.uniform(50, HEIGHT - 50)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.color = random.choice(COLORS)
        self.size = random.uniform(2, 5)
        self.trail = []
        self.id = None
        self.trail_ids = []

    def update(self, mx, my, attract):
        # Direction to mouse
        dx = mx - self.x
        dy = my - self.y
        dist = max(math.hypot(dx, dy), 10)

        # Gravity force (inverse square, capped)
        force = GRAVITY / (dist * dist + 100)
        force = min(force, 0.8)

        # Apply force
        if attract:
            self.vx += (dx / dist) * force
            self.vy += (dy / dist) * force
        else:
            # Repel
            self.vx -= (dx / dist) * force * 2
            self.vy -= (dy / dist) * force * 2

        # Damping
        self.vx *= DAMPING
        self.vy *= DAMPING

        # Move
        self.x += self.vx
        self.y += self.vy

        # Wrap around screen edges
        if self.x < 0: self.x = WIDTH
        if self.x > WIDTH: self.x = 0
        if self.y < 0: self.y = HEIGHT
        if self.y > HEIGHT: self.y = 0

        # Store trail point
        self.trail.append((self.x, self.y))
        if len(self.trail) > TRAIL_LENGTH:
            self.trail.pop(0)

    def draw(self):
        # Delete old drawings
        for tid in self.trail_ids:
            self.canvas.delete(tid)
        self.trail_ids.clear()

        # Draw trail
        if len(self.trail) > 1:
            for i in range(1, len(self.trail)):
                # Fade: older = more transparent
                alpha = i / len(self.trail)
                x1, y1 = self.trail[i - 1]
                x2, y2 = self.trail[i]

                # Approximate transparency with color brightness
                r, g, b = int(self.color[1:3], 16), int(self.color[3:5], 16), int(self.color[5:7], 16)
                r = int(r * alpha * 0.6)
                g = int(g * alpha * 0.6)
                b = int(b * alpha * 0.6)
                color = f"#{r:02x}{g:02x}{b:02x}"

                width = max(1, self.size * alpha)
                tid = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
                self.trail_ids.append(tid)

        # Draw particle
        r = self.size
        tid = self.canvas.create_oval(
            self.x - r, self.y - r, self.x + r, self.y + r,
            fill=self.color, outline="", width=0
        )
        self.trail_ids.append(tid)


# ── App ────────────────────────────────────────────────────────────────────────
class GravityPaint:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌌 Gravity Paint")
        self.root.configure(bg=BG)
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG, highlightthickness=0)
        self.canvas.pack()

        self.mx, self.my = WIDTH // 2, HEIGHT // 2
        self.attract = True
        self.particles = []

        # Spawn initial particles
        for _ in range(NUM_PARTICLES):
            self.particles.append(Particle(self.canvas))

        # Bindings
        self.canvas.bind("<Motion>", self.on_move)
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<B1-Motion>", self.on_move)
        self.root.bind("<space>", self.on_space)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        # Instructions
        self.canvas.create_text(
            WIDTH // 2, 25,
            text="🖱️ Move = attract  |  🖱️ Click = spawn  |  🖱️ Right-click = repel  |  Space = reset  |  Esc = quit",
            fill="#555577", font=("Consolas", 10)
        )

        # Gravity well indicator
        self.well_id = None

        self.loop()
        self.root.mainloop()

    def on_move(self, e):
        self.mx, self.my = e.x, e.y

    def on_left_click(self, e):
        # Spawn burst of particles at click
        for _ in range(8):
            self.particles.append(Particle(self.canvas, e.x, e.y))

    def on_right_click(self, e):
        self.attract = not self.attract

    def on_space(self, e):
        # Reset
        for p in self.particles:
            for tid in p.trail_ids:
                self.canvas.delete(tid)
        self.particles.clear()
        for _ in range(NUM_PARTICLES):
            self.particles.append(Particle(self.canvas))

    def loop(self):
        # Draw gravity well indicator
        if self.well_id:
            self.canvas.delete(self.well_id)

        # Pulsing circle at cursor
        pulse = 8 + 3 * math.sin(len(self.particles) * 0.05)
        color = "#444466" if self.attract else "#664444"
        self.well_id = self.canvas.create_oval(
            self.mx - pulse, self.my - pulse,
            self.mx + pulse, self.my + pulse,
            outline=color, width=1
        )

        # Update and draw particles
        for p in self.particles:
            p.update(self.mx, self.my, self.attract)
            p.draw()

        # Keep particle count reasonable
        while len(self.particles) > 300:
            old = self.particles.pop(0)
            for tid in old.trail_ids:
                self.canvas.delete(tid)

        # Particle count display
        self.canvas.delete("counter")
        self.canvas.create_text(
            WIDTH - 10, HEIGHT - 10, anchor="se",
            text=f"Particles: {len(self.particles)}",
            fill="#333355", font=("Consolas", 9), tags="counter"
        )

        self.root.after(16, self.loop)  # ~60fps


if __name__ == "__main__":
    GravityPaint()



