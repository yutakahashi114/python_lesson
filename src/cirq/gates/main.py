from cirq.ops import CNOT
from cirq.devices import GridQubit
import cirq

q0, q1 = (GridQubit(0, 0), GridQubit(0, 1))
print(CNOT.on(q0, q1))
print(CNOT(q0, q1))

print(cirq.unitary(cirq.X))
print(cirq.unitary(cirq.X**0.5))
