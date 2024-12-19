import json
import os
from PIL import Image

# Function to resize and pad images to maintain uniform size
def resize_and_pad_image(image_path, output_path, size=(816, 582), padding=10):
    try:
        with Image.open(image_path) as img:
            img.thumbnail((size[0] - padding * 2, size[1] - padding * 2))
            canvas = Image.new('RGB', size, (255, 255, 255))
            x = (size[0] - img.width) // 2
            y = (size[1] - img.height) // 2
            canvas.paste(img, (x, y))
            canvas.save(output_path)
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

# Function to generate an entire portfolio page
def generate_portfolio_pages(json_file):
    # Load project data
    with open(json_file, 'r') as file:
        projects = json.load(file)

    # Ensure output folder exists
    # os.makedirs(output_folder, exist_ok=True)

    # Preprocess: Group projects by category for related products
    category_projects = {}
    for project in projects:
        category_projects.setdefault(project['project_category'], []).append(project)

    # Generate pages for each project
    for project in projects:
        file_name = project['file_name']
        page_path = file_name

        # Handle images and resize
        image_folder = project['image_folder']
        resized_folder = os.path.join(image_folder, "resized")
        os.makedirs(resized_folder, exist_ok=True)

        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        resized_images = []
        for img in images:
            original_path = os.path.join(image_folder, img)
            resized_path = os.path.join(resized_folder, img)
            resize_and_pad_image(original_path, resized_path)
            resized_images.append(resized_path)

        # Prepare main and small images
        main_image = resized_images[0] if resized_images else ""
        small_images = resized_images[:4]  # First 4 images for thumbnails

        # Build Related Products HTML
        related_html = ""
        related_projects = [p for p in category_projects.get(project['project_category'], []) if p != project][:4]
        for rel in related_projects:
            related_html += f"""
            <div class='col-sm-12 col-md-4 col-lg-3'>
                <a href='{rel['file_name']}'>
                    <img style='width: -webkit-fill-available;' src='{rel['image_folder']}/resized/{os.listdir(rel['image_folder']+"/resized")[0]}' alt='{rel['project_name']}'>
                    <h4>{rel['project_name']}</h4>
                </a>
            </div>
            """

        # Build small image thumbnails
        small_images_html = "".join(
            f"""
            <div class='small-img-col'>
                <img src='{img}' width='100%' class='small-img'>
            </div>
            """ for img in small_images)

        # Generate full page HTML
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta content="width=device-width, initial-scale=1.0" name="viewport">
            <title>{project['project_name']} - BITS India</title>
            <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
            <link href="../assets/stylesheets/styles.css" rel="stylesheet">
          </head>

        <head>
            <meta charset="utf-8">
            <meta content="width=device-width, initial-scale=1.0" name="viewport">
        
            <title>{project['project_name']} - BITS India</title>
            <meta content="" name="BITS India - Business & IT Solutions | Innovating Defence & Commercial Technology">
            <meta name="description" content="BITS India - Business & IT Solutions | Innovating Defence & Commercial Technology">
        
            <meta name="keywords" content="Surveillance, CCTV, IOT"/>
        
            <!-- Favicons -->
            <link href="../assets/images/favicon.png" rel="icon">
            <link href="../assets/images/apple-touch-icon.png" rel="apple-touch-icon">
        
            <!-- Google Fonts -->
            <link href="../../../css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;display=swap" rel="stylesheet">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
            <link href="../../../css2-1?family=Oswald:wght@500&amp;display=swap" rel="stylesheet">
            <link href="../../../css2-2?family=Poppins:wght@300;400&amp;display=swap" rel="stylesheet">
            <!-- Vendor CSS Files -->
            <link href="../assets/vendor/aos/aos.css" rel="stylesheet">
            <link href="../assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
            <link href="../assets/stylesheets/font-awesome.min.css" rel="stylesheet">
            <link href="../assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
            <link href="../assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
            <link href="../assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
            <!-- Main CSS File -->
            <link href="../assets/stylesheets/styles.css" rel="stylesheet">
        
        </head>

          <body>
            <header id="header" class="header d-flex align-items-center sticked stikcy-menu">
                <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
                <a href="index.html" class="logo d-flex align-items-center">
                    <img src="../assets/images/Logo-new.png" alt="logo">
                </a>
                <nav id="navbar" class="navbar">
                    <ul>
                    <li><a href="index.html" class="">Home</a></li>
                    <li><a href="services.html" class="">Services</a></li>
                    <li><a href="portfolio.html" class="">Portfolio</a></li>
                    <li><a href="testimonials.html" class="">Testimonials</a></li>
                    <!-- <li><a href="team.html" class="">Team</a></li> -->
                    <li class="dropdown"><a href="#"><span>Menu</span> <i class="bi bi-chevron-down dropdown-indicator"></i></a>
                        <ul>
                        <li><a href="about.html">About</a></li>
                        <li><a href="packages.html">Pricing</a></li>
                        <li><a href="faqs.html">FAQs</a></li>
                        <!-- <li><a href="privacy-policy.html">Terms &amp; Conditions</a></li> -->
                        <li><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="blogs.html">Blogs</a></li>
                        </ul>
                    </li>
                    <li><a href="blogs.html">News</a></li>
                    </ul>
                </nav><!-- .navbar -->
                <a href="contact.html" class="btn-get-started hide-on-mobile">Get Quotes</a>
                <button id="darkmode-button"><i class="bi bi-moon-fill"></i></button>
                <i class="mobile-nav-toggle mobile-nav-show bi bi-list"></i>
                <i class="mobile-nav-toggle mobile-nav-hide d-none bi bi-x"></i>
                </div>
            </header>


              <!--  Breadcrumbs  -->
                <div class="breadcrumbs">
                    <div class="page-header d-flex align-items-center">
                    <div class="container position-relative">
                        <div class="row d-flex justify-content-center">
                        <div class="col-lg-6 text-center">
                            <h2>Our Services</h2>
                            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit</p>
                        </div>
                        </div>
                    </div>
                    </div>
                    <nav>
                    <div class="container">
                        <ol>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../portfolio.html">Our Portfolio</a></li>
                        <li><a href="../portfolio.html">{project['project_category']}</a></li>
                        <li>{project['project_name']}</li>
                        </ol>
                    </div>
                    </nav>
                </div><!-- End Breadcrumbs -->            


         <section style="padding: 0;">
            <!-- Single Products -->
    <div class="small-container single-product section">
        <div class="row">

<div class="col-sm-12 col-md-6 col-lg-6">
                <img src="{main_image}" width="100%" id="ProductImg">

                
                <div class="small-img-row">
                      {small_images_html}
                    </div>
                  </div>

                  <div class="col-sm-12 col-md-6 col-lg-6">
                    <h1>{project['project_name']}</h1>
                    <p>{project['description']}</p>
                    <a href="../contact.html" class="btn">Get a Quote</a>
                    <h3>Project Details <i class="bi bi-text-indent-left"></i></h3>
                    <ul>

        """
        for pointer in project['pointers']:
            html_content += f"<li style='color: black;'>{pointer}</li>\n"

        html_content += """
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Related Products -->
              <div class="small-container">
                <div class="row row-2">
                  <h2>Related Projects</h2>
                </div>
                <div class="row">
            """
        html_content += related_html

        html_content += """
                </div>
              </div>
            </main>

  <footer id="footer" class="footer-section">
    <div class="container">
      <div class="footer-content pt-5 pb-5">
        <div class="row">
          <div class="col-xl-4 col-lg-4 mb-50">
            <div class="footer-widget">
              <div class="footer-logo">
                <a href="../index.html" class="logo d-flex align-items-center">
                  <img src="../assets/images/Logo-new-2.png" alt="logo">
                </a>
              </div>
              <div class="footer-text">
                <p>BITS India specializes in delivering cutting-edge technology solutions across various domains, including application design, web development, surveillance, AI, cybersecurity, IoT, and smart systems. Our mission is to empower businesses with innovative tools and strategies that drive growth, efficiency, and security.
                </p>
              </div>

              <div class="footer-social-icon">
                <!-- <span>Follow us</span> -->
                <a href="https://www.linkedin.com/in/bits-india/" target="_blank" class="linkedin"><i class="bi bi-linkedin"></i></a>
              </div>

            </div>
          </div>
                
                <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                      <div class="service-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Services</h3>
                        </div>
                          <ul class="list">
                              <li><a href="portfolio.html#all" class="filter-active">All</a></li>
                              <li><a href="portfolio.html#application-design">Application Design</a></li>
                              <li><a href="portfolio.html#web-designing">Web Designing</a></li>
                              <li><a href="portfolio.html#surveillance-solutions">Surveillance Solutions</a></li>
                              <li><a href="portfolio.html#ai-solutions">AI Solutions</a></li>
                              <li><a href="portfolio.html#cybersecurity-solutions">Cybersecurity Solutions</a></li>
                              <li><a href="portfolio.html#iot-smart-systems">IoT and Smart Systems</a></li>
                              <li><a href="portfolio.html#ui-ux-designs">UI/UX Designs</a></li>
                          </ul>
                      </div>
                  </div>
                  <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
                      <div class="service-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Information</h3>
                        </div>
                          <ul class="list">
                            <li><a href="about.html">About</a></li>
                            <li><a href="porfolio.html">Portfolio</a></li>
                            <li><a href="faq.html">FAQs</a></li>
                            <li><a href="blogs.html">Blogs</a></li>
                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                          </ul>
                      </div>
                  </div>
                <div class="col-xl-4 col-lg-4 col-md-6 mb-50">
                    <div class="contact-widget footer-widget">
                        <div class="footer-widget-heading">
                            <h3>Contacts</h3>
                        </div>
                          <div class="footer-text">
                              <p><i class="bi bi-geo-alt-fill mr-15"></i> Shop No 10, Unity Splendour, Salunke Vihar Rd, Wanowrie, Pune, Maharashtra 411040</p>
                              <p><i class="bi bi-telephone-inbound-fill mr-15"></i> +1 1234 56 789</p>
                              <p><i class="bi bi-envelope-fill mr-15"></i> contact@bitsindia.in</p>
                          </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-xl-6 col-lg-6 text-left text-lg-left">
                    <div class="copyright-text">
                        <p>BITS India © 2024</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </footer>


  <a href="#" class="scroll-top d-flex align-items-center justify-content-center active">
    <i class="bi bi-arrow-up-short"></i>
  </a>

  <div id="preloader"></div>

  <!-- Vendor JS Files -->
  <script src="../assets/javascripts/jquery.min.js"></script>
  <script src="../assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="../assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="../assets/vendor/aos/aos.js"></script>
  <script src="../assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="../assets/javascripts/plugins.js"></script>
  <script src="../assets/javascripts/purecounter_vanilla.js"></script>
  <script src="../assets/javascripts/validator.min.js"></script>
  <script src="../assets/javascripts/contactform.js"></script>
  <script src="../assets/javascripts/particles.min.js"></script>
  <script src="../assets/javascripts/script.js"></script>

  <!-- Template Main JS File -->
  <script src="../assets/javascripts/main.js"></script>

<!-- product gallery -->
<script>
    var ProductImg = document.getElementById("ProductImg");
    var SmallImg = document.getElementsByClassName("small-img");

    for (let i = 0; i < SmallImg.length; i++) {
    SmallImg[i].onclick = function () {
        ProductImg.src = SmallImg[i].src;
    };
}

    var i = 0;

    function autoSlide() {
        ProductImg.src = SmallImg[i].src;
        i++;
        if (i >= SmallImg.length) {
            i = 0;
        }
    }

    setInterval(autoSlide, 3000);

</script>

</body></html>
        """

        # Write the HTML file
        with open(page_path, 'w') as page_file:
            page_file.write(html_content)
        print(f"Page generated: {page_path}")

# Usage
json_file = 'projects.json'  # Input JSON file
# output_folder = 'portfolio_pages'  # Output folder where HTML files will be saved
generate_portfolio_pages(json_file)