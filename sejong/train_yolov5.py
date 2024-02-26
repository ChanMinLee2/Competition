import torch
from IPython.display import Image, clear_output # Library for displaying results
from PIL import Image
import os
from tqdm import tqdm

clear_output()
print('Setup complete. Using torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

# After creating the YAML file, start training the model with the command below. Change yolov5s.pt to yolov5l.pt to use a larger and more accurate model
!python /content/drive/MyDrive/yolov5/train.py --img 640 --batch 16 --epochs 10 --data /content/drive/MyDrive/yolov5/data.yaml --weights yolov5s.pt --project /content/drive/MyDrive/yolov5/res --exist-ok

# Define the function for inference and saving labels
def inference_and_save_labels(model, image_folder, output_folder):
    # Set model to evaluation mode
    model.eval()

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over images in the input folder
    for image_name in tqdm(os.listdir(image_folder)):
        image_path = os.path.join(image_folder, image_name)
        output_path = os.path.join(output_folder, os.path.splitext(image_name)[0] + '_labels.txt')

        # Load and preprocess image
        img = Image.open(image_path)
        img_tensor = transforms.ToTensor()(img).unsqueeze(0).to(device)

        # Perform inference
        with torch.no_grad():
            results = model(img_tensor)

        # Parse results and save labels
        labels = []
        for result in results.pred:
            for det in result:
                if det[-1] == 0:  # Class 0 represents human objects
                    labels.append(det[:4].tolist())  # Save bounding box coordinates
        with open(output_path, 'w') as f:
            for label in labels:
                f.write(','.join(map(str, label)) + '\n')

# Define paths
new_image_folder = '/content/drive/MyDrive/sejong/segmentation/new_images'
output_folder = '/content/drive/MyDrive/sejong/new_labels_yolov5'

# Load the trained model
model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='/content/drive/MyDrive/yolov5/res/exp/weights/best.pt')

# Perform inference and save labels
inference_and_save_labels(model, new_image_folder, output_folder)