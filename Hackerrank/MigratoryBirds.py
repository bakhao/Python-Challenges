

def migratoryBirds(arr):
    minimumFrequency = None
    frequency_id = {}
    for id in arr:
        if id in frequency_id:
            frequency_id[id] += 1
        else:
            frequency_id[id] = 1
    max_frequency = max(frequency_id.values())
    minimumFrequency = float('inf')
    for id, freq in frequency_id.items():
        if freq == max_frequency and id < minimumFrequency:
            minimumFrequency = id
    return minimumFrequency