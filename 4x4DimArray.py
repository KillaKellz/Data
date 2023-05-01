multi_arr= ["Nick", "Zach", "Mike", "Muhammad"], ["Po", "John", "Joe", "Bobby"], ["Anne", "Alex", "Allison", "Alice"], ["Bruce", "Smithy", "Colin", "James"], 
grade_arr= [10, 15, 90, 60], [20, 26, 14, 3], [0, 6, 50, 30], [33, 100, 17, 5]

for i in range(len(multi_arr)):
    for j in range(len(multi_arr[i])):
        print(multi_arr[i][j], grade_arr[i][j])
        
