
def add_time(time,add,extra=False):
    
    time_12,am_or_pm = time.split(" ")
    time_hour,time_minute = time_12.split(":")

    add_hour,add_minute = add.split(":")

    time_hour = int(time_hour) + int(add_hour)
    total_minute = int(time_minute) + int(add_minute)
    # calution of total time and minute
    output_minute = total_minute % 60
    
    #cheking if the minute is less than 9 or greater than, so we can put a double digit minute (eg. 09 or 11)
    if output_minute <10:
        output_minute = "0"+ str(output_minute)
    else:
        output_minute = str(output_minute)
        
    minute_to_hr = total_minute // 60
    total_hr = (time_hour + minute_to_hr)
    output_hr = total_hr % 12
    check_am_pm = (total_hr // 12)%2
    
    # check for 12 in place of hour time
    if output_hr == 0:
        output_hr = 12
    else:
        output_hr 
#     check_am_pm = hr_to_day % 2
    def opposite(val):
        if val ==0:
            return am_or_pm.upper()
        elif (val == 1 and am_or_pm.upper() =="AM"):
            return "PM"
        else:
            return "AM"
    output_am_or_pm =opposite(check_am_pm)
    
    # 24 hr format01
    if am_or_pm =="AM":
        n_days = total_hr // 24 # counting the days
    else:
        n_days = (total_hr + 12) //24 # converting to 24 hr and counting the days

    def days(val):
        if val == 0:
            return ""
        elif val == 1:
            return ("(next day)")
        else:
            return ("({} days later)".format(val))
    day_string = days(n_days)
    time_string = str(output_hr) + ":" + str(output_minute) + " " + output_am_or_pm 
    
    # Making the weekend dictinary
    week = {0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
    # function to return key for any value
    def get_key(val):
        for key, value in week.items():
             if val == value:
                    return key
 
        return "Week Name Error"
    # get key (i.e in day)
    
    if extra :
        key = get_key(extra.capitalize())
        check_day = n_days+key 
        if check_day < 7 and day_string: 
            return time_string + ", " + week[check_day] + " " + day_string
        
        elif check_day < 7: 
            return time_string + ", " + week[check_day]
        
        elif day_string:
            check_day = check_day % 7
            return time_string + ", " + week[check_day] + " " + day_string
      
        else:
            check_day = check_day % 7
            return time_string + ", " + week[check_day]

    else:
        if day_string:
            return time_string + " " + day_string
        else:
            return time_string
    
        