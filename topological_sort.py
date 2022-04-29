# time: O(v+e) where v is vertices/jobs and edges are dependencies (just like a DFS approach time complexity)
# space: O(v+e)
def topologicalSort(jobs, deps):
    print("represent collection of jobs with prereqs as a directed graph")
    job_graph = Directed_graph(jobs)
    for prereq, job in deps:
        job_graph.add_prereqs(prereq, job)

    topologically_sorted_job_list = []

    print("priortize jobs/vertices w/ no prereqs")
    filtered_nodes = list(filter(lambda job_node: job_node.num_of_prereqs == 0, job_graph.nodes))

    print("append no-prereq vertices to output list & remove arrows since they are no longer prereq for any node.")
    while filtered_nodes:
        curr_node = filtered_nodes.pop()
        topologically_sorted_job_list.append(curr_node.job)
        remove_arrows_and_add_new_node(curr_node, filtered_nodes)

    print("see if there are any implied cycles before outputing")
    if any(node.num_of_prereqs > 0 for node in job_graph.nodes):
        return []
    else:
        return topologically_sorted_job_list


def remove_arrows_and_add_new_node(prereq_node, no_prereq_nodes):
    while prereq_node.needed_for:
        job = prereq_node.needed_for.pop()
        job.num_of_prereqs -= 1
        if job.num_of_prereqs == 0:
            no_prereq_nodes.append(job)


class Directed_graph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph_dict = {}  # could have used a list as well

        for job in jobs:
            self.add_node(job)

    def add_node(self, job_node):
        self.graph_dict[job_node] = Job_node(job_node)
        self.nodes.append(self.graph_dict[job_node])

    def get_node_obj(self, job_node):
        if job_node not in self.graph_dict:
            self.add_node(job_node)
        return self.graph_dict[job_node]

    def add_prereqs(self, prereq, job):
        prereq_node = self.get_node_obj(prereq)
        job_node = self.get_node_obj(job)
        prereq_node.needed_for.append(job_node)
        job_node.num_of_prereqs += 1


class Job_node:
    def __init__(self, job):
        self.job = job
        self.needed_for = []  # going to; will allow us to eliminate prereq arrows easily
        self.seen = False
        self.num_of_prereqs = 0
