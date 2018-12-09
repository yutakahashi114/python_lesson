import cirq
import random

length = 3

qubits = [cirq.GridQubit(i, j) for i in range(length) for j in range(length)]
print(qubits)

# circuit = cirq.Circuit()
# circuit.append(cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0 )
# circuit.append(cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1 )
# print(circuit)

# for i, m in enumerate(circuit):
#     print('Moment {}: {}'.format(i, m))

# circuit = cirq.Circuit()
# circuit.append([cirq.H(q) for q in qubits if (q.row + q.col) % 2 == 0], strategy = cirq.InsertStrategy.EARLIEST )
# circuit.append([cirq.X(q) for q in qubits if (q.row + q.col) % 2 == 1], strategy = cirq.InsertStrategy.EARLIEST )
# print(circuit)

def rot_x_layer(length, half_turns):
    rot = cirq.XPowGate(exponent=half_turns)
    for i in range(length):
        for j in range(length):
            yield rot(cirq.GridQubit(i ,j))

circuit = cirq.Circuit()
circuit.append(rot_x_layer(2, 0.1))
print(circuit)

def rand2d(rows, cols):
    return [[random.choice([+1, -1]) for _ in range(rows)] for _ in range(cols)]

def random_instance(length):
    h = rand2d(length, length)
    jr = rand2d(length, length - 1)
    jc = rand2d(length - 1, length)
    return h, jr, jc

h, jr, jc = random_instance(3)
print('transverse fields: {}'.format(h))
print('row j fields: {}'.format(jr))
print('column j fields: {}'.format(jc))
