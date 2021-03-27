hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hours_to_mins = hour * 60
total_mins = hours_to_mins + mins + dura #making a total of time in minutes

end_mins = total_mins % 60 #taking the end mins using the mod operator
subtract_mins = total_mins - end_mins #subtract the end_mins from total_mins to get end_hours in minutes
mins_to_hours = subtract_mins / 60
end_hours = mins_to_hours % 24 #taking the end_hours using the mod operator

print(int(end_hours),":",int(end_mins))


