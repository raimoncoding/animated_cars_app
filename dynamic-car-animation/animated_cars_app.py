import tkinter as tk

class AnimatedCarsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animated Cars")
        self.geometry("600x300")

        # Create a canvas for the cars to move on
        self.canvas = tk.Canvas(self, width=600, height=250)
        self.canvas.pack()

        # Define the start positions for the cars
        self.start_positions = [(10, 50, 60, 70), (10, 120, 60, 140), (10, 190, 60, 210)]

        # Create three cars with different starting positions and colors
        self.cars = [self.canvas.create_rectangle(*pos, fill=color) for pos, color in zip(self.start_positions, ["red", "green", "blue"])]

        # Speed control slider for the cars
        self.speed_scale = tk.Scale(self, from_=0, to=100, orient="horizontal", label="Cars Speed")
        self.speed_scale.pack()

        # Radio buttons to control the animation
        self.animation_control = tk.StringVar(value="all")

        self.start_all_radiobutton = tk.Radiobutton(self, text="Start All Cars", value="all",
                                                    variable=self.animation_control, command=self.start_animation, bg="#FFAAAA")
        self.start_all_radiobutton.pack()

        self.start_one_by_one_radiobutton = tk.Radiobutton(self, text="Start Cars One by One", value="one_by_one",
                                                           variable=self.animation_control, command=self.start_animation, bg="#AAFFAA")
        self.start_one_by_one_radiobutton.pack()

        self.reset_radiobutton = tk.Radiobutton(self, text="Reset Cars", value="reset",
                                                variable=self.animation_control, command=self.reset_cars, bg="#AAAAFF")
        self.reset_radiobutton.pack()

    def start_animation(self):
        choice = self.animation_control.get()
        if choice == "all":
            self.start_all_cars()
        elif choice == "one_by_one":
            self.start_cars_one_by_one()

    def start_all_cars(self):
        # Animate all cars simultaneously
        for car in self.cars:
            self.animate_car(car)

    def start_cars_one_by_one(self, index=0):
        # Animate cars one after the other
        if index < len(self.cars):
            self.animate_car(self.cars[index], lambda: self.start_cars_one_by_one(index + 1))

    def animate_car(self, car, callback=None):
        # Move the car on the canvas based on the speed set by the slider
        speed = self.speed_scale.get()
        position = self.canvas.coords(car)
        if position[2] < self.canvas.winfo_width():  # Check if the car has not yet reached the end of the canvas
            self.canvas.move(car, speed / 10, 0)  # Move the car
            self.after(50, lambda: self.animate_car(car, callback))  # Wait and repeat
        else:
            if callback:
                callback()  # Call the callback after the animation if there is one

    def reset_cars(self):
        # Reset all cars to their starting positions
        for car, pos in zip(self.cars, self.start_positions):
            self.canvas.coords(car, pos)

if __name__ == "__main__":
    app = AnimatedCarsApp()
    app.mainloop()
