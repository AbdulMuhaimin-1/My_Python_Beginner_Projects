def totaldiff(sensor_a, sensor_b, size):
    diff = 0
    for i in range(size):
        diff = sensor_a[i] - sensor_b[i]
        return diff

def main():
    firstsensor = [15, -4, 56, 10, -23]
    secondsensor = [14, -9, 56, 14, -23]
    print(f"The total difference in sensor reading is: {totaldiff(firstsensor, secondsensor, 5)}")

main()