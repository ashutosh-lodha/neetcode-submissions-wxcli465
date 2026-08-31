class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Process meetings in order of their start time

        rooms = []                 # (when_room_is_free, room_number)
        meeting_count = [0] * n    # Number of meetings held in each room


        # Initially, every room is free at time 0
        for room in range(n):
            heapq.heappush(rooms, (0, room))


        for start, end in meetings:

            # Make rooms that are free before the meeting starts
            # available at exactly 'start'
            while rooms and rooms[0][0] < start:
                free_time, room = heapq.heappop(rooms)
                heapq.heappush(rooms, (start, room))

            # Get the room that becomes available first
            free_time, room = heapq.heappop(rooms)

            # Meeting duration
            duration = end - start

            # Put the room back with its new ending time
            heapq.heappush(rooms, (free_time + duration, room))

            # Count this meeting for the room
            meeting_count[room] += 1


        # Return the room with the most meetings
        return meeting_count.index(max(meeting_count))