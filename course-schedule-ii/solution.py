class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #
        # BFS approach
        #   Time complexity: O(N + E)
        #       N ... numCourses
        #       E ... number of prerequisites
        #
        #   Space complexity: O(N + E)
        #
        courses = [0] * numCourses
        graph = {}
        for courseIdx, preIdx in prerequisites:

            # courses[couseIdx] keeps the number of prerequisite courses
            courses[courseIdx] += 1

            # graph[preIdx] keeps the next available courses
            nexts = graph.get(preIdx, [])
            nexts.append(courseIdx)
            graph[preIdx] = nexts

        # BFS search.
        # Starts from the courses which have no prerequisites
        q = []
        for i in range(numCourses):
            if courses[i] == 0:
                q.append(i)

        ans = []
        while(q):
            courseIdx = q.pop(0)

            # Take this course
            courses[courseIdx] -= 1


            # Some prerequisite courses are remained
            if courses[courseIdx] > 0:
                continue

            # if all prerequisite courses are completed,
            # add this course to the ans
            ans.append(courseIdx)

            if courseIdx in graph:
                # Add next available course indicies
                for nextIdx in graph[courseIdx]:
                    q.append(nextIdx)

        # All courses are completed
        if (len(ans) == numCourses):
            return ans

        # There is a cycled course
        else:
            return []
