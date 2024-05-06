from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
        
    """
    N = number of days
    V = value of package delivered on that day
    C = cost to enter the mail room (Note: you need to at least enter it on the last day to collect the packages)
    S = probability all packages in the mail room will get stolen on any given day
    """
    # Level in binary tree is set of all the paths of take-pass possibilities through a given day
    level = [[0, 0, 0]] # [[profit_taken_through_node, residual_end_of_day_at_node, day]]
    # [[7, 0, 1], [0, 8.5, 1]]

    def get_children(level):
       print(level)
       print(level[0][2])
       nonlocal N, V, C, S
       if level[0][2] == N:
          return level
       
       next_level = []

       for node in level:
          next_level.extend(get_children([[node[0] + V[node[2]] - C + node[1], 0, node[2] + 1]]))
          next_level.extend(get_children([[node[0], (V[node[2]] + node[1]) * (1 - S), node[2] + 1]]))
          
       return next_level
    
    final_row_of_nodes = get_children(level)
    print(final_row_of_nodes)
    return max([node_list[0] for node_list in final_row_of_nodes])

def getMaxExpectedProfit2(N: int, V: List[int], C: int, S: float, profit: float = 0.0, day: int = 0, residual: float = 0.0) -> float:
   if day == N:
      return profit
   return max(getMaxExpectedProfit2(N,V,C,S, profit + V[day] - C  + residual, day + 1, 0), getMaxExpectedProfit2(N,V,C,S, profit, day + 1, (V[day] + residual)*(1-S)))

if __name__ == "__main__":
  print(getMaxExpectedProfit(5, [10, 2, 8, 6, 4], 3, 0.15))
  print(getMaxExpectedProfit2(5, [10, 2, 8, 6, 4], 3, 0.15, 0.0, 0, 0.0))