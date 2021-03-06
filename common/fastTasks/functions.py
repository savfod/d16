#Write your functions here: they should be named parse_ints,
#parse_floats, filter_title_words, arithmetic_mean, arithmetic_median,
#positive_ammount, positive_percent, text_title

def hello_world():
    return "HelloWorld"

assert(hello_world() == "HelloWorld")

#1abc
assert(tuple(parse_ints("1 2 3 4")) == (1, 2, 3, 4))
assert(tuple(parse_ints("1 5 2 57")) == (1, 5, 2, 57))
assert(tuple(parse_ints("-16 46 0 13")) == (-16, 46, 0, 13))

assert(tuple(parse_floats("1.2 3.4 5.7")) == (1.2, 3.4, 5.7))
assert(tuple(parse_floats("5.2 4.655 6.894")) == (5.2, 4.655, 6.894))
assert(tuple(parse_floats("38.0 15.96 3.005")) == (38.0, 15.96, 3.005))

assert(tuple(filter_title_words("Abigale barse Carter durry Emerson flat Grey")) == ("Abigale", "Carter", "Emerson", "Grey"))
assert(tuple(filter_title_words("Titanic Normandy steamer captain Great Eastern sea")) == ("Titanic", "Normandy", "Great", "Eastern"))
assert(tuple(filter_title_words("accordeon Paris metropolitain Rouene arc du Triumph le Tour d Eiffel")) == ("Paris", "Rouene", "Triumph", "Tour", "Eiffel"))

#2abcd
assert((arithmetic_mean([1.0, -3.0, 5.0])) == 1.0)
assert((arithmetic_mean([23.0, 5.0, 14.0])) == 14.0)
assert((arithmetic_mean([1.6 , 4.0 , 6.8 , 5.7])) == 4.5249999999999995)

assert((arithmetic_median([1.0, 3.0, -5.0])) == 1.0)
assert((arithmetic_median([23.0, 5.0, 14.0 , 4.0 , 6.8])) == 6.8)
assert((arithmetic_median([-1.6 , 4.0 , 6.8 , 5.7])) == 4.8499999999999996)

assert((int(positive_ammount([-1.0, -3.0, 5.0]))) == 1)
assert((int(positive_ammount([23.0, -5.0, 14.0, -14.0]))) == 2)
assert((int(positive_ammount([1.6 , -4.0 , 6.8 , -5.7, -4.655, 6.894]))) == 3)

assert((int(positive_percent([-1.0, 5.0]))) == 50)
assert((int(positive_percent([23.0, -5.0, -14.0, -14.0]))) == 25)
assert((int(positive_percent([1.6 , 4.0 -5.7, 4.655, 6.894]))) == 80)

#4
assert((text_title("Aie, aie, ce que tu peux etre credule De ces gens malhonnetes Qui te promettent la lune, Leur laissant ton pouvoir Pour quils te manipulent, ta precieuse liberte Et parfois meme tes tunes. Cest fou, tu te crois a labri Tu te moques du monde Que tu juges avec mepris. Bien trop intelligent Pour, dans ce piege etre pris Tu te voiles bien la face Et se joue ce qui suit")) == "Aie, aie, ce que tu peux etre credule De ces gens malhonnetes Qui te promettent la lune, Leur laissa")
assert((text_title("Cet air qui mobsede jour et nuit Cet air nest pas ne daujourdhui Il vient daussi loin que je viens Traine par cent mille musiciens Un jour cet air me rendra folle Cent fois jai voulu dire pourquoi Mais il ma coupe la parole Il parle toujours avant moi Et sa voix couvre ma voix Padam...padam...padam... Il arrive en courant derriere moi Padam...padam...padam... Il me fait le coup du souviens-toi Padam...padam...padam... Cest un air qui me montre du doigt Et je traine apres moi comme une drole derreur Cet air qui sait tout par coeur")) == "Cet air qui mobsede jour et nuit Cet air nest pas ne daujourdhui Il vient daussi loin que je viens T")
assert((text_title("Je suis jamais alle by Yann Tiersen")) == "Je suis jamais alle by Yann Tiersen")

print("No errors detected, all tests finished correctly")
