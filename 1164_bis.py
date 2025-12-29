def read_datas():
    n = int(input())
    arrivals = []
    departures = []
    for _ in range(n):
        arrival, depart = map(int, input().split())
        arrivals.append(arrival)
        departures.append(depart)
    return n, arrivals, departures
 
 
def solve(n, arrivals, departures):
 
    rooms = []
    max_room = 0
 
    sorted_depart_indices = sorted(range(n), key=departures.__getitem__)
    sorted_arrival_indices = sorted(sorted_depart_indices, key=arrivals.__getitem__)
 
    consumer_depart_idx_it = iter(sorted_depart_indices)
    consumer_depart_index = next(consumer_depart_idx_it)
    rooms_attributions = [-1] * n
 
    for arrival_index in sorted_arrival_indices:
 
        curr_start = arrivals[arrival_index]
 
        while departures[consumer_depart_index] < curr_start:
            # restore the freed room
            rooms.append(rooms_attributions[consumer_depart_index])
            consumer_depart_index = next(consumer_depart_idx_it)
 
        if not rooms:
            # create more rooms if needed
            max_room += 1
            rooms.append(max_room)
 
        # use a new room
        rooms_attributions[arrival_index] = rooms.pop()
 
    return max_room, rooms_attributions
 
 
def solve2(n, arrivals, departures):
    rooms = []
    max_room = 0
 
    t_dim = 2 * n
    i_dim = n
    events = [
        *(t_dim * t + i for i, t in enumerate(arrivals)),
        *(t_dim * t + i + i_dim for i, t in enumerate(departures)),
    ]
    events.sort()
    rooms_attributions = [-1] * n
 
    for value in events:
        # unused
        # time = value // n_p
 
        other = value % t_dim
        index = other % i_dim
        is_departure = other // i_dim
 
        if is_departure:
            rooms.append(rooms_attributions[index])
        else:
            if not rooms:
                max_room += 1
                rooms.append(max_room)
            rooms_attributions[index] = rooms.pop()
 
    return max_room, rooms_attributions
 
 
def main():
 
    n, arrivals, departures = read_datas()
 
    # number_of_rooms, rooms_attributions = solve(n, arrivals, departures)
    # print(number_of_rooms)
    # print(*rooms_attributions)
 
    number_of_rooms, rooms_attributions = solve2(n, arrivals, departures)
    print(number_of_rooms)
    print(*rooms_attributions)
 
 
main()