class Graph_ES:
    def __init__(self, V = set(), E = set()):
        self._V = V
        self._E = E


    def __len__(self):
        return len(self._V)
    

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, V):
        self._V.add(V)

    def remove_vertex(self, V):
        for v in self._V:
            if v == V:
                self._V.remove(V)
                return

        raise KeyError('V not in graph')
    
    def add_edge(self, e):
        self._E.add(e)

    def remove_edge(self, e):
        if e in self._E:
            self._E.remove(e)

        else: raise KeyError('E not in graph')

    def _neighbors(self, v):
        edges = set()
        for u,w in self._E: 
            if u == v:
                edges.add(w)

        return edges
    

class Graph_AS:
    def __init__(self, V = set(), E = set()):
        self._V = V
        self._nbrs = {}
        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(e)


    def __len__(self):
        return len(self._V)
    

    def __iter__(self):
        return iter(self._V)

    def add_vertex(self, V):
        self._V.add(V)
        self._nbrs[V] = set()


    def remove_vertex(self, V):
        for v in self._V:
            if v == V:
                self._V.remove(V)
                return

        raise KeyError('V not in graph')
    
    def add_edge(self, e):
        v, w = e
        self._nbrs[v].add(w)

    def remove_edge(self, e):
        v, w = e
        if v in self._nbrs:
            self._nbrs[v].remove(w)

        else: raise KeyError('E not in graph')

    def _neighbors(self, v):
        return iter(self._nbrs[v])

