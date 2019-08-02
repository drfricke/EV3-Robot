# EV3-Robot

Setup EV3/Motor Drive/DC motors. (will provide documents)

In terminal (Mac) create a ssh connection with deired EV3. (ssh robot@ - ip address, password 'maker')

Open desired file. File c.py is the most up-to-date file to use for experiments (06/19/19). (ex. 'python3 c.py')

To upload a file from your computer to the EV3. Create a sftp (sftp robot@...) connection with the EV3 and use the 'put' command.


# Using file control.py

'w' - Enter the selected PWM

'p' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'o' - Decreases PWM by 5.

'l' - Increases PWM by 5. 0 = Full Reverse. ~50 = stop. 100 = Full Forward.

'k' - Decreases PWM by 5.

' ' - stop

# Using file Remote_Drive.py

