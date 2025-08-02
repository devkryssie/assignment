#name of 100 students
students = [
{"id": 1, "name": "alice",
"score": 78},
{"id": 2, "name": "bob",
"score": 45},
{"id": 3, "name": "charlie",
"score": 92},
{"id": 4, "name": "david",
"score": 60},
{"id": 5, "name": "eve",
"score": 30},
{"id": 6, "name": "faith",
"score": 68},
{"id": 7, "name": "gideon",
"score": 75},
{"id": 19, "name": "amala",
"score": 85},
{"id": 20, "name": "judith",
"score": 10},
{"id": 21, "name": "ice",
"score": 48},
{"id": 22, "name": "lice",
"score": 43},
{"id": 23, "name": "ace",
"score": 76},
{"id": 24, "name": "longs",
"score": 65},
{"id": 41, "name": "boy",
"score": 40},
{"id": 42, "name": "rina",
"score": 54},
{"id": 43, "name": "rejoice",
"score": 96},
{"id": 44, "name": "mannanaf",
"score": 27},
{"id": 45, "name": "lekwar",
"score": 43},
{"id": 46, "name": "adamu",
"score": 45},
{"id": 47, "name": "mercy",
"score": 43},
{"id": 48, "name": "abel",
"score": 11},
{"id": 49, "name": "ken",
"score": 44},
{"id": 50, "name": "kin",
"score": 43},
{"id": 51, "name": "kol",
"score": 44},
{"id": 52, "name": "chong",
"score": 11},
{"id": 53, "name": "miracle",
"score": 99},
{"id": 54, "name": "boll",
 "score": 19},
{"id": 55, "name": "nirot",
"score": 67},
{"id": 56, "name": "mollu",
"score": 73},
{"id": 57, "name": "lom",
"score": 12},
{"id": 58, "name": "endong",
"score": 74}, 
{"id": 59, "name": "isiah",
"score": 44}, 
{"id": 60, "name": "ima",
"score": 77},
{"id": 61, "name": "abel",
"score": 65},
{"id": 62, "name": "ken",
"score": 26}, 
{"id": 63, "name": "kopa",
"score": 19},
{"id": 64, "name": "roy",
"score": 55}, 
{"id": 65, "name": "nopaaa",
"score": 1}, 
{"id": 66, "name": "kenneth",
"score": 72}, 
{"id": 67, "name": "mangut",
"score": 76},
{"id": 68, "name": "tosis",
"score": 86},
{"id": 69, "name": "man",
"score": 73},
{"id": 70, "name": "abel",
"score": 66},
{"id": 71, "name": "tosin",
"score": 8},
{"id": 72, "name": "niken",
"score": 37},
{"id": 73, "name": "umar",
"score": 40}, 
{"id": 74, "name": "mtn",
"score": 27},
{"id": 75, "name": "malians",
"score": 95},
{"id": 76, "name": "nanchin",
"score": 20}, 
{"id": 77, "name": "kopaban",
"score": 100}, 
{"id": 78, "name": "royin",
"score": 0}, 
{"id": 79, "name": "nopaaa1",
"score": 1},  
{"id": 80, "name": "kenneth1",
"score": 12}, 
{"id": 81, "name": "mangut1",
"score": 76},
{"id": 82, "name": "tosis1",
"score": 83},
{"id": 83, "name": "mana",
"score": 38},
{"id": 84, "name": "isiah2",
"score": 41}, 
{"id": 85, "name": "ima6",
"score": 70},
{"id": 86, "name": "sadiq",
"score": 15},
{"id": 87, "name": "kenpon",
"score": 32}, 
{"id": 88, "name": "kopama",
"score": 11}, 
{"id": 89, "name": "royooo",
"score": 51}, 
{"id": 90, "name": "palmer",
"score": 22},  
{"id": 91, "name": "kennth",
"score": 92}, 
{"id": 92, "name": "manut",
"score": 46},
{"id": 93, "name": "osis",
"score": 55},
{"id": 94, "name": "1an",
"score": 21},
{"id": 95, "name": "manut22",
"score": 46},
{"id": 96, "name": "osis22",
"score": 55},
{"id": 97, "name": "1an",
"score": 42},
{"id": 98, "name": "mat22",
"score": 76},
{"id": 99, "name": "os22",
"score": 100},
{"id": 100, "name": "titus",
"score": 100}]
#craete empty list for each category
high_performers = [i for i in students if i["score"] >= 70]
average_performers = [i for i in students if 50<= i["score"]<=70]
low_performers = [i for i in students if i["score"]< 50]
print()
#loop through all students record and classify
for i in students:
    print(i)
    students_id = students[0]["id"]
    name = students[0]["name"]
    score = students[0]["score"] 
    record = {students_id : (name, score)}

    if score >= 70:
        high_performers.append(record)
     # print(i)
    elif 50 <= score < 70:   
        average_performers.append(record)
     # print(i)
    else:
        low_performers.append(record)
     # print(i)
print()
print("all high performers:")
print(high_performers)
print()
print("\nall average  performers:")
print(average_performers)
print()
print("\nall low performance:")
print(low_performers)
print()
#summary
print("\nsummart report:")
print("high performers:",
len(high_performers))
print("average_performance:",
len(average_performers))
print("low performers:",
len(low_performers))




















































