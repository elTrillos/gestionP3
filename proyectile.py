import math
class proyectile():


    def calculate_trajectory(angle_deg, initial_velocity, initial_x, initial_y, time_step, gravity, wind_acceleration, obstacle):
        # Convert angle from degrees to radians
        angle_rad = math.radians(angle_deg)
        
        # Initialize the initial velocity components
        velocity_x = initial_velocity * math.cos(angle_rad)
        velocity_y = initial_velocity * math.sin(angle_rad)

        # Initialize time
        time = 0
        projectile_path = []

        while initial_y >= 0:
            # Calculate new position
            new_x = initial_x + velocity_x * time + 0.5 * wind_acceleration * time**2
            new_y = initial_y + velocity_y * time - 0.5 * gravity * time**2
            projectile_path.append((new_x, new_y))

            # Update velocity_y
            velocity_y = velocity_y - gravity * time_step

            # Print position at one-second intervals
            if int(time) % 1 == 0:
                print(f"Time: {int(time)} seconds - X: {new_x:.2f} meters - Y: {new_y:.2f} meters")

            # Break the loop when y position is 0 or below
            if new_y <= 0:
                print("Projectile has reached the ground.")
                break
            if proyectile.detect_colision(projectile_path,obstacle):
                print("Projectile has reached the obstacle.")
                break

            # Update time
            time += time_step
        
        return projectile_path
    
    def detect_colision(projectile_path,obstacle):
        for [x,y] in projectile_path:
            if obstacle.x<x<obstacle.x+obstacle.width and obstacle.y<y<obstacle.y+obstacle.height:
                return True
        return False