from shopee_crawler import ShopeeCrawler
import time

def main() -> None:
    crawler = ShopeeCrawler()
    crawler.search('ID', 'iPhone')
    time.sleep(2)
    first_page_results = crawler.get_search_results()
    print(first_page_results)
    crawler.next_page()
    time.sleep(2)
    second_page_results = crawler.get_search_results()
    print(second_page_results)

if __name__ == '__main__':
    main()