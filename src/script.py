import tkinter as tk
import math


class ShapesMover:
    def __init__(self, root):
        self.root = root
        self.root.title("Hex")

        # Setup canvas
        self.canvas_width = 1850
        self.canvas_height = 1000
        self.canvas = tk.Canvas(
            root, width=self.canvas_width, height=self.canvas_height, bg="white"
        )
        self.canvas.pack()

        # Variables for dragging
        self.selected_item = None
        self.offset_x = 0
        self.offset_y = 0

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.create_initial_shapes()

    def create_initial_shapes(self):
        """Fill the canvas with stacks of shapes"""
        # Create some predefined hexagons
        n = 10
        x_first = 100
        y_space = 150
        self.create_stack(1, x_first, 1 * y_space, "#FFFFFF", self.create_hexagon)
        self.create_stack(n, x_first, 2 * y_space, "#999999", self.create_hexagon)
        self.create_stack(n, x_first, 3 * y_space, "#3d85c6", self.create_hexagon)
        self.create_stack(n, x_first, 4 * y_space, "#f1c232", self.create_hexagon)
        self.create_stack(n, x_first, 5 * y_space, "#6aa84f", self.create_hexagon)
        self.create_stack(1, x_first, 6 * y_space, "#FFFFFF", self.create_hexagon)
        # Create some predefined rectangles
        n = 5
        x_first = self.canvas_width - 100
        self.create_stack(3, x_first, 1 * y_space, "#ffffff", self.create_rectangle)
        self.create_stack(n, x_first, 2 * y_space, "#838383", self.create_rectangle)
        self.create_stack(n, x_first, 3 * y_space, "#ff0000", self.create_rectangle)
        self.create_stack(n, x_first, 4 * y_space, "#3a66b6", self.create_rectangle)
        self.create_stack(n, x_first, 5 * y_space, "#d8bd25", self.create_rectangle)
        self.create_stack(3, x_first, 6 * y_space, "#000000", self.create_rectangle)

    def create_stack(
        self,
        n: int,
        x_first: float,
        y_first: float,
        color: str,
        shape_function: callable,
    ):
        """create n new hexagons of the same color with a certain offset to one another"""
        x_offset = 10.0
        y_offset = 5.0
        for i in range(n):
            shape_function(x_first + i * x_offset, y_first + i * y_offset, color=color)

    def create_rectangle(self, x, y, color):
        """Creates a rectangle centered at (x, y)"""
        height = 50.0
        width = 30.0
        points = [
            x - width / 2,
            y - height / 2,
            x - width / 2,
            y + height / 2,
            x + width / 2,
            y + height / 2,
            x + width / 2,
            y - height / 2,
        ]
        # Create polygon and tag it as 'hexagon' for identification
        self.canvas.create_polygon(
            points, fill=color, outline="black", width=2, tags="hexagon"
        )

    def create_hexagon(self, x, y, color):
        """Creates a hexagon polygon centered at (x, y)"""
        # Define hexagon parameters
        hex_radius = 50
        points = []
        for i in range(6):
            angle_deg = 60 * i
            angle_rad = math.radians(angle_deg)
            px = x + hex_radius * math.cos(angle_rad)
            py = y + hex_radius * math.sin(angle_rad)
            points.append(px)
            points.append(py)

        # Create polygon and tag it as 'hexagon' for identification
        self.canvas.create_polygon(
            points, fill=color, outline="black", width=2, tags="hexagon"
        )

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
    app = ShapesMover(root)
    root.mainloop()
