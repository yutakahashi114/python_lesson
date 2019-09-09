import cirq
import random

class Alice:
    def __init__(self):
        self._origin_bits = []
        self.encode_gates = []
        self._secret_key = ''

    def create_origin_bits(self, bit_count):
        # ランダムなビット列を生成
        self._origin_bits = [random.choice([0, 1]) for _ in range(bit_count)]

    # def set_initial_qubits(self, qubits):
    #     bit_count = len(qubits)
    #     for index in range(bit_count):
    #         if self._origin_bits[index] == 1:
    #             # 初期値を1にするためにxゲートを通す
    #             yield cirq.X(qubits[index])

    def encode(self, qubits):
        bit_count = len(qubits)
        for index in range(bit_count):
            if self._origin_bits[index] == 1:
                # 初期値を1にするためにxゲートを通す
                yield cirq.X(qubits[index])

        self.encode_gates = []
        for index in range(bit_count):
            # 0:X基底、1:H基底
            bit = random.choice([0, 1])
            self.encode_gates.append(bit)
            if bit == 1:
                yield cirq.H(qubits[index])

    def set_secret_key(self, decode_gates):
        self._secret_key = ''
        for index, gate in enumerate(self.encode_gates):
            # エンコードしたゲートとデコードしたゲートが同じであれば、
            # 対応するorigin_bitを秘密鍵のbitに追加
            if gate == decode_gates[index]:
                self._secret_key += str(self._origin_bits[index])
        print('alice_secret_key : ' + self._secret_key )

    def encode_one_bit(self, origin_bit, encode_gate):
        def encode_function(qubit):
            if origin_bit == 1:
                yield cirq.X(qubit)
            if encode_gate == 1:
                yield cirq.H(qubit)
        return encode_function


    def encode(self, circuit, qubits):
        bit_count = len(self._origin_bits)
        for index in range(bit_count):



    def measure_qubits(self, circuit, qubits):
        circuit.append(cirq.measure(*qubits, key='alice'))
        # qubitを測定する
        simulator = cirq.google.XmonSimulator()
        result = simulator.run(circuit)
        return result.measurements['alice'][0]
