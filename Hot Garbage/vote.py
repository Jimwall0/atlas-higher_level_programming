#!/usr/bin/python3
class Candidate:
    def __init__(self, name: str, votes = 0):
        self.name = name
        self.votes = votes
    def __str__(self):
        return print("{} votes ({})".format(self.name, self.votes))

class VotingBooth:
    def __init__(self) -> None:
        self.candidates = []

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def vote(self, candidate):
        for c in self.candidates:
            if c == candidate:
                c.votes = c.votes + 1
    
George = Candidate("George")
vb = VotingBooth()
vb.add_candidate(George)
vb.vote(George)
print(f"{George.votes}")
