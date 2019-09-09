import cirq

from alice import Alice
from bob import Bob
from eve import Eve
from network import Network

def main():
    # 使用するqubitを用意
    bit_count = int(input('Bit count : '))
    qubits = [cirq.LineQubit(i) for i in range(bit_count)]

    alice = Alice()
    bob = Bob()
    eve = Eve()

    # アリスはランダムなビット列を生成する
    alice.create_origin_bits(bit_count)

    circuit = cirq.Circuit.from_ops(
        # アリスはX基底またはH基底でランダムにエンコードする
        # alice.set_initial_qubits(qubits),
        alice.encode(qubits),
        # # イヴが盗聴した場合
        # eve.decode(qubits),
        # ボブはX基底またはH基底でランダムにデコードする
        bob.decode(qubits)
    )
    print(circuit)
    # ボブは結果を測定する
    bob.measure_qubits(circuit)

    # アリスとボブは互いにどのビットをどの基底でエンコード・デコードしたかを教えあう
    # 基底が一致したビットを抽出し、秘密鍵とする
    alice.set_secret_key(bob.decode_gates)
    bob.set_secret_key(alice.encode_gates)

    # # イヴが盗聴した場合
    # eve.measure_qubits(circuit)
    # eve.set_secret_key(alice.encode_gates)

def main_2():
    alice = Alice()
    bob = Bob()
    network = Network()



if __name__ == '__main__':
    main()
