import json
import os
from PIL import Image

def resize_and_pad_image(image_path, output_path, size=(300, 250), padding=10):
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

def generate_html(json_file, output_file):
    # Delete the output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Load the project data from the JSON file
    with open(json_file, 'r') as file:
        projects = json.load(file)

    # Start building the HTML content
    html_content = '''<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>Technoit - IT Solutions & Business Services Multipurpose Responsive Website Template</title>
  <meta content="" name="Technoit - IT Solutions & Business Services Multipurpose Responsive Website Template">
  <meta name="description" content="Technoit - IT Solutions & Business Services Multipurpose Responsive Website Template">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">

  <!-- Favicons -->
  <link href="assets/images/favicon.png" rel="icon">
  <link href="assets/images/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="../../../css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,600;1,700&amp;family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&amp;display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
  <link href="../../../css2-1?family=Oswald:wght@500&amp;display=swap" rel="stylesheet">
  <link href="../../../css2-2?family=Poppins:wght@300;400&amp;display=swap" rel="stylesheet">
  <!-- Vendor CSS Files -->
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/stylesheets/font-awesome.min.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <!-- Main CSS File -->
  <link href="assets/stylesheets/styles.css" rel="stylesheet">


</head>

<body>

<style>
  .portfolio-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
    gap: 20px; /* Spacing between items */
    padding: 20px;
  }

  .portfolio-item {
    position: relative;
    overflow: hidden;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    background: #fff;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .portfolio-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }

  .portfolio-wrap {
    position: relative;
    text-align: center;
  }

  .portfolio-wrap img {
    max-width: 100%;
    height: auto;
    border-bottom: 1px solid #ddd;
  }

  .portfolio-info {
    padding: 10px;
  }

  .portfolio-info h3 {
    font-size: 1rem;
    color: #333;
    margin: 0;
  }

  .portfolio-info p {
    font-size: 0.8rem;
    color: #666;
    margin: 5px 0 0;
  }

  @media screen and (max-width: 768px) {
    .portfolio-container {
      grid-template-columns: 1fr; /* Single column on mobile */
    }
  }

    /* Default styling for filter links */
.portfolio-flters a {
  color: white; /* Make text white */
  text-decoration: none; /* Remove underline */
  padding: 5px 10px; /* Add some padding for better aesthetics */
  border-radius: 5px; /* Optional rounded corners */
}

/* Highlight the active filter link */
.portfolio-flters a.filter-active {
  /* background-color: #007bff; Highlight background */
  color: white; /* Ensure active link text remains white */
}

/* Hover effect for better UX */
.portfolio-flters a:hover {
  /* background-color: #555; Slightly darker background on hover */
  color: white; /* Keep text white on hover */
}

</style>



    <header id="header" class="header d-flex align-items-center sticked stikcy-menu">
        <div class="container-fluid container-xl d-flex align-items-center justify-content-between">
          <a href="index.html" class="logo d-flex align-items-center">
            <img src="assets/images/Logo-new.png" alt="logo">
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
                  <!-- <li><a href="blog-details.html">Blog Detail Page</a></li> -->
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

        <div class="breadcrumbs">
    <div class="page-header d-flex align-items-center">
      <div class="container position-relative">
        <div class="row d-flex justify-content-center">
          <div class="col-lg-6 text-center">
            <h2>Our Portfolio</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipiscing elit</p>
          </div>
        </div>
      </div>
    </div>
    <nav>
      <div class="container">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li>Our Porfolio</li>
        </ol>
      </div>
    </nav>
  </div><!-- End Breadcrumbs -->

  <main id="main">

    <div class="single-page">
      <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio">
      <div class="container" data-aos="fade-up">
        <div class="portfolio-isotope" data-portfolio-filter="*" data-portfolio-layout="masonry" data-portfolio-sort="original-order" data-aos="fade-up" data-aos-delay="100">
          <div>
            <ul class="portfolio-flters">
              <li><a href="portfolio.html?filter=all" class="filter-active">All</a></li>
              <li><a href="portfolio.html?filter=application-design">Application Design</a></li>
              <li><a href="portfolio.html?filter=web-designing">Web Designing</a></li>
              <li><a href="portfolio.html?filter=surveillance-solutions">Surveillance Solutions</a></li>
              <li><a href="portfolio.html?filter=ai-solutions">AI Solutions</a></li>
              <li><a href="portfolio.html?filter=cybersecurity-solutions">Cybersecurity Solutions</a></li>
              <li><a href="portfolio.html?filter=iot-and-smart-systems">IoT and Smart Systems</a></li>
              <li><a href="portfolio.html?filter=ui-ux-designs">UI/UX Designs</a></li>
            </ul>
            
          </div>

          <div class="portfolio-container">

          
'''

    for project in projects:
        category_class = project['project_category'].lower().replace(' ', '-')

        image_folder = os.path.join("portfolio", project['image_folder'])
        resized_folder = os.path.join(image_folder, "resized")
        os.makedirs(resized_folder, exist_ok=True)

        images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
        resized_images = []
        for img in images:
            original_path = os.path.join(image_folder, img)
            resized_path = os.path.join(resized_folder, img)
            resize_and_pad_image(original_path, resized_path)
            resized_images.append(resized_path)

        main_image = resized_images[0] if resized_images else ""

        html_content += f'''
        <div class="portfolio-item {category_class}">
        <div class="portfolio-wrap">
            <a href="{main_image}" data-gallery="portfolio-gallery-{category_class}" class="glightbox">
            <img src="{main_image}" class="img-fluid" alt="{project['project_category']}">
            </a>
            <div class="portfolio-info">
            <h3>{project['project_name']}</h3>
            <p>{project['project_category']}</p>
            </div>
        </div>
        </div>
        '''



    # Close the HTML structure
    html_content += '''
          </div>
          
        </div>

      </div>
    </section>
    </div>

  </main>

    <footer id="footer" class="footer-section">
    <div class="container">
      <div class="footer-content pt-5 pb-5">
        <div class="row">
          <div class="col-xl-4 col-lg-4 mb-50">
            <div class="footer-widget">
              <div class="footer-logo">
                <a href="index.html" class="logo d-flex align-items-center">
                  <img src="assets/images/Logo-new-2.png" alt="logo">
                </a>
              </div>
              <div class="footer-text">
                <p>Lorem ipsum dolor sit amet, consec tetur adipisicing elit, sed do eiusmod tempor incididuntut consec
                  tetur adipisicing
                  elit,Lorem ipsum dolor sit amet.</p>
              </div>
              <div class="footer-social-icon">
                <span>Follow us</span>
                <a href="#" class="twitter"><i class="bi bi-twitter"></i></a>
                <a href="#" class="facebook"><i class="bi bi-facebook"></i></a>
                <a href="#" class="instagram"><i class="bi bi-instagram"></i></a>
                <a href="#" class="linkedin"><i class="bi bi-linkedin"></i></a>
              </div>
            </div>
          </div>

          <div class="col-lg-2 col-md-6 col-sm-12 footer-column">
            <div class="service-widget footer-widget">
              <div class="footer-widget-heading">
                <h3>Services</h3>
              </div>
              <ul class="list">
                <li><a href="services.html">Web Design</a></li>
                <li><a href="services.html">App Developemnt</a></li>
                <li><a href="services.html">Cloud Services</a></li>
                <li><a href="services.html">Domain adn Hosting</a></li>
                <li><a href="services.html">Seo Optimization</a></li>
                <li><a href="services.html">Social Media</a></li>
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
                <!-- <li><a href="packages.html">Pricing</a></li> -->
                <!-- <li><a href="team.html">Team</a></li> -->
                <li><a href="porfolio.html">Portfolio</a></li>
                <li><a href="faq.html">FAQs</a></li>
                <!-- <li><a href="team.html">Team</a></li> -->
                <li><a href="blogs.html">Blogs</a></li>
                <!-- <li><a href="blogs-details.html">Blog Details</a></li> -->
                <!-- <li><a href="coming-soon.html">Coming Soon</a></li> -->
                <li><a href="privacy-policy.html">Terms & Conditions</a></li>
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
                <p><i class="bi bi-geo-alt-fill mr-15"></i> 101 West Town , PBO 12345, United States</p>
                <p><i class="bi bi-telephone-inbound-fill mr-15"></i> +1 1234 56 789</p>
                <p><i class="bi bi-envelope-fill mr-15"></i> contact@example.com</p>
              </div>
            </div>
            <div class="footer-widget">
              <div class="footer-widget-heading">
                <h3>Newsletter</h3>
              </div>
              <div class="footer-text mb-25">
                <p>Don't miss to subscribe to our new feeds, kindly fill the form below.</p>
              </div>
              <div class="subscribe-form">
                <form action="#">
                  <input type="text" placeholder="Email Address">
                  <button><i class="bi bi-telegram"></i></button>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-xl-6 col-lg-6 text-left text-lg-left">
            <div class="copyright-text">
              <p>Technoit © 2023 - Designed by <a href="https://www.templatemonster.com/authors/zrthemes/">Zr Themes</a>
              </p>
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
  <script src="assets/javascripts/jquery.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/javascripts/plugins.js"></script>
  <script src="assets/javascripts/purecounter_vanilla.js"></script>
  <script src="assets/javascripts/validator.min.js"></script>
  <script src="assets/javascripts/contactform.js"></script>
  <script src="assets/javascripts/particles.min.js"></script>
  <script src="assets/javascripts/script.js"></script>

  <!-- Template Main JS File -->
  <script src="assets/javascripts/main.js">
  </script>

  <script>
        document.addEventListener('DOMContentLoaded', () => {
      // Get the URL parameter for the filter
      const urlParams = new URLSearchParams(window.location.search);
      const filter = urlParams.get('filter') || 'all'; // Default to 'all'

      // Highlight the active filter
      const filterLinks = document.querySelectorAll('.portfolio-flters a');
      filterLinks.forEach(link => {
        if (link.href.includes(`filter=${filter}`)) {
          link.classList.add('filter-active');
        } else {
          link.classList.remove('filter-active');
        }
      });

      // Show/Hide Portfolio Items
      const portfolioItems = document.querySelectorAll('.portfolio-item');
      portfolioItems.forEach(item => {
        // Show all items if filter is 'all', otherwise show matching items only
        if (filter === 'all' || item.classList.contains(filter)) {
          item.style.display = 'block'; // Show matching items
        } else {
          item.style.display = 'none'; // Hide non-matching items
        }
      });
    });
  </script>



</body></html>
'''

    # Write the HTML content to the output file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Usage
json_file = 'portfolio/projects.json'  # Replace with your JSON file
output_file = 'portfolio.html'
generate_html(json_file, output_file)