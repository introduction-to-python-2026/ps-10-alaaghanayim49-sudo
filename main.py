from image_utils import load_image, edge_detection

image = load_image("example.jpg")

edges = edge_detection(image)

print(type(edges))      
print(edges.shape) 
