union = {
        "Partner1" : {
            "Name" : "Andrew Paul Novocin",
            "ChildOfUnion" : {
                   "Partner1" : {"Name": "Norb William Novocin Jr.",
                                 "ChildOfUnion" : {}
                                },
                   "Partner2" : {"Name":"Marie Ellen Novocin",
                                 "ChildOfUnion" : {}
                                },
                   "Offspring": [{"Name" : "Casey Mann Novocin"}, 
                                 {"Name" : "Judah Cutler Novocin"}, 
                                 {"Name" : "Andrew Paul Novocin"}]
                }
        },
        "Partner2" : {
            "Name" : "Sara Elizabeth Novocin",
            "ChildOfUnion" : {
                "Partner1" : {"Name": "Ron Preston",
                              "ChildOfUnion" : {}},
                "Partner2" : {"Name" : "Elizabeth Tripp",
                              "ChildOfUnion" : {}},
                "Offspring": [{"Name" : "Aubrey Preston"}, 
                              {"Name" : "Sara Elizabeth Novocin"}]
            }
        },
        "Offspring" : [{"Name" : "Simone Mairie Novocin"}]
    }

print(union)