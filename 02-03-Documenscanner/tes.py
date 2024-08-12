import cv2
import numpy as np
import argparse

# Konstruktor argumen untuk parsing argumen
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-l", "--lower", required=True, help="lower boundary of the color in HSV space")
ap.add_argument("-u", "--upper", required=True, help="upper boundary of the color in HSV space")
args = vars(ap.parse_args())

# Fungsi untuk mengubah string dari argumen ke numpy array
def str_to_np_array(str):
    return np.array([int(x) for x in str.split(',')])

# Memuat gambar dan mengubahnya ke ruang warna HSV
image = cv2.imread(args["image"])
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Mendefinisikan batas bawah dan atas untuk warna yang akan dideteksi
lower_bound = str_to_np_array(args["lower"])
upper_bound = str_to_np_array(args["upper"])

# Membuat mask dengan warna yang spesifik
mask = cv2.inRange(hsv, lower_bound, upper_bound)

# Menemukan kontur di dalam mask
cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Menyalin gambar asli untuk ditampilkan hasil deteksinya
output = image.copy()

# Menggambar semua kontur yang terdeteksi
object_count = 0
for c in cnts:
    # Menghitung area dari kontur
    area = cv2.contourArea(c)
    if area > 500:  # Menyaring kontur berdasarkan area
        cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
        object_count += 1

# Menampilkan jumlah objek yang terdeteksi pada gambar
cv2.putText(output, f"Objects detected: {object_count}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Menampilkan gambar asli dan hasil deteksinya
cv2.imshow("Original Image", image)
cv2.imshow("Detected Objects", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
