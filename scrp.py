from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'panda_images'})
google_crawler.crawl(
    keyword='panda',
    max_num=1000,
    min_size=(200,200),
    file_idx_offset=0
)
