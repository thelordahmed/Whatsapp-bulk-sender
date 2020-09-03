#####################################
########## Features #################

# extra
multi_messages_enabled = True
# Standard Package
contact_card_enabled = True
attachments_enabled = True

######################################
#--------------------------------------------------------------------------------
######################################
########### Functionilty #############

TYPE = "default"
version = "2.1.2"

if TYPE == "default":
    # sheet settings
    header_row = False
    name_row = 1
    phone_row = 2
    country_code = None  # assign None to ignore it
    # Interface text
    show_columns_note = True
else:
    # sheet settings
    header_row = True
    name_row = 1
    phone_row = 2
    country_code = 4    # assign None to ignore it
    # Interface text
    show_columns_note = False
################################################################
