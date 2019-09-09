import cirq
import random
import numpy as np
from cirq.ops import CZ, H
from cirq.circuits import InsertStrategy

qubits = [cirq.GridQubit(x, y) for x in range(3) for y in range(3)]

print(qubits[0])

x_gate = cirq.X

x_op = x_gate(qubits[0])

print(x_op)

cz = cirq.CZ(qubits[0], qubits[1])
x = cirq.X(qubits[2])
moment = cirq.Moment([x, cz])

print(moment)

cz01 = cirq.CZ(qubits[0], qubits[1])
x2 = cirq.X(qubits[2])
cz12 = cirq.CZ(qubits[1], qubits[2])
moment0 = cirq.Moment([cz01, x2])
moment1 = cirq.Moment([cz12])
circuit = cirq.Circuit((moment0, moment1))

print('a')
print(circuit)

q0, q1, q2 = [cirq.GridQubit(i, 0) for i in range(3)]
circuit = cirq.Circuit()
circuit.append([CZ(q0, q1), H(q2)])
print(circuit)

circuit.append([H(q0), CZ(q1, q2)])
print(circuit)

circuit = cirq.Circuit()
circuit.append([CZ(q0, q1), H(q2), H(q0), CZ(q1, q2)])
print(circuit)

circuit = cirq.Circuit()
circuit.append([CZ(q0, q1), H(q0), CZ(q1, q2), H(q2)], strategy=InsertStrategy.EARLIEST)
print(circuit)

circuit = cirq.Circuit()
circuit.append([CZ(q0, q1)])
circuit.append([H(q0), H(q2)], strategy=InsertStrategy.EARLIEST)
print(circuit)

circuit = cirq.Circuit()
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.NEW)
print(circuit)

circuit = cirq.Circuit()
circuit.append([CZ(q1, q2)])
circuit.append([CZ(q1, q2)])
circuit.append([H(q0), H(q1), H(q2)], strategy=InsertStrategy.INLINE)
print(circuit)

circuit = cirq.Circuit()
circuit.append([H(q0)])
circuit.append([CZ(q1, q2), H(q0)], strategy=InsertStrategy.NEW_THEN_INLINE)
print(circuit)

def my_layer():
    yield CZ(q0, q1)
    yield [H(q) for q in (q0, q1, q2)]
    yield [CZ(q1, q2)]
    yield [H(q0), [CZ(q1, q2)]]
circuit = cirq.Circuit()
circuit.append(my_layer())

for x in my_layer():
    print(x)

print(circuit)

circuit = cirq.Circuit.from_ops(H(q0), H(q1))
print(circuit)

circuit = cirq.Circuit.from_ops(H(q0), CZ(q0, q1))
for moment in circuit:
    print(moment)

circuit = cirq.Circuit.from_ops(H(q0), CZ(q0, q1), H(q1), CZ(q0, q1))
print(circuit)
print(circuit[1:3])
print(circuit[:-1])
print(circuit[::-1])
