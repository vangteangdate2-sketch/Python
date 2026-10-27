raw1_colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
raw2_colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue','cyan'}

is_red_present = 'cyan' in raw1_colors

union = raw1_colors | raw2_colors
intersection = raw1_colors & raw2_colors
diff = raw1_colors - raw2_colors
symetric_diff = raw1_colors ^ raw2_colors

print(union)
print(intersection)
print(diff)
print(symetric_diff)

