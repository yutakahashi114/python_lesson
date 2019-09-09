import cirq
import numpy as np

bit_count = 3
qubits = [cirq.GridQubit(i, 0) for i in range(bit_count)]

circuit = cirq.Circuit()
ccx = cirq.CCX(qubits[0], qubits[1], qubits[2])
# circuit.append(ccx)
# print((cirq.CCZ(qubits[0], qubits[1], qubits[2]))._decompose_())
# print(cirq.T.on(cirq.GridQubit(1, 0))._decompose_())
# print((cirq.CCZ(qubits[0], qubits[1], qubits[2])**(0.5))._decompose_())
# print(circuit)



# class QftInverse(cirq.MultiQubitGate):
#     def __init__(self, num_qubits):
#         super().__init__(num_qubits)

#     def _decompose_(self, qubits):
def test(qubits):
    exp = 0.5
    p = cirq.T**exp

    c1, c2, c3, t = qubits
    # yield cirq.H(t)
    yield p(c1)
    yield p(c2)
    # yield cirq.CZ(c1, c2)**exp
    yield p(c3)
    yield p(t)
    yield cirq.CCX(c1, c2, c3)
    yield cirq.CNOT(c3, t)
    yield (p**(-1))(c3)
    yield p(t)
    yield cirq.CCX(c1, c2, c3)
    yield cirq.CNOT(c3, t)
    yield cirq.CCX(c1, c2, c3)
    yield (p**(-1))(t)
    yield cirq.CNOT(c3, t)
    yield cirq.CCX(c1, c2, c3)
    yield (p**(-1))(t)
    yield cirq.CNOT(c3, t)
    # yield cirq.H(t)


bit_count = 4
qubits = [cirq.GridQubit(i, 0) for i in range(bit_count)]

c1, c2, c3, t = qubits

circuit = cirq.Circuit()
circuit.append(cirq.X(c1))
circuit.append(cirq.X(c2))
circuit.append(cirq.X(c3))
circuit.append(cirq.CCZ(c1, c2, c3))
result = cirq.Simulator().simulate(circuit)
for index, state in enumerate(result.final_state):
    print(index, state, abs(state))
print('----------------')
# circuit.append(cirq.measure(*qubits, key='m'))

circuit = cirq.Circuit()

circuit.append(cirq.X(c1))
circuit.append(cirq.X(c2))
circuit.append(cirq.X(c3))
circuit.append(cirq.X(t))

result = cirq.Simulator().simulate(circuit)
# for index, state in enumerate(result.final_state):
#     print(index, state)

circuit.append(test(qubits))
print(circuit)
result = cirq.Simulator().simulate(circuit)
# print(np.around(result.final_state, 3))
for index, state in enumerate(result.final_state):
    print(index, state, abs(state))
