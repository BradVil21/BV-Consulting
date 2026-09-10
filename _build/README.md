# Site build source

The public site is generated from these Python files. You don't need to use them to edit the site
(you can edit the HTML directly), but they make big changes fast and consistent.

```bash
cd _build
pip3 install pillow        # one time
python3 images.py          # compress photos in _build/src-images/ into AVIF, WebP & JPEG (480/800/1200px)
python3 build.py           # regenerate every page, sitemap.xml, robots.txt
```

- `common.py`: business info, services, header/footer, schema, image helper
- `page_home.py`, `page_services.py`, `page_other.py`: page content
- `posts_meta.py`, `posts_a.py`, `posts_b.py`: blog posts
- `base.css`, `add.css`, `add2.css`: combined into `/styles.css`

Note: editing a generated HTML file directly and then running `build.py` will overwrite that edit.
