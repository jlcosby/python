#errors and exceptions

#error 
integer = 50
string = "The number is"

print(string + integer)

#exception
import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(err))

#adding multiple statements

import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as t_err:
    logging.warning("Error - {}. You cannot add a string to an integer, without converting the integer to a string first".format(t_err))
except ValueError as v_err:
    logging.warning("Error - {}. Your message".format(v_err))

#boto30-generated exceptions
import logging
import boto3
from botocore.exceptions import ClientError

try:
    client = boto3.client('translate')
    <snip>
except ClientError as e:
    logging.warning("<your msg> {}".format(e))
