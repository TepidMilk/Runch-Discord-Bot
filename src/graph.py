class HomiePointsGraph:
    def __init__(self):
        self.graph = {}

    def add_debt(self, from_person, to_person, points):
        if from_person not in self.graph:
            self.add_person(from_person)
        if to_person not in self.graph:
            self.add_person(to_person)

        if to_person in self.graph[from_person]:
            self.graph[from_person][to_person] += points
        else:
            self.graph[from_person][to_person] = points

    def settle_debt(self, from_person, to_person, points = 0):
        if points == 0:
            self.graph[from_person][to_person] = 0
        if self.graph[from_person][to_person] < points:
            difference = points - self.graph[from_person][to_person]
            self.graph[to_person][from_person] = difference
            self.graph[from_person][to_person] = 0
        else:
            self.graph[from_person][to_person] -= points

    def get_debt(self, from_person, to_person):
        return self.graph.get(from_person, {}).get(to_person, 0)

    def get_total_debt(self, person):
        return sum(self.graph[person].values())

    def get_total_owed(self, person):
        total = 0
        for p in self.graph:
            if person in self.graph[p]:
                total += self.graph[p][person]
        return total

    def __str__(self):
        return "\n".join([f"{from_person} owes {to_person} {points} points" 
                          for from_person in self.graph 
                          for to_person, points in self.graph[from_person].items()])