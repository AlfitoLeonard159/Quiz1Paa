Nama : Alfito Leonard
NIM : F55123060

Analisis
Untuk Bubble Sort, dalam kondisi terbaik (array sudah terurut), algoritma ini masih melakukan perbandingan antar elemen, namun tidak melakukan pertukaran. Meskipun demikian, Bubble Sort dapat mengoptimalkan dirinya dengan mendeteksi bahwa tidak ada pertukaran yang dilakukan dalam satu putaran, dan dengan demikian dapat berhenti lebih awal. Pada kondisi terbaik ini, waktu eksekusi Bubble Sort menjadi \(O(n)\), karena algoritma hanya perlu memeriksa satu kali seluruh array untuk memastikan bahwa array sudah terurut, tanpa adanya pertukaran elemen.

Sementara itu, Merge Sort tetap membutuhkan waktu yang sama, yaitu \(O(n \log n)\), bahkan dalam kondisi terbaik. Ini karena algoritma Merge Sort selalu membagi array menjadi dua bagian, meskipun array sudah terurut. Setelah membagi, algoritma kemudian menggabungkan kembali dua sub-array yang sudah terurut tersebut. Tidak ada optimasi berdasarkan urutan data yang sudah ada. Oleh karena itu, meskipun array sudah terurut, Merge Sort tetap melakukan pembagian dan penggabungan, yang mengakibatkan kompleksitas waktu yang lebih tinggi dibandingkan dengan Bubble Sort pada best-case.

Kesimpulannya ecara keseluruhan, dalam best-case, Bubble Sort lebih efisien dibandingkan Merge Sort. Hal ini karena Bubble Sort dapat mengidentifikasi kondisi terurut dan mengurangi jumlah perbandingan serta pertukaran, sedangkan Merge Sort tetap melakukan proses pembagian dan penggabungan, meskipun data sudah terurut.
