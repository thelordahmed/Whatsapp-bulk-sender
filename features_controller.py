#####################################
########## Features #################
#####################################


packages = ["normal", "standard", "premium"]
##########################################################
package = packages[2]   # CHOOSE WHICH PACKAGE TO COMPILE
demo = False
##########################################################
if package == "normal":
    attachments_enabled = False
    scheduled_sending = False
elif package == "standard":
    attachments_enabled = True
    scheduled_sending = False
elif package == "premium":
    attachments_enabled = True
    scheduled_sending = True
# extras
contact_card_enabled = True
multi_messages_enabled = False
repeat_every_24h = False
extra_var = None  # assign None to disable it. to activate it, put the column number



######################################
########### Functionilty #############
######################################



# SETTINGS
version = "2.4.1"
language = "en"

# sheet settings
header_row = False
name_row = 1
phone_row = 2
country_code = None  # assign None to ignore it
# Interface
show_columns_note = True
copyright_link = True


################################################################
