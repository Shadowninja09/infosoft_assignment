class DataStream():
    def __init__(self):
#         constructor which creates a timer dictionary which is empty belonging to an object
        self.timer = dict()

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
#         if the string has never been displayed, then we add the string as key and timestamp as value to the timerdictionary
#         .get() method is used here because if the key does not exist in the dictionary then we get None instead of an program breaking error
        if not (self.timer.get(data_string)):
            self.timer[data_string] = timestamp
            # the string can be displayed if it has never been displayed before
            return True
        else:  # the string has been displayed before
            # if the difference between the time at which the string is to be displayed again and the time at which
            # it was previously displayed is greater than 5 units
            if timestamp - self.timer[data_string] > 5:
                # then we can update the string with the updated time in the timer dictionary
                self.timer[data_string] = timestamp
                # and the string can be displayed again
                return True

            else:  # if the difference is less than equal to 5 then the string cannot be displayed
                return False


data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))

print(data_stream.should_output_data_str(timestamp=1, data_string="world"))

print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))

print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))

print(data_stream.should_output_data_str(timestamp=8, data_string="world"))
