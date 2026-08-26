#!/usr/bin/env python3
"""Build Roushan-Blog-Theme.xml (v2.0) from 'Sian Free Version 1.0.xml'.

Every replacement is exact-match with assertions, so a mismatch aborts
instead of producing a broken template.
"""
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Sian Free Version 1.0.xml")
DST = os.path.join(ROOT, "Roushan-Blog-Theme.xml")

with io.open(SRC, "r", encoding="utf-8") as f:
    t = f.read()

t = t.replace("\r\n", "\n")

errors = []

def sub_once(old, new, label):
    global t
    c = t.count(old)
    if c != 1:
        errors.append(f"[{label}] expected 1 occurrence, found {c}")
        return
    t = t.replace(old, new)
    print(f"ok  {label}")

def sub_first(old, new, label):
    global t
    if old not in t:
        errors.append(f"[{label}] not found")
        return
    t = t.replace(old, new, 1)
    print(f"ok  {label}")

def sub_all(old, new, label, expect=None):
    global t
    c = t.count(old)
    if expect is not None and c != expect:
        errors.append(f"[{label}] expected {expect}, found {c}")
        return
    if c == 0:
        errors.append(f"[{label}] not found")
        return
    t = t.replace(old, new)
    print(f"ok  {label} (x{c})")

def sub_block(start, end, new, label, keep_end=False):
    global t
    if t.count(start) != 1:
        errors.append(f"[{label}] start marker found {t.count(start)}x")
        return
    i = t.index(start)
    j = t.index(end, i + len(start))
    tail = j + len(end) if keep_end else j
    t = t[:i] + new + t[tail:]
    print(f"ok  {label}")

# ---------------------------------------------------------------- 1. versions
sub_once("b:templateVersion='1.0.0'", "b:templateVersion='2.0.0'", "templateVersion")
sub_once("<b:skin version='1.0.0'>", "<b:skin version='2.0.0'>", "skin version")
sub_once(
"""Name:        Sian
License:     Free Version
Version:     1.0
Author:      Sora Templates
Author Url:  https://www.soratemplates.com/""",
"""Name:        Roushan Pro (Sian based)
License:     Personal Use
Version:     2.0
Author:      Roushan Gupta & Roushan Kumar
Author Url:  https://your-blog.blogspot.com/""",
"skin comment")

# ---------------------------------------------------------------- 2. new head
OLD_HEAD = """    <meta content='width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1' name='viewport'/>
    <title><data:view.title.escaped/></title>
    <b:include data='blog' name='all-head-content'/>
  <b:if cond='data:view.isHomepage'>
 <script type='application/ld+json'>{&quot;@context&quot;:&quot;http://schema.org&quot;,&quot;@type&quot;:&quot;WebSite&quot;,&quot;name&quot;:&quot;<data:view.title.escaped/>&quot;,&quot;url&quot;:&quot;<data:view.url.canonical/>&quot;,&quot;potentialAction&quot;:{&quot;@type&quot;:&quot;SearchAction&quot;,&quot;target&quot;:&quot;<data:view.url.canonical/>search?q={search_term_string}&quot;,&quot;query-input&quot;:&quot;required name=search_term_string&quot;}}</script>
    </b:if>
    <!-- Google Fonts -->
    <link href='//fonts.googleapis.com/css?family=Nunito:400,500,600,700,800.900|Poppins:400,400i,500,500i,700,700i|Indie+Flower' media='all' rel='stylesheet' type='text/css'/>
    <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css' rel='stylesheet'/>
    <link href='https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css' rel='stylesheet'/>"""

NEW_HEAD = """    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <meta content='#30bd9b' name='theme-color'/>
    <!-- ===== Roushan SEO: Title Tag ===== -->
    <b:if cond='data:view.isHomepage'>
      <title><data:blog.title.escaped/></title>
      <b:else/>
      <title><data:view.title.escaped/> | Roushan Gupta | Roushan Kumar</title>
    </b:if>
    <b:include data='blog' name='all-head-content'/>
    <!-- ===== Roushan SEO: Meta Description ===== -->
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description.escaped' name='description'/>
      <b:else/>
      <meta content='Roushan Gupta &amp; Roushan Kumar - Business, Technology, AI, Startups &amp; Digital Marketing blog. Latest tips, tools, reviews &amp; ideas to grow your business.' name='description'/>
    </b:if>
    <meta content='Roushan Gupta' name='author'/>
    <!-- ===== Roushan SEO: Robots ===== -->
    <b:if cond='data:view.search.query'>
      <meta content='noindex, follow' name='robots'/>
      <b:else/>
      <meta content='index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1' name='robots'/>
    </b:if>
    <b:if cond='data:view.isSingleItem'>
      <link expr:href='data:blog.canonicalUrl' rel='canonical'/>
    </b:if>
    <!-- ===== Roushan SEO: Open Graph + Twitter Card ===== -->
    <meta expr:content='data:blog.title.escaped' property='og:site_name'/>
    <b:if cond='data:view.isHomepage'>
      <meta expr:content='data:blog.title.escaped' property='og:title'/>
      <b:else/>
      <meta expr:content='data:view.title.escaped' property='og:title'/>
    </b:if>
    <meta expr:content='data:view.url.canonical' property='og:url'/>
    <b:if cond='data:view.isSingleItem'>
      <meta content='article' property='og:type'/>
      <b:else/>
      <meta content='website' property='og:type'/>
    </b:if>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description.escaped' property='og:description'/>
      <meta expr:content='data:view.description.escaped' name='twitter:description'/>
      <b:else/>
      <meta content='Roushan Gupta &amp; Roushan Kumar - Business, Technology, AI, Startups &amp; Digital Marketing blog.' property='og:description'/>
      <meta content='Roushan Gupta &amp; Roushan Kumar - Business, Technology, AI, Startups &amp; Digital Marketing blog.' name='twitter:description'/>
    </b:if>
    <meta content='summary_large_image' name='twitter:card'/>
    <b:if cond='data:view.isPost and data:posts.first.featuredImage'>
      <meta expr:content='data:posts.first.featuredImage.isYouTube ? data:posts.first.featuredImage.youtubeMaxResDefaultUrl : resizeImage(data:posts.first.featuredImage, 1200, &quot;1200:630&quot;)' property='og:image'/>
      <meta expr:content='data:posts.first.featuredImage.isYouTube ? data:posts.first.featuredImage.youtubeMaxResDefaultUrl : resizeImage(data:posts.first.featuredImage, 1200, &quot;1200:630&quot;)' name='twitter:image'/>
    </b:if>
    <!-- ===== Roushan SEO: WebSite + Person Schema (Roushan Gupta / Roushan Kumar) ===== -->
  <b:if cond='data:view.isHomepage'>
 <script type='application/ld+json'>{&quot;@context&quot;:&quot;https://schema.org&quot;,&quot;@type&quot;:&quot;WebSite&quot;,&quot;name&quot;:&quot;<data:blog.title.escaped/>&quot;,&quot;alternateName&quot;:&quot;Roushan Gupta | Roushan Kumar&quot;,&quot;url&quot;:&quot;<data:blog.homepageUrl/>&quot;,&quot;potentialAction&quot;:{&quot;@type&quot;:&quot;SearchAction&quot;,&quot;target&quot;:&quot;<data:blog.homepageUrl/>search?q={search_term_string}&quot;,&quot;query-input&quot;:&quot;required name=search_term_string&quot;}}</script>
 <script type='application/ld+json'>{&quot;@context&quot;:&quot;https://schema.org&quot;,&quot;@graph&quot;:[{&quot;@type&quot;:&quot;Person&quot;,&quot;@id&quot;:&quot;<data:blog.homepageUrl/>#roushan-gupta&quot;,&quot;name&quot;:&quot;Roushan Gupta&quot;,&quot;alternateName&quot;:&quot;Roushan&quot;,&quot;url&quot;:&quot;<data:blog.homepageUrl/>&quot;,&quot;jobTitle&quot;:&quot;Blogger, Business &amp; Technology Writer&quot;,&quot;knowsAbout&quot;:[&quot;Business&quot;,&quot;Technology&quot;,&quot;Artificial Intelligence&quot;,&quot;Startups&quot;,&quot;Digital Marketing&quot;],&quot;sameAs&quot;:[]},{&quot;@type&quot;:&quot;Person&quot;,&quot;@id&quot;:&quot;<data:blog.homepageUrl/>#roushan-kumar&quot;,&quot;name&quot;:&quot;Roushan Kumar&quot;,&quot;alternateName&quot;:&quot;Roushan&quot;,&quot;url&quot;:&quot;<data:blog.homepageUrl/>&quot;,&quot;jobTitle&quot;:&quot;Blogger, Business &amp; Technology Writer&quot;,&quot;knowsAbout&quot;:[&quot;Business&quot;,&quot;Technology&quot;,&quot;Artificial Intelligence&quot;,&quot;Startups&quot;,&quot;Digital Marketing&quot;],&quot;sameAs&quot;:[]},{&quot;@type&quot;:&quot;Blog&quot;,&quot;name&quot;:&quot;<data:blog.title.escaped/>&quot;,&quot;alternateName&quot;:&quot;Roushan Gupta | Roushan Kumar&quot;,&quot;url&quot;:&quot;<data:blog.homepageUrl/>&quot;,&quot;description&quot;:&quot;Business, Technology, AI, Startups and Digital Marketing blog by Roushan Gupta and Roushan Kumar&quot;,&quot;author&quot;:[{&quot;@id&quot;:&quot;<data:blog.homepageUrl/>#roushan-gupta&quot;},{&quot;@id&quot;:&quot;<data:blog.homepageUrl/>#roushan-kumar&quot;}]}]}</script>
    </b:if>
    <!-- ===== Performance: font preconnect + Google Fonts ===== -->
    <link href='https://fonts.googleapis.com' rel='preconnect'/>
    <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
    <link href='https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&amp;family=Poppins:ital,wght@0,400;0,500;0,700;1,400&amp;family=Indie+Flower&amp;display=swap' media='all' rel='stylesheet' type='text/css'/>
    <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css' media='all' rel='stylesheet'/>"""
sub_once(OLD_HEAD, NEW_HEAD, "head SEO block")

# ------------------------------------------------- 3. static defaults script
sub_once(
    '    noThumbnail = "https://4.bp.blogspot.com/-O3EpVMWcoKw/WxY6-6I4--I/AAAAAAAAB2s/KzC0FqUQtkMdw7VzT6oOR_8vbZO6EJc-ACK4BGAYYCw/s1600/nth.png",',
    '    noThumbnail = "data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27300%27 height=%27200%27%3E%3Crect width=%27300%27 height=%27200%27 fill=%27%23e9ecef%27/%3E%3Ctext x=%27150%27 y=%27105%27 font-family=%27Arial%27 font-size=%2715%27 fill=%27%23868e96%27 text-anchor=%27middle%27%3ERoushan Blog%3C/text%3E%3C/svg%3E",',
    "noThumbnail data-uri")
sub_once('    disqusShortname = "soratemplates";', '    disqusShortname = "";', "disqus shortname")
sub_once("<b:widget-setting name='link-0'>soratemplates</b:widget-setting>",
         "<b:widget-setting name='link-0'></b:widget-setting>",
         "theme options disqus")

# ---------------------------------------------------------------- 4. header
sub_once("title='Sian (Header)'", "title='Roushan Blog (Header)'", "header title")
sub_once(
"""          <b:widget-settings>
            <b:widget-setting name='displayUrl'>https://blogger.googleusercontent.com/img/a/AVvXsEgtIHaT2vCnSi49OOfGMGROlnmotuZ285fpS1HTuE_RMN1LRu-gYlvS7vzJ9hl2N2sFHaEaAcWwfAxdnngxZXpBWy8cCjqCMgEDFBMFxjjiuIlaG18Vrr6Zg8BJxfnIyHQyvoVahQ-78CTftJIuRkOj_smeC9cdfK9yAJvmFk1Dupna6urkxDUg0MRJMJa7=s102</b:widget-setting>
            <b:widget-setting name='displayHeight'>38</b:widget-setting>
            <b:widget-setting name='sectionWidth'>150</b:widget-setting>
            <b:widget-setting name='useImage'>true</b:widget-setting>
            <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
            <b:widget-setting name='imagePlacement'>REPLACE</b:widget-setting>
            <b:widget-setting name='displayWidth'>102</b:widget-setting>
          </b:widget-settings>""",
"""          <b:widget-settings>
            <b:widget-setting name='useImage'>false</b:widget-setting>
            <b:widget-setting name='imagePlacement'>BEHIND_TITLE</b:widget-setting>
          </b:widget-settings>""",
"header text logo")

# ------------------------------------------------------- 5. top scrolling menu
sub_once(
"""          <b:widget-settings>
            <b:widget-setting name='link-5'>#testimonial-wrap</b:widget-setting>
            <b:widget-setting name='link-6'>#main-wrapper</b:widget-setting>
            <b:widget-setting name='link-3'>#intro-author-wrap</b:widget-setting>
            <b:widget-setting name='link-4'>#head-text2</b:widget-setting>
            <b:widget-setting name='text-1'>Services</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='text-3'>Information</b:widget-setting>
            <b:widget-setting name='text-2'>Conuter</b:widget-setting>
            <b:widget-setting name='text-5'>Reviews</b:widget-setting>
            <b:widget-setting name='text-4'>Projects</b:widget-setting>
            <b:widget-setting name='text-6'>Blog</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
            <b:widget-setting name='link-1'>#serv-tile-wrap</b:widget-setting>
            <b:widget-setting name='link-2'>#counter-image-nav</b:widget-setting>
            <b:widget-setting name='link-0'>#header-wrap</b:widget-setting>
          </b:widget-settings>""",
"""          <b:widget-settings>
            <b:widget-setting name='link-4'>#footer-wrapper</b:widget-setting>
            <b:widget-setting name='link-3'>#counter-bar-nav</b:widget-setting>
            <b:widget-setting name='link-2'>#sidebar</b:widget-setting>
            <b:widget-setting name='link-1'>#main-wrapper</b:widget-setting>
            <b:widget-setting name='link-0'>#header-wrap</b:widget-setting>
            <b:widget-setting name='text-4'>Contact</b:widget-setting>
            <b:widget-setting name='text-3'>Achievements</b:widget-setting>
            <b:widget-setting name='text-2'>Popular</b:widget-setting>
            <b:widget-setting name='text-1'>Articles</b:widget-setting>
            <b:widget-setting name='text-0'>Home</b:widget-setting>
            <b:widget-setting name='sorting'>NONE</b:widget-setting>
          </b:widget-settings>""",
"top menu")

# ------------------------------------------------------------- 6. main menu
sub_once(
"""           <b:widget-settings>
             <b:widget-setting name='text-10'>_Web Documentation</b:widget-setting>
             <b:widget-setting name='sorting'>NONE</b:widget-setting>
             <b:widget-setting name='link-1'>#</b:widget-setting>
             <b:widget-setting name='link-2'>#</b:widget-setting>
             <b:widget-setting name='link-12'>https://www.soratemplates.com/2025/06/sian-blogger-templates.html</b:widget-setting>
             <b:widget-setting name='link-0'>/</b:widget-setting>
             <b:widget-setting name='link-11'>https://youtu.be/B6YqBaNKibE</b:widget-setting>
             <b:widget-setting name='link-10'>https://www.sorabloggingtips.com/2025/06/how-to-setup-sian-blogger-template.html</b:widget-setting>
             <b:widget-setting name='text-9'>Documentation</b:widget-setting>
             <b:widget-setting name='link-9'>#</b:widget-setting>
             <b:widget-setting name='text-8'>_Error Page</b:widget-setting>
             <b:widget-setting name='link-7'>https://www.sorabloggingtips.com/2017/01/how-to-add-sitemap-widget-in-blogspot-blogs.html</b:widget-setting>
             <b:widget-setting name='link-8'>https://sian-soratemplates.blogspot.com/soratemplates</b:widget-setting>
             <b:widget-setting name='link-5'>#</b:widget-setting>
             <b:widget-setting name='link-6'>https://sian-soratemplates.blogspot.com/p/page-markup-and-typography.html</b:widget-setting>
             <b:widget-setting name='link-3'>#</b:widget-setting>
             <b:widget-setting name='link-4'>#</b:widget-setting>
             <b:widget-setting name='text-1'>Features</b:widget-setting>
             <b:widget-setting name='text-0'>Home</b:widget-setting>
             <b:widget-setting name='text-3'>__DropDown 1</b:widget-setting>
             <b:widget-setting name='text-2'>_Multi DropDown</b:widget-setting>
             <b:widget-setting name='text-5'>__DropDown 3</b:widget-setting>
             <b:widget-setting name='text-4'>__DropDown 2</b:widget-setting>
             <b:widget-setting name='text-7'>_SiteMap</b:widget-setting>
             <b:widget-setting name='text-6'>_ShortCodes</b:widget-setting>
             <b:widget-setting name='text-11'>_Video Documentation</b:widget-setting>
             <b:widget-setting name='text-12'>Download This Template</b:widget-setting>
           </b:widget-settings>""",
"""           <b:widget-settings>
             <b:widget-setting name='link-5'>/p/contact.html</b:widget-setting>
             <b:widget-setting name='link-4'>/p/about.html</b:widget-setting>
             <b:widget-setting name='link-3'>/search/label/AI</b:widget-setting>
             <b:widget-setting name='link-2'>/search/label/Technology</b:widget-setting>
             <b:widget-setting name='link-1'>/search/label/Business</b:widget-setting>
             <b:widget-setting name='link-0'>/</b:widget-setting>
             <b:widget-setting name='text-5'>Contact</b:widget-setting>
             <b:widget-setting name='text-4'>About</b:widget-setting>
             <b:widget-setting name='text-3'>AI</b:widget-setting>
             <b:widget-setting name='text-2'>Technology</b:widget-setting>
             <b:widget-setting name='text-1'>Business</b:widget-setting>
             <b:widget-setting name='text-0'>Home</b:widget-setting>
             <b:widget-setting name='sorting'>NONE</b:widget-setting>
           </b:widget-settings>""",
"main menu")
sub_once("title='Menu Widget'", "title='Main Menu'", "main menu title")

# ---------------------------------------------------------------- 7. hero
sub_block(
    "<b:widget id='Image1' locked='true' title='The Power Of Subscription Economy.'",
    "</b:widget>",
"""<b:widget id='Image1' locked='true' title='Roushan Gupta &amp; Roushan Kumar' type='Image' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='displayUrl'>https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie6C_0nmpVrX81azVf4ELg4F3khf2pKW6NRXb3-PCNhl7-DKzj14xkNP0DiOQL9kJ4qLRXNFWb28DofJaTbGGswPIHWNT49Xsb53PZ5nAJ1Y6ESS5cKIZdZqzyiqM4mLM-d78dYpjde-H6ApwsDlkGRNQHUuc_slinbuMrJB7SkVA_8oGtQ0SamjVw9e8W/s1440/sora-bg.jpg</b:widget-setting>
            <b:widget-setting name='displayHeight'>1147</b:widget-setting>
            <b:widget-setting name='sectionWidth'>150</b:widget-setting>
            <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
            <b:widget-setting name='displayWidth'>1440</b:widget-setting>
            <b:widget-setting name='caption'><![CDATA[Business, Technology &amp; AI - the latest ideas, tools and insights to grow your business. Written by Roushan Gupta &amp; Roushan Kumar.]]></b:widget-setting>
          </b:widget-settings>
          <b:includable id='main'>
            <b:include name='content'/>
          </b:includable>
          <b:includable id='content'>
            <div class='row container widget-content'>
              &lt;style type=&#39;text/css&#39;&gt;
              #intro-wrap{display:block}
              #intro-wrap .full-height:after{background-image: url(<data:sourceUrl/>);background-size:cover;background-position:center;}
              &lt;/style&gt;
              <div class='wow animate__animated animate__fadeInUp intro-content' data-wow-delay='0.8s' data-wow-duration='0.8s'>
                <h3 class='intro-title'><data:title/></h3>
                <b:if cond='data:caption'>
                  <p class='intro-snippet'><data:caption/></p>
                </b:if>
                <div class='intro-action'>
                  <a href='#main-wrapper'>Read Blog</a>
                </div>
              </div>
            </div>
          </b:includable>
        """,
"hero widget")

# ---------------------------------------------------------------- 8. index headline
sub_once("title='Recent Blog Posts'", "title='Latest Articles'", "index headline title")
sub_once(
    "<b:widget-setting name='content'><![CDATA[Lorem Ipsum has been the industry's standard dummy text.]]></b:widget-setting>",
    "<b:widget-setting name='content'><![CDATA[Fresh articles on Business, Technology, AI, Startups &amp; Digital Marketing - written by Roushan Gupta &amp; Roushan Kumar.]]></b:widget-setting>",
    "index headline text")

# --------------------------------------------------------- 9. achievements
sub_once("<b:widget id='Image10' locked='true' title='1458'", "<b:widget id='Image10' locked='true' title='150'", "counter 1")
sub_once("name='link'>ri-pages-line", "name='link'>fa-file-lines", "counter 1 icon")
sub_once("name='caption'>Projects Completed", "name='caption'>Articles Published", "counter 1 caption")
sub_once("<b:widget id='Image11' locked='true' title='1247'", "<b:widget id='Image11' locked='true' title='5000'", "counter 2")
sub_once("name='link'>ri-cup-line", "name='link'>fa-users", "counter 2 icon")
sub_once("name='caption'>Cups of Coffee", "name='caption'>Happy Readers", "counter 2 caption")
sub_first("<b:widget id='Image12' locked='true' title='1763'", "<b:widget id='Image12' locked='true' title='5'", "counter 3")
sub_first("name='link'>ri-earth-line", "name='link'>fa-calendar-check", "counter 3 icon")
sub_first("name='caption'>Worldwide Clients", "name='caption'>Years of Blogging", "counter 3 caption")
sub_first("<b:widget id='Image13' locked='true' title='1763'", "<b:widget id='Image13' locked='true' title='100'", "counter 4")
sub_first("name='link'>ri-earth-line", "name='link'>fa-tags", "counter 4 icon")
sub_first("name='caption'>Worldwide Clients", "name='caption'>Topics Covered", "counter 4 caption")

# ---------------------------------------------------------------- 10. sidebar
sub_once("<b:widget-setting name='timeRange'>LAST_WEEK</b:widget-setting>",
         "<b:widget-setting name='timeRange'>ALL_TIME</b:widget-setting>", "popular timeRange")
sub_once(
"""<b:widget id='HTML7' locked='false' title='Projects' type='HTML' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='content'>3/Health/post-list</b:widget-setting>
            </b:widget-settings>""",
"""<b:widget id='HTML7' locked='false' title='About Roushan' type='HTML' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='content'><![CDATA[<div class="about-box">
  <div class="about-ava">RG</div>
  <p>Hi, I&#39;m <b>Roushan Gupta</b> along with <b>Roushan Kumar</b>. We write about <b>Business, Technology, AI, Startups &amp; Digital Marketing</b> - simple ideas, real tools and honest reviews to help you grow online.</p>
  <a class="about-more" href="/p/about.html">Read My Story</a>
</div>]]></b:widget-setting>
            </b:widget-settings>""",
"about widget")
sub_once(
"""              <b:widget-setting name='content'><![CDATA[<div class="videoWrapper">
    <!-- Copy & Pasted from YouTube -->
    <iframe width="560" height="349" src="https://www.youtube.com/embed/keqDKvHV8Pk" frameborder="0" allowfullscreen></iframe>
</div>
<style>
.videoWrapper {
position: relative;
padding-bottom: 56.25%; /* 16:9 */
padding-top: 25px;
height: 0;
}
.videoWrapper iframe {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
}
</style>]]></b:widget-setting>""",
"""              <b:widget-setting name='content'><![CDATA[<div class="contact-box">
  <p>Got a topic idea, a question or a business project? Drop a message - we read everything and reply fast.</p>
  <a class="about-more" href="/p/contact.html">Contact Us</a>
</div>]]></b:widget-setting>""",
"contact widget")
sub_once("title='Subscribe Us'", "title='Get in Touch'", "contact title")
sub_once("<b:widget-setting name='selectedLabelsList'>Business,Learn,Lifestyle,Nature,People,Technology</b:widget-setting>",
         "<b:widget-setting name='selectedLabelsList'>Business,Technology,AI,Startups,Marketing,AI Tools</b:widget-setting>",
         "categories labels")

# ------------------------------------------------------- 11. blog widget SEO
sub_block(
    "<b:includable id='postBreadcrumbs' var='post'>",
    "</b:includable>",
"""<b:includable id='postBreadcrumbs' var='post'>
              <!-- Post Breadcrumbs (JSON-LD, SEO) -->
              <script type='application/ld+json'>
              {
                &quot;@context&quot;: &quot;https://schema.org&quot;,
                &quot;@type&quot;: &quot;BreadcrumbList&quot;,
                &quot;itemListElement&quot;: [{
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: 1,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<data:messages.home/>&quot;,
                    &quot;@id&quot;: &quot;<data:blog.homepageUrl/>&quot;
                  }
                },
                <b:if cond='data:post.labels'>
                {
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: 2,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<data:post.labels.first.name/>&quot;,
                    &quot;@id&quot;: &quot;<data:post.labels.first.url/>&quot;
                  }
                },
                </b:if>
                {
                  &quot;@type&quot;: &quot;ListItem&quot;,
                  &quot;position&quot;: <b:if cond='data:post.labels'>3<b:else/>2</b:if>,
                  &quot;item&quot;: {
                    &quot;name&quot;: &quot;<data:post.title/>&quot;,
                    &quot;@id&quot;: &quot;<data:post.url.jsonEscaped/>&quot;
                  }
                }]
              }
              </script>
            """,
"breadcrumbs")

# insert Article JSON-LD includable before postMetadataJSONImage
sub_once(
    "<b:includable id='postMetadataJSONImage'>",
"""<b:includable id='postMetadataJSON' var='post'>
              <!-- Article JSON-LD (SEO) -->
              <script type='application/ld+json'>
              {
                &quot;@context&quot;: &quot;https://schema.org&quot;,
                &quot;@type&quot;: &quot;<b:if cond='data:view.isPost'>BlogPosting<b:else/>WebPage</b:if>&quot;,
                &quot;mainEntityOfPage&quot;: {
                  &quot;@type&quot;: &quot;WebPage&quot;,
                  &quot;@id&quot;: &quot;<data:post.url.jsonEscaped/>&quot;
                },
                &quot;headline&quot;: &quot;<data:post.title.jsonEscaped/>&quot;,
                <b:include data='post' name='postMetadataJSONImage'/>
                <b:include data='post' name='postMetadataJSONPublisher'/>
                &quot;inLanguage&quot;: &quot;en&quot;,
                &quot;datePublished&quot;: &quot;<data:post.date.iso8601/>&quot;,
                &quot;dateModified&quot;: &quot;<data:post.lastUpdated.iso8601/>&quot;,
                <b:if cond='data:post.labels'>
                &quot;articleSection&quot;: &quot;<data:post.labels.first.name/>&quot;,
                &quot;keywords&quot;: &quot;<data:post.labels.first.name/>&quot;,
                </b:if>
                &quot;author&quot;: {
                  &quot;@type&quot;: &quot;Person&quot;,
                  &quot;name&quot;: &quot;Roushan Gupta&quot;,
                  &quot;alternateName&quot;: &quot;Roushan Kumar&quot;,
                  &quot;url&quot;: &quot;<data:blog.homepageUrl/>&quot;
                }
              }
              </script>
            </b:includable>
            <b:includable id='postMetadataJSONImage'>""",
"article JSON-LD")

sub_once(
""" &quot;publisher&quot;: {
    &quot;@type&quot;: &quot;Organization&quot;,
    &quot;name&quot;: &quot;Blogger&quot;,
    &quot;logo&quot;: {
      &quot;@type&quot;: &quot;ImageObject&quot;,
      &quot;url&quot;: &quot;https://lh3.googleusercontent.com/ULB6iBuCeTVvSjjjU1A-O8e9ZpVba6uvyhtiWRti_rBAs9yMYOFBujxriJRZ-A=h60&quot;,
      &quot;width&quot;: 206,
      &quot;height&quot;: 60
    }
  },
""",
""" &quot;publisher&quot;: {
    &quot;@type&quot;: &quot;Organization&quot;,
    &quot;name&quot;: &quot;Roushan Gupta | Roushan Kumar&quot;,
    &quot;url&quot;: &quot;<data:blog.homepageUrl/>&quot;
  },
""",
"publisher brand")

# lazy loading for thumbnails (all post-thumb images)
sub_all("class='post-thumb'", "class='post-thumb' loading='lazy' decoding='async'", "lazy thumbs")

# share buttons: remove demo twitter handle
sub_once("twitter.com/intent/tweet?via=templatesyard&amp;url=", "twitter.com/intent/tweet?url=", "twitter share")

# 404 page: drop icon font glyph
sub_once("<a class='homepage' expr:href='data:blog.homepageUrl'><i class='fa fa-home'/> <data:messages.home/></a>",
         "<a class='homepage' expr:href='data:blog.homepageUrl'><data:messages.home/></a>", "404 link")

# itemPost: add Table of Contents
sub_block(
    "<b:includable id='itemPost' var='post'>",
    "</b:includable>",
"""<b:includable id='itemPost' var='post'>
              <!-- Item Post Content -->
              <b:include data='post' name='postMeta'/>
              <div class='post-header'>
                <b:include data='post' name='postHeader'/>
              </div>
              <b:if cond='data:view.isPost'>
                <div class='post-toc-wrap'>
                  <h4 class='toc-title'><i class='fa fa-list-ul'/> Table of Contents</h4>
                  <ul class='post-toc' data-toc-headings='h2,h3'/>
                </div>
              </b:if>
              <b:include data='post' name='postBody'/>
              <b:include cond='data:view.isPost' data='post' name='postFooter'/>
            """,
"itemPost TOC")

# ---------------------------------------------------------------- 12. footer
sub_once(
    "        <div class='copyright-area'>Created By <a href='http://soratemplates.com/' id='mycontent' rel='dofollow' title='SoraTemplates'>Sora</a>  | Distributed By <a href='https://gooyaabitemplates.com/' rel='dofollow' style='color:#ff00ba;' target='_blank' title='Gooyaabi'>Gooyaabi</a></div>",
    "        <div class='copyright-area'>\u00a9 <span id='copyright-year'>2026</span> <strong>Roushan Gupta</strong> &amp; <strong>Roushan Kumar</strong> - All Rights Reserved.</div>",
    "copyright")
sub_once(
"""       <b:widget-settings>
         <b:widget-setting name='sorting'>NONE</b:widget-setting>
         <b:widget-setting name='text-1'>About</b:widget-setting>
         <b:widget-setting name='link-1'>https://sian-soratemplates.blogspot.com/p/about-us.html</b:widget-setting>
         <b:widget-setting name='text-0'>Home</b:widget-setting>
         <b:widget-setting name='link-2'>https://sian-soratemplates.blogspot.com/p/contact-us.html</b:widget-setting>
         <b:widget-setting name='link-0'>/</b:widget-setting>
         <b:widget-setting name='text-2'>Contact Us</b:widget-setting>
       </b:widget-settings>""",
"""       <b:widget-settings>
         <b:widget-setting name='sorting'>NONE</b:widget-setting>
         <b:widget-setting name='text-3'>Privacy Policy</b:widget-setting>
         <b:widget-setting name='link-3'>/p/privacy-policy.html</b:widget-setting>
         <b:widget-setting name='text-2'>Contact</b:widget-setting>
         <b:widget-setting name='link-2'>/p/contact.html</b:widget-setting>
         <b:widget-setting name='text-1'>About</b:widget-setting>
         <b:widget-setting name='link-1'>/p/about.html</b:widget-setting>
         <b:widget-setting name='text-0'>Home</b:widget-setting>
         <b:widget-setting name='link-0'>/</b:widget-setting>
       </b:widget-settings>""",
"footer menu")

# ---------------------------------------------------------------- 13. scripts
# remove the 424KB obfuscated credit-lock script line
marker = "var _0x11c464=_0x19c8;"
i = t.index(marker)
line_start = t.rfind("\n", 0, i)
line_end = t.index("\n", i)
t = t[:line_start] + t[line_end:]
print("ok  removed obfuscated credit-lock script")

# remove Facebook SDK (unused)
sub_block(
    "<!-- Facebook SDK -->",
    "</script>",
    "",
    "facebook sdk",
    keep_end=True,
)

# insert Roushan enhancement script before the overlay markup
sub_once(
    "<!-- Overlay and Back To Top -->",
"""<!-- ===== Roushan v2.0: related posts, timeago, TOC, back-to-top, auto year ===== -->
<script type='text/javascript'>
//<![CDATA[
(function ($) {
  'use strict';
  function decodeHtml(s) {
    return s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'");
  }
  $(function () {
    // 1) Auto copyright year
    var y = new Date().getFullYear();
    var cy = document.getElementById('copyright-year');
    if (cy) { cy.textContent = y; }

    // 2) Back to top
    $('.back-top').on('click', function () {
      $('html, body').animate({ scrollTop: 0 }, 350);
    });

    // 3) "2 hours ago" style dates
    if ($.fn.timeago) { $('.timeago').timeago(); }

    // 4) Table of contents on single posts
    if ($.fn.toc && $('.post-toc').length) {
      $('.post-toc').toc({ content: 'body', headings: 'h2,h3' });
    }

    // 5) Related posts (label based, fallback random)
    var $rw = $('#related-wrap');
    if ($rw.length && $.fn.jquery) {
      var label = $rw.find('.related-tag').attr('data-label');
      var host = window.location.protocol + '//' + window.location.host;
      var feed;
      if (label && label !== 'random') {
        feed = host + '/feeds/posts/summary/-/' + encodeURIComponent(label) + '?max-results=5&alt=json';
      } else {
        feed = host + '/feeds/posts/summary?max-results=5&alt=json';
      }
      $.get(feed).done(function (data) {
        try {
          var entries = data.feed.entry || [];
          if (!entries.length) { return; }
          var here = window.location.href.split('?')[0];
          var html = '<ul class="related-posts">';
          var n = 0;
          for (var i = 0; i < entries.length && n < 4; i++) {
            var e = entries[i];
            var link = '';
            for (var j = 0; j < e.link.length; j++) {
              if (e.link[j].rel === 'alternate') { link = e.link[j].href; break; }
            }
            if (!link || link.split('?')[0] === here) { continue; }
            var title = decodeHtml(e.title.$t || '');
            var img = '';
            if (e.media$thumbnail) { img = e.media$thumbnail.url.replace(/\\/s[0-9]+(-c)?(\\/[a-z0-9]+)?\\//, '/s240-rw-c/'); }
            html += '<li class="related-item"><a class="post-image-link" href="' + link + '">';
            if (img) { html += '<img alt="' + title.replace(/"/g, '') + '" loading="lazy" src="' + img + '"/>'; }
            html += '</a><h2 class="post-title"><a href="' + link + '">' + title + '</a></h2></li>';
            n++;
          }
          html += '</ul>';
          if (n > 0) { $rw.html(html); }
        } catch (err) { /* ignore */ }
      });
    }
  });
})(jQuery);
//]]>
</script>

<!-- Overlay and Back To Top -->""",
"enhancement script")

# ---------------------------------------------------------------- 14. custom CSS
sub_once(
    "]]></b:skin>",
"""
/* ================= Roushan v2.0 CSS ================= */
/* Post: Table of Contents */
.post-toc-wrap{
    margin:0 0 25px;
    padding:18px 20px;
    background:#f6f8fa;
    border:1px solid #e6e9ec;
    border-left:4px solid $(main.color);
    border-radius:8px;
}
.toc-title{
    margin:0 0 10px;
    font-size:16px;
    font-weight:700;
    color:$(title.color);
}
.toc-title i{
    color:$(main.color);
    margin:0 8px 0 0;
    font-size:14px;
}
.post-toc{
    margin:0;
    padding:0;
    list-style:none;
}
.post-toc li{
    padding:4px 0;
    font-size:14px;
}
.post-toc a{
    color:$(body.text.color);
    text-decoration:none;
    transition:color .17s ease;
}
.post-toc a:hover{
    color:$(main.color);
}
.post-toc ul{
    margin:0 0 0 16px;
    padding:0;
    list-style:none;
}
.post-toc-wrap ul:empty{
    display:none;
}
.post-toc-wrap:has(ul:empty){
    display:none;
}
/* Sidebar: About + Contact boxes */
.about-box .about-ava{
    width:70px;
    height:70px;
    margin:0 auto 12px;
    line-height:70px;
    text-align:center;
    font-size:24px;
    font-weight:800;
    color:#ffffff;
    background:$(main.color);
    border-radius:50%;
}
.about-box p{
    font-size:13px;
    line-height:1.7;
    margin:0 0 12px;
}
.contact-box p{
    font-size:13px;
    line-height:1.7;
    margin:0 0 12px;
}
.about-more{
    display:inline-block;
    height:36px;
    line-height:36px;
    padding:0 18px;
    font-size:13px;
    font-weight:600;
    color:#ffffff;
    background:$(main.color);
    border-radius:6px;
    text-decoration:none;
    transition:background .17s ease;
}
.about-more:hover{
    background:$(dark.color);
}
/* Post body responsive media */
.post-body img, .post-body iframe{
    max-width:100%;
    height:auto;
}
/* Related posts images */
.related-posts .post-image-link img{
    width:100%;
    height:90px;
    object-fit:cover;
}
/* Footer brand */
.copyright-area strong{
    font-weight:700;
}
@media (max-width:767px){
    .post-toc-wrap{
        padding:14px 16px;
    }
    .intro-title{
        font-size:30px;
    }
}
]]></b:skin>""",
"custom css")

# --------------------------------------------------------------- validate
if errors:
    print("\n".join(errors))
    print(f"\nFAILED with {len(errors)} error(s). Output NOT written.")
    sys.exit(1)

# sanity: no leftover demo/brand junk
leftovers = []
for bad in ["remixicon", "_0x11c464", "soratemplates", "gooyaabitemplates",
            "SoraTemplates", "Sian (Header)", "fa fa-home", "via=templatesyard",
            "facebook-jssdk", "Conuter", "DropDown 1", "Lorem Ipsum"]:
    if bad in t:
        leftovers.append(bad)
if leftovers:
    print("LEFTOVERS:", leftovers)
    sys.exit(1)

# restore CRLF line endings (matches original)
t = t.replace("\n", "\r\n")

with io.open(DST, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print(f"\nWROTE {DST} ({os.path.getsize(DST)} bytes)")
