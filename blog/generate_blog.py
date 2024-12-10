import json
import os
from PIL import Image, ImageOps

def resize_and_pad_image(image_path, output_path, size=(816, 582), padding=0):
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

def generate_blog_html(json_file, output_file):
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Load the blog data from the JSON file
    with open(json_file, 'r') as file:
        blogs = json.load(file)

    html_blocks = []

    for blog in blogs:
        # Resize blog image
        blog_image = blog['blog_image']
        resized_folder = "resized_images"
        os.makedirs(resized_folder, exist_ok=True)
        resized_image_path = os.path.join(resized_folder, os.path.basename(blog_image))
        resize_and_pad_image(blog_image, resized_image_path)

        # Generate HTML for the blog
        blog_html = f"""
        <div class=\"breadcrumbs\">
          <div class=\"page-header d-flex align-items-center\">
            <div class=\"container position-relative\">
              <div class=\"row d-flex justify-content-center\">
                <div class=\"col-lg-6 text-center\">
                  <h2>{blog['blog_title']}</h2>
                  <p>{blog['blog_intro']}</p>
                </div>
              </div>
            </div>
          </div>
          <nav>
            <div class=\"container\">
              <ol>
                <li><a href=\"index.html\">Home</a></li>
                <li>{blog['blog_title']}</li>
              </ol>
            </div>
          </nav>
        </div>
        
        <main id=\"main\">
          <section class=\"single-page\">
            <div class=\"container\" data-aos=\"fade-up\">
              <div class=\"row\">
                <div class=\"col-lg-12\">
                  <h2 class=\"title\">{blog['blog_title']}</h2>
                  <div class=\"d-flex align-items-center details-post-data\">
                    <div class=\"post-meta d-flex\">
                      <p class=\"post-author\">By {blog['author_name']}</p>
                      <p class=\"post-sperator\"> - </p>
                      <p class=\"post-date\">
                        <time datetime=\"{blog['date']}\">{blog['date']}</time>
                      </p>
                    </div>
                  </div>
                  <div class=\"col-lg-12\">
                    <img src=\"{resized_image_path}\" class=\"img-fluid rounded-4 mb-4\" alt=\"{blog['blog_title']}\">
                  </div>
                  <p>{blog['blog_intro']}</p>
        
        """
        for i, pointer in enumerate(blog['blog_pointers'], start=1):
            blog_html += f"""
                  <h3>{i}. {pointer['title']}</h3>
                  <p>{pointer['content']}</p>
            """

        blog_html += """
                </div>
              </div>
            </div>
          </section>
        </main>
        """

        html_blocks.append(blog_html)

    # Write the combined HTML to the output file
    with open(output_file, 'w') as file:
        file.write("\n".join(html_blocks))

json_file = 'blogs.json' 

with open(json_file, 'r') as file:
    blog_data = json.load(file)

# Generate the blog HTML
output_file = 'blogs.html'
generate_blog_html(json_file, output_file)