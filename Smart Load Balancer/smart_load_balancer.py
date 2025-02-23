import csv
import random  # To spread appliance usage across non-peak hours

# Function to read appliance energy data from CSV
def read_energy_data():
    appliances = []
    with open('energy_data.csv', mode='r', encoding="utf-8") as file:  # Fixed encoding issue
        reader = csv.DictReader(file)
        for row in reader:
            appliances.append({
                'name': row['Appliance'],
                'power': float(row['Power_Consumption(kW)']),
                'hours': float(row['Usage_Hours'])
            })
    return appliances

# Function to calculate daily energy consumption for each appliance
def calculate_energy_usage(appliances):
    for device in appliances:  # Renamed 'appliance' to 'device' to prevent name conflict
        device['total_energy'] = round(device['power'] * device['hours'], 2)  # Round to 2 decimal places
    return appliances

# Function to suggest the best time to use appliances
def suggest_best_time(device):
    peak_hours = range(18, 22)  # Peak hours: 6 PM - 10 PM
    non_peak_hours = [h for h in range(24) if h not in peak_hours]  # All other hours

    # Choose a well-distributed non-peak hour
    best_time = random.choice(non_peak_hours)  
    return best_time

# Main execution
if __name__ == "__main__":
    # Read CSV data
    appliance_data = read_energy_data()

    # Calculate energy usage
    appliance_data = calculate_energy_usage(appliance_data)

    # Display energy consumption and best time suggestions
    print("\n📌 **Daily Energy Consumption for Each Appliance:**")
    for device in appliance_data:
        print(f"{device['name']} uses {device['total_energy']} kWh per day.")

    print("\n⚡ **Suggested Best Time to Use Appliances (Avoiding Peak Hours):**")
    for device in appliance_data:
        best_time = suggest_best_time(device)
        print(f"Best time to use {device['name']}: {best_time}:00")
