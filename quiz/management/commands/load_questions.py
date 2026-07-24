from django.core.management.base import BaseCommand
from quiz.models import Question


QUESTIONS = [

    # =========================================================
    # FIFA WORLD CUP - 20 QUESTIONS
    # =========================================================

    {
        "question": "Which country won the 2010 FIFA World Cup?",
        "answer_a": "Brazil",
        "answer_b": "Germany",
        "answer_c": "Spain",
        "answer_d": "Netherlands",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Spain won its first FIFA World Cup in 2010, "
            "defeating the Netherlands 1–0 in the final."
        ),
    },

    {
        "question": "Who scored the winning goal in the 2010 FIFA World Cup final?",
        "answer_a": "David Villa",
        "answer_b": "Andres Iniesta",
        "answer_c": "Xavi",
        "answer_d": "Fernando Torres",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Andres Iniesta scored in the 116th minute "
            "to give Spain a 1–0 victory over the Netherlands."
        ),
    },

    {
        "question": "Which country has won the most FIFA World Cup titles?",
        "answer_a": "Germany",
        "answer_b": "Argentina",
        "answer_c": "Italy",
        "answer_d": "Brazil",
        "correct_answer": "D",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Brazil has won five FIFA World Cups: "
            "1958, 1962, 1970, 1994 and 2002."
        ),
    },

    {
        "question": "Which country hosted the first FIFA World Cup in 1930?",
        "answer_a": "Uruguay",
        "answer_b": "Brazil",
        "answer_c": "Italy",
        "answer_d": "Argentina",
        "correct_answer": "A",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Uruguay hosted and won the inaugural "
            "FIFA World Cup in 1930."
        ),
    },

    {
        "question": "Who scored the famous 'Hand of God' goal at the 1986 FIFA World Cup?",
        "answer_a": "Pele",
        "answer_b": "Diego Maradona",
        "answer_c": "Jorge Valdano",
        "answer_d": "Gary Lineker",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Diego Maradona scored the controversial goal "
            "against England in the 1986 quarter-final."
        ),
    },

    {
        "question": "Which African nation became the first to reach a FIFA World Cup semi-final?",
        "answer_a": "Cameroon",
        "answer_b": "Senegal",
        "answer_c": "Morocco",
        "answer_d": "Ghana",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Morocco became the first African nation to reach "
            "a World Cup semi-final at Qatar 2022."
        ),
    },

    {
        "question": "Who won the Golden Boot at the 2014 FIFA World Cup?",
        "answer_a": "Thomas Muller",
        "answer_b": "Lionel Messi",
        "answer_c": "Neymar",
        "answer_d": "James Rodriguez",
        "correct_answer": "D",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "James Rodriguez scored six goals for Colombia "
            "and won the 2014 World Cup Golden Boot."
        ),
    },

    {
        "question": "Which country won the 2022 FIFA World Cup?",
        "answer_a": "France",
        "answer_b": "Argentina",
        "answer_c": "Brazil",
        "answer_d": "Croatia",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Argentina defeated France on penalties after "
            "a dramatic 3–3 draw in the 2022 final."
        ),
    },

    {
        "question": "Who scored a hat-trick in the 2022 FIFA World Cup final?",
        "answer_a": "Lionel Messi",
        "answer_b": "Julian Alvarez",
        "answer_c": "Kylian Mbappe",
        "answer_d": "Antoine Griezmann",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Kylian Mbappe scored three goals for France "
            "in the 2022 World Cup final."
        ),
    },

    {
        "question": "Which nation won the FIFA World Cup in 1966?",
        "answer_a": "England",
        "answer_b": "West Germany",
        "answer_c": "Brazil",
        "answer_d": "Portugal",
        "correct_answer": "A",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "England won its first and so far only World Cup "
            "by defeating West Germany 4–2 after extra time."
        ),
    },

    {
        "question": "Who scored a hat-trick for England in the 1966 World Cup final?",
        "answer_a": "Bobby Charlton",
        "answer_b": "Geoff Hurst",
        "answer_c": "Roger Hunt",
        "answer_d": "Martin Peters",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Geoff Hurst became the first player to score "
            "a hat-trick in a men's World Cup final."
        ),
    },

    {
        "question": "Which country defeated Brazil 7–1 in the 2014 World Cup semi-final?",
        "answer_a": "Argentina",
        "answer_b": "Netherlands",
        "answer_c": "Germany",
        "answer_d": "France",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Germany defeated host nation Brazil 7–1 "
            "in Belo Horizonte in one of football's most famous results."
        ),
    },

    {
        "question": "Which player scored twice in the 1998 World Cup final as France defeated Brazil?",
        "answer_a": "Thierry Henry",
        "answer_b": "Zinedine Zidane",
        "answer_c": "David Trezeguet",
        "answer_d": "Youri Djorkaeff",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Zinedine Zidane scored two headed goals "
            "as France defeated Brazil 3–0."
        ),
    },

    {
        "question": "Which country won the 2006 FIFA World Cup?",
        "answer_a": "France",
        "answer_b": "Germany",
        "answer_c": "Italy",
        "answer_d": "Brazil",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Italy defeated France on penalties "
            "in the 2006 World Cup final in Berlin."
        ),
    },

    {
        "question": "Which player was sent off in the 2006 FIFA World Cup final?",
        "answer_a": "Marco Materazzi",
        "answer_b": "Zinedine Zidane",
        "answer_c": "Fabio Cannavaro",
        "answer_d": "Patrick Vieira",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Zinedine Zidane was sent off in extra time "
            "after headbutting Marco Materazzi."
        ),
    },

    {
        "question": "Which nation won the 1954 FIFA World Cup?",
        "answer_a": "Hungary",
        "answer_b": "Brazil",
        "answer_c": "West Germany",
        "answer_d": "Uruguay",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "hard",
        "explanation": (
            "West Germany defeated heavily favoured Hungary 3–2 "
            "in the final known as the Miracle of Bern."
        ),
    },

    {
        "question": "Which player scored the winning goal in the 2014 FIFA World Cup final?",
        "answer_a": "Mario Gotze",
        "answer_b": "Miroslav Klose",
        "answer_c": "Thomas Muller",
        "answer_d": "Andre Schurrle",
        "correct_answer": "A",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Mario Gotze scored in extra time as Germany "
            "defeated Argentina 1–0."
        ),
    },

    {
        "question": "Which country did Brazil defeat in the 2002 FIFA World Cup final?",
        "answer_a": "Italy",
        "answer_b": "Germany",
        "answer_c": "France",
        "answer_d": "Argentina",
        "correct_answer": "B",
        "category": "world_cup",
        "difficulty": "medium",
        "explanation": (
            "Brazil defeated Germany 2–0 in Yokohama, "
            "with Ronaldo scoring both goals."
        ),
    },

    {
        "question": "Who scored both goals for Brazil in the 2002 World Cup final?",
        "answer_a": "Rivaldo",
        "answer_b": "Ronaldinho",
        "answer_c": "Ronaldo Nazario",
        "answer_d": "Roberto Carlos",
        "correct_answer": "C",
        "category": "world_cup",
        "difficulty": "easy",
        "explanation": (
            "Ronaldo Nazario scored both goals in Brazil's "
            "2–0 victory over Germany."
        ),
    },

    {
        "question": "Which nation reached three consecutive World Cup finals from 1982 to 1990?",
        "answer_a": "Brazil",
        "answer_b": "Argentina",
        "answer_c": "Italy",
        "answer_d": "West Germany",
        "correct_answer": "D",
        "category": "world_cup",
        "difficulty": "hard",
        "explanation": (
            "West Germany reached the finals in 1982, 1986 and 1990, "
            "winning the tournament in 1990."
        ),
    },


    # =========================================================
    # CHAMPIONS LEAGUE & EUROPEAN CUP - 20 QUESTIONS
    # =========================================================

    {
        "question": "Which club has won the most European Cup and UEFA Champions League titles?",
        "answer_a": "AC Milan",
        "answer_b": "Real Madrid",
        "answer_c": "Liverpool",
        "answer_d": "Bayern Munich",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Real Madrid is the most successful club "
            "in European Cup and Champions League history."
        ),
    },

    {
        "question": "Which club completed the famous comeback against AC Milan in the 2005 Champions League final?",
        "answer_a": "Manchester United",
        "answer_b": "Barcelona",
        "answer_c": "Liverpool",
        "answer_d": "Chelsea",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Liverpool recovered from 3–0 down and defeated "
            "AC Milan on penalties in Istanbul."
        ),
    },

    {
        "question": "Who scored Real Madrid's famous bicycle kick against Juventus in the 2017–18 Champions League?",
        "answer_a": "Cristiano Ronaldo",
        "answer_b": "Gareth Bale",
        "answer_c": "Karim Benzema",
        "answer_d": "Sergio Ramos",
        "correct_answer": "A",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Cristiano Ronaldo scored a spectacular bicycle kick "
            "against Juventus in Turin in April 2018."
        ),
    },

    {
        "question": "Which club won the 1999 UEFA Champions League final after scoring twice in stoppage time?",
        "answer_a": "Bayern Munich",
        "answer_b": "Manchester United",
        "answer_c": "Juventus",
        "answer_d": "Real Madrid",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Manchester United defeated Bayern Munich 2–1 "
            "with late goals from Teddy Sheringham and Ole Gunnar Solskjaer."
        ),
    },

    {
        "question": "Which Romanian club won the European Cup in 1986?",
        "answer_a": "Dinamo Bucuresti",
        "answer_b": "Rapid Bucuresti",
        "answer_c": "Universitatea Craiova",
        "answer_d": "Steaua Bucuresti",
        "correct_answer": "D",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Steaua Bucuresti defeated Barcelona on penalties "
            "in the 1986 European Cup final."
        ),
    },

    {
        "question": "Which goalkeeper saved four penalties in the 1986 European Cup final shootout?",
        "answer_a": "Helmuth Duckadam",
        "answer_b": "Silviu Lung",
        "answer_c": "Walter Zenga",
        "answer_d": "Andoni Zubizarreta",
        "correct_answer": "A",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Helmuth Duckadam saved all four Barcelona penalties "
            "in the shootout."
        ),
    },

    {
        "question": "Which club won the first European Cup in 1956?",
        "answer_a": "Benfica",
        "answer_b": "Real Madrid",
        "answer_c": "AC Milan",
        "answer_d": "Reims",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Real Madrid defeated Reims 4–3 "
            "in the inaugural European Cup final."
        ),
    },

    {
        "question": "Which club won the 2012 UEFA Champions League final?",
        "answer_a": "Chelsea",
        "answer_b": "Bayern Munich",
        "answer_c": "Barcelona",
        "answer_d": "Real Madrid",
        "correct_answer": "A",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Chelsea defeated Bayern Munich on penalties "
            "at the Allianz Arena."
        ),
    },

    {
        "question": "Who scored Chelsea's equaliser in the 2012 Champions League final?",
        "answer_a": "Frank Lampard",
        "answer_b": "Fernando Torres",
        "answer_c": "Didier Drogba",
        "answer_d": "Juan Mata",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Didier Drogba headed in Chelsea's equaliser "
            "before scoring the winning penalty in the shootout."
        ),
    },

    {
        "question": "Which club won the 2010 UEFA Champions League under Jose Mourinho?",
        "answer_a": "Inter Milan",
        "answer_b": "Chelsea",
        "answer_c": "Real Madrid",
        "answer_d": "Porto",
        "correct_answer": "A",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Inter Milan defeated Bayern Munich 2–0 "
            "to complete a historic treble."
        ),
    },

    {
        "question": "Who scored both goals for Inter Milan in the 2010 Champions League final?",
        "answer_a": "Samuel Eto'o",
        "answer_b": "Wesley Sneijder",
        "answer_c": "Diego Milito",
        "answer_d": "Goran Pandev",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Diego Milito scored both goals "
            "in Inter's 2–0 victory over Bayern Munich."
        ),
    },

    {
        "question": "Which club defeated Manchester United in both the 2009 and 2011 Champions League finals?",
        "answer_a": "Real Madrid",
        "answer_b": "Barcelona",
        "answer_c": "Bayern Munich",
        "answer_d": "AC Milan",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Pep Guardiola's Barcelona defeated Manchester United "
            "in the 2009 and 2011 finals."
        ),
    },

    {
        "question": "Which player scored the decisive penalty for Real Madrid in the 2016 Champions League final shootout?",
        "answer_a": "Sergio Ramos",
        "answer_b": "Gareth Bale",
        "answer_c": "Cristiano Ronaldo",
        "answer_d": "Luka Modric",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Cristiano Ronaldo converted the decisive penalty "
            "against Atletico Madrid in Milan."
        ),
    },

    {
        "question": "Which club won the 1991 European Cup?",
        "answer_a": "Red Star Belgrade",
        "answer_b": "Marseille",
        "answer_c": "Benfica",
        "answer_d": "Barcelona",
        "correct_answer": "A",
        "category": "champions_league",
        "difficulty": "hard",
        "explanation": (
            "Red Star Belgrade defeated Marseille on penalties "
            "in the 1991 European Cup final."
        ),
    },

    {
        "question": "Which club won the 1993 UEFA Champions League?",
        "answer_a": "AC Milan",
        "answer_b": "Marseille",
        "answer_c": "Barcelona",
        "answer_d": "Juventus",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "hard",
        "explanation": (
            "Marseille defeated AC Milan 1–0 "
            "to become the first French club to win the competition."
        ),
    },

    {
        "question": "Which player scored the winning goal in the 1993 Champions League final?",
        "answer_a": "Didier Deschamps",
        "answer_b": "Rudi Voller",
        "answer_c": "Basile Boli",
        "answer_d": "Abedi Pele",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "hard",
        "explanation": (
            "Basile Boli scored the only goal "
            "as Marseille defeated AC Milan."
        ),
    },

    {
        "question": "Which club won the Champions League in 2004 under Jose Mourinho?",
        "answer_a": "Chelsea",
        "answer_b": "Porto",
        "answer_c": "Monaco",
        "answer_d": "Inter Milan",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Porto defeated Monaco 3–0 in the 2004 final "
            "under Jose Mourinho."
        ),
    },

    {
        "question": "Which club did Liverpool defeat in the 2019 Champions League final?",
        "answer_a": "Chelsea",
        "answer_b": "Tottenham Hotspur",
        "answer_c": "Manchester City",
        "answer_d": "Ajax",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "easy",
        "explanation": (
            "Liverpool defeated Tottenham Hotspur 2–0 "
            "in Madrid in the 2019 final."
        ),
    },

    {
        "question": "Who scored Liverpool's opening goal in the 2019 Champions League final?",
        "answer_a": "Sadio Mane",
        "answer_b": "Roberto Firmino",
        "answer_c": "Mohamed Salah",
        "answer_d": "Divock Origi",
        "correct_answer": "C",
        "category": "champions_league",
        "difficulty": "medium",
        "explanation": (
            "Mohamed Salah scored from the penalty spot "
            "in the second minute."
        ),
    },

    {
        "question": "Which club won the 1997 UEFA Champions League?",
        "answer_a": "Juventus",
        "answer_b": "Borussia Dortmund",
        "answer_c": "Ajax",
        "answer_d": "Manchester United",
        "correct_answer": "B",
        "category": "champions_league",
        "difficulty": "hard",
        "explanation": (
            "Borussia Dortmund defeated Juventus 3–1 "
            "in the 1997 final in Munich."
        ),
    },


    # =========================================================
    # PLAYERS & LEGENDS - 20 QUESTIONS
    # =========================================================

    {
        "question": "Which player won three FIFA World Cups with Brazil?",
        "answer_a": "Diego Maradona",
        "answer_b": "Pele",
        "answer_c": "Johan Cruyff",
        "answer_d": "Franz Beckenbauer",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Pele won the World Cup with Brazil "
            "in 1958, 1962 and 1970."
        ),
    },

    {
        "question": "Which player was nicknamed 'Der Kaiser'?",
        "answer_a": "Gerd Muller",
        "answer_b": "Lothar Matthaus",
        "answer_c": "Franz Beckenbauer",
        "answer_d": "Karl-Heinz Rummenigge",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "German legend Franz Beckenbauer "
            "was famously nicknamed 'Der Kaiser'."
        ),
    },

    {
        "question": "Which Romanian footballer was nicknamed 'The Maradona of the Carpathians'?",
        "answer_a": "Gheorghe Popescu",
        "answer_b": "Ilie Balaci",
        "answer_c": "Adrian Mutu",
        "answer_d": "Gheorghe Hagi",
        "correct_answer": "D",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Gheorghe Hagi became Romania's most internationally "
            "celebrated footballer."
        ),
    },

    {
        "question": "Which goalkeeper is the only goalkeeper to have won the Ballon d'Or?",
        "answer_a": "Gianluigi Buffon",
        "answer_b": "Lev Yashin",
        "answer_c": "Manuel Neuer",
        "answer_d": "Dino Zoff",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Lev Yashin won the Ballon d'Or in 1963."
        ),
    },

    {
        "question": "Which Dutch legend became the iconic figure associated with Total Football?",
        "answer_a": "Marco van Basten",
        "answer_b": "Ruud Gullit",
        "answer_c": "Johan Cruyff",
        "answer_d": "Dennis Bergkamp",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Johan Cruyff became the most famous player "
            "associated with Dutch Total Football."
        ),
    },

    {
        "question": "Which Brazilian striker was nicknamed 'O Fenomeno'?",
        "answer_a": "Ronaldinho",
        "answer_b": "Romario",
        "answer_c": "Rivaldo",
        "answer_d": "Ronaldo Nazario",
        "correct_answer": "D",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Ronaldo Nazario was widely known "
            "by the nickname 'O Fenomeno'."
        ),
    },

    {
        "question": "Which player was nicknamed 'The Divine Ponytail'?",
        "answer_a": "Roberto Baggio",
        "answer_b": "Andrea Pirlo",
        "answer_c": "Paolo Maldini",
        "answer_d": "Francesco Totti",
        "correct_answer": "A",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Italian legend Roberto Baggio "
            "was famously known as 'The Divine Ponytail'."
        ),
    },

    {
        "question": "Which French player was nicknamed 'King Eric' by Manchester United supporters?",
        "answer_a": "Thierry Henry",
        "answer_b": "Eric Cantona",
        "answer_c": "David Ginola",
        "answer_d": "Patrick Vieira",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Eric Cantona became an iconic figure "
            "at Manchester United during the 1990s."
        ),
    },

    {
        "question": "Which player spent the majority of his career at AC Milan and was famous as an elite defender?",
        "answer_a": "Paolo Maldini",
        "answer_b": "Fabio Cannavaro",
        "answer_c": "Alessandro Nesta",
        "answer_d": "Giorgio Chiellini",
        "correct_answer": "A",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Paolo Maldini spent his entire senior club career "
            "with AC Milan."
        ),
    },

    {
        "question": "Which player won the 2006 Ballon d'Or after captaining Italy to the World Cup title?",
        "answer_a": "Andrea Pirlo",
        "answer_b": "Gianluigi Buffon",
        "answer_c": "Fabio Cannavaro",
        "answer_d": "Francesco Totti",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Fabio Cannavaro won the 2006 Ballon d'Or "
            "after captaining Italy to World Cup glory."
        ),
    },

    {
        "question": "Which Liberian player won the Ballon d'Or in 1995?",
        "answer_a": "George Weah",
        "answer_b": "Abedi Pele",
        "answer_c": "Samuel Eto'o",
        "answer_d": "Didier Drogba",
        "correct_answer": "A",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "George Weah won the Ballon d'Or in 1995 "
            "and remains one of Africa's greatest footballers."
        ),
    },

    {
        "question": "Which player scored the famous 'Goal of the Century' against England in 1986?",
        "answer_a": "Gabriel Batistuta",
        "answer_b": "Diego Maradona",
        "answer_c": "Mario Kempes",
        "answer_d": "Claudio Caniggia",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Diego Maradona dribbled past several England players "
            "to score one of football's most celebrated goals."
        ),
    },

    {
        "question": "Which Portuguese player was known as the 'Black Panther'?",
        "answer_a": "Luis Figo",
        "answer_b": "Cristiano Ronaldo",
        "answer_c": "Eusebio",
        "answer_d": "Rui Costa",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Eusebio was nicknamed the 'Black Panther' "
            "and became one of Portugal's greatest players."
        ),
    },

    {
        "question": "Which midfielder scored France's two headed goals in the 1998 World Cup final?",
        "answer_a": "Didier Deschamps",
        "answer_b": "Zinedine Zidane",
        "answer_c": "Emmanuel Petit",
        "answer_d": "Youri Djorkaeff",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Zinedine Zidane scored twice from corners "
            "against Brazil in the 1998 final."
        ),
    },

    {
        "question": "Which player was famous for wearing number 10 for Napoli and Argentina?",
        "answer_a": "Diego Maradona",
        "answer_b": "Hernan Crespo",
        "answer_c": "Juan Roman Riquelme",
        "answer_d": "Javier Zanetti",
        "correct_answer": "A",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Diego Maradona became an icon at Napoli "
            "and with the Argentina national team."
        ),
    },

    {
        "question": "Which English midfielder was famous for his long-range goals and wore number 8 for Liverpool?",
        "answer_a": "Paul Scholes",
        "answer_b": "Frank Lampard",
        "answer_c": "Steven Gerrard",
        "answer_d": "David Beckham",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Steven Gerrard became one of Liverpool's greatest players "
            "and was famous for powerful long-range goals."
        ),
    },

    {
        "question": "Which Spanish goalkeeper captained Spain to the 2010 World Cup title?",
        "answer_a": "Victor Valdes",
        "answer_b": "Iker Casillas",
        "answer_c": "Pepe Reina",
        "answer_d": "David de Gea",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "easy",
        "explanation": (
            "Iker Casillas captained Spain during "
            "their historic 2010 World Cup triumph."
        ),
    },

    {
        "question": "Which midfielder was nicknamed 'Il Divin Codino' in Italian football?",
        "answer_a": "Roberto Baggio",
        "answer_b": "Andrea Pirlo",
        "answer_c": "Gianni Rivera",
        "answer_d": "Alessandro Del Piero",
        "correct_answer": "A",
        "category": "players",
        "difficulty": "hard",
        "explanation": (
            "'Il Divin Codino', meaning 'The Divine Ponytail', "
            "was Roberto Baggio's famous nickname."
        ),
    },

    {
        "question": "Which German striker was nicknamed 'Der Bomber'?",
        "answer_a": "Jurgen Klinsmann",
        "answer_b": "Miroslav Klose",
        "answer_c": "Gerd Muller",
        "answer_d": "Rudi Voller",
        "correct_answer": "C",
        "category": "players",
        "difficulty": "medium",
        "explanation": (
            "Gerd Muller was nicknamed 'Der Bomber' "
            "because of his extraordinary goalscoring ability."
        ),
    },

    {
        "question": "Which Italian goalkeeper captained Italy to the 1982 World Cup title at the age of 40?",
        "answer_a": "Walter Zenga",
        "answer_b": "Dino Zoff",
        "answer_c": "Gianluca Pagliuca",
        "answer_d": "Gianluigi Buffon",
        "correct_answer": "B",
        "category": "players",
        "difficulty": "hard",
        "explanation": (
            "Dino Zoff captained Italy to the 1982 World Cup "
            "at the age of 40."
        ),
    },


    # =========================================================
    # EUROPEAN CHAMPIONSHIP - 15 QUESTIONS
    # =========================================================

    {
        "question": "Which country won UEFA Euro 2004?",
        "answer_a": "Portugal",
        "answer_b": "Greece",
        "answer_c": "France",
        "answer_d": "Italy",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "easy",
        "explanation": (
            "Greece produced one of football's greatest surprises "
            "by winning Euro 2004."
        ),
    },

    {
        "question": "Which country won UEFA Euro 1992 after entering as a late replacement?",
        "answer_a": "Denmark",
        "answer_b": "Sweden",
        "answer_c": "Netherlands",
        "answer_d": "Germany",
        "correct_answer": "A",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Denmark entered after Yugoslavia was excluded "
            "and went on to win Euro 1992."
        ),
    },

    {
        "question": "Who scored the famous volley for the Netherlands in the Euro 1988 final?",
        "answer_a": "Ruud Gullit",
        "answer_b": "Frank Rijkaard",
        "answer_c": "Marco van Basten",
        "answer_d": "Ronald Koeman",
        "correct_answer": "C",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Marco van Basten scored a spectacular volley "
            "against the Soviet Union."
        ),
    },

    {
        "question": "Which country hosted UEFA Euro 2016?",
        "answer_a": "Germany",
        "answer_b": "France",
        "answer_c": "Portugal",
        "answer_d": "Poland",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "easy",
        "explanation": (
            "France hosted Euro 2016, which was won by Portugal."
        ),
    },

    {
        "question": "Which country won UEFA Euro 2016?",
        "answer_a": "France",
        "answer_b": "Spain",
        "answer_c": "Portugal",
        "answer_d": "Germany",
        "correct_answer": "C",
        "category": "euro",
        "difficulty": "easy",
        "explanation": (
            "Portugal defeated France 1–0 after extra time "
            "in the Euro 2016 final."
        ),
    },

    {
        "question": "Who scored Portugal's winning goal in the Euro 2016 final?",
        "answer_a": "Cristiano Ronaldo",
        "answer_b": "Nani",
        "answer_c": "Eder",
        "answer_d": "Ricardo Quaresma",
        "correct_answer": "C",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Eder scored the only goal of the final "
            "in extra time against France."
        ),
    },

    {
        "question": "Which country won both Euro 2008 and Euro 2012?",
        "answer_a": "Germany",
        "answer_b": "France",
        "answer_c": "Italy",
        "answer_d": "Spain",
        "correct_answer": "D",
        "category": "euro",
        "difficulty": "easy",
        "explanation": (
            "Spain won consecutive European Championships "
            "in 2008 and 2012."
        ),
    },

    {
        "question": "Which country did Spain defeat in the Euro 2012 final?",
        "answer_a": "Germany",
        "answer_b": "Italy",
        "answer_c": "Portugal",
        "answer_d": "France",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "easy",
        "explanation": (
            "Spain defeated Italy 4–0 in Kyiv "
            "in the Euro 2012 final."
        ),
    },

    {
        "question": "Which nation won the first European Championship in 1960?",
        "answer_a": "Soviet Union",
        "answer_b": "Spain",
        "answer_c": "West Germany",
        "answer_d": "Yugoslavia",
        "correct_answer": "A",
        "category": "euro",
        "difficulty": "hard",
        "explanation": (
            "The Soviet Union defeated Yugoslavia "
            "to win the inaugural European Championship."
        ),
    },

    {
        "question": "Which country won Euro 1996?",
        "answer_a": "Czech Republic",
        "answer_b": "Germany",
        "answer_c": "England",
        "answer_d": "France",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Germany defeated the Czech Republic "
            "in the Euro 1996 final."
        ),
    },

    {
        "question": "Who scored the golden goal in the Euro 1996 final?",
        "answer_a": "Jurgen Klinsmann",
        "answer_b": "Oliver Bierhoff",
        "answer_c": "Matthias Sammer",
        "answer_d": "Andreas Moller",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "hard",
        "explanation": (
            "Oliver Bierhoff scored the golden goal "
            "that gave Germany the Euro 1996 title."
        ),
    },

    {
        "question": "Which country won Euro 1984?",
        "answer_a": "Spain",
        "answer_b": "France",
        "answer_c": "West Germany",
        "answer_d": "Italy",
        "correct_answer": "B",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "France won Euro 1984 on home soil."
        ),
    },

    {
        "question": "Which French player scored nine goals at Euro 1984?",
        "answer_a": "Michel Platini",
        "answer_b": "Alain Giresse",
        "answer_c": "Jean Tigana",
        "answer_d": "Dominique Rocheteau",
        "correct_answer": "A",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Michel Platini scored nine goals in five matches "
            "as France won Euro 1984."
        ),
    },

    {
        "question": "Which country won Euro 1988?",
        "answer_a": "Soviet Union",
        "answer_b": "West Germany",
        "answer_c": "Netherlands",
        "answer_d": "Italy",
        "correct_answer": "C",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "The Netherlands defeated the Soviet Union 2–0 "
            "to win Euro 1988."
        ),
    },

    {
        "question": "Which country defeated Germany in the Euro 1992 final?",
        "answer_a": "Denmark",
        "answer_b": "Netherlands",
        "answer_c": "Sweden",
        "answer_d": "France",
        "correct_answer": "A",
        "category": "euro",
        "difficulty": "medium",
        "explanation": (
            "Denmark defeated Germany 2–0 "
            "to complete their remarkable Euro 1992 campaign."
        ),
    },


    # =========================================================
    # FOOTBALL CLUBS - 15 QUESTIONS
    # =========================================================

    {
        "question": "Which club plays its home matches at Anfield?",
        "answer_a": "Everton",
        "answer_b": "Arsenal",
        "answer_c": "Liverpool",
        "answer_d": "Manchester United",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Anfield has been Liverpool's home ground "
            "since the club's formation in 1892."
        ),
    },

    {
        "question": "Which club is traditionally known as 'The Old Lady'?",
        "answer_a": "Inter Milan",
        "answer_b": "Juventus",
        "answer_c": "AC Milan",
        "answer_d": "Roma",
        "correct_answer": "B",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Juventus is famously known as "
            "'La Vecchia Signora' or 'The Old Lady'."
        ),
    },

    {
        "question": "Which German club is commonly nicknamed 'Die Roten'?",
        "answer_a": "Borussia Dortmund",
        "answer_b": "Bayer Leverkusen",
        "answer_c": "Schalke 04",
        "answer_d": "Bayern Munich",
        "correct_answer": "D",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "Bayern Munich is commonly known as "
            "'Die Roten', meaning 'The Reds'."
        ),
    },

    {
        "question": "Which Spanish club plays its home matches at the Santiago Bernabeu?",
        "answer_a": "Atletico Madrid",
        "answer_b": "Barcelona",
        "answer_c": "Real Madrid",
        "answer_d": "Sevilla",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "The Santiago Bernabeu is the historic home "
            "of Real Madrid."
        ),
    },

    {
        "question": "Which club plays at Old Trafford?",
        "answer_a": "Manchester City",
        "answer_b": "Manchester United",
        "answer_c": "Liverpool",
        "answer_d": "Leeds United",
        "correct_answer": "B",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Old Trafford has been Manchester United's home "
            "since 1910."
        ),
    },

    {
        "question": "Which club is known as 'The Gunners'?",
        "answer_a": "Chelsea",
        "answer_b": "Tottenham Hotspur",
        "answer_c": "Arsenal",
        "answer_d": "West Ham United",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Arsenal is known as 'The Gunners', "
            "a reference to the club's historical origins."
        ),
    },

    {
        "question": "Which club is known as 'The Rossoneri'?",
        "answer_a": "AC Milan",
        "answer_b": "Inter Milan",
        "answer_c": "Roma",
        "answer_d": "Torino",
        "correct_answer": "A",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "'Rossoneri' means 'Red and Blacks' "
            "and is a famous nickname for AC Milan."
        ),
    },

    {
        "question": "Which club is known as 'The Nerazzurri'?",
        "answer_a": "Juventus",
        "answer_b": "Napoli",
        "answer_c": "Inter Milan",
        "answer_d": "Lazio",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "'Nerazzurri' refers to Inter Milan's "
            "traditional black and blue colours."
        ),
    },

    {
        "question": "Which club plays its home matches at Signal Iduna Park?",
        "answer_a": "Bayern Munich",
        "answer_b": "Borussia Dortmund",
        "answer_c": "RB Leipzig",
        "answer_d": "Schalke 04",
        "correct_answer": "B",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Signal Iduna Park is the home stadium "
            "of Borussia Dortmund."
        ),
    },

    {
        "question": "Which club is traditionally associated with the 'Yellow Wall'?",
        "answer_a": "Borussia Dortmund",
        "answer_b": "Celtic",
        "answer_c": "Feyenoord",
        "answer_d": "Galatasaray",
        "correct_answer": "A",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "Borussia Dortmund's famous south stand "
            "is known internationally as the Yellow Wall."
        ),
    },

    {
        "question": "Which Scottish club plays at Celtic Park?",
        "answer_a": "Rangers",
        "answer_b": "Aberdeen",
        "answer_c": "Celtic",
        "answer_d": "Hearts",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Celtic Park is the home stadium of Celtic FC "
            "in Glasgow."
        ),
    },

    {
        "question": "Which club plays its home matches at Stamford Bridge?",
        "answer_a": "Chelsea",
        "answer_b": "Fulham",
        "answer_c": "Arsenal",
        "answer_d": "Tottenham Hotspur",
        "correct_answer": "A",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "Stamford Bridge has been Chelsea's home "
            "since the club was founded in 1905."
        ),
    },

    {
        "question": "Which Portuguese club plays at the Estadio da Luz?",
        "answer_a": "Porto",
        "answer_b": "Sporting CP",
        "answer_c": "Braga",
        "answer_d": "Benfica",
        "correct_answer": "D",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "The Estadio da Luz in Lisbon "
            "is the home of Benfica."
        ),
    },

    {
        "question": "Which Dutch club plays at the Johan Cruyff Arena?",
        "answer_a": "PSV Eindhoven",
        "answer_b": "Ajax",
        "answer_c": "Feyenoord",
        "answer_d": "AZ Alkmaar",
        "correct_answer": "B",
        "category": "clubs",
        "difficulty": "easy",
        "explanation": (
            "The Johan Cruyff Arena in Amsterdam "
            "is the home stadium of Ajax."
        ),
    },

    {
        "question": "Which Turkish club is traditionally known as 'The Lions'?",
        "answer_a": "Fenerbahce",
        "answer_b": "Besiktas",
        "answer_c": "Galatasaray",
        "answer_d": "Trabzonspor",
        "correct_answer": "C",
        "category": "clubs",
        "difficulty": "medium",
        "explanation": (
            "Galatasaray is commonly associated "
            "with the lion symbol and nickname."
        ),
    },


    # =========================================================
    # FOOTBALL HISTORY - 10 QUESTIONS
    # =========================================================

    {
        "question": "In which country were the modern Laws of Association Football first codified in 1863?",
        "answer_a": "Scotland",
        "answer_b": "England",
        "answer_c": "France",
        "answer_d": "Italy",
        "correct_answer": "B",
        "category": "history",
        "difficulty": "medium",
        "explanation": (
            "The Football Association was formed in England "
            "in 1863 and established a unified set of laws."
        ),
    },

    {
        "question": "What was the original FIFA World Cup trophy later commonly known as?",
        "answer_a": "Jules Rimet Trophy",
        "answer_b": "Henri Delaunay Trophy",
        "answer_c": "Victory Shield",
        "answer_d": "FIFA Golden Cup",
        "correct_answer": "A",
        "category": "history",
        "difficulty": "hard",
        "explanation": (
            "The original World Cup trophy was renamed "
            "the Jules Rimet Trophy in 1946."
        ),
    },

    {
        "question": "Which organization governs international association football?",
        "answer_a": "UEFA",
        "answer_b": "IOC",
        "answer_c": "FIFA",
        "answer_d": "IFAB",
        "correct_answer": "C",
        "category": "history",
        "difficulty": "easy",
        "explanation": (
            "FIFA is the international governing body "
            "for association football."
        ),
    },

    {
        "question": "In which year was FIFA founded?",
        "answer_a": "1863",
        "answer_b": "1888",
        "answer_c": "1904",
        "answer_d": "1930",
        "correct_answer": "C",
        "category": "history",
        "difficulty": "hard",
        "explanation": (
            "FIFA was founded in Paris in 1904."
        ),
    },

    {
        "question": "In which city was FIFA founded in 1904?",
        "answer_a": "London",
        "answer_b": "Paris",
        "answer_c": "Zurich",
        "answer_d": "Geneva",
        "correct_answer": "B",
        "category": "history",
        "difficulty": "hard",
        "explanation": (
            "FIFA was founded in Paris on 21 May 1904."
        ),
    },

    {
        "question": "Which country is widely regarded as the birthplace of modern association football?",
        "answer_a": "Brazil",
        "answer_b": "Italy",
        "answer_c": "England",
        "answer_d": "Germany",
        "correct_answer": "C",
        "category": "history",
        "difficulty": "easy",
        "explanation": (
            "Modern association football was codified "
            "in England during the nineteenth century."
        ),
    },

    {
        "question": "Which competition is the oldest national football competition in the world?",
        "answer_a": "FA Cup",
        "answer_b": "Copa del Rey",
        "answer_c": "Scottish Cup",
        "answer_d": "DFB-Pokal",
        "correct_answer": "A",
        "category": "history",
        "difficulty": "medium",
        "explanation": (
            "The FA Cup was first played in the 1871–72 season "
            "and is the oldest national football competition."
        ),
    },

    {
        "question": "Which club won the first FA Cup in 1872?",
        "answer_a": "Royal Engineers",
        "answer_b": "Wanderers",
        "answer_c": "Old Etonians",
        "answer_d": "Blackburn Rovers",
        "correct_answer": "B",
        "category": "history",
        "difficulty": "hard",
        "explanation": (
            "Wanderers defeated Royal Engineers "
            "to win the first FA Cup final in 1872."
        ),
    },

    {
        "question": "In which year was the first FIFA World Cup held?",
        "answer_a": "1924",
        "answer_b": "1928",
        "answer_c": "1930",
        "answer_d": "1934",
        "correct_answer": "C",
        "category": "history",
        "difficulty": "easy",
        "explanation": (
            "The first FIFA World Cup was held "
            "in Uruguay in 1930."
        ),
    },

    {
        "question": "Which body is responsible for determining the Laws of the Game in association football?",
        "answer_a": "FIFA alone",
        "answer_b": "UEFA",
        "answer_c": "International Football Association Board",
        "answer_d": "International Olympic Committee",
        "correct_answer": "C",
        "category": "history",
        "difficulty": "hard",
        "explanation": (
            "The International Football Association Board, "
            "commonly known as IFAB, determines the Laws of the Game."
        ),
    },

]


class Command(BaseCommand):

    help = (
        "Loads the 100 Football Trivia "
        "questions into the database."
    )

    def handle(self, *args, **options):

        created_count = 0
        updated_count = 0

        self.stdout.write("")
        self.stdout.write(
            "========================================"
        )
        self.stdout.write(
            "       FOOTBALL TRIVIA IMPORTER"
        )
        self.stdout.write(
            "========================================"
        )
        self.stdout.write("")

        for data in QUESTIONS:

            question_text = data["question"]

            defaults = {
                key: value
                for key, value in data.items()
                if key != "question"
            }

            question, created = (
                Question.objects.update_or_create(
                    question=question_text,
                    defaults=defaults
                )
            )

            if created:

                created_count += 1

                self.stdout.write(
                    self.style.SUCCESS(
                        f"ADDED: {question.question}"
                    )
                )

            else:

                updated_count += 1

                self.stdout.write(
                    self.style.WARNING(
                        f"UPDATED: {question.question}"
                    )
                )

        self.stdout.write("")
        self.stdout.write(
            "----------------------------------------"
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Added: {created_count}"
            )
        )

        self.stdout.write(
            self.style.WARNING(
                f"Updated: {updated_count}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Questions in this file: "
                f"{len(QUESTIONS)}"
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Total questions in database: "
                f"{Question.objects.count()}"
            )
        )

        self.stdout.write(
            "----------------------------------------"
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Import complete."
            )
        )

        self.stdout.write("")