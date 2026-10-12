class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_0 = students.count(0)
        count_1 = students.count(1)

        for s in sandwiches:
            if s:
                if count_1:
                    count_1 -= 1
                else:
                    return count_0
            else:
                if count_0:
                    count_0 -= 1
                else:
                    return count_1
        
        return 0