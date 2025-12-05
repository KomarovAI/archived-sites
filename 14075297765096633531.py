import os,psycopg2,re
from pathlib import Path
from urllib.parse import urlparse,unquote
print("\n## EXPORT SITE FROM DB")
c=psycopg2.connect(host='postgres',database='kestra',user='kestra',password='k3str4_s3cr3t')
cur=c.cursor()
site='site1123123124124124'
target='.'
inc_assets='true'.lower()=='true'
site_dir=Path(target)/site if target!='.'else Path(site)
site_dir.mkdir(parents=True,exist_ok=True)
cur.execute("SELECT COUNT(*)FROM archived_pages WHERE site_name=%s",(site,))
pg_cnt=cur.fetchone()[0]
if pg_cnt==0:print(f"ERROR: No pages found for site '{site}'");cur.close();c.close();exit(1)
print(f"Site: {site} | Pages: {pg_cnt}")
cur.execute("SELECT url,html_content FROM archived_pages WHERE site_name=%s",(site,))
for url,html in cur.fetchall():
    parsed=urlparse(url)
    path=unquote(parsed.path).strip('/')or'index.html'
    if not path.endswith(('.html','.htm')):path+='.html'if not'.'in Path(path).name else''
    fp=site_dir/path
    fp.parent.mkdir(parents=True,exist_ok=True)
    fp.write_text(html,encoding='utf-8')
print(f"✅ Exported {pg_cnt} pages")
if inc_assets:
    cur.execute("SELECT COUNT(*)FROM archived_assets WHERE site_name=%s",(site,))
    as_cnt=cur.fetchone()[0]
    if as_cnt>0:
        print(f"Assets: {as_cnt}")
        cur.execute("SELECT asset_url,content,local_path FROM archived_assets WHERE site_name=%s",(site,))
        for url,content,lp in cur.fetchall():
            if lp:ap=site_dir/lp.lstrip('/')
            else:
                parsed=urlparse(url)
                ap=site_dir/unquote(parsed.path).strip('/')
            ap.parent.mkdir(parents=True,exist_ok=True)
            ap.write_bytes(bytes(content))
        print(f"✅ Exported {as_cnt} assets")
    else:print("⚠️  No assets found")
else:print("Assets: SKIP")
cur.close();c.close()
print(f"\nExported to: {site_dir}")
