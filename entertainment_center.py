from media import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story","Em um mundo onde os brinquedos são seres vivos que fingem não ter vida quando os humanos estão olhando.","https://upload.wikimedia.org/wikipedia/pt/thumb/d/dc/Movie_poster_toy_story.jpg/250px-Movie_poster_toy_story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = Movie("Avatar", "A marine on a alien planet","https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=6ziBFh3V1aM")

spider_man = Movie("Spider-man","High-school senior Peter Parker, a school outcast, lives with his aunt May and his uncle Ben. On a school field trip, he visits an Oscorp genetics laboratory with his friend Harry Osborn and his love interest Mary Jane Watson. Peter is then bitten by a genetically engineered 'radioactive spider', one of the laboratory's experiments","https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Spider-Man2002Poster.jpg/220px-Spider-Man2002Poster.jpg","https://www.youtube.com/watch?v=AiwOet6QfgU")

intestellar = Movie("Interstellar","In the mid-21st century, crop blights and dust storms threaten humanity's survival. Joseph Cooper, a widowed engineer and former NASA pilot, runs a farm with his father-in-law Donald, son Tom, and daughter Murph.","https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg","https://www.youtube.com/watch?v=zSWdZVtXT7E")

deadpool = Movie("Deadpool 2","After successfully working as the mercenary Deadpool for two years, Wade Wilson fails to kill one of his targets on his anniversary with Vanessa, his girlfriend. That night, after the pair decide to start a family together, the target tracks Wilson down and kills Vanessa.","http://t2.gstatic.com/images?q=tbn:ANd9GcQdkAManFPMdW8FueyMO6lIMovZ1eeIdzla-JtsQtmhk6PPyYxS","https://www.youtube.com/watch?v=1P9OzWX6nzE")

fantastic_beasts = Movie("Fantastic Beasts: The Crimes of Grindelwald","In 1927, the Magical Congress of the United States of America (MACUSA) is transferring the powerful dark wizard Gellert Grindelwald from their maximum security prison to London to be tried for his crimes in Europe. Grindelwald escapes during the transfer, aided by his follower and MACUSA employee, Abernathy.","https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Fantastic_Beasts_-_The_Crimes_of_Grindelwald_Poster.png/220px-Fantastic_Beasts_-_The_Crimes_of_Grindelwald_Poster.png","https://www.youtube.com/watch?v=8bYBOVWLNIs")

movies = [toy_story,avatar,spider_man,intestellar,fantastic_beasts,deadpool]

fresh_tomatoes.open_movies_page(movies)
