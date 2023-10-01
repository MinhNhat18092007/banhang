names = ['z', 'a', '5', '4', 'u', 't', 'o', '2', 'hv', 'c', 'dg', '3', 'n', 's', '7', 'x', 'r', '8', 'v', 'p', 'm', 'y', 'g', 'h', 'l', 'ht', 'hc', 'hinhchop', 'k', 'hinhtru', 'b']

# Chuỗi ký tự mới để thêm vào
new_characters_1 = "dg e b 6 g hinhchop p c 7 4 u n s o y 9 r f 2 h 8 t hv l a q"
new_characters_2 = "6 y 7 q e r u hv 4 v dg 9 l m s 5 t n c p 2 k hinhchop g hinhtru 3 h a o 8 hinhcau d j"

# Tách chuỗi ký tự mới thành danh sách
new_items_1 = new_characters_1.split()
new_items_2 = new_characters_2.split()

# Hợp nhất hai danh sách phần tử mới
all_new_items = new_items_1 + new_items_2

# Thêm phần tử vào danh sách names nếu chưa có
for item in all_new_items:
    if item not in names:
        names.append(item)

print(names)
print(len(names
          ))

