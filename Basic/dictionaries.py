def run():
    my_dictionary = {
        "key1": 1,
        "key2": 2,
        "key3": 3,
    }
    
    # print(my_dictionary["key1"])
    # print(my_dictionary["key2"])
    # print(my_dictionary["key3"])

    country_population = {
        "Argentina": 44938712,
        "Brasil": 210147125,
        "Colombia": 50372424
    }

    # print(country_population["Bolivia"])

    # for country in country_population.keys():
    #     print(country)
    
    # for country in country_population.values():
    #     print(country)

    for country, population in country_population.values():
        print(country + " has" + str(population) + " inhabitants")

if __name__ == "__main__":
    run()