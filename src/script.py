import tkinter as tk
import math

class HexagonMover:
    def __init__(self, root):
        self.root = root
        self.root.title("Move the Hexagons")
        
        # Setup canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Define hexagon parameters
        self.hex_radius = 50
        self.hex_color = "#ADD8E6" # Light Blue
        
        # Create some predefined hexagons
        self.create_hexagon(100, 100)
        self.create_hexagon(300, 200)
        self.create_hexagon(500, 150)

        # Variables for dragging
        self.selected_item = None
        self.offset_x = 0
        self.offset_y = 0

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def create_hexagon(self, x, y):
        """Creates a hexagon polygon centered at (x, y)"""
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.radians(angle_deg)
            px = x + self.hex_radius * math.cos(angle_rad)
            py = y + self.hex_radius * math.sin(angle_rad)
            points.append(px)
            points.append(py)
        
        # Create polygon and tag it as 'hexagon' for identification
        self.canvas.create_polygon(points, fill=self.hex_color, 
                                   outline="black", width=2, tags="hexagon")

    def on_press(self, event):
        """Finds the clicked hexagon"""
        item = self.canvas.find_closest(event.x, event.y)[0]
        if "hexagon" in self.canvas.gettags(item):
            self.selected_item = item
            self.offset_x = event.x
            self.offset_y = event.y

    def on_drag(self, event):
        """Moves the selected hexagon"""
        if self.selected_item:
            dx = event.x - self.offset_x
            dy = event.y - self.offset_y
            self.canvas.move(self.selected_item, dx, dy)
            self.offset_x = event.x
            self.offset_y = event.y

    def on_release(self, event):
        """Resets selection"""
        self.selected_item = None

if __name__ == "__main__":
    root = tk.Tk()
    app = HexagonMover(root)
    root.mainloop()
