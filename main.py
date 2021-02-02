from infos_to_files import save_book_data_to_csvfile, save_images_to_file, urlSite
from scraping_urls import get_category_links
from tqdm import tqdm


if __name__ == "__main__":
    # fonction qui parcours les catégories
    for category_url in tqdm(get_category_links(urlSite)):
        save_book_data_to_csvfile(category_url)
        save_images_to_file(category_url)
