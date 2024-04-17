from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n, meetings):
        """
        Time O(M * logM + M * logN) M -> meeting个数  N -> PQ里面的元素个数
        Space O(n)
        用两个min heap记录，一个记录当前available的room，一个记录当前正在进行的meeting的end时间和用的哪个room，
        我们每次check新的meeting的时候先看看正在开的meeting是不是有开完的，如果有开完的找到room编号最小的那个，
        然后给新的这个meeting排这个room，如果新来的和之前都有交集，那说明两种情况，第一种如果有空房间，直接把最小的排给新的，
        第二种如果没有新房间，说明需要等，也就会delay新来的meeting，找到最先完成的meeting，
        然后计算出delay时间，occupied_rooms heap添加更新过后delay的meeting完成时间和房间号。
        """
        # Create a list of available rooms using indices from 0 to num_rooms-1
        available_rooms = [room for room in range(n)]
        occupied_rooms = []  # Stores rooms that are currently occupied
        heapify(available_rooms)  # Convert the available_rooms list into a heap
        booking_counts = [0] * n  # Initialize a list to keep track of booking counts per room

        # Sort the meetings in ascending order based on the start time
        sorted_meetings = sorted(meetings, key=lambda x: x[0])
        for start_time, end_time in sorted_meetings:
            # Check if there are any available rooms at the start time of the meeting
            # 一定要先check当前是否有meeting已经完成了在新加入得meeting前，因为我们是选择完成meeting里面房间号最小的，而不是最先完成
            # 的房间，加入新的meeting的时候，所以需要弹出所有已经完成的meeting，并把房间号从新加入回available room
            while occupied_rooms and occupied_rooms[0][0] <= start_time:
                # Room becomes available, add it back to the available_rooms heap
                end, room = heappop(occupied_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                # Assign an available room from the available_rooms heap to the meeting
                room = heappop(available_rooms)
                heappush(occupied_rooms, [end_time, room])  # Add the meeting to the occupied_rooms heap
            else:
                # All rooms are occupied, find the room with the earliest end time
                current_end, room = heappop(occupied_rooms)
                new_end = current_end + end_time - start_time  # Update the room's end time
                heappush(occupied_rooms, [new_end, room])

            booking_counts[room] += 1  # Increment the booking count for the assigned room

        # Find the room with the maximum booking count and return its index
        max_booking_count = max(booking_counts)
        most_booked_room = booking_counts.index(max_booking_count)
        return most_booked_room


s = Solution()
print(s.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]]))
print(s.mostBooked(n=4, meetings=[[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]))
