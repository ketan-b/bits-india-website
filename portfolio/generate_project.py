import json
import os
from PIL import Image, ImageOps

def resize_and_pad_image(image_path, output_path, size=(816, 582), padding=10):
    """
    Resizes the image to fit within the given size, preserving aspect ratio.
    Pads with white background if needed to maintain the target size.
    """
    try:
        with Image.open(image_path) as img:
            # Resize image maintaining aspect ratio
            img.thumbnail((size[0] - padding * 2, size[1] - padding * 2))

            # Create a white canvas
            canvas = Image.new('RGB', size, (255, 255, 255))

            # Calculate position to paste the resized image onto the canvas
            x = (size[0] - img.width) // 2
            y = (size[1] - img.height) // 2

            canvas.paste(img, (x, y))

            # Save the resized and padded image
            canvas.save(output_path)
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def generate_html(json_file, output_file):
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Load the project data from the JSON file
    with open(json_file, 'r') as file:
        projects = json.load(file)

    html_blocks = []

    for project in projects:
        # Get the folder path and list all image files
        image_folder = project['image_folder']
        resized_folder = os.path.join(image_folder, "resized")
        os.makedirs(resized_folder, exist_ok=True)

        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        resized_images = []

        # Resize and pad images
        for img in images:
            original_path = os.path.join(image_folder, img)
            resized_path = os.path.join(resized_folder, img)
            resize_and_pad_image(original_path, resized_path)
            resized_images.append(resized_path)

        # Generate HTML for images
        if resized_images:
            main_image = resized_images[0]
            small_images = resized_images[0:5]  # Display up to 4 small images

            image_html = f"""
            <div class=\"col-sm-12 col-md-6 col-lg-6\">
                <img src=\"{main_image}\" width=\"100%\" id=\"ProductImg\">

                <div class=\"small-img-row\">
            """
            for img in small_images:
                image_html += f"""
                    <div class=\"small-img-col\">
                        <img src=\"{img}\" width=\"100%\" class=\"small-img\">
                    </div>
                """
            image_html += """
                </div>
            </div>
            """
        else:
            image_html = "<div>No images found for this project.</div>"

        # Generate HTML for project details
        project_html = f"""
        <div class=\"col-sm-12 col-md-6 col-lg-6\">
            <h1>{project['project_name']}</h1>
            <p>{project['description']}</p>
            <a href=\"\" class=\"btn\">Get a Quote</a>
            <h3>Project Details <i class=\"bi bi-text-indent-left\"></i></h3>
            <p>{project['details']}
                <ul>
        """
        for pointer in project['pointers']:
            project_html += f"<li>{pointer}</li>\n"
        
        project_html += """
                </ul>
            </p>
        </div>
        """

        # Combine the two HTML parts
        html_blocks.append(image_html + project_html)

    # Write the combined HTML to the output file
    with open(output_file, 'w') as file:
        file.write("\n".join(html_blocks))

# Usage
json_file = 'projects.json'  # Replace with your JSON file
output_file = 'output.html'
generate_html(json_file, output_file)