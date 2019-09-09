import cirq

# フーリエ変換
def fourierTransform(qubits):
    bit_count = len(qubits)
    for target in range(bit_count):
        # アダマールゲート
        yield cirq.H(qubits[target])
        for index, control in enumerate(range(target + 1, bit_count)):
            # 制御回転ゲート
            yield cirq.CZ(qubits[target], qubits[control])**(1 / (2 ** (index + 1)))
    # スワップゲート
    yield allSwap(qubits)

# スワップゲート
def allSwap(qubits):
    bit_count = len(qubits)
    for target_1 in range(bit_count // 2):
        target_2 = bit_count - target_1 - 1
        # 1番目とbit_count番目、2番目とbit_count-1番目...のビットを入れ替える
        yield cirq.SWAP(qubits[target_1], qubits[target_2])

# 始状態
def initialState(qubits, number):
    bin_string = format(number, 'b')
    bit_count = len(qubits)
    for index, state in enumerate(reversed(bin_string)):
        if state == '1':
            # 初期値を1にするためにxゲートを通す
            yield cirq.X(qubits[bit_count - index - 1])

def main():
    bit_count = int(input('Bit count : '))
    number = int(input('Number : '))
    # ビット数が足りていなければ終了
    if len(format(number, 'b')) > bit_count:
        print('bit_count is too small')
        return
    # qubit、回路を生成
    qubits = [cirq.GridQubit(i, 0) for i in range(bit_count)]
    circuit = cirq.Circuit()
    # 始状態、フーリエ変換を回路に追加
    circuit.append(initialState(qubits, number))
    circuit.append(fourierTransform(qubits))
    print(circuit)
    # シミュレーション
    result = cirq.Simulator().simulate(circuit)
    for index, state in enumerate(result.final_state):
        print(index, state)

if __name__ == '__main__':
    main()
