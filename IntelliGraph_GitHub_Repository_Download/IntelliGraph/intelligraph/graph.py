from collections import deque

class KnowledgeGraph:
    """Adjacency-list graph: each topic maps to its prerequisite topics."""
    def __init__(self, prerequisites=None):
        self.prerequisites={}
        for topic, reqs in (prerequisites or {}).items():
            self.add_topic(topic)
            for req in reqs: self.add_prerequisite(topic, req)

    def add_topic(self, topic):
        topic=topic.strip()
        if not topic: raise ValueError("Topic cannot be empty.")
        self.prerequisites.setdefault(topic, [])

    def add_prerequisite(self, topic, prerequisite):
        topic, prerequisite=topic.strip(), prerequisite.strip()
        if not topic or not prerequisite: raise ValueError("Topic and prerequisite are required.")
        if topic==prerequisite: raise ValueError("A topic cannot be its own prerequisite.")
        self.add_topic(topic); self.add_topic(prerequisite)
        if prerequisite not in self.prerequisites[topic]:
            self.prerequisites[topic].append(prerequisite)
            if self.has_cycle():
                self.prerequisites[topic].remove(prerequisite)
                raise ValueError("Dependency rejected because it creates a cycle.")

    def has_cycle(self):
        state={t:0 for t in self.prerequisites}
        def visit(t):
            state[t]=1
            for req in self.prerequisites[t]:
                if state[req]==1: return True
                if state[req]==0 and visit(req): return True
            state[t]=2
            return False
        return any(state[t]==0 and visit(t) for t in self.prerequisites)

    def prerequisite_closure(self, target):
        if target not in self.prerequisites: raise KeyError(f"Unknown target: {target}")
        found=set(); stack=list(self.prerequisites[target])
        while stack:
            t=stack.pop()
            if t not in found:
                found.add(t); stack.extend(self.prerequisites[t])
        return found

    def learning_path(self, target, mastered=()):
        needed=self.prerequisite_closure(target)|{target}
        indegree={t:0 for t in needed}; dependents={t:[] for t in needed}
        for topic in needed:
            for req in self.prerequisites[topic]:
                if req in needed:
                    indegree[topic]+=1; dependents[req].append(topic)
        queue=deque(sorted(t for t,d in indegree.items() if d==0)); order=[]
        while queue:
            cur=queue.popleft(); order.append(cur)
            for nxt in sorted(dependents[cur]):
                indegree[nxt]-=1
                if indegree[nxt]==0: queue.append(nxt)
        mastered=set(mastered)
        return [t for t in order if t not in mastered]

    def summary(self):
        return [{"topic":t,"prerequisites":list(reqs)} for t,reqs in sorted(self.prerequisites.items())]

    def connections(self):
        return sorted((req,topic) for topic,reqs in self.prerequisites.items() for req in reqs)
