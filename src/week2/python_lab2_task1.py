# 1. Create a list of temperatures for one week
temperatures = [22, 24, 19, 23, 25, 21, 20]  # example temperatures

# 2. Create a dictionary of city populations
city_population = {
    "Istanbul": 15000000,
    "Ankara": 5500000,
    "Izmir": 4500000,
    "Bursa": 3000000,
    "Antalya": 2500000
}

# 3. Compute aggregates

# Average temperature
average_temperature = sum(temperatures) / len(temperatures)

# Maximum and minimum population
largest_city = max(city_population, key=city_population.get) # type: ignore
largest_population = city_population[largest_city]

smallest_city = min(city_population, key=city_population.get) # type: ignore
smallest_population = city_population[smallest_city]

# Total population
total_population = sum(city_population.values())

# 4. Print results
print(f"Average temperature: {average_temperature:.2f}°C")
print(f"Largest city: {largest_city} - {largest_population}")
print(f"Smallest city: {smallest_city} - {smallest_population}")
print(f"Total population of all cities: {total_population}")