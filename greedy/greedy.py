# Greedy Algorithm

def activity_selection(start, finish):
    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])  # Sort activities by finish time
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]
    
    for activity in activities[1:]:
        start_time, finish_time = activity
        if start_time >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = finish_time
    
    return selected_activities

start_times = [1, 3, 0, 5, 8, 5]
finish_times = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start_times, finish_times)
print(selected)
