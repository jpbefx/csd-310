
import datetime as dt
from faker import Faker

fake = Faker()
#
#
#print(fake.date_between(start_date="-1y",end_date="now")) # date between 2021 and 2022
#Faker.seed(0)
#for i in range(4):
#    print(fake.date_time_this_year())
#
#for _ in range(5):
#    print(fake.past_datetime(start_date="-1y"))
#
#
#
#
class Timeclock:
    def __init__(self, clock_in, clock_out):
        self.clock_in = clock_in
        self.clock_out = clock_out


    def __str__(self):
        return f'cursor.execute("INSERT INTO employee_clocks(employee_id, department_id, clock_in, clock_out) VALUES(7, 5, {clock_in}, {clock_out});")'

    #def __repr__(self):
       # return f'cursor.execute("INSERT INTO employee_clocks(employee_id, department_id, clock_in, clock_out) VALUES(1, 1, {self.clock_in}, {self.clock_out}");")'

#c_in = fake.date_between(start_date="-1y",end_date="now")
#c_out = fake.date_between(start_date=c_in,end_date="now")
clock_in = fake.past_datetime(start_date="-1y")
clock_out = fake.past_datetime()


timeclock = Timeclock(clock_in, clock_out)
#timeclock(str(c_in),str(c_out))
for m in range(100):
    print(f"{timeclock}")
    

#def timeclock1(clock_in1, clock_out1):
   # print("'"+clock_in1+"'" + ", " + "'"+ clock_out1+"'")

#c1_in_date = fake.past_date()
#c1_in_time = fake.time()
#
#c1_in = dt.combine(c1_in_date,c1_in_time)
#
#c_out_date = c1_in_date
#c_out_time = fake.time()
#
#c1_out = dt.combine(c_out_date,c_out_time)
#
#timeclock1(c1_in, c1_out)
#
#print(fake.time())