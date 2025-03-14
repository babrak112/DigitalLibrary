# Project Digital library

## Project description

Funkcionalita:

- `Zoznam knih`(ISBN, zaner, jazyk, 
pocet stran/format, datum vydani, nakladatel, popis, 
vazba - tvrda, makka, ebok, hmotnost, preklad, hodnotenie)

- `detail knihy`
  - `zoradenie knih:`
  - `podla nazvu`
  - `datum vydania`
  - `podla hodnotenia`
  - `podla stran`
    
- `filtrovanie knih:`
  - `podla zanru`
  - `podla povodu`
  - `podla autora`
  - `podla hodnotenie`
  - `podla preklad`
  - `podla ceny`
  
  - `hodnotenie knih - good to have`
  - `vkladanie, editacia a mazanie knih`
      - `formular`
      - `na základe práv uzivatelov`
  - `vkladanie, editacia a mazanie autorov`
      - `formular`
      - `na základe práv uzivatelov`
  - `informacie o autoroch`
  - `vyhladavanie`
  - `velmi nahodne odporucanie knih - good to have`
  
## Databáze

### Modely
- [] genre
  - [] name
  - [] books -> ManyToMany(book)
- [] user
  - [] username
  - [] first_name
  - [] last_name
  - [] password
  - [] email
  - [] phone number (CZ)
- [] review
  - [] comment
  - [] rating
  - [] recommendation
  - [] reviewer -> ForeignKey(Profile)
  - [] book -> ForeignKey(book)
- [] country
  - [] name
  - [] books -> ManyToMany(book)
- [] author
  - [] first_name
  - [] surname
  - [] date_of_birth
  - [] date_of_death
  - [] country -> ForeignKey(country)
  - [] author -> ManyToMany(book) - ktore knihy napisal
  - [] biography (opis zivota)
- [] book
  - [] title_orig
  - [] title_cz
  - [] author -> ManyToMany(book)
  - [] ISBN
  - [] genre
  - [] language (original)
  - [] number of pages
  - [] format
  - [] year of publish
  - [] publisher
  - [] description
  - [] book case
  - [] weight
  - [] review
  - [] cover
  - [] where to buy (good to have, heureka api - https://sluzby.heureka.cz/napoveda/marketplace-api/ pomoc od Petra)
  


