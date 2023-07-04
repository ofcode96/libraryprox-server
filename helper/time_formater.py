from datetime import datetime
import time ,ciso8601

class TimeFormater :
   
   @staticmethod
   def convert_timestemps(real_time:str)->float:
      year , month , day  = tuple(real_time.split('-'))
      date_time = datetime(year=int(year),month=int(month),day=int(day))
 
      date_string = f'{year}-{date_time.month}-{date_time.day}'
      date_format = '%Y-%m-%d'

      # Convert the date string to a datetime object
      dt = datetime.strptime(date_string, date_format)

      # Get the timestamp in seconds
      timestamp = (dt - datetime(1970, 1, 1)).total_seconds()
      

      
      return timestamp
   
   @staticmethod
   def convert_real_time(timestemps:float):
      return datetime.fromtimestamp(timestemps).strftime("%Y-%m-%d")
   
   
   @staticmethod
   def convert_now_timestemp():
      return datetime.timestamp(datetime.now())
   
   

