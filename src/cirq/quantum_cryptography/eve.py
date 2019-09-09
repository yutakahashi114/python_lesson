import cirq
import random

class Eve:
    def __init__(self):
        self._result_bits = []
        self.decode_gates = []
        self._secret_key = ''

    def decode(self, qubits):
        bit_count = len(qubits)
        self.decode_gates = []
        for index in range(bit_count):
            # 0:X基底、1:H基底
            bit = random.choice([0, 1])
            self.decode_gates.append(bit)
            if bit == 1:
                yield cirq.H(qubits[index])
        yield cirq.measure(*qubits, key='eve')

    def measure_qubits(self, circuit):
        # qubitを測定する
        simulator = cirq.google.XmonSimulator()
        result = simulator.run(circuit)
        self._result_bits = [int(bit) for bit in result.measurements['eve'][0]]

    def set_secret_key(self, encode_gates):
        self._secret_key = ''
        for index, gate in enumerate(self.decode_gates):
            # エンコードしたゲートとデコードしたゲートが同じであれば、
            # 対応するorigin_bitを秘密鍵のbitに追加
            if gate == encode_gates[index]:
                self._secret_key += str(self._result_bits[index])
        print('eve_secret_key   : ' + self._secret_key )
