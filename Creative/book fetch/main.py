import requests
from bs4 import BeautifulSoup
import html5lib

class GetBook():
    def __init__(self, link, chapters=100000000):
        self.next_link = link
        self.chapters = chapters
        self.next_chapter = ' '
        self.fetch()

    def get_heading(self, soup):
        self.book_name = soup.find('header', class_='header').find('h1').find('span').find('a').text
        self.chapter_name = soup.find('div', id='divContent').find('h3').text
    
    def get_content(self, soup):
        text_div = soup.find('div', id='bookContent')
        self.content = text_div.text.replace(r'(adsbygoogle = window.adsbygoogle || []).push({});','').replace('章节缺失、错误举报','').replace('www.uukanshu.com','').split()
    
    def get_link(self,soup):
        self.next_chapter = soup.find('a', id='read_next')
        if self.next_chapter:
            self.next_link = 'https://sj.uukanshu.com/'+self.next_chapter['href']

    def print_heading(self):
        print(self.book_name)
        print(self.chapter_name)
        print(f'本章链接: {self.current_link}\n')
    
    def save_content(self):
        with open(f"{' '.join(self.chapter_name.split())}.txt", 'w') as f:
            f.write(self.book_name+'   ')
            f.write(self.chapter_name+'   ')
            f.write(f'本章链接: {self.current_link}')
            f.write('\n\n\n\n')
            for i in self.content:
                f.write(i)
                f.write('\n\n')

    def conclude(self, saved_chapters):
        if saved_chapters == self.chapters:
            print('---------------------------------')
            print(f'Saved a total of {saved_chapters} chapters.')
            print('---------------------------------')
        else:
            print('---------------------------------')
            print('End of book')
            print(f'Saved a total of {saved_chapters} chapters.')
            print('---------------------------------')
        exit()

    def fetch(self):
        saved_chapters = 0
        for i in range(self.chapters):
            if self.next_chapter:
                page = requests.get(self.next_link)
                soup = BeautifulSoup(page.content, 'html5lib')
                self.current_link = self.next_link

                self.get_heading(soup)
                self.get_content(soup)
                self.get_link(soup)
                
                if list(self.chapter_name)[0] == '第':
                    self.print_heading()
                    self.save_content()
                    saved_chapters += 1
                    
        self.conclude(saved_chapters)


if __name__ == '__main__':
    book = GetBook(link='https://sj.uukanshu.com/read.aspx?tid=559&sid=13573', chapters=20)