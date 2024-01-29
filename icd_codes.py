from typing import List, Dict
from collections import defaultdict

# under pressure

lst = [['icd_2','icd_3'],['icd_3','icd_4', 'icd_2'],['icd_5']]

#Answer:- {icd_2:2, icd_3:2 , icd_4:2 , icd_5:0}

# working with sets instead of for loops and dicts could have been a better choice; we are just putting items in sets and counting the items - 1
def icd_counter(list_of_lists):
    counter_dict = {}

    for icd_list in list_of_lists:
        inner_list_set = set()

        for icd in icd_list:
            inner_list_set.add(icd)

            # init if needed; default dict could probably be a better choice
            if icd not in counter_dict:
                # counter and icd relation initialization
                counter_dict[icd] = [0, set()]
        
        # print(counter_dict)
        for counter_key in counter_dict.keys():
            # print("counter_key", counter_key)
            for relation in inner_list_set:
                # print("relation", relation)
                # print("relationships", counter_dict[counter_key][1])
                if counter_key in inner_list_set and relation != counter_key and relation not in counter_dict[counter_key][1]:
                    curr_set = counter_dict[counter_key][1]
                    curr_set.add(relation)
                    counter_dict[counter_key] = [counter_dict[counter_key][0]+1, curr_set]
                # print("counter_dict update:", counter_dict)    
    
    for key in counter_dict.keys():
        counter_dict[key] = counter_dict[key][0]

    return counter_dict

print(icd_counter(lst))


# not under pressure; thinking slower and clearer
def icd_counter2(list_of_lists: List[List[str]]) -> Dict[str, int]:
    """graph analysis: list of fully connected graphs provided.
    function counts the number of connected icd_codes for each icd_code node."""
    
    node_dict = {} # icd_code: [count, set_of_edges]

    for icd_list in list_of_lists:
        fully_connected_nodes = set()

        # create the set 
        for icd in icd_list:
            fully_connected_nodes.add(icd)

            # init if needed; default dict could probably be a better choice
            if icd not in node_dict:
                node_dict[icd] = [0, set()]
        
        # go through potential icd code nodes that will need to be incremented
        for relation_start in fully_connected_nodes:
            for relation_end in fully_connected_nodes:
                if relation_start != relation_end and relation_end not in node_dict[relation_start][1]:
                    node_dict[relation_start][1].add(relation_end)
                    node_dict[relation_start][0] += 1

    return {k: node_dict[k][0] for k in node_dict.keys()}

print(icd_counter2(lst))

# refining it to something elegant (after looking up how to initialize a default dict with a function)
def icd_counter3(list_of_lists: List[List[str]]) -> Dict[str, int]:
    """graph analysis: list of fully connected graphs provided.
    function counts the number of connected icd_codes for each icd_code node."""
    
    node_defaultdict = defaultdict(lambda: [0, set()]) # icd_code: [icd connection count, set of node connection edges]

    for icd_list in list_of_lists:
        for relation_start in icd_list:
            for relation_end in icd_list:
                curr_node = node_defaultdict[relation_start] # gets initalized ahead of time instead of creation and index at once
                if relation_start != relation_end and relation_end not in curr_node[1]:
                    curr_node[1].add(relation_end)
                    curr_node[0] += 1

    return {k: node_defaultdict[k][0] for k in node_defaultdict.keys()}

print(icd_counter3(lst))

# we don't even need the counter and maybe we don't need to to use curr_node to initialize it
def icd_counter4(list_of_lists: List[List[str]]) -> Dict[str, int]:
    """
    function counts the number of connected icd_code edges for each icd_code node.
    graph analysis: list of fully-connected node-lists provided.
    """
    
    node_edge_set = defaultdict(lambda: set()) # icd_code: set of node connections (edges)

    for icd_list in list_of_lists:
        for icd in icd_list:
            for to_icd in icd_list:
                node_edge_set[icd].add(to_icd) # will include itself

    return {k: len(node_edge_set[k]) - 1 for k in node_edge_set.keys()}

print(icd_counter4(lst))