from dataclasses import dataclass
import math

@dataclass(frozen=True)
class City:
    name: str
    x: float
    y: float
    
def load_cities(file_path: str) -> dict[int, City]:
    """Load cities from a file and return a dictionary of City objects."""

    cities = {}
    
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            
            if not line:
                continue  # skip empty lines

            parts = line.split()
            if len(parts) != 3:
                raise ValueError(
                    f"Invalid format at line {line_num}: {line}"
                )
            
            city_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            cities[city_id] = City(city_id, x, y)

    ## print(f"Loaded {len(cities)} cities from {file_path}")
    ## print(f"City {cities[12].name}: x = {cities[12].x}, y = {cities[12].y}")  # Example access to city with ID 12
    ## print(f"City {cities[25].name}: x = {cities[25].x}, y = {cities[25].y}")  # Example access to city with ID 25
    ## print(f"City {cities[39].name}: x = {cities[39].x}, y = {cities[39].y}")  # Example access to city with ID 39

    return cities

def load_distance_matrix(file_path: str) -> list[list[float]]:
    """Load a distance matrix from a file and return it as a 2D list."""

    distance_matrix = []
    
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            
            if not line:
                continue  # skip empty lines

            row = [float(value) for value in line.split()]
            distance_matrix.append(row)

    ## print("Distance matrix loaded successfully.")
    ## for row in distance_matrix:
    ##     print("\n")
    ##     print(" ".join(str(value) for value in row))

    return distance_matrix

