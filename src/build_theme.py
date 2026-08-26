#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build SkillBlog Pro — complete Blogger theme XML."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = (ROOT / "src" / "skin.css").read_text(encoding="utf-8")
JS = (ROOT / "src" / "app.js").read_text(encoding="utf-8")

# Blogger Theme Designer variables (must live in a CSS comment)
VARS = r"""
/*---------------------------------------------------------------------------
Theme: SkillBlog Pro 1.0.0
Designer: Roushan Blog
Inspired by: skillcourse.in
----------------------------------------------------------------------------
<Group description="Brand Colors">
  <Variable name="keycolor" description="Brand Gold" type="color" default="#e5b549" value="#e5b549"/>
  <Variable name="keycolor2" description="Gold Highlight" type="color" default="#f5c518" value="#f5c518"/>
  <Variable name="orange" description="Accent Orange" type="color" default="#ea580c" value="#ea580c"/>
  <Variable name="peach" description="Peach" type="color" default="#fecda5" value="#fecda5"/>
  <Variable name="peachbg" description="Peach Background" type="color" default="#fff6ec" value="#fff6ec"/>
  <Variable name="navy" description="Navy" type="color" default="#1b2431" value="#1b2431"/>
  <Variable name="navy2" description="Navy Soft" type="color" default="#243044" value="#243044"/>
  <Variable name="muted" description="Muted Text" type="color" default="#5c6573" value="#5c6573"/>
  <Variable name="line" description="Borders" type="color" default="#ede4d4" value="#ede4d4"/>
  <Variable name="card" description="Card Surface" type="color" default="#ffffff" value="#ffffff"/>
</Group>
<Group description="Page">
  <Variable name="body.background.color" description="Page Background" type="color" default="#fffbf5" value="#fffbf5"/>
  <Variable name="body.text.color" description="Body Text" type="color" default="#1b2431" value="#1b2431"/>
  <Variable name="body.font" description="Body Font" type="font"
      default="400 16.5px Plus Jakarta Sans, Noto Sans Devanagari, sans-serif"
      value="400 16.5px Plus Jakarta Sans, Noto Sans Devanagari, sans-serif"/>
  <Variable name="title.font" description="Heading Font" type="font"
      default="800 28px Plus Jakarta Sans, Noto Sans Devanagari, sans-serif"
      value="800 28px Plus Jakarta Sans, Noto Sans Devanagari, sans-serif"/>
</Group>
---------------------------------------------------------------------------*/
"""

ICON_CAP = """<svg viewBox='0 0 24 24' aria-hidden='true'><path d='M12 3L1 8l11 5 9-4.09V17h2V8L12 3zm-7 9.18V15c0 1.66 3.13 3 7 3s7-1.34 7-3v-2.82l-7 3.18-7-3.18z'/></svg>"""

def xml():
    return r"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' b:templateVersion='1.0.0' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <meta charset='utf-8'/>
  <meta content='width=device-width, initial-scale=1, minimum-scale=1' name='viewport'/>
  <meta content='IE=edge' http-equiv='X-UA-Compatible'/>
  <meta content='#e5b549' name='theme-color'/>
  <meta content='yes' name='mobile-web-app-capable'/>
  <meta content='SkillBlog Pro' name='apple-mobile-web-app-title'/>
  <b:include data='blog' name='all-head-content'/>

  <title><data:view.title.escaped/></title>

  <b:if cond='data:view.isSingleItem and data:view.description'>
    <meta expr:content='data:view.description' name='description'/>
  <b:elseif cond='data:blog.metaDescription'/>
    <meta expr:content='data:blog.metaDescription' name='description'/>
  <b:else/>
    <meta expr:content='data:blog.title + &quot; — Learn skills that help you build a better career.&quot;' name='description'/>
  </b:if>

  <b:if cond='data:view.isError'>
    <meta content='noindex,follow' name='robots'/>
  <b:else/>
    <meta content='index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1' name='robots'/>
  </b:if>

  <link expr:href='data:view.url.canonical' rel='canonical'/>
  <b:if cond='data:blog.blogspotFaviconUrl'>
    <link expr:href='data:blog.blogspotFaviconUrl' rel='icon'/>
  </b:if>
  <link expr:href='data:blog.homepageUrl + &quot;feeds/posts/default&quot;' rel='alternate' title='Atom' type='application/atom+xml'/>
  <link expr:href='data:blog.homepageUrl + &quot;feeds/posts/default?alt=rss&quot;' rel='alternate' title='RSS' type='application/rss+xml'/>

  <meta expr:content='data:view.title.escaped' property='og:title'/>
  <meta expr:content='data:view.isPost ? &quot;article&quot; : &quot;website&quot;' property='og:type'/>
  <meta expr:content='data:view.url.canonical' property='og:url'/>
  <meta expr:content='data:blog.title' property='og:site_name'/>
  <meta content='en_IN' property='og:locale'/>
  <b:if cond='data:view.description'>
    <meta expr:content='data:view.description' property='og:description'/>
  </b:if>
  <b:if cond='data:view.featuredImage'>
    <meta expr:content='data:view.featuredImage' property='og:image'/>
    <meta expr:content='data:view.featuredImage' name='twitter:image'/>
  <b:elseif cond='data:blog.blogspotFaviconUrl'/>
    <meta expr:content='data:blog.blogspotFaviconUrl' property='og:image'/>
  </b:if>
  <meta content='summary_large_image' name='twitter:card'/>
  <meta expr:content='data:view.title.escaped' name='twitter:title'/>
  <b:if cond='data:view.description'>
    <meta expr:content='data:view.description' name='twitter:description'/>
  </b:if>

  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='anonymous' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Noto+Sans+Devanagari:wght@400;600;700&amp;display=swap' rel='stylesheet'/>

  <script type='application/ld+json'>
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "<data:blog.title.escaped/>",
  "url": "<data:blog.homepageUrl/>",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "<data:blog.searchUrl/>{search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
  </script>
  <b:if cond='data:view.isPost'>
  <script type='application/ld+json'>
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "<data:view.title.escaped/>",
  "description": "<data:view.description/>",
  "mainEntityOfPage": "<data:view.url.canonical/>",
  "url": "<data:view.url.canonical/>",
  "publisher": {
    "@type": "Organization",
    "name": "<data:blog.title.escaped/>",
    "url": "<data:blog.homepageUrl/>"
  }
}
  </script>
  <script type='application/ld+json'>
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"<data:blog.homepageUrl/>"},
    {"@type":"ListItem","position":2,"name":"<data:view.title.escaped/>","item":"<data:view.url.canonical/>"}
  ]
}
  </script>
  </b:if>

  <b:skin version='1.0.0'><![CDATA[
@@VARS@@
@@CSS@@
  ]]></b:skin>

  <b:template-skin>
    <b:variable default='1200px' name='content.width' type='length' value='1200px'/>
    <b:variable default='18px' name='content.padding' type='length' value='18px'/>
    <![CDATA[
      body#layout { width: 980px; margin: 20px auto; background: #fff6ec; }
      body#layout .sb-preloader, body#layout .sb-drawer, body#layout .sb-search, body#layout .sb-cookie, body#layout .sb-top, body#layout .sb-wa { display:none !important; }
      body#layout .sb-header { position: relative; }
      body#layout .sb-hero, body#layout .sb-why, body#layout .sb-stats, body#layout .sb-news { display:block !important; }
    ]]>
  </b:template-skin>
</head>

<body>
  <b:class cond='data:view.isHomepage' name='is-homepage'/>
  <b:class cond='data:view.isPost' name='is-post'/>
  <b:class cond='data:view.isPage' name='is-page'/>
  <b:class cond='data:view.isError' name='is-error'/>
  <b:class cond='data:view.isSearch and !data:view.isLabelSearch' name='is-search'/>
  <b:class cond='data:view.isLabelSearch' name='is-label'/>
  <b:class cond='data:view.isArchive' name='is-archive'/>
  <b:class cond='data:view.isMultipleItems' name='is-index'/>
  <b:class cond='data:view.isLayoutMode' name='layout-mode'/>
  <b:class cond='data:view.isPreview' name='is-preview'/>

  <a class='skip-link' href='#main-content'>Skip to content</a>
  <div class='sb-progress' aria-hidden='true'/>
  <div class='sb-preloader' aria-hidden='true'><div class='sb-loader-mark'>@@ICON_CAP@@</div></div>

  <!-- ===== HEADER ===== -->
  <header class='sb-header'>
    <div class='container sb-header-inner'>
      <a class='sb-logo' expr:href='data:blog.homepageUrl' expr:title='data:blog.title'>
        <span class='sb-logo-mark'>@@ICON_CAP@@</span>
        <span><data:blog.title/> <em>.</em></span>
      </a>

      <nav class='sb-nav' aria-label='Primary'>
        <b:section class='page-nav' id='page-nav' maxwidgets='1' name='Main Menu' showaddelement='yes'>
          <b:widget id='PageList1' locked='false' title='Pages' type='PageList' version='2' visible='true'>
            <b:widget-settings>
              <b:widget-setting name='pageListJson'><![CDATA[{"link0":"true"}]]></b:widget-setting>
              <b:widget-setting name='homeTitle'>Home</b:widget-setting>
              <b:widget-setting name='sortAlpha'>false</b:widget-setting>
            </b:widget-settings>
            <b:includable id='main'>
              <b:include name='content'/>
            </b:includable>
            <b:includable id='content'>
              <ul>
                <li><a expr:href='data:blog.homepageUrl'>Home</a></li>
                <b:loop values='data:links' var='link'>
                  <li><a expr:href='data:link.href'><data:link.title/></a></li>
                </b:loop>
              </ul>
            </b:includable>
          </b:widget>
        </b:section>
      </nav>

      <div class='sb-actions'>
        <button class='sb-icon-btn' data-action='search' title='Search (Ctrl+K)' type='button' aria-label='Open search'>
          <svg viewBox='0 0 24 24'><circle cx='11' cy='11' r='7'/><path d='M20 20l-3.5-3.5'/></svg>
        </button>
        <button class='sb-icon-btn' data-action='theme' title='Toggle dark mode' type='button' aria-label='Toggle theme'>
          <svg class='icon-sun' viewBox='0 0 24 24'><circle cx='12' cy='12' r='4'/><path d='M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4'/></svg>
          <svg class='icon-moon' viewBox='0 0 24 24'><path d='M21 14.5A8.5 8.5 0 1 1 9.5 3 7 7 0 0 0 21 14.5z'/></svg>
        </button>
        <a class='sb-cta' expr:href='data:blog.homepageUrl + &quot;p/courses.html&quot;'>Explore Courses</a>
        <button class='sb-icon-btn sb-burger' data-action='menu' title='Menu' type='button' aria-label='Open menu'>
          <svg viewBox='0 0 24 24'><path d='M4 7h16M4 12h16M4 17h16'/></svg>
        </button>
      </div>
    </div>
  </header>

  <div class='sb-drawer'>
    <div class='sb-drawer-bg' data-action='menu-close'/>
    <aside class='sb-drawer-panel' aria-label='Mobile menu'>
      <div class='sb-drawer-head'>
        <strong>Menu</strong>
        <button class='sb-icon-btn' data-action='menu-close' type='button' aria-label='Close menu'>
          <svg viewBox='0 0 24 24'><path d='M6 6l12 12M18 6L6 18'/></svg>
        </button>
      </div>
      <div class='sb-drawer-nav'/>
    </aside>
  </div>

  <div class='sb-search' role='dialog' aria-label='Search'>
    <div class='sb-search-box'>
      <form expr:action='data:blog.searchUrl' method='get'>
        <input autocomplete='off' name='q' placeholder='Search courses, notes, tutorials…' type='text'/>
        <button class='sb-search-go' type='submit'>Search</button>
        <button data-action='search-close' type='button'>Close</button>
      </form>
    </div>
  </div>

  <!-- ===== HERO (homepage) ===== -->
  <section class='sb-hero'>
    <div class='container sb-hero-grid'>
      <div>
        <div class='sb-kicker'>Job-oriented skill blog</div>
        <h1>Learn skills that help you <span>build a Better Career</span></h1>
        <p class='sb-hero-lead'>Practical tutorials on Excel, Power BI, SQL, Python, AI and office skills — written the SkillCourse way: simple steps, real examples, career results.</p>
        <ul class='sb-checks'>
          <li><i>✓</i> Learn from expert educators</li>
          <li><i>✓</i> Updated curriculum and notes</li>
          <li><i>✓</i> Dedicated support mindset</li>
        </ul>
        <div class='sb-hero-actions'>
          <a class='sb-btn sb-btn-primary' href='#main-content'>Explore Articles</a>
          <a class='sb-btn sb-btn-ghost' expr:href='data:blog.homepageUrl + &quot;p/about.html&quot;'>About this blog</a>
        </div>
      </div>
      <div class='sb-hero-art' aria-hidden='true'>
        <div class='sb-orb'/>
        <div class='sb-hero-card sb-hc1'><span class='sb-chip gold'>★</span><div><b>250k+</b><small>Active learners</small></div></div>
        <div class='sb-hero-card sb-hc2'><span class='sb-chip blue'>▣</span><div><b>20+</b><small>Skill tracks</small></div></div>
        <div class='sb-hero-card sb-hc3'><span class='sb-chip green'>✓</span><div><b>ISO style</b><small>Quality lessons</small></div></div>
      </div>
    </div>
  </section>

  <div class='sb-404'>
    <b>404</b>
    <h2>This page took a coffee break</h2>
    <p>The link may be broken or the post was moved. Try search or go back home.</p>
    <a class='sb-btn sb-btn-primary' expr:href='data:blog.homepageUrl'>Back to Home</a>
  </div>

  <b:if cond='data:view.isSearch or data:view.isLabelSearch or data:view.isArchive'>
    <div class='container' style='padding-top:28px'>
      <div class='sb-section-head' style='margin-bottom:10px'>
        <h1 style='font-size:1.8rem'><data:view.title.escaped/></h1>
        <p>Browse lessons, notes and career guides in this collection.</p>
      </div>
    </div>
  </b:if>

  <!-- ===== MAIN ===== -->
  <div class='container sb-layout' id='main-content'>
    <main class='sb-main'>
      <b:if cond='data:view.isHomepage'>
        <div class='sb-section-head'>
          <h2>Latest Mastery Articles</h2>
          <p>Simple and in-depth lessons with real-world examples — perfect for beginners and working professionals.</p>
        </div>
      </b:if>

      <b:section class='main-posts' id='main' maxwidgets='2' name='Main Posts' showaddelement='yes'>
        <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='showDateHeader'>false</b:widget-setting>
            <b:widget-setting name='commentsText'>Comments</b:widget-setting>
            <b:widget-setting name='postCommentMsg'>Post a Comment</b:widget-setting>
            <b:widget-setting name='showCommentLink'>true</b:widget-setting>
            <b:widget-setting name='showDummy'>false</b:widget-setting>
            <b:widget-setting name='neverShowDateHeader'>true</b:widget-setting>
            <b:widget-setting name='timestampLabel'/>
            <b:widget-setting name='authorLabel'/>
            <b:widget-setting name='showAuthorName'>true</b:widget-setting>
            <b:widget-setting name='showPopupAd'>false</b:widget-setting>
            <b:widget-setting name='showCommentForm'>true</b:widget-setting>
            <b:widget-setting name='showPostLinks'>true</b:widget-setting>
            <b:widget-setting name='usePostSummary'>true</b:widget-setting>
            <b:widget-setting name='showAuthorProfile'>true</b:widget-setting>
            <b:widget-setting name='showTimestamps'>true</b:widget-setting>
            <b:widget-setting name='showBacklinks'>false</b:widget-setting>
            <b:widget-setting name='showInlineAds'>false</b:widget-setting>
            <b:widget-setting name='showReactions'>false</b:widget-setting>
            <b:widget-setting name='showShareButtons'>false</b:widget-setting>
            <b:widget-setting name='showLocation'>false</b:widget-setting>
            <b:widget-setting name='showLabels'>true</b:widget-setting>
            <b:widget-setting name='showCreatedDate'>true</b:widget-setting>
            <b:widget-setting name='postsPerAd'>1</b:widget-setting>
            <b:widget-setting name='mobile'>false</b:widget-setting>
            <b:widget-setting name='postsPerPage'>9</b:widget-setting>
          </b:widget-settings>

          <b:includable id='main'>
            <b:include name='status-message'/>
            <div class='blog-posts hfeed'>
              <b:loop values='data:posts' var='post'>
                <article class='post-outer hentry'>
                  <b:include data='post' name='post'/>
                </article>
              </b:loop>
            </div>
            <b:include name='nextprev'/>
            <b:include name='feedLinks'/>
          </b:includable>

          <b:includable id='post' var='post'>
            <b:if cond='data:view.isMultipleItems'>
              <!-- CARD -->
              <b:if cond='data:post.firstImageUrl'>
                <a class='post-thumb' expr:href='data:post.url' expr:title='data:post.title'>
                  <img expr:alt='data:post.title' expr:src='data:post.firstImageUrl' loading='lazy'/>
                  <b:if cond='data:post.labels any'>
                    <b:loop index='i' values='data:post.labels' var='label'>
                      <b:if cond='data:i == 0'><span class='sb-badge'><data:label.name/></span></b:if>
                    </b:loop>
                  </b:if>
                </a>
              </b:if>
              <div class='sb-card-body'>
                <b:if cond='!data:post.firstImageUrl and data:post.labels any'>
                  <div>
                    <b:loop index='i' values='data:post.labels' var='label'>
                      <b:if cond='data:i == 0'><a class='sb-badge' expr:href='data:label.url'><data:label.name/></a></b:if>
                    </b:loop>
                  </div>
                </b:if>
                <h3 class='post-title entry-title'>
                  <a expr:href='data:post.url'><data:post.title/></a>
                </h3>
                <p class='post-snippet'>
                  <b:if cond='data:post.snippets.short'><data:post.snippets.short/><b:else/><data:post.snippet/></b:if>
                </p>
                <div class='sb-meta'>
                  <span><data:post.author.name/></span>
                  <span><data:post.date/></span>
                  <span class='js-read'>4 min</span>
                </div>
                <div class='sb-card-foot'>
                  <a class='sb-explore' expr:href='data:post.url'>Explore →</a>
                  <b:if cond='data:post.allowComments'>
                    <a expr:href='data:post.url + &quot;#comments&quot;'><data:post.numberOfComments/></a>
                  </b:if>
                </div>
                <b:include data='post' name='postQuickEdit'/>
              </div>
            <b:else/>
              <!-- SINGLE -->
              <div class='sb-article'>
                <nav class='sb-crumb' aria-label='Breadcrumb'>
                  <a expr:href='data:blog.homepageUrl'>Home</a>
                  <span>/</span>
                  <b:if cond='data:post.labels any'>
                    <b:loop index='i' values='data:post.labels' var='label'>
                      <b:if cond='data:i == 0'><a expr:href='data:label.url'><data:label.name/></a></b:if>
                    </b:loop>
                    <span>/</span>
                  </b:if>
                  <span><data:post.title/></span>
                </nav>
                <h1 class='sb-article-title post-title entry-title'><data:post.title/></h1>
                <div class='sb-meta'>
                  <span><data:post.author.name/></span>
                  <time><data:post.date/></time>
                  <span data-readtime='.post-body'>4 min read</span>
                  <b:if cond='data:post.allowComments'>
                    <a expr:href='data:post.url + &quot;#comments&quot;'><data:post.numberOfComments/> comments</a>
                  </b:if>
                </div>
                <b:if cond='data:post.firstImageUrl'>
                  <div class='sb-feat'>
                    <img expr:alt='data:post.title' expr:src='data:post.firstImageUrl'/>
                  </div>
                </b:if>
                <div class='sb-toc'>
                  <strong data-action='toc'>Table of contents <span>▾</span></strong>
                  <ol id='sb-toc-list'/>
                </div>
                <div class='post-body entry-content'>
                  <data:post.body/>
                </div>
                <b:if cond='data:post.labels any'>
                  <div class='sb-tags'>
                    <b:loop values='data:post.labels' var='label'>
                      <a expr:href='data:label.url' rel='tag'><data:label.name/></a>
                    </b:loop>
                  </div>
                </b:if>
                <div class='sb-share'>
                  <span>Share</span>
                  <a data-share='fb' href='#' rel='nofollow' title='Facebook'>f</a>
                  <a data-share='tw' href='#' rel='nofollow' title='X'>𝕏</a>
                  <a data-share='wa' href='#' rel='nofollow' title='WhatsApp'>W</a>
                  <a data-share='li' href='#' rel='nofollow' title='LinkedIn'>in</a>
                  <a data-share='tg' href='#' rel='nofollow' title='Telegram'>✈</a>
                  <button data-share='copy' title='Copy link' type='button'>⧉</button>
                </div>
                <div class='sb-author'>
                  <b:if cond='data:post.author.authorPhoto.image'>
                    <img alt='Author' expr:src='data:post.author.authorPhoto.image'/>
                  <b:else/>
                    <img alt='Author' src='https://www.blogger.com/img/blogger_logo_round_35.png'/>
                  </b:if>
                  <div>
                    <h4><data:post.author.name/></h4>
                    <p>Sharing practical skill tutorials so you can learn more, pay less, and earn more.</p>
                  </div>
                </div>
                <div class='sb-related'>
                  <h3>Related lessons</h3>
                  <div class='sb-related-grid' id='sb-related'>
                    <b:attr expr:value='data:post.url' name='data-current'/>
                    <b:if cond='data:post.labels any'>
                      <b:loop index='i' values='data:post.labels' var='label'>
                        <b:if cond='data:i == 0'><b:attr expr:value='data:label.name' name='data-label'/></b:if>
                      </b:loop>
                    </b:if>
                  </div>
                </div>
                <b:if cond='data:view.isPost and data:post.allowComments'>
                  <section class='comments' id='comments'>
                    <h3 class='title'><data:post.numberOfComments/> Comments</h3>
                    <div class='comments-content'>
                      <b:loop values='data:post.comments' var='comment'>
                        <article class='comment-block'>
                          <b:attr expr:value='data:comment.markerId' name='id'/>
                          <strong><data:comment.author/></strong>
                          <div class='sb-meta'><data:comment.timestamp/></div>
                          <div><data:comment.body/></div>
                        </article>
                      </b:loop>
                    </div>
                    <div class='comment-form'>
                      <h4>Leave a comment</h4>
                      <b:if cond='data:post.commentFormIframeSrc'>
                        <iframe allowtransparency='true' class='blogger-iframe-colorize blogger-comment-from-post' expr:src='data:post.commentFormIframeSrc' frameborder='0' height='290' id='comment-editor' src='' width='100%'/>
                      </b:if>
                    </div>
                  </section>
                </b:if>
                <b:include data='post' name='postQuickEdit'/>
              </div>
            </b:if>
          </b:includable>

          <b:includable id='nextprev'>
            <div class='blog-pager' id='blog-pager'>
              <b:if cond='data:newerPageUrl'>
                <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:messages.newerPosts'><data:messages.newerPosts/></a>
              </b:if>
              <b:if cond='data:olderPageUrl'>
                <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:messages.olderPosts'><data:messages.olderPosts/></a>
              </b:if>
              <a class='home-link' expr:href='data:blog.homepageUrl'><data:messages.home/></a>
            </div>
          </b:includable>

          <b:includable id='feedLinks'>
            <b:if cond='data:feedLinks'>
              <div class='blog-feeds' style='display:none'>
                <b:loop values='data:feedLinks' var='f'><a expr:href='data:f.url'><data:f.name/></a></b:loop>
              </div>
            </b:if>
          </b:includable>

          <b:includable id='status-message'>
            <b:if cond='data:navMessage'>
              <div class='sb-section-head'>
                <p><data:navMessage/></p>
              </div>
            </b:if>
          </b:includable>

          <b:includable id='postQuickEdit' var='post'>
            <b:if cond='data:post.editUrl'>
              <span class='quickedit item-control'><a expr:href='data:post.editUrl' target='_blank'>Edit</a></span>
            </b:if>
          </b:includable>

          <b:includable id='commentDeleteIcon' var='comment'/>
          <b:includable id='backlinkDeleteIcon' var='backlink'/>
          <b:includable id='iframe_share'/>
          <b:includable id='shareButtons' var='post'/>
        </b:widget>
      </b:section>
    </main>

    <aside class='sb-sidebar' id='sidebar'>
      <b:section class='sidebar' id='sidebar-right' name='Sidebar' preferred='yes' showaddelement='yes'>
        <b:widget id='BlogSearch1' locked='false' title='Search lessons' type='BlogSearch' version='2' visible='true'/>

        <b:widget id='PopularPosts1' locked='false' title='Popular lessons' type='PopularPosts' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='numItemsToShow'>5</b:widget-setting>
            <b:widget-setting name='showThumbnails'>true</b:widget-setting>
            <b:widget-setting name='showSnippets'>true</b:widget-setting>
          </b:widget-settings>
        </b:widget>

        <b:widget id='Label1' locked='false' title='Skill tracks' type='Label' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
            <b:widget-setting name='display'>CLOUD</b:widget-setting>
            <b:widget-setting name='selectedLabelsList'/>
            <b:widget-setting name='showType'>ALL</b:widget-setting>
            <b:widget-setting name='showFreqNumbers'>true</b:widget-setting>
          </b:widget-settings>
        </b:widget>

        <b:widget id='BlogArchive1' locked='false' title='Archive' type='BlogArchive' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='style'>FLAT</b:widget-setting>
            <b:widget-setting name='showWeekEnd'>true</b:widget-setting>
            <b:widget-setting name='titleText'>Archive</b:widget-setting>
          </b:widget-settings>
        </b:widget>

        <b:widget id='Profile1' locked='false' title='About the author' type='Profile' version='2' visible='true'/>

        <b:widget id='FollowByEmail1' locked='false' title='Get new lessons' type='FollowByEmail' version='2' visible='true'/>

        <b:widget id='HTML1' locked='false' title='Sidebar Ad' type='HTML' version='2' visible='true'>
          <b:widget-settings>
            <b:widget-setting name='content'><![CDATA[<div class="sb-ad">Your Ad / Affiliate slot</div>]]></b:widget-setting>
          </b:widget-settings>
        </b:widget>
      </b:section>
    </aside>
  </div>

  <!-- ===== WHY / STATS / NEWSLETTER ===== -->
  <section class='sb-section sb-why'>
    <div class='container'>
      <div class='sb-section-head'>
        <h2>Why choose this blog?</h2>
        <p>Built like SkillCourse — practical skills, clear teaching, and career-first content.</p>
      </div>
      <div class='sb-why-grid'>
        <div class='sb-why-card'><div class='ico'>🎓</div><h3>Expert educators</h3><p>Lessons structured the way working professionals actually learn tools.</p></div>
        <div class='sb-why-card'><div class='ico'>⏱️</div><h3>Learn anytime</h3><p>Short, searchable posts you can finish on a break and apply the same day.</p></div>
        <div class='sb-why-card'><div class='ico'>🛠️</div><h3>Practical skills</h3><p>Real examples from Excel, Power BI, SQL, Python and AI analysis.</p></div>
        <div class='sb-why-card'><div class='ico'>🏅</div><h3>Career focused</h3><p>Every article aims at better jobs, promotions and confident interviews.</p></div>
      </div>
    </div>
  </section>

  <section class='sb-stats'>
    <div class='container'>
      <div class='sb-stat'><b data-count='2.5' data-suf='M+'>2.5M+</b><span>Learners inspired</span></div>
      <div class='sb-stat'><b data-count='100' data-suf='k+'>100k+</b><span>Premium members</span></div>
      <div class='sb-stat'><b data-count='25' data-suf='+'>25+</b><span>Skill tracks</span></div>
      <div class='sb-stat'><b data-count='5000' data-suf='+'>5000+</b><span>Learning minutes</span></div>
    </div>
  </section>

  <section class='sb-news'>
    <div class='container'>
      <div class='sb-news-box'>
        <div>
          <h2>Want to learn live?</h2>
          <p>Get roadmaps, case studies and new-skill alerts. Stay updated — that is how you secure your future.</p>
        </div>
        <form action='https://feedburner.google.com/fb/a/mailverify' method='post' target='_blank'>
          <input name='email' placeholder='Enter your email' required='required' type='email'/>
          <button type='submit'>Get notified</button>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer class='sb-footer'>
    <div class='container sb-foot-grid'>
      <div>
        <a class='sb-logo' expr:href='data:blog.homepageUrl' style='color:#fff'>
          <span class='sb-logo-mark'>@@ICON_CAP@@</span>
          <span><data:blog.title/></span>
        </a>
        <p>Job-oriented skill articles at an affordable learning curve. Enhance your professional capabilities and open doors to high-paying work.</p>
        <div class='sb-social'>
          <a expr:href='data:blog.homepageUrl' rel='noopener' title='Home'>⌂</a>
          <a href='https://www.youtube.com/' rel='noopener' target='_blank' title='YouTube'>▶</a>
          <a href='https://www.instagram.com/' rel='noopener' target='_blank' title='Instagram'>◎</a>
          <a href='https://www.linkedin.com/' rel='noopener' target='_blank' title='LinkedIn'>in</a>
          <a href='https://t.me/' rel='noopener' target='_blank' title='Telegram'>✈</a>
        </div>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a expr:href='data:blog.homepageUrl'>Home</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/about.html&quot;'>About</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/courses.html&quot;'>Courses</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;search/label/Excel&quot;'>Excel</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;search/label/Power%20BI&quot;'>Power BI</a></li>
        </ul>
      </div>
      <div>
        <h4>Resources</h4>
        <ul>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/privacy.html&quot;'>Privacy Policy</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/disclaimer.html&quot;'>Disclaimer</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/contact.html&quot;'>Contact</a></li>
          <li><a expr:href='data:blog.homepageUrl + &quot;p/terms.html&quot;'>Terms</a></li>
        </ul>
        <b:section id='footer-links' maxwidgets='1' name='Footer Links' showaddelement='yes'>
          <b:widget id='LinkList1' locked='false' title='' type='LinkList' version='2' visible='true'/>
        </b:section>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>Email: hello@yourblog.com</li>
          <li>Learn more. Earn more.</li>
        </ul>
        <b:section id='footer-extra' maxwidgets='1' name='Footer Extra' showaddelement='yes'>
          <b:widget id='Attribution1' locked='true' title='' type='Attribution' version='2' visible='true'/>
        </b:section>
      </div>
    </div>
    <div class='container sb-copy'>
      <span>© <span data-year='1'>2026</span> <data:blog.title/>. All rights reserved.</span>
      <span>Theme: SkillBlog Pro · Inspired by SkillCourse</span>
    </div>
  </footer>

  <!-- Hidden required / extra gadgets -->
  <div style='display:none'>
    <b:section id='hidden' maxwidgets='3' name='Hidden' showaddelement='yes'>
      <b:widget id='Header1' locked='true' title='SkillBlog' type='Header' version='2' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='displayUrl'/>
          <b:widget-setting name='displayHeight'>0</b:widget-setting>
          <b:widget-setting name='sectionWidth'>0</b:widget-setting>
          <b:widget-setting name='useImage'>false</b:widget-setting>
          <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'><b:include name='content'/></b:includable>
        <b:includable id='content'><div class='header-widget'><h1><data:title/></h1></div></b:includable>
      </b:widget>
      <b:widget id='ReportAbuse1' locked='false' title='' type='ReportAbuse' version='2' visible='true'>
        <b:includable id='main'><b:include name='content'/></b:includable>
        <b:includable id='content'><data:messages.reportAbuse/></b:includable>
      </b:widget>
    </b:section>
  </div>

  <button class='sb-top' title='Back to top' type='button' aria-label='Back to top'>↑</button>
  <a class='sb-wa' href='https://wa.me/' rel='noopener' target='_blank' title='Chat on WhatsApp' aria-label='WhatsApp'>
    <svg fill='currentColor' height='22' viewBox='0 0 24 24' width='22'><path d='M20.5 3.5A11 11 0 0 0 2.1 16.8L1 23l6.4-1.1A11 11 0 0 0 20.5 3.5zM12 20.4a8.4 8.4 0 0 1-4.3-1.2l-.3-.2-3.8.7.7-3.7-.2-.3A8.4 8.4 0 1 1 12 20.4zm4.6-6.3c-.2-.1-1.4-.7-1.6-.8s-.4-.1-.5.1-.6.8-.8 1-.3.2-.5.1a6.9 6.9 0 0 1-2-1.2 7.6 7.6 0 0 1-1.4-1.7c-.1-.3 0-.4.1-.5l.4-.4.1-.3c0-.1 0-.3 0-.4s-.5-1.3-.7-1.8-.4-.4-.5-.4h-.4c-.1 0-.4.1-.6.3s-.8.8-.8 1.9.8 2.2.9 2.3 1.6 2.5 3.9 3.4c.5.2 1 .4 1.3.5.6.2 1.1.2 1.5.1.5-.1 1.4-.6 1.6-1.1s.2-1 .1-1.1-.2-.2-.4-.3z'/></svg>
  </a>
  <div class='sb-cookie'>
    <p>We use cookies to improve your learning experience and remember theme preference.</p>
    <button data-action='cookie' type='button'>Accept</button>
  </div>
  <div class='sb-lite'><img alt='Preview' src=''/></div>

  <script type='text/javascript'>
//<![CDATA[
@@JS@@
//]]>
  </script>
</body>
</html>
"""

def main():
    out = ROOT / "myblog.xml"
    text = (
        xml()
        .replace("@@VARS@@", VARS)
        .replace("@@CSS@@", CSS)
        .replace("@@JS@@", JS)
        .replace("@@ICON_CAP@@", ICON_CAP)
    )
    if "]]>" in CSS or "]]>" in JS:
        raise SystemExit("CDATA closer found in CSS/JS")
    out.write_text(text, encoding="utf-8")
    print("Wrote %s (%s bytes, %s lines)" % (out, out.stat().st_size, text.count("\n") + 1))


if __name__ == "__main__":
    main()
