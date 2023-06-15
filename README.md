# Aplikacja Lista Zadań

# Spis Treści
* [Opis aplikacji](#opis-aplikacji)
* [Technologie](#technologie)
* [Wymagania funkcjonalne](#wymagania-funkcjonalne)
* [Wymagania niefunkcjonalne](#wymagania-niefunkcjonalne)
* [Struktura bazy danych](#struktura-bazy-danych)
* [Autor](#autor)


## Opis aplikacji
Celem aplikacji jest ułatwienie użytkownikowi prowadzenia listy zadań z możliwością
zaznaczania ich jako wykonane, usuwanie i oczywiście dodawania nowych. Każde zadanie
składa się z tytułu, opisu, daty oraz statusu.


## Technologie
Aplikacja została zrealizowana w języku <b>Python 3.10</b>
przy użyciu frameworka <b>Django 4.2</b>, a dane
są przechowywane w bazie <b>PostgreSQL 14</b>.


## Wymagania funkcjonalne
* <b>Dodawanie nowych zadań</b>
* <b>Usuwanie zadań</b>
* <b>Zmiana statusu zadań</b>
* <b>Szybki podgląd każdego aspektu zadania</b>
* <b>System nie wysyła żadnych informacji do internetu</b>


## Wymagania niefunkcjonalne
* <b>Performance</b> - aplikacja działając lokalnie, nie potrzebuje dużych zasobów mocy obliczeniowej
by wykonywać swoje zadania z bardzo dużą prędkością
* <b>Dostępność</b> - z racji działania aplikacji lokalnie, nie jest potrzebne połączenie z internetem
aby aplikacja działała poprawnie


## Struktura bazy danych
Ze względu na prostotę aplikacji, jedyną customową tabelą jest tabela z zadaniami wytworzonymi przez użytkownika.
Prezentuje się ona następująco

| id     | title   | details | date | is_done |
|--------|---------|---------| --- |---------|
| bigint | charvar | text | date | boolean |

Reszta kolumn została automatycznie wytworzona przez framework Django z tego powodu nie warto ich prezentować,
ponieważ nie mają wpływu na aplikację w aktualnej formie.


## Autor
Wojciech Batorski