#####################################
########## Features #################
#####################################


packages = ["normal", "standard", "premium"]
##########################################################
package = packages[2]   # CHOOSE WHICH PACKAGE TO COMPILE
demo = False
copyright_url = "https://www.fiverr.com/lordahmed"   # "https://www.fiverr.com/lordahmed"
copyright_text = "AhmeDSaeeD | (lordahmed on Fiverr)"    #  "AhmeDSaeeD | (lordahmed on Fiverr)"
##########################################################
if package == "normal":
    attachments_enabled = False
    scheduled_sending = False
    contact_card_enabled = False
elif package == "standard":
    attachments_enabled = True
    scheduled_sending = False
    contact_card_enabled = True
elif package == "premium":
    attachments_enabled = True
    scheduled_sending = True
    contact_card_enabled = True
# extras
multi_messages_enabled = True
repeat_every_24h = False
extra_var = None  # assign None to disable it. to activate it, put the column number



######################################
########### Functionilty #############
######################################



# SETTINGS
version = "2.7.0"
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
