class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for query in queries:
            p1 = p2 =  0
            N1, N2 = len(query), len(pattern)
            while(p1 < N1) and (p2 < N2):
                isP1Lower = query[p1].islower()
                isP2Lower = pattern[p2].islower()

                if isP1Lower == isP2Lower:
                    if query[p1] != pattern[p2]:
                        if (isP2Lower):
                            # Continue p1 to find the expect point
                            #
                            #  ControlPanel
                            #    ↑  ↑
                            #   p1  expect
                            #
                            #  CooP
                            #    ↑
                            p1 += 1
                        else:
                            break;
                    else:
                        # If the characters at p1 and p2 are the same,
                        # move on to the next character on the pattern.
                        p1 += 1
                        p2 += 1
                else:
                    # If the character cases at p1 and p2 do not match,
                    # continue p1
                    p1 += 1


            if (p2 == N2) and (p1 < N1):
                #
                # If p2 reaches to the end on the pattern,
                # but p1 doesn't, we still have some characters on the query.
                # Since lowercase English letters may ignore,
                # it's true if all the remained characters on the query are lower case.
                #
                # ---------------
                #  (True case)
                #
                #  FooBar
                #     ↑
                #  FB
                #   ↑
                # ---------------
                #  (False case)
                #
                #  FooBarTest
                #     ↑
                #  FB
                #   ↑
                while(p1 < N1) and (query[p1].islower()):
                    p1 += 1

            #
            # Both p1 and p2 should reach to the ends
            #
            ans.append((p1 == N1) and (p2 == N2))
        return ans
