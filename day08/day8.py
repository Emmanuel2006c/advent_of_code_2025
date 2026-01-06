import time,re,itertools,math

def loadfile(file):
    with open(file) as f:
        return [tuple(int(coord) for coord in line.split(',')) for line in f.read().splitlines()]

def distance(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]- b[2])**2

class Circuit:
    def __init__(self, members):
        self.members = list(members) if members is not None else []

    def merge(self,circuit_to_merge):
        for member in circuit_to_merge.members:
            if member not in self.members:
                self.members.append(member)
    
    def add(self,junction):
        if junction not in self.members:
            self.members.append(junction)

    def __repr__(self):
        return f"Circuit(members={self.members})"
    
    def __len__(self):
        return len(self.members)

    def contains(self,junction):
        return junction in self.members

  
def solve(p):
    p1 = 1
    p2 = 0 
    junction_boxes = p
    total_points = len(junction_boxes)
    distances = []
    for a,b in itertools.combinations(p,2):
        distances.append((distance(a,b),a ,b))
    distances = sorted(distances)
    circuits = []
    def findcircuit(junction):
        for circuit in circuits:
            if circuit.contains(junction):
             return circuit
        return None
    
    for distance_value,a,b in distances[:1000]:
        circuit_a = findcircuit(a)
        circuit_b = findcircuit(b)

        if circuit_a is None and circuit_b is None:
            new_circuit = Circuit([a,b])
            circuits.append(new_circuit)
        elif circuit_a is not None and circuit_b is None:
            circuit_a.add(b)
        elif circuit_a is None and circuit_b is not None:
            circuit_b.add(a)
        elif circuit_a is not circuit_b:
            circuit_a.merge(circuit_b)
            circuits.remove(circuit_b)
      
    sorted_circuits = sorted(circuits, key = len, reverse = True)
    threebiggestcircuits = sorted_circuits[:3]
    for circuit in threebiggestcircuits:
        p1*=len(circuit)

    connected = set()
    for circuit in circuits:
        connected.update(circuit.members)
    
    last_connection = None

    for distance_value,a,b in distances[1000:]:
        circuit_a = findcircuit(a)
        circuit_b = findcircuit(b)

        last_connection = (a, b)
        
        if circuit_a is None and circuit_b is None:
            new_circuit = Circuit([a,b])
            circuits.append(new_circuit)
            connected.add(a)
            connected.add(b)
        elif circuit_a is not None and circuit_b is None:
            circuit_a.add(b)
            connected.add(b)
        elif circuit_a is None and circuit_b is not None:
            circuit_b.add(a)
            connected.add(a)
        elif circuit_a is not circuit_b:
            circuit_a.merge(circuit_b)
            circuits.remove(circuit_b)

        if len(connected) == total_points:
            print(f"Last connection: {last_connection[0]} and {last_connection[1]}")
            p2 += last_connection[0][0] * last_connection[1][0]
            break
    
    return p1,p2

start_time = time.perf_counter()
print(f"Solution: {solve(loadfile('day8.txt'))}")
print(f"Thought for {time.perf_counter() - start_time:.6f} Seconds")