import cirq

class Network:
    def test(self, encode_function):
        qubits = [cirq.LineQubit(i) for i in range(3)]
        circuit = cirq.Circuit.from_ops(
            encode_function(qubits[0]),
            cirq.H(qubits[1]),
            cirq.CNOT(qubits[2], qubits[1]),
            cirq.CNOT(qubits[1], qubits[0]),
            cirq.H(qubits[0])
        )
        return circuit, qubits
