-- Создание таблиц
create table author
	(
	id int primary key,
	first_name varchar(50),
	last_name varchar(50)
	);

create table genre
	(
	id int primary key,
	name varchar(50)
	);

create table book
	(
	id int primary key,
	title varchar(70),
	publication_year int,
	author_id int,
	genre_id int,
	foreign key (author_id) references author(id) on delete cascade,
	foreign key (genre_id) references genre(id) on delete cascade
	);


-- Добавление данных в таблицы
insert into author(id, first_name, last_name)
values (1, 'Жюль', 'Верн'),
	(2, 'Борис', 'Васильев'),
	(3, 'Антон', 'Чехов'),
	(4, 'Лев', 'Толстой'),
	(5, 'Даниель', 'Дефо'),
	(6, 'Александр', 'Дюма'),
	(7, 'Александр', 'Пушкин');

insert into genre(id, name)
values (1, 'Комедия'),
	(2, 'Лирическое стихотворение'),
	(3, 'Мелодрама'),
	(4, 'Фантастика'),
	(5, 'Повесть'),
	(6, 'Поэма'),
	(7, 'Рассказ'),
	(8, 'Роман'),
	(9, 'Трагедия'),
	(10, 'Утопия'),
	(11, 'Эпопея'),
	(12, 'Драма');

insert into book(id, title, publication_year, author_id, genre_id)
values (1, 'Двадцать тысяч лье под водой', 1869, 1, 4),
	(2, 'А зори здесь тихие', 1969, 2, 12),
	(3, 'Воскресение', 1899, 4, 12),
	(4, 'Рассказы', 1885, 3, 7),
	(5, 'Дети капитана Гранта', 1868, 1, 4),
	(6, 'Робинзон Крузо', 1719, 5, 8),
	(7, 'Двадцать лет спустя', 1845, 6, 8),
	(8, 'Руслан и Людмила', 1820, 7, 8);



-- Редактирование данных в таблицах
update author
set first_name = 'Алекс'
where id = 7;

update genre
set name = 'Научная фантастика'
where name = 'Фантастика';

update book
set publication_year  = 1821
where title = 'Руслан и Людмила';


-- Удаление данных из таблиц
delete from author
where id = 7;

delete from genre
where name = 'Лирическое стихотворение';

delete from book
where title = 'Дети капитана Гранта';


-- Поиск книг по автору
select author.first_name as first_name,
	author.last_name as last_name,
	book.title as title
from author
inner join book on author.id = book.author_id
where author.first_name = 'Александр' and author.last_name = 'Дюма';


-- Поиск книг по жанру
select genre.name as genre_name,
	book.title as title,
	author.first_name as first_name,
	author.last_name  as last_name
from genre
inner join book on genre.id = book.genre_id
inner join author on author.id = book.author_id
where genre."name"  = 'Драма';


-- Поиск книг по жанру по частичному совпадению
select genre.name as genre_name,
	book.title as title,
	author.first_name as first_name,
	author.last_name  as last_name
from genre
inner join book on genre.id = book.genre_id
inner join author on author.id = book.author_id
where genre."name"  like '%Р%';


-- Поиск книг по имени автора по частичному совпадению
select author.first_name as first_name,
	author.last_name as last_name,
	book.title as title
from author
inner join book on author.id = book.author_id
where author.first_name like '%А%';


-- Поиск книг по частичному наименованию
select book.title as book,
	book.publication_year as publication_year,
	author.first_name as author_first_name,
	author.last_name as author_last_name
from book
inner join author on author.id = book.author_id
where book.title like '%Двадцать%';