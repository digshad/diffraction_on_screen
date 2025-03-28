import numpy as np

# -np.array - слева направо (к доске)
# -np.flip - справа налево (от доски)
# [...]_reverse – несимметричная фигура, перевёрнутая по вертикальной оси

full_x = np.linspace(-100, 100, 41)
cut_x_60 = np.linspace(-60, 60, 25) #ранее называлась cut_x
cut_x_25 = np.linspace(-25, 25, 26) #ранее называлась cut_x_DOP
cut_x_50 = np.linspace(-50, 50, 51)

# Маленький круг - диаметр 30 см
# Для оси х используется full_x
circle_8_2ghz = - np.array(
    [48.4, 49.1, 48.3, 48.4, 48.8, 48.1, 49.1, 48.2, 48.1, 48.6, 49.3, 47.9, 47.6, 48.3, 48.7, 48.8, 50.2, 53.3, 54.2, 53.5, 51.6, 51.2, 52.4, 53.6, 53.2, 50.8, 48.9, 48.8, 49, 48.3, 48.3, 49.2, 49.3, 48.3, 48.4, 49, 48.8, 48.5, 48.7, 48.2, 48.2]
    )
circle_10ghz = - np.array(
    [54.7, 55.3, 55.5, 55.1, 54.5, 54.7, 55.3, 55.7, 55.3, 55.8, 55.7, 55.5, 54.1, 55.0, 55.8, 56, 56.4, 59.5, 62, 59.5, 56.4, 57, 57.7, 61.1, 62.5, 58.7, 56.9, 56, 55.5, 55.2, 55.6, 56.3, 56.3, 55.4, 56.3, 55.7, 55.9, 56.2, 56, 56, 55.4]
    )
circle_11_8ghz = - np.flip(
    [60.6, 61, 60.6, 60.9, 61, 60.8, 60.4, 61.6, 60.4, 61.3, 61, 60.3, 60, 60.8, 61.5, 61.9, 64.5, 70.5, 67, 63.5, 64.2, 69.2, 67.9, 62.1, 60.2, 60.5, 59, 59.1, 60.7, 61.5, 59.9, 61.1, 60.4, 60, 60.5, 60.1, 60.5, 61, 60.7, 60.9, 60.8]
    )

# Большой круг - диаметр 43 см
# Для оси х используется full_x
big_circle_8_2ghz = - np.flip(
    [48.1, 48, 47.9, 48.4, 48.5, 47.8, 48, 47.9, 48.5, 48.3, 47.5, 47, 47.8, 49.4, 50.1, 50.1,51.4,55.5,58.3,55.6,53.2,54.6,60.7,56,51.9,50,50.8,49.5,48,47.1,47.9,48.8,48.8,48,48.2,48,48.7,47.9,48,48.6,47.4]
    )
big_circle_10ghz = - np.array(
    [55.2, 55, 55.4, 55.2, 55.3, 55.4, 55.5, 55.3, 56.4, 54.8, 54.2, 54.3, 55.3, 55.9, 59.1, 59.3, 59.2, 63.2, 62.4, 58.5, 57, 59.5, 64, 61.1, 58.3, 59.1, 57.1, 55.2, 55, 54.4, 55.2, 55.3, 56.2, 54.7, 55.2, 55.1, 55, 55.4, 55, 55, 55.2]
    )
big_circle_11_8ghz = - np.flip(
    [60.5,60.3,60.4,60.4,60.5,60.1,60,60.7,59.7,60.3,60.6,60,59.5,59.6,60.8,60.9,64.2,64.4,67.8,75,65.5,64.3,71.5,69.7,64.7,65.9,61.7,60.5,60.3,58.9,59.8,59.9,61.2,59.9,59.8,61.2,59.9,60.9,59.7,60.5,59.6]
    )

# Самый большой круг - диаметр 55 см
# Для оси х используется full_x; для данных с припиской dop используется cut_x_25
max_circle_8_2ghz = - np.array(
    [48,47.8,48.3,48.4,46.9,48.2,48.8,47.7,46.9,47.7,47.1,48.2,49.8,50.8,52.6,53.6,52.8,58.4,63.5,55.5,56.3,62.1,56.8,52.4,52.2,52.8,50.9,49.6,48.4,47.5,47.5,47.1,47.7,48.8,48.2,47.3,48.2,48.3,48,47.8,47.8]
    )
max_circle_8_2ghz_dop = - np.array(
    [53.3, 53.4, 53.1, 53.2, 55.2, 57.6, 63.4, 68.8, 63.3, 59.7, 57.7, 56.9, 56.3, 57.6, 60.2, 62.6, 63.7, 59.5, 56.3, 54.2, 53.1, 52.5, 52.5, 52.6, 52.7, 52.5]
    )
max_circle_10ghz = - np.flip(
    [56.1,55.6,56.4,55.5,55.8,56,54.8,56.2,56.7,55.6,54.9,55,56.4,56.6,59.1,60,62.9,60.8,60.2,64.8,59.7,59.8,64.9,64.3,60.4,63.2,60.9,58.4,57.3,55.7,54.8,54.6,54.7,55.7,56.2,55.3,55.7,56.4,56,55.9,55.4]
    )
max_circle_10ghz_dop = - np.flip(
    [58.9, 61.3, 61., 60.1, 59.2, 59.5, 60.3, 60.6, 62.6, 64.2, 63.9, 63.2, 61.3, 60.2, 60.3, 62.5, 66.8, 65.2, 64.8, 63.3, 60.4, 59.5, 59.1, 60.4, 61.9, 62.3]
    )    
max_circle_11_8ghz = - np.array(
    [60.3, 60.1, 60.2,59.8,61,60.8,59.9,60.4,61,58.4,58.7,59.4,60.5,60.2,64.7,64.2,71,70.3,73.2,70.2,66.6,70.9,69.1,74.4,68.9,65.6,64.1,61.4,59.9,59.5,59.3,60.9,60.9,59.7,60.2,59.6,60,59.8,60.2,60.1,60.3]
    )
max_circle_11_8ghz_dop = - np.array(
    [63.7, 64.9, 67.3, 69.5, 70.1, 70.9, 67.1, 70.6, 72.7, 73.9, 73.2, 72.3, 68.7, 69.1, 61.7, 72.8, 72.1, 69.8, 67.9, 67.3, 69.8, 69.8, 68, 66.1, 64.2, 64.1]
    )

# Квадрат со стороной 34 см
# Для оси х используется full_x
square_8_2_ghz = - np.flip(
    [47.9, 47.9, 47.9, 48.1, 48.3, 48.2, 48, 48, 48.7, 48.3, 47.4, 47.8, 48.2, 48.3, 48.2, 48.7, 50.2, 54.3, 57.6, 55, 53, 53.5, 57, 54.9, 50.8, 49.6, 49.9, 49.6, 47.8, 46.7, 47.5, 48.4, 47.9, 47.9, 48.3, 47.6, 48.2, 48, 47.9, 48.1, 47.9]
    )
square_10_ghz = - np.array(
    [52.5, 52.7, 52.8, 52.5, 52.6, 53.3, 53, 52.8, 53.4, 53.3, 52.8, 53, 52.9, 52.6, 54.5, 56.4, 56.3, 57.3, 68, 59.9, 57, 56.9, 59.9, 61.8, 57.8, 55.8, 54.6, 54.4, 54.4, 53.9, 53.5, 53.8, 54.2, 54.1, 54, 53.9, 54.1, 54.3, 54.1, 54.3, 54.2]
    )
square_11_8ghz = - np.flip(
    [60.6,60.7,60.7,60.8,60.9,60.6,60.7,60.4,60.8,60.8,60.8,60.4,60.2,60.6,61.5,61.8,61.4,62.7,67.9,74.3,66.4,63.7,67.8,74.1,65.5,64.4,63.6,59.2,59,59.2,59.3,60.8,61.3,60.5,60.2,61.5,60.4,61,60.5,60.5,60.8]
    )    

# Комбинация круга и овала
# 8.2 и 10 GHz: для оси х используется full_x;
# 11.8 GHz: cut_x_60;
# 11.8 GHz DOP: cut_x_25;
# reverse: cut_x_50
nonsymmetrical_8_2_ghz = - np.array(
    [48.1, 48.7, 47.7, 48.1, 48.3, 47.8, 49.4, 48.2, 48.9, 47.6, 47.2, 47, 47.8, 49.7, 50.9, 51.7, 53.6, 52.4, 52.1, 56.3, 59.8, 59.2, 62.4, 66.2, 55.2, 51.2, 51.2, 51, 50.3, 49.6, 47.8, 46.6, 48, 48.1, 48.9, 48.2, 48.1, 48.1, 48.2, 47.8, 48.6]
    )
nonsymmetrical_8_2_ghz_reverse = - np.array(
    [52.5, 53.1, 53.8, 54.5, 54.3, 54.5, 54.8, 55.1, 55.6, 56.4, 57.2, 57.1, 56.9, 56.3, 55.9, 55.7, 55.6, 56.2, 57.1, 58.9, 62.1, 67.3, 67.9, 62.5, 61.2, 60.4, 59.9, 60.1, 59.9, 61.2, 61.1, 60.4, 59.4, 58, 56.7, 56.1, 55.8, 55.7, 55.9, 56.5, 56.7, 56.4, 55.9, 56.2, 56.1, 55.9, 56.3, 55.5, 55.1, 54.3, 53.3]
    )
nonsymmetrical_10_ghz = - np.flip(
    [54.5, 55.7, 55.7, 55.6, 55.4, 54.3, 55.8, 55.9, 55, 54.5, 54.3, 56.4, 56.9, 58.2, 58.1, 59.9, 60.1, 61.1, 65.2, 67.3, 63.9, 61.9, 59.2, 59.5, 60.8, 60.6, 59.1, 58.4, 56., 54.6, 53.1, 54.9, 55.6, 55, 54.8, 54.7, 55.9, 55, 55.2, 55.5, 54.9]
    )
nonsymmetrical_10_ghz_reverse = - np.flip(
    [49.1, 48.2, 48.8, 51, 50.4, 49.7, 51.2, 52.3, 51.7, 51.4, 51.1, 51.9, 52.8, 52.9, 52.9, 52.6, 51.9, 52.1, 52.5, 53.7, 55.3, 57.2, 59.1, 60.4, 62.1, 66.3, 68.3, 70.5, 62.5, 57.8, 54.3, 52.5, 52.2, 51.9, 53.2, 54.4, 54.6, 53.6, 52.4, 51.7, 51.4, 51.2, 51.4, 51.5, 51.1, 50.6, 49.6, 49.0, 48.7, 48.6, 48.5]
    )
nonsymmetrical_11_8ghz = - np.array(
    [62, 60.4, 59.8, 58.8, 61.1, 63.7, 64.9, 66.4, 65.3, 69.8, 65.6, 70.3, 75.6, 74.1, 68.5, 65.8, 66.5, 63.9, 63.8, 62.5, 61.5, 59.8, 60.1, 60, 61.1]
    )
nonsymmetrical_11_8ghz_DOP = - np.flip(
    [64.9, 65.9, 66.1, 67.2, 67.3, 67.4, 67.3, 68.3, 70.2, 71.2, 74.2, 72.7, 72.9, 75.4, 72.5, 70.1, 68.5, 67.2, 65.8, 66.5, 69.1, 68.8, 67.3, 65.9, 65.4, 66.1]
    )
nonsymmetrical_11_8ghz_reverse = - np.array(
    [52.4, 52.3, 52.7, 53.4, 54.3, 55.5, 56.6, 57.9, 58.1, 59.4, 59.8, 59.2, 59.1, 59.4, 61.3, 63.5, 63.4, 60.4, 59.8, 58.9, 59.6, 62.9, 69.6, 73, 65.8, 64.4, 63.9, 64.7, 64.3, 63.9, 61.8, 59.2, 58.1, 58.2, 58.9, 60.5, 61.9, 62.1, 60.9, 60, 61.7, 63.1, 61.8, 62.7, 61.2, 60.6, 59.9, 57.6, 54.1, 53.3, 52.9]
    )

# z – два соединённых вместе прямоугольника со сдвигом друг относительно друга
# Для оси х используется cut_x_50
z_8_2_ghz = - np.array(
    [52.5, 52.8, 52.6, 52.4, 52.8, 53.2, 54, 54.6, 55.3, 55.6, 55.4, 55.7, 55.6, 55.4, 54.9, 54.8, 54.6, 54.7, 54.6, 54.5, 54.4, 54.5, 54.8, 54.3, 54.2, 54.4, 54.9, 55.1, 55.7, 56.3, 57.7, 60, 62.5, 63, 61.5, 58.9, 56.6, 54.7, 53.3, 52.3, 51.3, 51.0, 50.8, 51.1, 51.4, 51.9, 52.4, 53.1, 53.2, 53.2, 53.5]
    )
z_8_2_ghz_reverse = - np.flip(
    [52.1, 51.9, 52.2, 52.9, 53.5, 54.2, 55.1, 55.8, 55.6, 55.2, 54.8, 54.7, 54.6, 54.4, 54.5, 54.5, 54.3, 54.5, 54.8, 54.4, 53.9, 54.0, 53.9, 54.3, 55.4, 56.1, 56.8, 58.7, 60.6, 62.2, 61.8, 60.4, 58.6, 56.8, 54.9, 53.6, 52.5, 51.8, 51.4, 51.3, 51.4, 51.8, 52.1, 52.6, 53.4, 54.0, 54.4, 54.2, 53.6, 53.4, 53.1]
    )
z_10_ghz = - np.array(
    [48.6, 48.5, 48.6, 48.4, 48.7, 48.6, 48.5, 48.5, 48.8, 49.5, 50, 51.1, 51.8, 52.8, 53.6, 53.7, 53.1, 52.5, 52.1, 52, 51.4, 51, 50.6, 50.2, 50.2, 50, 50.3, 50.9, 51.3, 52.6, 54.8, 59.2, 62.2, 65.9, 59.8, 54.4, 51.5, 50, 48.7, 48.3, 48.4, 48.6, 49.2, 49.6, 49.6, 49.5, 49.6, 49.8, 49.6, 49.5, 49.5]
    )
z_10_ghz_reverse = - np.flip(
    [48.9, 48.7, 48.9, 48.8, 48.6, 48.5, 49.1, 49.8, 50.9, 52.5, 53.6, 54.5, 54.8, 54.5, 54.2, 53, 51.8, 51.2, 50.8, 50.4, 50.1, 49.6, 49.7, 50, 50.5, 51, 51.8, 53.4, 54.8, 58.2, 61.4, 60.2, 56, 52.6, 50.6, 49.2, 48.1, 47.7, 47.8, 48, 48.5, 49.2, 49.5, 49.7, 49.8, 49.9, 50.1, 50.4, 50.3, 50, 49.5]
    )
z_11_8_ghz = - np.array(
    [55.9, 54.9, 53.7, 52.8, 52.7, 53.3, 53.9, 53.9, 54.2, 54.6, 54.9, 55.2, 55.9, 55.9, 54.9, 54.6, 54.2, 54.4, 55.8, 57.8, 61.5, 66.4, 74.0, 67.1, 61.9, 59.9, 56.6, 56.2, 55.2, 54.6, 55.1, 55.8, 55.9, 56.3, 56.5, 57.8, 60.2, 60.8, 61.5, 64.2, 63.9, 61.1, 57.6, 56.7, 56.1, 56.2, 56.4, 55.4, 54.6, 54.8, 53.8]
    )
z_11_8_ghz_reverse = - np.flip(
    [54.7, 54.8, 54.9, 55.7, 56.4, 56.4, 55.9, 55.6, 55.8, 56.2, 56.6, 56.1, 54.8, 54.4, 55.1, 56.8, 59.8, 62.8, 70.5, 73, 65.5, 61.2, 59.2, 58.3, 57.3, 56.2, 55.9, 55.2, 54.9, 55.2, 56.2, 57.4, 58.6, 59.8, 61.2, 62.8, 63.6, 60.9, 57.7, 56.1, 54.8, 54.3, 54.2, 54.1, 54.3, 53.9, 53.2, 53.1, 53.3, 54, 54.8]
    )

# ge – комбинация из прямоугольника и трапеции
# Для оси х используется cut_x_50
ge_8_2_ghz = - np.array(
    [53.7, 53.8, 53.9, 53.6, 53.2, 53, 53.2, 53.1, 53, 52.7, 52.6, 52.2, 52.3, 52.5, 53.4, 54.5, 55.5, 56.1, 56.8, 57.1, 57.2, 57.8, 58.2, 59, 58.9, 58.4, 57.7, 56.8, 56, 55.3, 55, 54.5, 54.7, 54.6, 54.8, 54.6, 54.9, 54.7, 54.5, 54.4, 53.9, 53.6, 53.3, 53.1, 53.2, 53.7, 54.7, 55.3, 56.2, 56.7, 56.1]
    )
ge_8_2_ghz_reverse = - np.flip(
    [53.7, 53.4, 52.9, 52.6, 52.3, 51.9, 51.8, 51.8, 52.1, 52.3, 52.7, 53.4, 54.4, 55.3, 56.6, 57.4, 57.8, 57.8, 58.1, 57.9, 57.7, 58.2, 58.5, 57.2, 56.4, 56.3, 55.2, 54.6, 54.4, 54.1, 54.3, 54.5, 54.4, 54.7, 54.7, 54.4, 54.1, 53.8, 53.3, 53.2, 53.2, 53.3, 54.2, 55.1, 55.9, 56.2, 56.4, 56.1, 54.9, 54, 53.8]
    )    
ge_10_ghz = - np.array(
    [50.6, 50.2, 49.7, 49.3, 49.5, 49.3, 49.1, 49, 48.6, 48, 48, 47.8, 47.9, 48.5, 48.8, 49.4, 50.4, 51.6, 52.6, 54.2, 54.8, 54.7, 54.2, 53.2, 53.1, 53.6, 54.3, 53.8, 52.8, 52.1, 51.3, 50.7, 50.7, 50.8, 50.8, 51.1, 51.4, 51.4, 51.1, 50.9, 50.4, 50.7, 50.9, 51.6, 52.6, 53.4, 53.6, 52.9, 52.2, 51.5, 51.3]
    )
ge_10_ghz_reverse = - np.flip(
    [50, 50.2, 49.8, 49.9, 49.7, 48.7, 48.2, 48.4, 48.8, 48.8, 49.1, 49.6, 49.8, 50.9, 52.4, 53.9, 55.9, 57.3, 57.1, 55.6, 54.7, 54.3, 54.7, 54.9, 54.1, 53.6, 52.4, 52, 51.5, 50.8, 50.6, 50.7, 50.8, 51.1, 51.1, 51.3, 50.9, 50.4, 50.1, 50.3, 50.8, 51, 52.7, 53.6, 53.4, 52.4, 51.8, 51.4, 51.5, 51.2, 51.3]
    )
ge_11_8_ghz_reverse = - np.array(
    [55.2, 55.5, 55.4, 54.7, 54.6, 54.9, 55.9, 56.5, 56.8, 56.3, 55.8, 54.4, 53.5, 53.3, 53.3, 53.7, 54.1, 54.9, 55.1, 55, 55.3, 55.5, 56.7, 58.2, 57.6, 57.3, 57.1, 55.7, 55.8, 55.5, 56.2, 56.9, 57.7, 56.8, 55.7, 54.3, 54, 53.4, 53.5, 52.2, 51.7, 51.6, 52, 52.2, 52.4, 52.2, 52.1, 52.2, 52.6, 52.8, 53.1]
    )
ge_11_8_ghz = - np.flip(
    [54.6, 54.5, 54.3, 54.6, 55.4, 55.8, 55.4, 54.3, 53.6, 53.7, 53.4, 53.6, 54.3, 55.6, 56.1, 56.1, 55.6, 55.5, 55.5, 56.2, 56.1, 56.6, 56.9, 57.1, 56.9, 56.2, 57.5, 57.4, 57.9, 57.4, 56.6, 55.4, 54.6, 54.2, 53.5, 53.4, 52.8, 52.2, 52.0, 52.3, 52.5, 53, 53.1, 53.1, 53.2, 53.9, 54.7, 54.8, 54.4, 55.2, 54.9]
    )
