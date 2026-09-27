import heapq
from typing import List

class Solution:
    # self solved , asked by Deepak
    # Constructive Algorithm
    # TC: O(NlogN [sorting] + N*logN [Wrost case, when all the early comers never leave the party])

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(time, i) for i, time in enumerate(times)]
        times = sorted(times, key=lambda x:x[0][0])
        print(times)
        vacantChairs = list()
        nonEmptyChair = list()
        # heapq.heapify(vacantChairs)
        # heapq.heapify(nonEmptyChair)
        for time, fId in times:
            found = False
            # Check all the Vacant seats for current friend
            while(nonEmptyChair and nonEmptyChair[0][0] <= time[0]):
                min_chair = heapq.heappop(nonEmptyChair)
                # Push vacant chairs ChairId : min_chair[1] in the vacantChairs Min Heap
                heapq.heappush(vacantChairs, min_chair[1])
                found = True
            if found or vacantChairs:
                # Some of friends are left the party

                # Pick the minChair and make new arrived friend sit there
                min_chair = heapq.heappop(vacantChairs)
                if targetFriend == fId:
                    return min_chair
                
                # Push (Leaving, ChairIndex, freindID) in nonEmptyChair Min Heap, so that ChairId is not Vacant anymore
                heapq.heappush(nonEmptyChair, (time[1], min_chair, fId))
            if not found:
                # if first friend OR None of the friend has left the party

                # Push (Leaving, ChairIndex, freindID) in Min Heap
                heapq.heappush(nonEmptyChair, (time[1], len(nonEmptyChair), fId))
                if targetFriend == fId:
                    return len(nonEmptyChair)-1
                
if __name__ == '__main__':
    times = [[34167,60534],[60630,89180],[48573,81877],[53509,69027],[13079,25333],[89711,89767],[28805,43922],[25977,56144],[528,31398],[6748,93874],[64733,88382],[50274,52941],[95502,97229],[90688,93595],[81261,94153],[18850,59994],[42413,61445],[89930,96929],[95600,95849],[5329,50505],[83034,87122],[30427,51573],[90387,95139],[51980,88563],[82562,98036],[30694,58600],[45957,67135],[97064,97771],[66660,68834],[94640,99286],[21524,37219],[76795,89900],[79811,83819],[19451,47010],[26800,88830],[77436,93023],[93453,98564],[46654,62042],[77262,79360],[63260,95404],[53684,91281],[84135,98459],[93992,95157],[15506,71795],[22123,73407],[20552,92274],[66423,90807],[28674,32334],[99001,99523],[83280,97419],[45624,54798],[59214,94025],[68067,79088],[20872,54573],[21190,65833],[19161,96879],[37805,58798],[63181,74945],[74222,89454],[13446,14963],[6921,77989],[98553,99299],[84779,90074],[74189,98054],[54868,56501],[74690,88690],[73104,96025],[16937,34354],[6448,27829],[18378,54243],[75265,85678],[30159,34783],[1753,22910],[1689,8139],[58154,93484],[5076,31157],[70092,75270],[55284,68181],[2045,15795],[48898,72243],[50357,97998],[57324,95680],[35117,77065],[88270,97089],[90605,92758],[81811,98671],[58696,62748]]
    targetFriend = 52
    print(Solution().smallestChair(times, targetFriend))
    