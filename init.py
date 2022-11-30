import csv

raw_dataset_path = "/root/graphdb/youtube/com-youtube.ungraph.txt"
vertex_path = "/root/graphdb/youtube/youtube-vertex.csv"
edge_path = "/root/graphdb/youtube/youtube-edge.csv"

f = open(raw_dataset_path)
v_csv = open(vertex_path, 'w')
e_csv = open(edge_path, 'w')
v_writer = csv.writer(v_csv)
e_writer = csv.writer(e_csv)

vertex_dataset = set()
lines = f.readlines()
for line in lines:
    if line[0] != '#':
        vertice = line.split()
        vertex_dataset.add(int(vertice[0]))
        vertex_dataset.add(int(vertice[1]))
        e_writer.writerow([int(vertice[0]), int(vertice[1])])


vertex_list = list(vertex_dataset)
vertex_list.sort()
print(len(vertex_list))
print(vertex_list[0:100])

for vertex in vertex_list:
    v_writer.writerow([vertex])

f.close()
v_csv.close()
e_csv.close()