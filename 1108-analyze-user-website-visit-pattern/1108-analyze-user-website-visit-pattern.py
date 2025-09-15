class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """
        Given username := List[str] -> username[i]   |      Username visit website at timestamp 

              website := List[str] -> website[i].    |

              timestamp := List[int] -> timestamp[i]  |


        Pattern := list of three websites. May or may not be all disitinct

        Score of a pattern := number of users that visited all the websites inthe pattern in the same order they apperead in the pattern


        Input: 
            username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
            timestamp = [1,2,3,4,5,6,7,8,9,10],
            website = ["home","about","career","home","cart","maps","home","home","about","career"]

     {
        joe: [home, about, career]
     }

     {
        "home": [joe, jamesx2, mary]
        "about", [joe, mary]
        "career",[ joe, mary]
        "cart", [james]
        "maps",[james]
     }


        """

        users = defaultdict(list)
        
        for user, time, site in sorted(
            zip(username, timestamp, website), key=lambda x: (x[0], x[1])
            ):
            users[user].append(site)
        
        patterns = Counter()
        for user, sites in users.items():
            patterns.update(
               set(combinations(sites, 3))
            )
            
        return max(sorted(patterns), key=patterns.get)
        