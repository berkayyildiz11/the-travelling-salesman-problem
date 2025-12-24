import matplotlib.pyplot as plt
import numpy as np

def plot_route(cities_dict, tour_indices, title="TSP Route", start_city_index=None):
    x_coords = []
    y_coords = []
    
    # Handle start city rotation
    if start_city_index is not None:
        # Convert tour_indices to list to avoid numpy issues
        tour_list = list(tour_indices)
        if start_city_index in tour_list:
            start_pos = tour_list.index(start_city_index)
            display_order = np.roll(tour_indices, -start_pos)
        else:
            print(f"Warning: Start city {start_city_index} not found in tour.")
            display_order = tour_indices
    else:
        display_order = tour_indices

    # Build coordinates
    for city_idx in display_order:
        # Try accessing by ID directly, handle potential 0 vs 1 indexing mismatch
        if city_idx in cities_dict:
            c = cities_dict[city_idx]
        elif (city_idx + 1) in cities_dict:
            c = cities_dict[city_idx + 1]
        else:
            continue # Should not happen if data is consistent
            
        x_coords.append(c.x)
        y_coords.append(c.y)

    # Close the loop
    if x_coords:
        x_coords.append(x_coords[0])
        y_coords.append(y_coords[0])

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(x_coords, y_coords, 'o-', mfc='r', mec='k', markersize=8, label='Route')
    plt.plot(x_coords[0], y_coords[0], 'D', color='green', markersize=12, label='Start City')
    
    plt.title(title)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid(True)
    plt.show()

def visualize_five_starts(cities_dict, best_tour_indices):
    # Pick 5 equidistant points in the tour to show diversity
    step = len(best_tour_indices) // 5
    start_points = [best_tour_indices[i * step] for i in range(5)]
    
    print("\n--- Generating Plots for 5 Different Starting Cities ---")
    for start_node in start_points:
        plot_route(cities_dict, best_tour_indices, 
                   title=f"Route Starting from City {start_node}", 
                   start_city_index=start_node)