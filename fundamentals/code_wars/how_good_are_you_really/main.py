def better_than_average(class_points, your_points):
    sum = 0 
    count = 0
    for points in class_points:
        sum += points
        count += 1
    average = sum / count
    if your_points > average:
        return True
    else:
        return False