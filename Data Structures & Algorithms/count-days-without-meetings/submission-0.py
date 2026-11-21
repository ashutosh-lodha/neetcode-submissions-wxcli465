class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        free_days = 0
        last_meeting_end = 0

        for start, end in meetings:
            # Add the gap before this meeting
            free_days += max(0, start - last_meeting_end - 1)

            # Extend the occupied period
            last_meeting_end = max(last_meeting_end, end)

        # Add free days after the last meeting
        return free_days + days - last_meeting_end
